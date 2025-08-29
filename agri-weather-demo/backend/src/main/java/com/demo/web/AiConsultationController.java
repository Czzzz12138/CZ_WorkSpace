package com.demo.web;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api/ai")
@CrossOrigin(origins = "*")
public class AiConsultationController {

    @Value("${deepseek.api.key:}")
    private String deepseekApiKey;
    
    @Value("${deepseek.api.url:https://api.deepseek.com/v1/chat/completions}")
    private String deepseekApiUrl;

    private final RestTemplate restTemplate = new RestTemplate();

    @PostMapping(value = "/consultation", produces = "application/json;charset=UTF-8")
    public Map<String, Object> consultation(@RequestBody Map<String, String> request) {
        String question = request.get("question");
        Map<String, Object> result = new HashMap<>();
        
        if (question == null || question.trim().isEmpty()) {
            result.put("success", false);
            result.put("message", "问题不能为空");
            return result;
        }

        try {
            // 如果有API密钥，调用DeepSeek API
            if (deepseekApiKey != null && !deepseekApiKey.trim().isEmpty()) {
                String aiResponse = callDeepSeekApi(question);
                result.put("success", true);
                result.put("response", aiResponse);
                result.put("source", "ai");
            } else {
                // fallback到预设回复
                String fallbackResponse = getFallbackResponse(question);
                result.put("success", true);
                result.put("response", fallbackResponse);
                result.put("source", "template");
            }
        } catch (Exception e) {
            // 如果API调用失败，使用fallback
            String fallbackResponse = getFallbackResponse(question);
            result.put("success", true);
            result.put("response", fallbackResponse);
            result.put("source", "fallback");
            result.put("error", e.getMessage());
        }

        return result;
    }

    private String callDeepSeekApi(String question) {
        try {
            HttpHeaders headers = new HttpHeaders();
            headers.setContentType(MediaType.APPLICATION_JSON);
            headers.set("Authorization", "Bearer " + deepseekApiKey);

            Map<String, Object> requestBody = new HashMap<>();
            requestBody.put("model", "deepseek-chat");
            requestBody.put("max_tokens", 1000);
            requestBody.put("temperature", 0.7);
            requestBody.put("stream", false);
            
            Map<String, Object> systemMessage = new HashMap<>();
            systemMessage.put("role", "system");
            systemMessage.put("content", "你是一位专业的农业技术专家，拥有丰富的农业种植、病虫害防治、土壤管理和农业气象等方面的知识。请用专业、友好的语气回答用户的农业相关问题，提供实用的建议和解决方案。回答要具体、可操作，并注意地域性差异。");
            
            Map<String, Object> userMessage = new HashMap<>();
            userMessage.put("role", "user");
            userMessage.put("content", question);
            
            requestBody.put("messages", List.of(systemMessage, userMessage));

            HttpEntity<Map<String, Object>> entity = new HttpEntity<>(requestBody, headers);
            
            Map response = restTemplate.exchange(
                deepseekApiUrl,
                HttpMethod.POST,
                entity,
                Map.class
            ).getBody();

            if (response != null && response.containsKey("choices")) {
                List choices = (List) response.get("choices");
                if (!choices.isEmpty()) {
                    Map choice = (Map) choices.get(0);
                    Map message = (Map) choice.get("message");
                    return (String) message.get("content");
                }
            }
            
            throw new RuntimeException("API返回格式异常: " + response);
            
        } catch (Exception e) {
            throw new RuntimeException("AI API调用失败: " + e.getMessage());
        }
    }

    private String getFallbackResponse(String question) {
        // 预设的农业知识库回复
        Map<String, String> knowledgeBase = new HashMap<>();
        knowledgeBase.put("小麦", "小麦种植要注意选择适合当地气候的品种，适时播种，合理施肥，做好田间管理和病虫害防治工作。");
        knowledgeBase.put("玉米", "玉米种植需要充足的阳光和水分，注意密度控制，及时追肥，防治玉米螟等害虫。");
        knowledgeBase.put("水稻", "水稻种植要做好水分管理，保持浅水分蘖，深水护苗，干湿交替，注意稻瘟病等病害防治。");
        knowledgeBase.put("施肥", "施肥要遵循基肥为主、追肥为辅的原则，根据土壤肥力和作物需求合理搭配氮磷钾肥料。");
        knowledgeBase.put("病虫害", "病虫害防治要坚持预防为主、综合防治的方针，选用抗病品种，合理轮作，科学用药。");
        knowledgeBase.put("土壤", "土壤管理要注重有机质的补充，定期深耕松土，保持土壤结构良好，调节土壤酸碱度。");
        knowledgeBase.put("灌溉", "灌溉要根据作物生长阶段和土壤墒情合理安排，提倡节水灌溉技术，避免过量灌溉。");

        // 简单匹配回复
        for (Map.Entry<String, String> entry : knowledgeBase.entrySet()) {
            if (question.contains(entry.getKey())) {
                return entry.getValue() + "\n\n如需更详细的指导建议，请联系当地农技推广站或提供更多具体信息。";
            }
        }

        return "感谢您的咨询！这是一个很有价值的农业问题。建议您：\n" +
               "1. 结合当地气候条件和土壤特点\n" +
               "2. 咨询当地农技推广站获取专业指导\n" +
               "3. 参考当地成功种植经验\n" +
               "4. 如有具体情况可详细描述，我们将提供更精准的建议。";
    }
}
