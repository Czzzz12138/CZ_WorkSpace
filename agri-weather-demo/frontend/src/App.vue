<template>
  <div class="page">
    <!-- 顶部导航栏 -->
    <nav class="navbar">
      <div class="nav-left">
        <div class="logo-circle">
          <span class="logo-icon">🌾</span>
        </div>
        <h1 class="platform-title">智慧农业服务平台</h1>
      </div>
      
      <div class="nav-center">
        <a href="#" class="nav-link" :class="{ active: currentPage === 'home' }" @click="switchPage('home')">首页</a>
        <a href="#" class="nav-link" :class="{ active: currentPage === 'weather' }" @click="switchPage('weather')">气象数据</a>
        <a href="#" class="nav-link" :class="{ active: currentPage === 'planting' }" @click="switchPage('planting')">种植方案</a>
        <a href="#" class="nav-link" :class="{ active: currentPage === 'consultation' }" @click="switchPage('consultation')">咨询服务</a>
        <a href="#" class="nav-link" :class="{ active: currentPage === 'policy' }" @click="switchPage('policy')">农业政策</a>
        <a href="#" class="nav-link" :class="{ active: currentPage === 'announcement' }" @click="switchPage('announcement')">系统公告</a>
      </div>
      
      <div class="nav-right">
        <button class="btn-login">登录</button>
        <button class="btn-register">注册</button>
      </div>
    </nav>

    <!-- 页面标题区域 -->
    <div class="hero-section">
      <div class="page-content">
        <h2 class="hero-title">智慧农业, 科技兴农</h2>
        <p class="hero-subtitle">实时气象监测 · 智能种植指导 · 专家在线咨询</p>
      </div>
    </div>

        <!-- 主要内容区域 -->
    <div class="page-content">
      <!-- 首页内容 -->
      <div v-if="currentPage === 'home'" class="home-content">
        <div class="welcome-section">
          <h2>欢迎使用智慧农业服务平台</h2>
          <p>选择下方功能模块开始使用</p>
        </div>
        
        <div class="feature-grid">
          <div class="feature-card" @click="switchPage('weather')">
            <div class="feature-icon">🌤️</div>
            <h3>气象数据</h3>
            <p>实时天气监测、预警信息、气象分析</p>
          </div>
          <div class="feature-card" @click="switchPage('planting')">
            <div class="feature-icon">🌱</div>
            <h3>种植方案</h3>
            <p>智能种植指导、作物管理、生长监测</p>
          </div>
          <div class="feature-card" @click="switchPage('consultation')">
            <div class="feature-icon">👨‍🌾</div>
            <h3>咨询服务</h3>
            <p>专家在线咨询、技术指导、问题解答</p>
          </div>
          <div class="feature-card" @click="switchPage('policy')">
            <div class="feature-icon">📋</div>
            <h3>农业政策</h3>
            <p>政策解读、补贴信息、法规指导</p>
          </div>
          <div class="feature-card" @click="switchPage('announcement')">
            <div class="feature-icon">📢</div>
            <h3>系统公告</h3>
            <p>平台通知、政策信息、重要更新</p>
          </div>
        </div>
      </div>

      <!-- 气象数据页面 -->
      <div v-if="currentPage === 'weather'" class="weather-content">
        <div class="page-header">
          <h2>气象数据</h2>
          <p>实时监测、预警分析、气象预报</p>
        </div>
        
        <!-- 地图与天气模块 -->
        <section class="card map-card">
          <div class="card-head">
            <h2>地图与天气</h2>
            <button class="btn" @click="loadAmap">同步</button>
          </div>
          <div class="amap">
            <div class="amap-toolbar">
              <button class="btn" @click="onGeolocate">自动定位</button>
              <select class="select" v-model="quickCity" @change="onSelectQuickCity">
                <option value="">常用城市</option>
                <option v-for="c in quickCities" :key="c" :value="c">{{ c }}</option>
              </select>
              <select class="select" v-model="historySelected" @change="onSelectHistory">
                <option value="">历史记录</option>
                <option v-for="h in histories" :key="h" :value="h">{{ h }}</option>
              </select>
              <input class="input" placeholder="输入城市/地址后回车" v-model="address" @keyup.enter="onSearchAddress" />
              <button class="btn" @click="onSearchAddress">查询</button>
            </div>
            <div class="kv"><span>省/市</span><b>{{ amap.city ? amap.province + ' / ' + amap.city : '—' }}</b></div>
            <div class="kv"><span>行政区</span><b>{{ amap.adcode || '—' }}</b></div>
            <div class="kv"><span>天气</span><b>{{ weather.weather || '—' }}（{{ weather.temperature ?? '-' }}°C，湿度{{ weather.humidity ?? '-' }}%）</b></div>
            <div id="amapContainer" class="mapbox"></div>
          </div>
        </section>

        <!-- 气象数据网格 -->
        <div class="grid three-cols">
          <section class="card">
            <div class="card-head">
              <h2>实时气象</h2>
              <div class="realtime-controls">
                <span class="data-source" v-if="amap.city">📍 {{ amap.city }}</span>
                <button class="btn" @click="loadRealtime">同步</button>
              </div>
            </div>
            <div class="stats">
              <div class="stat">
                <span>测站</span><b>{{ realtime.location || '-' }}</b>
              </div>
              <div class="stat">
                <span>温度(°C)</span><b>{{ realtime.temperature ?? '-' }}</b>
              </div>
              <div class="stat">
                <span>湿度</span>
                <div class="meter" :title="formatPercent(realtime.humidity)">
                  <div class="bar blue" :style="{ width: humidityPct + '%' }"></div>
                </div>
                <b>{{ formatPercent(realtime.humidity) }}</b>
              </div>
              <div class="stat">
                <span>风向/风力</span><b>{{ weather.winddirection ? (weather.winddirection + ' / ' + (weather.windpower || '-')) : (realtime.windSpeed ? (realtime.windSpeed + ' m/s') : '-') }}</b>
              </div>
              <div class="stat">
                <span>光照(lux)</span><b>{{ realtime.illumination ?? '-' }}</b>
              </div>
                <div class="stat"><span>时间</span><b>{{ formatTime(realtime.timestamp) }}</b></div>
            </div>
          </section>

          <section class="card">
            <div class="card-head">
              <h2>预警信息</h2>
              <button class="btn" @click="loadAlerts">获取</button>
            </div>
            <ul class="alerts">
              <li v-for="(it, idx) in (alerts.items || [])" :key="idx">
                <span class="tag" :class="it.level">{{ it.level }}</span>
                <div class="alert-body">
                  <b>{{ zhAlertType(it.type) }}</b>
                  <p>{{ it.message }}</p>
                  <small>{{ formatTime(it.issuedAt) }}</small>
                </div>
              </li>
              <li v-if="!(alerts.items && alerts.items.length)">暂无预警</li>
            </ul>
          </section>

          <section class="card">
            <div class="card-head">
              <h2>未来预报</h2>
              <button class="btn" @click="loadForecast">刷新</button>
            </div>
            <div class="forecast">
              <svg v-if="trendPoints && chartData" :viewBox="'0 0 320 140'" class="chart">
                <!-- 背景 -->
                <rect x="0" y="0" width="320" height="140" fill="#fafbfc" />
                
                <!-- 网格线 -->
                <g class="grid-lines">
                  <line 
                    v-for="(line, idx) in chartData.gridLines" 
                    :key="'grid-' + idx"
                    :x1="line.x1" :y1="line.y1" :x2="line.x2" :y2="line.y2"
                    stroke="#e2e8f0" stroke-width="1" stroke-dasharray="2,2"
                  />
                </g>
                
                <!-- Y轴坐标标签 -->
                <g class="temp-labels">
                  <text 
                    v-for="(label, idx) in chartData.tempLabels" 
                    :key="'temp-' + idx"
                    :x="10" :y="label.y + 3"
                    font-size="10" fill="#64748b" font-family="monospace"
                  >
                    {{ label.temp }}°
                  </text>
                </g>
                
                <!-- 温度趋势线 -->
                <polyline 
                  :points="trendPoints" 
                  fill="none" 
                  stroke="#0ea5e9" 
                  stroke-width="3"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
                
                <!-- 温度点 -->
                <g class="temp-points">
                  <circle 
                    v-for="(point, idx) in trendPoints.split(' ')" 
                    :key="'point-' + idx"
                    :cx="point.split(',')[0]" 
                    :cy="point.split(',')[1]"
                    r="4" 
                    fill="#0ea5e9" 
                    stroke="#fff" 
                    stroke-width="2"
                  />
                </g>
                
                <!-- X轴日期标签 -->
                <g class="date-labels">
                  <text 
                    v-for="(label, idx) in chartData.dateLabels" 
                    :key="'date-' + idx"
                    :x="label.x" :y="135"
                    font-size="10" fill="#64748b" text-anchor="middle"
                  >
                    {{ label.date }}
                  </text>
                </g>
              </svg>
              
              <div v-for="(d, idx) in forecast.days || []" :key="idx" class="day">
                <div class="date">{{ d.date }}（周{{ d.week }}）</div>
                <div class="weather">
                  <span class="weather-emoji">{{ getWeatherEmoji(d.dayweather) }}</span>
                  白天 {{ d.dayweather }} 
                  <span class="weather-divider">/</span> 
                  <span class="weather-emoji">{{ getWeatherEmoji(d.nightweather) }}</span>
                  夜间 {{ d.nightweather }}
                </div>
                <div class="temps">
                  <span class="temp-range">{{ d.nighttemp }}°C ~ {{ d.daytemp }}°C</span>
                </div>
                <div class="wind">
                  <span class="wind-icon">💨</span>
                  {{ d.daywind }} 风力 {{ d.daypower }}
                </div>
              </div>
              <div v-if="!(forecast.days && forecast.days.length)" class="empty">暂无数据</div>
            </div>
          </section>
        </div>
      </div>

      <!-- 其他页面占位 -->
      <div v-if="currentPage === 'planting'" class="other-content">
        <h2>种植方案</h2>
        <p>功能开发中...</p>
      </div>
      
      <div v-if="currentPage === 'consultation'" class="consultation-content">
        <div class="page-header">
          <h2>专家咨询服务</h2>
          <p>农业技术问题在线答疑，专业指导助您丰收</p>
        </div>
        
        <div class="consultation-layout">
          <!-- 对话区域 -->
          <div class="chat-section">
            <div class="chat-header">
              <div class="expert-info">
                <div class="expert-avatar">🤖</div>
                <div class="expert-details">
                  <h3>AI智能农业助手</h3>
                  <span class="status online">AI已接入 • 在线服务</span>
                </div>
              </div>
              <div class="chat-stats">
                <div class="ai-badge">
                  <span class="ai-icon">✨</span>
                  <span>DeepSeek驱动</span>
                </div>
              </div>
            </div>
            
            <div class="chat-messages" ref="chatMessages">
              <div 
                v-for="message in messages" 
                :key="message.id"
                :class="['message', message.type]"
                :data-source="message.avatar === '🤖' ? 'ai' : 'human'"
              >
                <div class="message-avatar">
                  {{ message.type === 'expert' ? message.avatar : '🧑‍🌾' }}
                </div>
                <div class="message-content">
                  <div class="message-text">{{ message.content }}</div>
                  <div class="message-time">{{ message.time }}</div>
                </div>
              </div>
              
              <div v-if="isTyping" class="message expert typing">
                <div class="message-avatar">👨‍🌾</div>
                <div class="message-content">
                  <div class="typing-indicator">
                    <span></span>
                    <span></span>
                    <span></span>
                  </div>
                </div>
              </div>
            </div>
            
            <div class="chat-input">
              <input 
                type="text" 
                v-model="currentQuestion"
                placeholder="请输入您的农业问题..."
                @keyup.enter="askQuestion(currentQuestion)"
                class="question-input"
              />
              <button 
                @click="askQuestion(currentQuestion)"
                :disabled="!currentQuestion.trim() || isTyping"
                class="send-btn"
              >
                <span v-if="!isTyping">发送</span>
                <span v-else>...</span>
              </button>
            </div>
          </div>
          
          <!-- 常见问题区域 -->
          <div class="faq-section">
            <h3>常见问题</h3>
            <p class="faq-subtitle">点击问题快速咨询</p>
            
            <div class="faq-categories">
              <div 
                v-for="category in frequentQuestions" 
                :key="category.id"
                class="faq-category"
              >
                <h4 class="category-title">
                  <span class="category-icon">
                    {{ category.category === '种植管理' ? '🌱' : 
                        category.category === '病虫害防治' ? '🐛' : 
                        category.category === '土壤管理' ? '🌍' : '🌤️' }}
                  </span>
                  {{ category.category }}
                </h4>
                <div class="questions-list">
                  <button 
                    v-for="question in category.questions" 
                    :key="question"
                    @click="selectFrequentQuestion(question)"
                    class="question-btn"
                    :disabled="isTyping"
                  >
                    {{ question }}
                  </button>
                </div>
              </div>
            </div>
            
            <div class="contact-info">
              <h4>📞 紧急联系</h4>
              <p>农技热线：400-123-4567</p>
              <p>在线时间：8:00-20:00</p>
            </div>
            
            <div class="ai-config-info">
              <h4>🤖 AI智能问答</h4>
              <p>系统已接入DeepSeek AI模型</p>
              <p>提供24小时智能农业咨询</p>
              <small>💡 配置API密钥可获得更精准回答</small>
            </div>
          </div>
        </div>
      </div>
      
      <div v-if="currentPage === 'policy'" class="other-content">
        <h2>农业政策</h2>
        <p>功能开发中...</p>
      </div>
      
      <div v-if="currentPage === 'announcement'" class="other-content">
        <h2>系统公告</h2>
        <p>功能开发中...</p>
      </div>
    </div>
    </div>
