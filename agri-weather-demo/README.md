# 农业气象智能咨询系统

基于 Spring Boot + Vue3 + AI 的农业气象服务平台，提供实时气象监测和智能农业咨询服务。

## 🌟 主要功能

- **实时气象监测** - 温度、湿度、风速、光照等数据监测
- **天气预警系统** - 霜冻、高温、强降雨等预警信息
- **气象预报可视化** - 带网格坐标轴的温度趋势图表
- **🤖 AI智能咨询** - 集成DeepSeek大模型的农业技术问答
- **地图服务** - 高德地图集成，支持位置定位和天气查询
- **响应式设计** - 支持PC和移动端访问

## 🏗️ 技术架构

```
agri-weather-demo/
  backend/        # Spring Boot 服务，端口 8080
    ├── AiConsultationController.java    # AI咨询接口
    ├── WeatherController.java           # 气象数据接口
    └── AmapController.java              # 地图服务接口
  frontend/       # Vue3 + Vite 应用，端口 5173
    └── App.vue                          # 主应用组件
  AI_CONFIG.md    # AI配置说明文档
```

## 🚀 快速启动

### 1. 后端启动
```bash
cd backend
mvn spring-boot:run
```

### 2. 前端启动
```bash
cd frontend
npm install
npm run dev
```

### 3. 访问应用
打开浏览器访问 `http://localhost:5173`

## 🤖 AI智能咨询配置

系统已集成DeepSeek AI大模型，提供智能农业技术咨询。

### 配置API密钥（可选）

1. 获取DeepSeek API密钥：访问 [DeepSeek官网](https://platform.deepseek.com/)
2. 配置环境变量：
   ```bash
   # Windows
   set DEEPSEEK_API_KEY=你的API密钥
   
   # Linux/Mac
   export DEEPSEEK_API_KEY=你的API密钥
   ```
3. 重启后端服务

> 📝 如不配置API密钥，系统会使用预设的农业知识库回复

详细配置说明请参考：[AI_CONFIG.md](AI_CONFIG.md)

## 📱 功能页面

- **首页** - 功能导航和平台介绍
- **气象数据** - 实时监测、预警信息、未来预报
- **咨询服务** - AI智能问答、常见问题、专家联系
- **种植方案** - 待开发
- **农业政策** - 待开发
- **系统公告** - 待开发

## 🛠️ 核心特性

### 气象数据可视化
- SVG温度趋势图表，带网格和坐标轴
- 实时气象数据监测仪表盘
- 天气预报卡片，集成天气emoji图标

### AI智能咨询
- DeepSeek大模型驱动的农业问答
- 支持种植管理、病虫害防治、土壤管理等咨询
- 智能对话界面，打字动画效果
- 常见问题快速选择

### 地图服务
- 高德地图集成
- 自动定位和手动搜索
- 反向地理编码
- 历史查询记录

## 🔧 技术栈

**后端**
- Spring Boot 2.7.18
- JDK 17
- Maven
- RestTemplate (HTTP客户端)

**前端**
- Vue 3 + Composition API
- TypeScript
- Vite
- Axios
- 响应式CSS设计

**第三方服务**
- 高德地图API
- DeepSeek AI API

## 📋 API接口

### 气象服务
- `GET /api/weather/realtime` - 实时气象数据
- `GET /api/weather/alerts` - 天气预警信息
- `GET /api/reports/summary` - 气象决策报告

### AI咨询服务
- `POST /api/ai/consultation` - AI智能问答

### 地图服务
- `GET /api/amap/ip` - IP定位
- `GET /api/amap/weather` - 区域天气查询
- `GET /api/amap/forecast` - 天气预报
- `GET /api/amap/geocode` - 地理编码
- `GET /api/amap/reverse` - 反向地理编码

## 🎯 未来扩展

- [ ] 用户注册登录系统
- [ ] 角色权限管理（农民/专家/管理员）
- [ ] MySQL数据库集成
- [ ] 历史数据存储和分析
- [ ] 更多AI模型支持（GPT、Claude等）
- [ ] 移动端APP开发
- [ ] 消息推送服务
- [ ] 数据导出功能

## 📞 技术支持

如有问题，请查看项目文档或联系开发团队。

---

**License**: MIT  
**作者**: 农业科技团队  
**更新时间**: 2025年8月
