import http from '@/axios.js'

export function getMaterialList() {
  return http.get('/materials/')
}

export function login(data) {
  return http.post('/login/', data)
}

export function getInStashList() {
  return http.get('/in-stash/')
}
