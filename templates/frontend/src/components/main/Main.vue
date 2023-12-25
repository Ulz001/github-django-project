<template>
  <el-row>
    <el-col :span="8">
      <div class="chart" ref="chart" id="chart" />
    </el-col>
    <el-col :span="8">
      <div class="chart" ref="inChart" id="inChart" />
    </el-col>
    <el-col :span="8">
      <div class="chart" ref="outChart" id="outChart" />
    </el-col>
  </el-row>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { getMaterialList, getInStashList, getOutStashList } from '@/api/api.js'

import * as echarts from 'echarts'
import { GridComponent } from 'echarts/components'
import { BarChart } from 'echarts/charts'
import { CanvasRenderer } from 'echarts/renderers'

echarts.use([GridComponent, BarChart, CanvasRenderer])

const chart = ref('')
const inChart = ref('')
const outChart = ref('')

onMounted(async () => {
  const chartDom = echarts.init(chart.value)
  const inChartDom = echarts.init(inChart.value)
  const outChartDom = echarts.init(outChart.value)

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

  await getInStashList()
    .then((res) => {
      const option = {
        tooltip: {
          trigger: 'item'
        },
        legend: {
          top: '5%',
          left: 'center'
        },
        series: [
          {
            name: 'Access From',
            type: 'pie',
            radius: ['40%', '70%'],
            avoidLabelOverlap: false,
            itemStyle: {
              borderRadius: 10,
              borderColor: '#fff',
              borderWidth: 2
            },
            label: {
              show: false,
              position: 'center'
            },
            emphasis: {
              label: {
                show: true,
                fontSize: 40,
                fontWeight: 'bold'
              }
            },
            labelLine: {
              show: false
            },
            data: res.data.data
          }
        ]
      }
      option && inChartDom.setOption(option)
    })
    .catch((err) => {
      console.log(err)
    })

  await getOutStashList().then((res) => {
    const option = {
      tooltip: {
        trigger: 'item'
      },
      legend: {
        top: '5%',
        left: 'center'
      },
      series: [
        {
          name: 'Access From',
          type: 'pie',
          radius: ['40%', '70%'],
          avoidLabelOverlap: false,
          itemStyle: {
            borderRadius: 10,
            borderColor: '#fff',
            borderWidth: 2
          },
          label: {
            show: false,
            position: 'center'
          },
          emphasis: {
            label: {
              show: true,
              fontSize: 40,
              fontWeight: 'bold'
            }
          },
          labelLine: {
            show: false
          },
          data: res.data.data
        }
      ]
    }
    outChartDom.setOption(option)
  })
})
</script>

<style scoped>
.chart {
  width: 500px;
  height: 300px;
}
</style>
