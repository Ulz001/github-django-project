<template>
  <div class="container">
    <el-form
      label-position="top"
      ref="ruleFormRef"
      :model="ruleForm"
      status-icon
      :rules="rules"
      label-width="120px"
      class="demo-ruleForm"
    >
      <h1>登录</h1>
      <el-form-item prop="user">
        <el-input v-model.number="ruleForm.user" placeholder="用户名" />
      </el-form-item>
      <el-form-item prop="pass">
        <el-input v-model="ruleForm.pass" type="password" autocomplete="off" placeholder="密码" />
      </el-form-item>

      <el-form-item style="float: right">
        <el-button type="primary" @click="submitForm(ruleFormRef)">登录</el-button>
      </el-form-item>
      <el-form-item style="position: absolute; right: 12%; top: 80%">
        <el-link href="/" target="_self">没有账号？前往注册</el-link>
      </el-form-item>
    </el-form>
  </div>
</template>

<script lang="ts" setup>
import { reactive, ref } from 'vue'
import type { FormInstance, FormRules, ElNotification } from 'element-plus'
import axios from 'axios'
import router from '../router'

const ruleFormRef = ref<FormInstance>()

const checkUser = (rule: any, value: any, callback: any) => {
  if (value === '') {
    return callback(new Error('请输入用户名'))
  }
  setTimeout(() => {
    if (value) {
      callback()
    } else {
      console.log(value)
      callback(new Error('用户名不能超过32个字符'))
    }
  }, 1000)
}

const validatePass = (rule: any, value: any, callback: any) => {
  if (value === '') {
    callback(new Error('请输入密码'))
  } else {
    if (!ruleFormRef.value) return
    ruleFormRef.value.validateField('checkPass', () => null)
    callback()
  }
}

const ruleForm = reactive({
  pass: '',
  user: ''
})

const rules = reactive<FormRules<typeof ruleForm>>({
  pass: [{ validator: validatePass, trigger: 'blur' }],
  user: [{ validator: checkUser, trigger: 'blur' }]
})

const submitForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return
  formEl.validate(async (valid) => {
    if (valid) {
      await axios
        .post('/login/', {
          username: ruleForm.user,
          password: ruleForm.pass
        })
        .then((res) => {
          if (res.data['status'] === 200) {
            console.log(res.data)
            localStorage.setItem('token', res.data['token'])
            router.push('/home')
            return ElNotification({
              title: 'Success',
              message: '登录成功!',
              type: 'success'
            })
          } else if (res.data['status'] === 401) {
            return ElNotification({
              title: 'Error',
              message: res.data['error'],
              type: 'error'
            })
          }
        })
        .catch((err) => {
          return ElNotification({
            title: err.title,
            message: err.message,
            type: 'error'
          })
        })
    }
  })
}
</script>

<style scoped>
.container {
  box-shadow: var(--el-box-shadow-dark);
  border-radius: 5px;
  width: 300px;
  height: 300px;
  margin: auto;
  padding: 50px;
  text-align: center;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  //background-image: url('http://127.0.0.1:8000/media/upload_images/jarry.jpg');
}
</style>