package com.demo.web;

import com.demo.service.AmapService;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.*;

import java.util.Map;

@RestController
@RequestMapping("/api/amap")
@CrossOrigin(origins = "*")
public class AmapController {
    private final AmapService amapService;
    public AmapController(AmapService amapService) { this.amapService = amapService; }

    @GetMapping(value = "/ip", produces = "application/json;charset=UTF-8")
    public Map<String, Object> ip() {
        return amapService.ipLocation();
    }

    @GetMapping(value = "/weather", produces = "application/json;charset=UTF-8")
    public Map<String, Object> weather(@RequestParam String adcode) {
        return amapService.weatherByAdcode(adcode);
    }
    
    @GetMapping(value = "/forecast", produces = "application/json;charset=UTF-8")
    public Map<String, Object> forecast(@RequestParam String adcode) {
        return amapService.forecastByAdcode(adcode);
    }

    @GetMapping(value = "/static-map", produces = MediaType.TEXT_PLAIN_VALUE)
    public String staticMap(@RequestParam double lng, @RequestParam double lat) {
        return amapService.buildStaticMapUrl(lng, lat);
    }

    @GetMapping(value = "/reverse", produces = "application/json;charset=UTF-8")
    public Map<String, Object> reverse(@RequestParam double lng, @RequestParam double lat) {
        return amapService.reverseGeocode(lng, lat);
    }

    @GetMapping(value = "/geocode", produces = "application/json;charset=UTF-8")
    public Map<String, Object> geocode(@RequestParam String address) {
        return amapService.geocodeByAddress(address);
    }
}