</template>

<script setup lang="ts">
import axios from 'axios';
import { ref, computed, onMounted } from 'vue';

type Realtime = {
  timestamp?: string;
  location?: string;
  temperature?: number;
  humidity?: number;
  windSpeed?: number;
  illumination?: number;
}

type AlertItem = { level: string; type: string; message: string; issuedAt: string }
type Alerts = { count?: number; items?: AlertItem[] }
type Report = { generatedAt?: string; recommendation?: string; riskIndex?: number }

const currentPage = ref('home');
const realtime = ref<Realtime>({});
const alerts = ref<Alerts>({});
const report = ref<Report>({});
const amap = ref<{ province?: string; city?: string; adcode?: string; centerLng?: number; centerLat?: number }>({});
const weather = ref<{ weather?: string; temperature?: string; humidity?: string; winddirection?: string; windpower?: string }>({});
const forecast = ref<{ days?: any[] }>({});
const trendPoints = computed(() => {
  const days = forecast.value?.days || [];
  const temps = days.map((d: any) => Number(d.daytemp)).filter((n: number) => !Number.isNaN(n));
  if (temps.length === 0) return '';
  const min = Math.min(...temps), max = Math.max(...temps);
  const w = 320, h = 120; const pad = 20;
  const step = temps.length > 1 ? (w - pad * 2) / (temps.length - 1) : 0;
  const mapY = (t: number) => pad + (h - pad * 2) * (1 - (t - min) / Math.max(1, (max - min)));
  return temps.map((t: number, i: number) => `${pad + i * step},${mapY(t)}`).join(' ');
});

