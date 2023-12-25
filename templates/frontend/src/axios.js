import axios from 'axios'
import { useUserStore } from '@/stores/user/index.js'
import { ElNotification } from 'element-plus'
import router from '@/router/index.js'

const http = axios.create({
  baseURL: 'http://localhost:8000/api/v1/',
  headers: {
    'Content-Type': 'application/json'
  }
})

http.interceptors.request.use(
  (config) => {
    if (useUserStore().getUserData().token !== '') {
      config.headers.Authorization = 'jwt ' + useUserStore().getUserData().token
    }
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

http.interceptors.response.use(
  (response) => {
      return response
  },
  (error) => {
    if (error.response.status === 401) {
      useUserStore().removeUserData()
      ElNotification({
        title: '错误',
        message: '登录已过期，请重新登录',
        type: 'error'
      })
      router.push('/login')
    }
    return Promise.reject(error)
  }
)

export default http
