import {createApp} from 'vue'
import {createPinia} from 'pinia'

import App from './App.vue'
import router from './router'
import axios from "axios";
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'

axios.defaults.baseURL = "http://127.0.0.1:8000/api/v1"

const app = createApp(App)
const pinia = createPinia()

app.use(pinia)

pinia.use(piniaPluginPersistedstate)

app.use(router)
app.config.globalProperties.$axios = axios // 全局注册axios

app.mount('#app')
