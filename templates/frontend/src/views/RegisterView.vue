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
      <h1>注册</h1>
      <el-form-item prop="user">
        <el-input v-model.number="ruleForm.user" placeholder="用户名" />
      </el-form-item>
      <el-form-item prop="email">
        <el-input v-model="ruleForm.email" type="email" placeholder="邮箱" />
      </el-form-item>
      <el-form-item prop="pass">
        <el-input v-model="ruleForm.pass" type="password" autocomplete="off" placeholder="密码" />
      </el-form-item>
      <el-form-item prop="checkPass">
        <el-input
          v-model="ruleForm.checkPass"
          type="password"
          autocomplete="off"
          placeholder="确认密码"
        />
      </el-form-item>

      <el-form-item>
        <el-button type="primary" @click="submitForm(ruleFormRef)">注册</el-button>
        <el-button @click="resetForm(ruleFormRef)">重置</el-button>
      </el-form-item>
      <el-form-item style="float: right">
        <el-link href="/login" target="_self">Login</el-link>
      </el-form-item>
    </el-form>
  </div>
</template>

<script lang="ts" setup>
import { reactive, ref } from 'vue'
import type { ElNotification, FormInstance, FormRules } from 'element-plus'
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

const checkEmail = (rule: any, value: any, callback: any) => {
  if (value === '') {
    return callback(new Error('请输入邮箱'))
  } else {
    if (/^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/.test(value)) {
      callback()
    } else {
      callback(new Error('请输入正确的邮箱'))
    }
  }
}

const validatePass = (rule: any, value: any, callback: any) => {
  if (value === '') {
    callback(new Error('请输入密码'))
  } else {
    if (ruleForm.checkPass !== '') {
      if (!ruleFormRef.value) return
      ruleFormRef.value.validateField('checkPass', () => null)
    }
    callback()
  }
}
const validatePass2 = (rule: any, value: any, callback: any) => {
  if (value === '') {
    callback(new Error('请确认密码'))
  } else if (value !== ruleForm.pass) {
    callback(new Error('密码不一致!'))
  } else {
    callback()
  }
}

const ruleForm = reactive({
  pass: '',
  checkPass: '',
  user: '',
  email: ''
})

const rules = reactive<FormRules<typeof ruleForm>>({
  pass: [{ validator: validatePass, trigger: 'blur' }],
  checkPass: [{ validator: validatePass2, trigger: 'blur' }],
  user: [{ validator: checkUser, trigger: 'blur' }],
  email: [{ validator: checkEmail, trigger: 'blur' }]
})

const submitForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return
  formEl.validate((valid) => {
    if (valid) {
      axios
        .post('http://127.0.0.1:8000/api/v1/users/', {
          username: ruleForm.user,
          password: ruleForm.pass,
          email: ruleForm.email
        })
        .then((res) => {
          router.push({
            path: '/login',
            query: {
              user: ruleForm.user
            }
          })
          return ElNotification({
            title: 'Success',
            message: '成功注册' + res.data.username + '!',
            type: 'success'
          })
        })
        .catch((err) =>
          ElNotification({
            title: 'Error',
            message: err.response.data.error,
            type: 'error'
          })
        )
    } else {
      return ElNotification({
        title: 'Error',
        message: '提交错误！',
        type: 'error'
      })
    }
  })
}

const resetForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return
  formEl.resetFields()
}
</script>

<style scoped>
.container {
  box-shadow: var(--el-box-shadow-dark);
  border-radius: 5px;
  width: 300px;
  height: 350px;
  margin: auto;
  padding: 50px;
  text-align: center;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
</style>
