package com.demo.web;

import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.time.Instant;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api")
@CrossOrigin(origins = "*")
public class WeatherController {

    @GetMapping(value = "/weather/realtime", produces = "application/json;charset=UTF-8")
    public Map<String, Object> realtime() {
        Map<String, Object> data = new HashMap<>();
        data.put("timestamp", Instant.now().toString());
        data.put("location", "demo-station-001");
        data.put("temperature", 22.6);
        data.put("humidity", 0.63);
        data.put("windSpeed", 3.2);
        data.put("illumination", 560.0);
        return data;
    }

    @GetMapping(value = "/weather/alerts", produces = "application/json;charset=UTF-8")
    public Map<String, Object> alerts() {
        Map<String, Object> payload = new HashMap<>();
        payload.put("count", 1);
        payload.put("items", List.of(
                Map.of(
                        "level", "WARN",
                        "type", "FROST",
                        "message", "未来24小时夜间低温风险，请注意防霜冻",
                        "issuedAt", Instant.now().toString()
                )));
        return payload;
    }

    @GetMapping(value = "/reports/summary", produces = "application/json;charset=UTF-8")
    public Map<String, Object> reportSummary() {
        return Map.of(
                "generatedAt", Instant.now().toString(),
                "recommendation", "本周适宜播种小麦，注意周三可能有降雨",
                "riskIndex", 0.18
        );
    }
}


