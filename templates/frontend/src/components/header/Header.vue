<template>
  <el-menu
    :default-active="activeIndex"
    class="el-menu"
    mode="horizontal"
    :ellipsis="false"
    background-color="#F2F6FC"
    @open="handleOpen"
    @close="handleClose"
    @select="handleSelect"
  >
    <el-menu-item index="0">
      <el-icon>
        <el-image src="http://localhost:8000/media/logo/logo.png"></el-image>
      </el-icon>
      <h1>商店库存管理系统</h1>
    </el-menu-item>
    <div class="flex-grow" />
    <el-sub-menu index="1">
      <template #title>欢迎你！{{ username }}</template>
      <el-menu-item index="2-1" @click="logout">
        <el-icon>
          <Close color="#c45656" />
        </el-icon>
        注销
      </el-menu-item>
    </el-sub-menu>
  </el-menu>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import { useUserStore } from '@/stores/user'
import { Close } from '@element-plus/icons-vue'
import router from '../../router'

const activeIndex = ref('1')

const userStore = useUserStore()
const data = userStore.getUserData()
const username = data.username

const handleSelect = (key: string, keyPath: string[]) => {}
const handleOpen = () => true
const handleClose = () => {}

const logout = () => {
  userStore.removeUserData()
  localStorage.removeItem('token')
  router.push({ name: 'login' })
}
</script>

<style>
.flex-grow {
  flex-grow: 1;
}
</style>