const chartData = computed(() => {
  const days = forecast.value?.days || [];
  const temps = days.map((d: any) => Number(d.daytemp)).filter((n: number) => !Number.isNaN(n));
  if (temps.length === 0) return null;
  
  const min = Math.min(...temps), max = Math.max(...temps);
  const w = 320, h = 120, pad = 20;
  
  // 生成网格线
  const gridLines = [];
  for (let i = 0; i <= 4; i++) {
    const y = pad + (h - pad * 2) * (i / 4);
    gridLines.push({ x1: pad, y1: y, x2: w - pad, y2: y });
  }
  
  // 生成温度标签
  const tempLabels = [];
  for (let i = 0; i <= 4; i++) {
    const temp = max - (max - min) * (i / 4);
    const y = pad + (h - pad * 2) * (i / 4);
    tempLabels.push({ temp: Math.round(temp), y });
  }
  
  // 生成日期标签
  const dateLabels = [];
  const step = temps.length > 1 ? (w - pad * 2) / (temps.length - 1) : 0;
  days.forEach((d: any, i: number) => {
    if (!isNaN(Number(d.daytemp))) {
      const x = pad + i * step;
      dateLabels.push({ 
        date: d.date ? d.date.substring(5) : '', // 只显示月-日
        x 
      });
    }
  });
  
  return { gridLines, tempLabels, dateLabels, min, max };
});
let map: any = null;
let marker: any = null;
const address = ref('');
const quickCities = ['北京', '上海', '广州', '深圳', '杭州', '成都', '南京', '武汉'];
const quickCity = ref('');
const histories = ref<string[]>(JSON.parse(localStorage.getItem('amapHistory') || '[]'));
const historySelected = ref('');

// 咨询服务相关数据
const currentQuestion = ref('');
const messages = ref<Array<{id: number, type: 'user' | 'expert', content: string, time: string, avatar?: string}>>([
  {
    id: 1,
    type: 'expert',
    content: '您好！我是农业专家助手，很高兴为您服务。您可以咨询任何关于农业种植、病虫害防治、土壤管理等方面的问题。',
    time: new Date().toLocaleTimeString(),
    avatar: '👨‍🌾'
  }
]);
const isTyping = ref(false);

const frequentQuestions = [
  {
    id: 1,
    category: '种植管理',
    questions: [
      '小麦什么时候播种最合适？',
      '玉米施肥的最佳时间是什么时候？',
      '水稻田间管理要注意哪些事项？',
      '蔬菜大棚如何控制温湿度？'
    ]
  },
  {
    id: 2,
    category: '病虫害防治',
    questions: [
      '小麦条纹花叶病如何防治？',
      '玉米螟虫害的识别和防治方法？',
      '番茄晚疫病的预防措施有哪些？',
      '蚜虫防治的生物方法有哪些？'
    ]
  },
  {
    id: 3,
    category: '土壤管理',
    questions: [
      '如何判断土壤酸碱度是否合适？',
      '土壤板结如何改良？',
      '有机肥和化肥如何搭配使用？',
      '盐碱地改良的有效方法？'
    ]
  },
  {
    id: 4,
    category: '气象服务',
    questions: [
      '如何根据天气预报安排农事活动？',
      '霜冻预警时应该采取哪些防护措施？',
      '强降雨对农作物的影响及应对策略？',
      '干旱天气下如何进行灌溉管理？'
    ]
  }
];

const expertResponses: Record<string, string> = {
  '小麦什么时候播种最合适？': '小麦播种时间主要分为冬小麦和春小麦。冬小麦一般在9-10月播种，春小麦在3-4月播种。具体时间要根据当地气候条件确定，确保播种后有足够的积温。',
  '玉米施肥的最佳时间是什么时候？': '玉米施肥分为基肥、苗期追肥和穗期追肥。基肥在播种前施入，苗期在6-8叶时追施，穗期在大喇叭口期追施。要根据土壤肥力和玉米品种调整施肥量。',
  '水稻田间管理要注意哪些事项？': '水稻田间管理主要包括：水分管理（深水返青、浅水分蘖、足水孕穗）、施肥管理（基肥、分蘖肥、穗肥）、病虫害防治和杂草控制。',
  '蔬菜大棚如何控制温湿度？': '大棚温度控制：白天25-30℃，夜间15-18℃。湿度控制：空气相对湿度60-80%。可通过通风、遮阳网、加温设备、除湿等措施调节。',
  '小麦条纹花叶病如何防治？': '小麦条纹花叶病防治：选用抗病品种、种子处理、适期播种、田间清洁、药剂防治。可用吡虫啉拌种，发病初期喷施病毒清等药剂。',
  '玉米螟虫害的识别和防治方法？': '玉米螟识别：叶片上有虫孔、茎秆内有虫道。防治：生物防治（释放赤眼蜂）、物理防治（杀虫灯）、化学防治（BT菌剂、氯虫苯甲酰胺）。',
  '番茄晚疫病的预防措施有哪些？': '番茄晚疫病预防：选用抗病品种、合理密植、控制湿度、轮作倒茬。药剂预防可用代森锰锌、烯酰吗啉等保护性杀菌剂。',
  '蚜虫防治的生物方法有哪些？': '蚜虫生物防治：保护天敌（瓢虫、草蛉）、释放蚜茧蜂、种植驱避植物（薄荷、万寿菊）、使用生物农药（苦参碱、印楝素）。',
  '如何判断土壤酸碱度是否合适？': '土壤pH值测定：使用土壤pH计或试纸。大多数作物适宜pH 6.0-7.5。酸性土壤可施用石灰改良，碱性土壤可施用硫磺或有机酸改良。',
  '土壤板结如何改良？': '土壤板结改良：增施有机肥、深耕松土、种植绿肥、覆盖秸秆、控制机械压实。有机肥能改善土壤结构，增加土壤有机质含量。',
  '有机肥和化肥如何搭配使用？': '有机肥与化肥配合：有机肥做基肥，化肥做追肥；有机肥提供缓效养分，化肥提供速效养分。推荐有机肥占60-70%，化肥占30-40%。',
  '盐碱地改良的有效方法？': '盐碱地改良：排水降盐、深耕翻压、施用有机肥、种植耐盐植物、覆盖薄膜。也可施用石膏、硫磺等改良剂降低土壤盐分。',
  '如何根据天气预报安排农事活动？': '根据天气预报安排农事：晴天适合播种、收获、施药；雨前施肥效果好；雨后适合移栽；大风天避免喷药；低温时注意防冻。',
  '霜冻预警时应该采取哪些防护措施？': '霜冻防护措施：覆盖薄膜、点燃熏烟、灌水保温、喷施防冻剂、搭建风障。对果树可用石灰水涂白树干，延迟开花期。',
  '强降雨对农作物的影响及应对策略？': '强降雨影响：土壤积水、根系缺氧、病害加重。应对策略：及时排水、中耕松土、补施肥料、喷施叶面肥、防治病害。',
  '干旱天气下如何进行灌溉管理？': '干旱灌溉管理：节水灌溉（滴灌、喷灌）、适时适量、避开高温时段、覆盖保墒、选用抗旱品种。关键生育期保证水分供应。'
};

