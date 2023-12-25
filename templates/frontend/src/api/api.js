import http from '@/axios.js'

export function getMaterialList() {
  return http.get('/materials/')
}

export function login(data) {
  return http.post('/login/', data)
}

