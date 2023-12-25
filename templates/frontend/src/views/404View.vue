<template>
  <div class="main-wrapper">
    <div class="wscn-http404-container">
      <div class="wscn-http404">
        <div class="pic-404">
          <img class="pic-404__parent" src="./images/404.png" alt="404" />
          <img class="pic-404__child left" src="./images/404_cloud.png" alt="404" />
          <img class="pic-404__child mid" src="./images/404_cloud.png" alt="404" />
          <img class="pic-404__child right" src="./images/404_cloud.png" alt="404" />
        </div>
        <div class="bullshit">
          <div class="bullshit__oops">努力更新中，敬请期待...</div>
          <!--          <div class="bullshit__headline">{{ message }}</div>-->
          <div class="bullshit__info">您可以点击下面按钮返回</div>
          <div @click="handleBack" class="bullshit__return-home">返回</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Page404',
  computed: {
    message() {
      return '没有找到你要访问的页面。。。'
    }
  },
  methods: {
    handleBack() {
      this.$router.go(-1)
    }
  }
}
</script>