const humidityPct = computed(() => {
  const v = realtime.value.humidity;
  if (v === undefined || v === null) return 0;
  return Math.max(0, Math.min(100, Math.round(v * 100)));
});
const riskPct = computed(() => {
  const v = report.value.riskIndex;
  if (v === undefined || v === null) return 0;
  return Math.max(0, Math.min(100, Math.round(v * 100)));
});

function switchPage(page: string) {
  currentPage.value = page;
}

function formatTime(t?: string) {
  if (!t) return '-';
  try { return new Date(t).toLocaleString('zh-CN'); } catch { return t; }
}
function formatPercent(n?: number) {
  if (n === undefined || n === null) return '-';
  return Math.round(n * 100) + '%';
}
function zhAlertType(t?: string) {
  if (!t) return '未知';
  const map: Record<string, string> = { FROST: '霜冻', HEAT: '高温', WIND: '大风', RAIN: '强降雨' };
  return map[t] || t;
}

function getWeatherEmoji(weather?: string) {
  if (!weather) return '☀️';
  const weatherMap: Record<string, string> = {
    '晴': '☀️',
    '多云': '⛅',
    '阴': '☁️',
    '小雨': '🌦️',
    '中雨': '🌧️',
    '大雨': '⛈️',
    '暴雨': '🌩️',
    '雷阵雨': '⛈️',
    '小雪': '🌨️',
    '中雪': '❄️',
    '大雪': '🌨️',
    '雨夹雪': '🌨️',
    '雾': '🌫️',
    '沙尘暴': '🌪️',
    '霾': '😷',
    '风': '💨'
  };
  
  // 尝试精确匹配
  if (weatherMap[weather]) return weatherMap[weather];
  
  // 模糊匹配
  if (weather.includes('晴')) return '☀️';
  if (weather.includes('云')) return '⛅';
  if (weather.includes('阴')) return '☁️';
  if (weather.includes('雨')) {
    if (weather.includes('大') || weather.includes('暴')) return '⛈️';
    if (weather.includes('中')) return '🌧️';
    return '🌦️';
  }
  if (weather.includes('雪')) return '🌨️';
  if (weather.includes('雷')) return '⛈️';
  if (weather.includes('雾')) return '🌫️';
  if (weather.includes('风') || weather.includes('沙')) return '💨';
  
  return '☀️'; // 默认晴天
}

// 咨询服务功能
async function askQuestion(question: string) {
  if (!question.trim()) return;
  
  // 添加用户消息
  messages.value.push({
    id: Date.now(),
    type: 'user',
    content: question,
    time: new Date().toLocaleTimeString()
  });
  
  currentQuestion.value = '';
  isTyping.value = true;
  
  try {
    // 调用后端AI接口
    const response = await axios.post('/api/ai/consultation', {
      question: question
    });
    
    const aiResponse = response.data;
    
    if (aiResponse.success) {
      // 添加AI回复
      messages.value.push({
        id: Date.now() + 1,
        type: 'expert',
        content: aiResponse.response,
        time: new Date().toLocaleTimeString(),
        avatar: aiResponse.source === 'ai' ? '🤖' : '👨‍🌾'
      });
      
      // 如果是AI回复，可以添加来源说明
      if (aiResponse.source === 'ai') {
        setTimeout(() => {
          messages.value.push({
            id: Date.now() + 2,
            type: 'expert',
            content: '💡 此回答由AI智能生成，如需更详细指导请联系专业农技人员。',
            time: new Date().toLocaleTimeString(),
            avatar: '💡'
          });
        }, 500);
      }
    } else {
      // 错误处理
      messages.value.push({
        id: Date.now() + 1,
        type: 'expert',
        content: '抱歉，暂时无法处理您的问题，请稍后重试或联系在线客服。',
        time: new Date().toLocaleTimeString(),
        avatar: '😔'
      });
    }
  } catch (error) {
    console.error('AI咨询请求失败:', error);
    
    // 失败时使用本地预设回复
    const fallbackResponse = expertResponses[question] || '感谢您的提问！由于网络问题，暂时无法获取AI回复。建议您：\n1. 检查网络连接后重试\n2. 联系当地农技推广站\n3. 提供更多具体信息以便我们给出更精准的建议';
    
    messages.value.push({
      id: Date.now() + 1,
      type: 'expert',
      content: fallbackResponse,
      time: new Date().toLocaleTimeString(),
      avatar: '👨‍🌾'
    });
  } finally {
    isTyping.value = false;
    
    // 自动滚动到底部
    setTimeout(() => {
      const chatContainer = document.querySelector('.chat-messages');
      if (chatContainer) {
        chatContainer.scrollTop = chatContainer.scrollHeight;
      }
    }, 100);
  }
}

function selectFrequentQuestion(question: string) {
  currentQuestion.value = question;
  askQuestion(question);
}

async function loadRealtime() {
  // 如果有地图模块的位置信息，使用高德地图的天气数据
  if (amap.value.adcode) {
    try {
      const wRes = await axios.get('/api/amap/weather', { params: { adcode: amap.value.adcode } });
      weather.value = wRes.data as any;
      applyWeatherToRealtime();
    } catch (error) {
      console.error('获取天气数据失败:', error);
      // 如果获取高德天气失败，fallback到模拟数据
      const { data } = await axios.get('/api/weather/realtime');
      realtime.value = data;
    }
  } else {
    // 如果没有位置信息，先获取位置，然后获取天气数据
    try {
      await loadAmap();
      if (amap.value.adcode) {
        const wRes = await axios.get('/api/amap/weather', { params: { adcode: amap.value.adcode } });
        weather.value = wRes.data as any;
        applyWeatherToRealtime();
      } else {
        // 如果还是没有位置信息，使用模拟数据
        const { data } = await axios.get('/api/weather/realtime');
        realtime.value = data;
      }
    } catch (error) {
      console.error('获取位置或天气数据失败:', error);
      // fallback到模拟数据
      const { data } = await axios.get('/api/weather/realtime');
      realtime.value = data;
    }
  }
}
async function loadAlerts() {
  const { data } = await axios.get('/api/weather/alerts');
  alerts.value = data;
}
async function loadReport() {
  const { data } = await axios.get('/api/reports/summary');
  report.value = data;
}

