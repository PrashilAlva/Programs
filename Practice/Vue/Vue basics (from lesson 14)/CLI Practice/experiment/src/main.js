import Vue from 'vue'
import App from './App.vue'
import Food from './Nest.vue'

Vue.component('foods',Food)

new Vue({
  el: '#app',
  render: h => h(App)
})
