# AI智能问答配置说明

## DeepSeek API接入配置

本系统已集成DeepSeek AI大模型，为农业咨询服务提供智能化问答支持。

### 1. 获取API密钥

1. 访问 [DeepSeek官网](https://platform.deepseek.com/)
2. 注册账号并登录
3. 在控制台中创建API密钥
4. 复制生成的API密钥

### 2. 配置方式

#### 方式一：环境变量配置（推荐）
```bash
# Windows
set DEEPSEEK_API_KEY=你的API密钥

# Linux/Mac
export DEEPSEEK_API_KEY=你的API密钥
```

#### 方式二：配置文件配置
在 `backend/src/main/resources/application.yml` 中直接配置：
```yaml
deepseek:
  api:
    key: 你的API密钥
    url: https://api.deepseek.com/v1/chat/completions
```

### 3. 功能特性

- **智能问答**：基于DeepSeek大模型的农业专业知识问答
- **上下文理解**：能够理解复杂的农业技术问题
- **专业回复**：针对农业领域优化的回答质量
- **降级机制**：API不可用时自动降级到预设回复

### 4. 使用说明

1. 配置API密钥后重启后端服务
2. 访问咨询服务页面
3. 输入农业相关问题
4. 系统会自动调用AI模型生成专业回答
5. AI回答会有特殊标识（🤖 AI）

### 5. 注意事项

- 确保网络能够访问DeepSeek API
- API调用会产生费用，请注意用量控制
- 如未配置API密钥，系统会使用预设的知识库回复
- 建议在生产环境中使用环境变量方式配置密钥

### 6. 故障排除

如果AI回答不可用：
1. 检查API密钥是否正确配置
2. 检查网络连接是否正常
3. 查看后端日志获取详细错误信息
4. 系统会自动降级到预设回复模式

### 7. 扩展支持

系统架构支持接入其他AI模型：
- OpenAI GPT系列
- Claude
- 文心一言
- 通义千问
- ChatGLM

只需修改相应的API调用代码即可。

## 联系支持

如有技术问题，请联系开发团队或查看项目文档。
