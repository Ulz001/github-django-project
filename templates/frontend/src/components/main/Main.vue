<template>
  <el-row>
    <el-col :span="6">
      <div class="chart" style="width: 300px; height: 300px" ref="chart" id="chart" />
    </el-col>
    <el-col :span="6">
      <div class="chart" style="width: 300px; height: 300px" ref="in" id="in" />
    </el-col>
    <el-col :span="6">
      <div class="chart" style="width: 300px; height: 300px" ref="out" id="out" />
    </el-col>
    <el-col :span="6">
      <div class="chart" style="width: 300px; height: 300px" ref="check" id="check" />
    </el-col>
  </el-row>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { getMaterialList } from '@/api/api.js'

import * as echarts from 'echarts'
import { GridComponent } from 'echarts/components'
import { BarChart } from 'echarts/charts'
import { CanvasRenderer } from 'echarts/renderers'

echarts.use([GridComponent, BarChart, CanvasRenderer])

const chart = ref('')

onMounted(async () => {
  const chartDom = echarts.init(chart.value)

  await getMaterialList()
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
