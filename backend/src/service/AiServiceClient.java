@Service
public class AiServiceClient {

    private final RestTemplate restTemplate;
    private final String aiBaseUrl;

    public AiServiceClient(@Value("${ai.service.url}") String aiBaseUrl) {
        this.aiBaseUrl = aiBaseUrl;
        RestTemplateBuilder builder = new RestTemplateBuilder();
        this.restTemplate = builder
            .setConnectTimeout(Duration.ofSeconds(10))
            .setReadTimeout(Duration.ofSeconds(10))
            .build();
    }

    public Map describe(String input) {
        return callAi("/describe", Map.of("input", input));
    }

    public Map recommend(String input) {
        return callAi("/recommend", Map.of("input", input));
    }

    public Map generateReport(String input) {
        return callAi("/generate-report", Map.of("input", input));
    }

    private Map callAi(String path, Map body) {
        try {
            ResponseEntity response = restTemplate.postForEntity(
                aiBaseUrl + path, body, Map.class);
            return response.getBody();
        } catch (Exception e) {
            log.error("AI service call failed for {}: {}", path, e.getMessage());
            return null;
        }
    }
}