async function loadAmap() {
  const ipRes = await axios.get('/api/amap/ip');
  amap.value = ipRes.data;
  if (amap.value.adcode) {
    const wRes = await axios.get('/api/amap/weather', { params: { adcode: amap.value.adcode } });
    weather.value = wRes.data as any;
  }
  if (amap.value.centerLng && amap.value.centerLat && (window as any).AMap) {
    if (!map) {
      map = new (window as any).AMap.Map('amapContainer', {
        zoom: 11,
        center: [amap.value.centerLng, amap.value.centerLat],
      });
      map.addControl(new (window as any).AMap.Scale());
      map.addControl(new (window as any).AMap.ToolBar());
    } else {
      map.setZoomAndCenter(11, [amap.value.centerLng, amap.value.centerLat]);
    }
    if (!marker) {
      marker = new (window as any).AMap.Marker({ position: [amap.value.centerLng, amap.value.centerLat] });
      map.add(marker);
    } else {
      marker.setPosition([amap.value.centerLng, amap.value.centerLat]);
    }
    // 地图点击：反向地理编码并刷新天气
    map.on('click', async (e: any) => {
      const lng = e.lnglat.lng;
      const lat = e.lnglat.lat;
      const rev = await axios.get('/api/amap/reverse', { params: { lng, lat } });
      amap.value = rev.data as any;
      if (amap.value.adcode) {
        const wRes = await axios.get('/api/amap/weather', { params: { adcode: amap.value.adcode } });
        weather.value = wRes.data as any;
        await loadForecast();
      }
      marker.setPosition([lng, lat]);
      map.setZoomAndCenter(11, [lng, lat]);
      applyWeatherToRealtime();
    });
  }
  // 初始加载完成后，同步数据到实时气象模块
  applyWeatherToRealtime();
}

async function loadForecast() {
  if (!amap.value.adcode) return;
  const { data } = await axios.get('/api/amap/forecast', { params: { adcode: amap.value.adcode } });
  forecast.value = data as any;
}

function saveHistory(val: string) {
  if (!val) return;
  const arr = new Set([val, ...histories.value]);
  histories.value = Array.from(arr).slice(0, 8);
  localStorage.setItem('amapHistory', JSON.stringify(histories.value));
}

function applyWeatherToRealtime() {
  if (!weather.value) return;
  
  // 设置位置信息
  realtime.value.location = amap.value.city || amap.value.province || '未知位置';
  
  // 设置温度
  const t = Number((weather.value as any).temperature);
  if (!Number.isNaN(t)) realtime.value.temperature = t;
  
  // 设置湿度（高德返回的是百分比，需要转换为小数）
  const h = Number((weather.value as any).humidity);
  if (!Number.isNaN(h)) realtime.value.humidity = h / 100;
  
  // 设置风速（如果有风力等级，转换为大概的风速）
  if ((weather.value as any).windpower) {
    const windpower = (weather.value as any).windpower;
    // 简单的风力等级到风速的转换（大概值）
    const windpowerNum = parseInt(windpower.replace(/[^0-9]/g, ''));
    if (!isNaN(windpowerNum)) {
      realtime.value.windSpeed = windpowerNum * 2; // 简单转换，风力等级*2作为风速
    }
  }
  
  // 设置模拟的光照值（高德API不提供光照数据，设置一个基于天气的模拟值）
  const weatherDesc = (weather.value as any).weather || '';
  if (weatherDesc.includes('晴')) {
    realtime.value.illumination = 800 + Math.random() * 200; // 800-1000 lux
  } else if (weatherDesc.includes('云')) {
    realtime.value.illumination = 400 + Math.random() * 300; // 400-700 lux
  } else if (weatherDesc.includes('阴')) {
    realtime.value.illumination = 200 + Math.random() * 200; // 200-400 lux
  } else if (weatherDesc.includes('雨') || weatherDesc.includes('雪')) {
    realtime.value.illumination = 100 + Math.random() * 150; // 100-250 lux
  } else {
    realtime.value.illumination = 500 + Math.random() * 300; // 默认值
  }
  
  // 设置时间戳
  realtime.value.timestamp = new Date().toISOString();
}

async function onSearchAddress() {
  if (!address.value) return;
  const geo = await axios.get('/api/amap/geocode', { params: { address: address.value } });
  const data = geo.data as any;
  if (!data || !data.adcode) return;
  amap.value = data;
  const wRes = await axios.get('/api/amap/weather', { params: { adcode: amap.value.adcode } });
  weather.value = wRes.data as any;
  await loadForecast();
  if (map && amap.value.centerLng && amap.value.centerLat) {
    marker.setPosition([amap.value.centerLng, amap.value.centerLat]);
    map.setZoomAndCenter(11, [amap.value.centerLng, amap.value.centerLat]);
  }
  applyWeatherToRealtime();
  saveHistory(address.value);
  address.value = '';
}

async function onSelectQuickCity() {
  if (!quickCity.value) return;
  address.value = quickCity.value;
  await onSearchAddress();
}

async function onSelectHistory() {
  if (!historySelected.value) return;
  address.value = historySelected.value;
  await onSearchAddress();
}

async function onGeolocate() {
  if (!('geolocation' in navigator)) {
    await loadAmap();
    applyWeatherToRealtime();
    return;
  }
  navigator.geolocation.getCurrentPosition(async (pos) => {
    const lng = pos.coords.longitude;
    const lat = pos.coords.latitude;
    const rev = await axios.get('/api/amap/reverse', { params: { lng, lat } });
    amap.value = rev.data as any;
    if (amap.value.adcode) {
      const wRes = await axios.get('/api/amap/weather', { params: { adcode: amap.value.adcode } });
      weather.value = wRes.data as any;
      applyWeatherToRealtime();
    }
    if (map) {
      marker.setPosition([lng, lat]);
      map.setZoomAndCenter(11, [lng, lat]);
    }
  }, async () => {
    await loadAmap();
    applyWeatherToRealtime();
  }, { enableHighAccuracy: true, timeout: 5000 });
}

loadRealtime();
loadAlerts();
loadReport();
onMounted(() => { loadAmap(); });
</script>

