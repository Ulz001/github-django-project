<template>
  <div class="common-layout">
    <el-container>
      <el-header style="padding: 0">
        <Header />
      </el-header>

      <el-container>
        <el-aside width="400px">
          <Aside />
        </el-aside>
        <el-container>
          <el-main> </el-main>
        </el-container>
      </el-container>
    </el-container>
  </div>
</template>
<script setup>
import Header from '@/components/header/Header.vue'
import Aside from '@/components/aside/Aside.vue'
</script>
