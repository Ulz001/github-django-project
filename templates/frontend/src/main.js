import './assets/global.css'

import {createApp} from 'vue'
import {createPinia} from 'pinia'

import App from './App.vue'
import router from './router'
import axios from "axios";
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'

const app = createApp(App)
const pinia = createPinia()

app.use(pinia)

pinia.use(piniaPluginPersistedstate)

app.use(router)
app.config.globalProperties.$axios = axios // 全局注册axios

app.mount('#app')