<style>
  .page { 
    width: 100%; 
    margin: 0; 
    padding: 0; 
    font-family: -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,'Noto Sans','PingFang SC','Hiragino Sans GB','Microsoft YaHei','WenQuanYi Micro Hei',sans-serif; 
    color: #0f172a; 
  }
  
  .page-content {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 24px;
  }
  
  /* 导航栏样式 */
  .navbar { 
    background: #343a40; 
    padding: 0 32px; 
    height: 80px; 
    display: flex; 
    align-items: center; 
    justify-content: space-between; 
    margin: -24px -16px 24px -16px; 
    box-shadow: 0 4px 20px rgba(0,0,0,0.15);
    width: 100vw;
    position: relative;
    left: 50%;
    right: 50%;
    margin-left: -50vw;
    margin-right: -50vw;
    overflow: hidden;
    box-sizing: border-box;
  }
  
  .nav-left { 
    display: flex; 
    align-items: center; 
    gap: 20px; 
    z-index: 20;
    position: relative;
  }
  .logo-circle { 
    width: 52px; 
    height: 52px; 
    background: linear-gradient(135deg, #28a745, #20c997); 
    border-radius: 50%; 
    display: flex; 
    align-items: center; 
    justify-content: center; 
    box-shadow: 0 4px 12px rgba(40, 167, 69, 0.4);
    transition: all 0.3s ease;
  }
  .logo-circle:hover {
    transform: scale(1.05);
    box-shadow: 0 6px 16px rgba(40, 167, 69, 0.6);
  }
  .logo-icon { 
    font-size: 26px; 
    color: white; 
    filter: drop-shadow(0 1px 2px rgba(0,0,0,0.3));
  }
  .platform-title { 
    color: white; 
    font-size: 22px; 
    font-weight: 700; 
    margin: 0; 
    text-shadow: 0 2px 4px rgba(0,0,0,0.3);
    letter-spacing: 0.5px;
  }
  
  .nav-center { 
    display: flex; 
    gap: 50px; 
    margin: 0 auto; 
    position: absolute; 
    left: 50%; 
    transform: translateX(-50%);
    z-index: 10;
    max-width: 600px;
  }
  .nav-link { 
    color: white; 
    text-decoration: none; 
    font-size: 16px; 
    padding: 16px 0; 
    border-bottom: 3px solid transparent; 
    transition: all 0.3s ease;
    font-weight: 600;
    letter-spacing: 1px;
    position: relative;
    white-space: nowrap;
  }
  .nav-link:hover, .nav-link.active { 
    border-bottom-color: #28a745; 
    color: #28a745;
    transform: translateY(-2px);
    text-shadow: 0 0 8px rgba(40, 167, 69, 0.3);
  }
  .nav-link::after {
    content: '';
    position: absolute;
    bottom: -2px;
    left: 0;
    width: 0;
    height: 3px;
    background: #28a745;
    transition: width 0.3s ease;
  }
  .nav-link:hover::after, .nav-link.active::after {
    width: 100%;
  }
  
  .nav-right { 
    display: flex; 
    gap: 16px; 
    z-index: 20;
    position: relative;
    align-items: center;
    flex-shrink: 0;
    min-width: 180px;
  }
  .btn-login { 
    padding: 10px 20px; 
    background: #28a745; 
    color: white; 
    border: none; 
    border-radius: 6px; 
    font-size: 14px; 
    font-weight: 600;
    cursor: pointer; 
    transition: all 0.3s ease;
    box-shadow: 0 2px 8px rgba(40, 167, 69, 0.3);
    min-width: 70px;
    box-sizing: border-box;
    white-space: nowrap;
  }
  .btn-login:hover { 
    background: #218838; 
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(40, 167, 69, 0.4);
  }
  .btn-register { 
    padding: 10px 20px; 
    background: rgba(255, 255, 255, 0.15); 
    color: white; 
    border: 2px solid rgba(255, 255, 255, 0.9); 
    border-radius: 6px; 
    font-size: 14px; 
    font-weight: 600;
    cursor: pointer; 
    transition: all 0.3s ease;
    backdrop-filter: blur(10px);
    text-shadow: 0 1px 2px rgba(0,0,0,0.3);
    min-width: 70px;
    white-space: nowrap;
    box-sizing: border-box;
  }
  .btn-register:hover { 
    background: rgba(255, 255, 255, 0.25); 
    border-color: white;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(255, 255, 255, 0.3);
  }
  
  .hero-section { 
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
    padding: 48px 0; 
    margin-bottom: 32px; 
    text-align: center; 
    color: white;
    width: 100vw;
    position: relative;
    left: 50%;
    right: 50%;
    margin-left: -50vw;
    margin-right: -50vw;
  }
  .hero-title { 
    font-size: 32px; 
    font-weight: 700; 
    margin: 0 0 16px 0; 
  }
  .hero-subtitle { 
    font-size: 18px; 
    margin: 0; 
    opacity: 0.9; 
  }

  /* 首页样式 */
  .home-content { padding: 32px 0; }
  .welcome-section { 
    text-align: center; 
    margin-bottom: 48px; 
    padding: 40px 0;
  }
  .welcome-section h2 { 
    font-size: 36px; 
    color: #1f2937; 
    margin: 0 0 16px 0; 
  }
  .welcome-section p { 
    font-size: 18px; 
    color: #6b7280; 
    margin: 0; 
  }
  
  .feature-grid { 
    display: grid; 
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); 
    gap: 24px; 
    margin-top: 32px; 
    max-width: 1200px;
    margin-left: auto;
    margin-right: auto;
  }
  .feature-card { 
    background: white; 
    border: 1px solid #e5e7eb; 
    border-radius: 16px; 
    padding: 32px 24px; 
    text-align: center; 
    cursor: pointer; 
    transition: all 0.3s ease; 
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
  }
  .feature-card:hover { 
    transform: translateY(-4px); 
    box-shadow: 0 8px 25px rgba(0,0,0,0.1); 
    border-color: #28a745;
  }
  .feature-icon { 
    font-size: 48px; 
    margin-bottom: 16px; 
  }
  .feature-card h3 { 
    font-size: 20px; 
    color: #1f2937; 
    margin: 0 0 12px 0; 
    font-weight: 600;
  }
  .feature-card p { 
    color: #6b7280; 
    margin: 0; 
    line-height: 1.5;
  }

  /* 页面头部样式 */
  .page-header { 
    text-align: center; 
    margin-bottom: 32px; 
    padding: 32px 0;
  }
  .page-header h2 { 
    font-size: 32px; 
    color: #1f2937; 
    margin: 0 0 12px 0; 
    font-weight: 700;
  }
  .page-header p { 
    font-size: 18px; 
    color: #6b7280; 
    margin: 0; 
  }

  /* 其他页面样式 */
  .other-content { 
    text-align: center; 
    padding: 80px 0; 
    color: #6b7280;
  }
  .other-content h2 { 
    font-size: 28px; 
    margin: 0 0 16px 0; 
    color: #1f2937;
  }
  .other-content p { 
    font-size: 16px; 
    margin: 0; 
  }

  /* 咨询服务页面样式 */
  .consultation-content {
    padding: 0;
  }
  
  .consultation-layout {
    display: grid;
    grid-template-columns: 2fr 1fr;
    gap: 24px;
    margin-top: 24px;
    height: calc(100vh - 300px);
    min-height: 600px;
  }
  
  .chat-section {
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 16px;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
  }
  
  .chat-header {
    background: linear-gradient(135deg, #28a745, #20c997);
    color: white;
    padding: 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  
  .expert-info {
    display: flex;
    align-items: center;
    gap: 12px;
  }
  
  .expert-avatar {
    width: 48px;
    height: 48px;
    background: rgba(255,255,255,0.2);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    backdrop-filter: blur(10px);
  }
  
  .expert-details h3 {
    margin: 0;
    font-size: 18px;
    font-weight: 600;
  }
  
  .status.online {
    font-size: 12px;
    opacity: 0.9;
    display: flex;
    align-items: center;
    gap: 4px;
  }
  
  .status.online::before {
    content: '';
    width: 8px;
    height: 8px;
    background: #00ff88;
    border-radius: 50%;
    display: inline-block;
    animation: pulse 2s infinite;
  }
  
  .chat-stats {
    font-size: 14px;
    opacity: 0.9;
    display: flex;
    align-items: center;
  }
  
  .ai-badge {
    background: rgba(255,255,255,0.2);
    padding: 6px 12px;
    border-radius: 20px;
    display: flex;
    align-items: center;
    gap: 6px;
    font-size: 13px;
    backdrop-filter: blur(10px);
  }
  
  .ai-icon {
    animation: sparkle 2s infinite;
  }
  
  .chat-messages {
    flex: 1;
    padding: 20px;
    overflow-y: auto;
    background: #f8fafc;
  }
  
  .message {
    display: flex;
    gap: 12px;
    margin-bottom: 20px;
    animation: slideIn 0.3s ease-out;
  }
  
  .message.user {
    flex-direction: row-reverse;
  }
  
  .message-avatar {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    flex-shrink: 0;
  }
  
  .message.expert .message-avatar {
    background: linear-gradient(135deg, #28a745, #20c997);
  }
  
  .message.expert[data-source="ai"] .message-avatar {
    background: linear-gradient(135deg, #6366f1, #8b5cf6);
  }
  
  .message.user .message-avatar {
    background: linear-gradient(135deg, #0ea5e9, #06b6d4);
  }
  
  .message-content {
    max-width: 70%;
    min-width: 120px;
  }
  
  .message-text {
    background: white;
    padding: 12px 16px;
    border-radius: 16px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    line-height: 1.5;
    position: relative;
  }
  
  .message.expert .message-text {
    background: linear-gradient(135deg, #f0f9ff, #e0f2fe);
    border: 1px solid #0ea5e9;
  }
  
  .message.expert[data-source="ai"] .message-text {
    background: linear-gradient(135deg, #f3f4f6, #e5e7eb);
    border: 1px solid #6366f1;
    position: relative;
  }
  
  .message.expert[data-source="ai"] .message-text::before {
    content: '🤖 AI';
    position: absolute;
    top: -8px;
    right: 8px;
    background: #6366f1;
    color: white;
    font-size: 10px;
    padding: 2px 6px;
    border-radius: 8px;
    font-weight: 600;
  }
  
  .message.user .message-text {
    background: linear-gradient(135deg, #28a745, #20c997);
    color: white;
  }
  
  .message-time {
    font-size: 11px;
    color: #64748b;
    margin-top: 4px;
    text-align: right;
  }
  
  .message.user .message-time {
    text-align: left;
  }
  
  .typing-indicator {
    display: flex;
    gap: 4px;
    padding: 12px 16px;
  }
  
  .typing-indicator span {
    width: 8px;
    height: 8px;
    background: #64748b;
    border-radius: 50%;
    animation: typing 1.4s infinite;
  }
  
  .typing-indicator span:nth-child(2) {
    animation-delay: 0.2s;
  }
  
  .typing-indicator span:nth-child(3) {
    animation-delay: 0.4s;
  }
  
  .chat-input {
    padding: 20px;
    background: white;
    border-top: 1px solid #e5e7eb;
    display: flex;
    gap: 12px;
  }
  
  .question-input {
    flex: 1;
    padding: 12px 16px;
    border: 1px solid #d1d5db;
    border-radius: 24px;
    outline: none;
    font-size: 14px;
    transition: all 0.3s ease;
  }
  
  .question-input:focus {
    border-color: #28a745;
    box-shadow: 0 0 0 3px rgba(40, 167, 69, 0.1);
  }
  
  .send-btn {
    padding: 12px 24px;
    background: linear-gradient(135deg, #28a745, #20c997);
    color: white;
    border: none;
    border-radius: 24px;
    cursor: pointer;
    font-weight: 600;
    transition: all 0.3s ease;
    min-width: 80px;
  }
  
  .send-btn:hover:not(:disabled) {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(40, 167, 69, 0.3);
  }
  
  .send-btn:disabled {
    opacity: 0.6;
    cursor: not-allowed;
  }
  
  .faq-section {
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 16px;
    padding: 24px;
    overflow-y: auto;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
  }
  
  .faq-section h3 {
    margin: 0 0 8px 0;
    color: #1f2937;
    font-size: 20px;
    font-weight: 700;
  }
  
  .faq-subtitle {
    color: #6b7280;
    margin: 0 0 24px 0;
    font-size: 14px;
  }
  
  .faq-category {
    margin-bottom: 24px;
  }
  
  .category-title {
    display: flex;
    align-items: center;
    gap: 8px;
    margin: 0 0 12px 0;
    color: #374151;
    font-size: 16px;
    font-weight: 600;
  }
  
  .category-icon {
    font-size: 18px;
  }
  
  .questions-list {
    display: flex;
    flex-direction: column;
    gap: 8px;
  }
  
  .question-btn {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 10px 14px;
    text-align: left;
    cursor: pointer;
    transition: all 0.3s ease;
    font-size: 13px;
    line-height: 1.4;
    color: #374151;
  }
  
  .question-btn:hover:not(:disabled) {
    background: #f1f5f9;
    border-color: #28a745;
    transform: translateX(4px);
  }
  
  .question-btn:disabled {
    opacity: 0.6;
    cursor: not-allowed;
  }
  
  .contact-info {
    background: linear-gradient(135deg, #f0f9ff, #e0f2fe);
    border: 1px solid #0ea5e9;
    border-radius: 12px;
    padding: 16px;
    margin-top: 24px;
  }
  
  .contact-info h4 {
    margin: 0 0 12px 0;
    color: #1e293b;
    font-size: 16px;
  }
  
  .contact-info p {
    margin: 4px 0;
    color: #475569;
    font-size: 14px;
  }
  
  .ai-config-info {
    background: linear-gradient(135deg, #f8fafc, #f1f5f9);
    border: 1px solid #6366f1;
    border-radius: 12px;
    padding: 16px;
    margin-top: 16px;
  }
  
  .ai-config-info h4 {
    margin: 0 0 12px 0;
    color: #1e293b;
    font-size: 16px;
  }
  
  .ai-config-info p {
    margin: 4px 0;
    color: #475569;
    font-size: 14px;
  }
  
  .ai-config-info small {
    color: #6366f1;
    font-weight: 500;
  }
  
  @keyframes sparkle {
    0%, 100% { 
      transform: scale(1) rotate(0deg);
      opacity: 1;
    }
    50% { 
      transform: scale(1.2) rotate(180deg);
      opacity: 0.8;
    }
  }
  
  @keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.5; }
  }
  
  @keyframes slideIn {
    from {
      opacity: 0;
      transform: translateY(20px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }
  
  @keyframes typing {
    0%, 60%, 100% {
      transform: translateY(0);
    }
    30% {
      transform: translateY(-10px);
    }
  }

  .header { margin-bottom: 16px; display: flex; align-items: center; justify-content: space-between; }
  .brand { display: flex; gap: 10px; align-items: center; }
  .logo { font-size: 28px; line-height: 1; }
  .header h1 { margin: 0; font-size: 26px; }
  .subtitle { margin: 4px 0 0; color: #64748b; }
  .tabs { display: flex; gap: 8px; }
  .tab { padding: 6px 10px; border: 1px solid #e2e8f0; border-radius: 999px; color: #334155; background: #fff; cursor: default; }
  .tab.active { background: #0ea5e9; color: #fff; border-color: #0ea5e9; }
  .grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; }
  .three-cols { grid-template-columns: repeat(3, 1fr); }
  .card { border: 1px solid #e5e7eb; border-radius: 12px; padding: 14px 16px; background: #fff; box-shadow: 0 1px 2px rgba(0,0,0,0.04); }
  .card-head { display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px; }
  .realtime-controls { display: flex; align-items: center; gap: 12px; }
  .data-source { 
    font-size: 12px; 
    color: #6b7280; 
    background: #f3f4f6; 
    padding: 4px 8px; 
    border-radius: 12px;
    display: flex;
    align-items: center;
    gap: 4px;
  }
  .btn { padding: 6px 12px; border: 1px solid #CBD5E1; border-radius: 8px; background: #f8fafc; cursor: pointer; }
  .btn:hover { background: #f1f5f9; }
  .stats { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px; }
  .stat { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 10px; display: flex; align-items: center; justify-content: space-between; }
  .stat span { color: #64748b; }
  .stat .meter { flex: 1; height: 8px; background: #f1f5f9; border-radius: 999px; margin: 0 8px; overflow: hidden; border: 1px solid #e2e8f0; }
  .stat .meter.small { height: 6px; margin-right: 8px; }
  .bar { height: 100%; border-radius: 999px; }
  .bar.blue { background: linear-gradient(90deg, #22d3ee, #0ea5e9); }
  .bar.orange { background: linear-gradient(90deg, #fbbf24, #f59e0b); }
  .alerts { list-style: none; padding: 0; margin: 0; display: grid; gap: 10px; }
  .alerts li { display: flex; gap: 10px; align-items: center; border: 1px solid #e2e8f0; border-radius: 8px; padding: 10px; background: #f8fafc; }
  .tag { display: inline-flex; align-items: center; justify-content: center; min-width: 54px; text-align: center; font-size: 12px; padding: 4px 8px; border-radius: 999px; color: white; font-weight: 600; }
  .tag.WARN { background: #f59e0b; }
  .tag.ERROR, .tag.ALERT { background: #ef4444; }
  .alert-body b { display: block; margin-bottom: 4px; }
  .report { display: grid; gap: 8px; }
  .kv { display: flex; align-items: center; justify-content: space-between; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 8px 10px; }
  .recommend { margin: 0 0 8px; padding: 8px 10px; background: #ecfeff; border: 1px solid #67e8f9; border-radius: 8px; }
  .amap { display: grid; gap: 8px; }
  .amap-toolbar { display: flex; gap: 8px; align-items: center; flex-wrap: wrap; }
  .select { padding: 6px 8px; border: 1px solid #e2e8f0; border-radius: 8px; background: #fff; }
  .input { padding: 6px 10px; border: 1px solid #e2e8f0; border-radius: 8px; min-width: 200px; }
  .staticmap { width: 100%; border-radius: 8px; border: 1px solid #e2e8f0; }
  .map-card { margin-bottom: 16px; }
  .mapbox { height: 420px; border-radius: 8px; border: 1px solid #e2e8f0; }
  .chart { 
    width: 100%; 
    height: 160px; 
    background: #fafbfc; 
    border: 1px solid #e2e8f0; 
    border-radius: 8px; 
    box-shadow: inset 0 1px 3px rgba(0,0,0,0.05);
  }
  .forecast { 
    display: grid; 
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); 
    gap: 16px; 
    align-items: stretch; 
  }
  .forecast .chart { 
    grid-column: 1 / -1; 
    margin-bottom: 8px; 
  }
  .forecast .day { 
    background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%); 
    border: 1px solid #e2e8f0; 
    border-radius: 12px; 
    padding: 16px; 
    display: grid; 
    gap: 8px; 
    transition: all 0.3s ease;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
  }
  .forecast .day:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    border-color: #0ea5e9;
  }
  .forecast .date { 
    font-weight: 700; 
    margin-bottom: 4px; 
    font-size: 14px; 
    color: #1e293b;
  }
  .forecast .weather { 
    font-size: 13px; 
    line-height: 1.5; 
    color: #475569;
    display: flex;
    align-items: center;
    gap: 4px;
    flex-wrap: wrap;
  }
  .forecast .weather-emoji {
    font-size: 16px;
    margin-right: 2px;
  }
  .forecast .weather-divider {
    margin: 0 4px;
    color: #94a3b8;
  }
  .forecast .temps { 
    font-size: 15px; 
    line-height: 1.35; 
    font-weight: 600;
    color: #0ea5e9;
  }
  .forecast .temp-range {
    background: linear-gradient(90deg, #0ea5e9, #06b6d4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }
  .forecast .wind { 
    font-size: 12px; 
    line-height: 1.35; 
    color: #64748b;
    display: flex;
    align-items: center;
    gap: 4px;
  }
  .forecast .wind-icon {
    font-size: 14px;
  }
  .forecast .empty { 
    color: #64748b; 
    text-align: center;
    padding: 20px;
    grid-column: 1 / -1;
  }

  @media (max-width: 980px) {
    .forecast { grid-template-columns: repeat(auto-fill, minmax(160px, 1fr)); }
    .grid { grid-template-columns: 1fr; }
    .navbar { 
      padding: 0 20px; 
      height: 70px; 
    }
    .nav-center { 
      gap: 24px; 
      position: static; 
      transform: none; 
      margin: 0; 
    }
    .nav-link { 
      font-size: 15px; 
      padding: 12px 0; 
    }
    .nav-right {
      gap: 12px;
      min-width: 160px;
    }
    .page-content { padding: 0 16px; }
    .hero-section { padding: 32px 0; }
    .hero-title { font-size: 28px; }
    .hero-subtitle { font-size: 16px; }
    .logo-circle { 
      width: 48px; 
      height: 48px; 
    }
    .logo-icon { font-size: 24px; }
    .platform-title { font-size: 20px; }
    .feature-grid { 
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); 
      gap: 20px; 
    }
    .welcome-section h2 { font-size: 30px; }
    .page-header h2 { font-size: 28px; }
  }
  
  @media (max-width: 768px) {
    .navbar { 
      padding: 0 12px; 
      height: 65px; 
    }
    .nav-center { 
      gap: 16px; 
      flex-wrap: wrap;
      justify-content: center;
    }
    .nav-link { 
      font-size: 14px; 
      padding: 8px 0; 
    }
    .platform-title { font-size: 18px; }
    .logo-circle { 
      width: 44px; 
      height: 44px; 
    }
    .logo-icon { font-size: 22px; }
    .nav-left { gap: 12px; }
    .nav-right { 
      gap: 8px; 
      min-width: 140px;
    }
    .btn-login, .btn-register { 
      padding: 8px 16px; 
      font-size: 13px; 
      min-width: 60px;
    }
    .feature-grid { 
      grid-template-columns: 1fr; 
      gap: 16px; 
    }
    .forecast { 
      grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); 
    }
    .forecast .day {
      padding: 12px;
      gap: 6px;
    }
    .forecast .weather {
      font-size: 12px;
    }
    .forecast .weather-emoji {
      font-size: 14px;
    }
    .consultation-layout {
      grid-template-columns: 1fr;
      gap: 16px;
      height: auto;
      min-height: auto;
    }
    .chat-section {
      height: 500px;
    }
    .faq-section {
      height: auto;
      max-height: 400px;
    }
    .welcome-section h2 { font-size: 26px; }
    .page-header h2 { font-size: 24px; }
  }
  
  @media (max-width: 480px) {
    .consultation-layout {
      gap: 12px;
    }
    .chat-section {
      height: 400px;
    }
    .chat-header {
      padding: 16px;
    }
    .expert-avatar {
      width: 40px;
      height: 40px;
      font-size: 20px;
    }
    .expert-details h3 {
      font-size: 16px;
    }
    .chat-messages {
      padding: 16px;
    }
    .message-content {
      max-width: 85%;
    }
    .faq-section {
      padding: 16px;
      max-height: 350px;
    }
    .question-btn {
      font-size: 12px;
      padding: 8px 12px;
    }
  }
</style>


