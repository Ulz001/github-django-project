<template>
  <div class="echart" style="width: 600px; height: 400px" ref="chart" id="chart"></div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue'
import axios from 'axios'
import { useUserStore } from '@/stores/user/index.js'

axios.defaults.headers.get['Authorization'] = 'jwt ' + useUserStore().getUserData().token

import * as echarts from 'echarts'
import { GridComponent } from 'echarts/components'
import { BarChart } from 'echarts/charts'
import { CanvasRenderer } from 'echarts/renderers'

echarts.use([GridComponent, BarChart, CanvasRenderer])

const chart = ref('')

onMounted(() => {
  const chartDom = echarts.init(chart.value)

  axios
    .get('/materials/')
    .then((res) => {
      const xAxis = res.data.materials[0]
      const series = res.data.materials[1]
      const option = {
        xAxis: {
          type: 'category',
          data: xAxis
        },
        yAxis: {
          type: 'value'
        },
        series: [
          {
            data: series,
            type: 'bar'
          }
        ]
      }
      option && chartDom.setOption(option)
    })
    .catch((err) => {
      console.log(err)
    })
})
</script>
