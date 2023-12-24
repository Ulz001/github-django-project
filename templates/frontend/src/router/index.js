import { createRouter, createWebHistory } from 'vue-router'
import { useUserStore } from '@/stores/user/index.js'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'register',
      component: () => import('../views/RegisterView.vue')
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LoginView.vue')
    },
    {
      path: '/home',
      name: 'home',
      component: () => import('../views/HomeView.vue')
    }
  ]
})

router.beforeEach((to, from, next) => {
  const userStore = useUserStore()
  const { status, username, token } = userStore.getUserData()
  if (to.name === 'login' || to.name === 'register') {
    next()
  } else if (token === '') {
    next({ name: 'login' })
  } else {
    next()
  }
})

export default router
