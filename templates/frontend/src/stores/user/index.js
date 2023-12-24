import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useUserStore = defineStore(
  'user',
  () => {
    const userData = ref({
      status: '',
      username: '',
      token: ''
    })

    const getUserData = () => {
      return userData.value
    }

    const setUserData = (data) => {
      userData.value.status = data.status
      userData.value.username = data.username
      userData.value.token = data.token
    }

    const removeUserData = () => {
      userData.value = {
        status: '',
        username: '',
        token: ''
      }
    }

    return { userData, getUserData, setUserData, removeUserData }
  },
  {
    persist: true
  }
)
