package com.demo.service;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.HashMap;
import java.util.Map;

@Service
public class AmapService {

    @Value("${amap.key}")
    private String apiKey;

    @Value("${amap.base:https://restapi.amap.com}")
    private String base;

    private final RestTemplate restTemplate = new RestTemplate();

    public Map<String, Object> ipLocation() {
        String url = base + "/v3/ip?key=" + apiKey;
        Map body = restTemplate.getForObject(url, Map.class);
        Map<String, Object> result = new HashMap<>();
        if (body == null) return result;
        result.put("province", body.getOrDefault("province", ""));
        result.put("city", body.getOrDefault("city", ""));
        result.put("adcode", body.getOrDefault("adcode", ""));
        Object rectangle = body.get("rectangle");
        if (rectangle instanceof String) {
            String rect = (String) rectangle; // lng1,lat1;lng2,lat2
            try {
                String[] parts = rect.split(";");
                String[] p1 = parts[0].split(",");
                String[] p2 = parts[1].split(",");
                double lng = (Double.parseDouble(p1[0]) + Double.parseDouble(p2[0])) / 2.0;
                double lat = (Double.parseDouble(p1[1]) + Double.parseDouble(p2[1])) / 2.0;
                result.put("centerLng", lng);
                result.put("centerLat", lat);
            } catch (Exception ignored) {}
        }
        return result;
    }

    public Map<String, Object> weatherByAdcode(String adcode) {
        String url = base + "/v3/weather/weatherInfo?city=" + adcode + "&key=" + apiKey + "&extensions=base";
        Map body = restTemplate.getForObject(url, Map.class);
        Map<String, Object> result = new HashMap<>();
        if (body == null) return result;
        try {
            Object livesObj = body.get("lives");
            if (livesObj instanceof java.util.List && !((java.util.List) livesObj).isEmpty()) {
                Map live = (Map) ((java.util.List) livesObj).get(0);
                result.put("province", live.get("province"));
                result.put("city", live.get("city"));
                result.put("weather", live.get("weather"));
                result.put("temperature", live.get("temperature"));
                result.put("humidity", live.get("humidity"));
                result.put("winddirection", live.get("winddirection"));
                result.put("windpower", live.get("windpower"));
                result.put("reporttime", live.get("reporttime"));
            }
        } catch (Exception ignored) {}
        return result;
    }

    public Map<String, Object> forecastByAdcode(String adcode) {
        String url = base + "/v3/weather/weatherInfo?city=" + adcode + "&key=" + apiKey + "&extensions=all";
        Map body = restTemplate.getForObject(url, Map.class);
        Map<String, Object> result = new HashMap<>();
        if (body == null) return result;
        try {
            Object forecasts = body.get("forecasts");
            if (forecasts instanceof java.util.List && !((java.util.List) forecasts).isEmpty()) {
                Map f0 = (Map) ((java.util.List) forecasts).get(0);
                java.util.List casts = (java.util.List) f0.get("casts");
                java.util.List<Map<String, Object>> days = new java.util.ArrayList<>();
                if (casts != null) {
                    for (Object cObj : casts) {
                        Map c = (Map) cObj;
                        Map<String, Object> d = new HashMap<>();
                        d.put("date", c.get("date"));
                        d.put("week", c.get("week"));
                        d.put("dayweather", c.get("dayweather"));
                        d.put("nightweather", c.get("nightweather"));
                        d.put("daytemp", c.get("daytemp"));
                        d.put("nighttemp", c.get("nighttemp"));
                        d.put("daywind", c.get("daywind"));
                        d.put("daypower", c.get("daypower"));
                        days.add(d);
                    }
                }
                result.put("city", f0.get("city"));
                result.put("adcode", f0.get("adcode"));
                result.put("reporttime", f0.get("reporttime"));
                result.put("days", days);
            }
        } catch (Exception ignored) {}
        return result;
    }

    public String buildStaticMapUrl(double lng, double lat) {
        String location = lng + "," + lat;
        String markers = "mid,0xFF0000,A:" + location;
        // size 最大 1024*1024；放大到 1024x512 提升可读性
        return base + "/v3/staticmap?location=" + location + "&zoom=11&size=1024*512&markers=" + markers + "&key=" + apiKey;
    }

    public Map<String, Object> reverseGeocode(double lng, double lat) {
        String url = base + "/v3/geocode/regeo?location=" + lng + "," + lat + "&key=" + apiKey + "&extensions=base";
        Map body = restTemplate.getForObject(url, Map.class);
        Map<String, Object> result = new HashMap<>();
        if (body == null) return result;
        try {
            Map regeocode = (Map) body.get("regeocode");
            if (regeocode != null) {
                Map addr = (Map) regeocode.get("addressComponent");
                if (addr != null) {
                    result.put("province", addr.get("province"));
                    Object city = addr.get("city");
                    result.put("city", city instanceof String ? city : (addr.get("district")));
                    result.put("adcode", addr.get("adcode"));
                }
                result.put("formattedAddress", regeocode.get("formatted_address"));
            }
        } catch (Exception ignored) {}
        result.put("centerLng", lng);
        result.put("centerLat", lat);
        return result;
    }

    public Map<String, Object> geocodeByAddress(String address) {
        String url = base + "/v3/geocode/geo?address=" + address + "&key=" + apiKey;
        Map body = restTemplate.getForObject(url, Map.class);
        Map<String, Object> result = new HashMap<>();
        if (body == null) return result;
        try {
            java.util.List geocodes = (java.util.List) body.get("geocodes");
            if (geocodes != null && !geocodes.isEmpty()) {
                Map first = (Map) geocodes.get(0);
                result.put("adcode", first.get("adcode"));
                result.put("province", first.get("province"));
                result.put("city", first.get("city"));
                Object loc = first.get("location");
                if (loc instanceof String) {
                    String[] arr = ((String) loc).split(",");
                    if (arr.length == 2) {
                        result.put("centerLng", Double.parseDouble(arr[0]));
                        result.put("centerLat", Double.parseDouble(arr[1]));
                    }
                }
            }
        } catch (Exception ignored) {}
        return result;
    }
}


