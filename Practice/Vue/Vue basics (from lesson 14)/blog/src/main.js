import Vue from 'vue'
import App from './App.vue'
import VueResource from 'vue-resource'
import VueRouter from 'vue-router'
import Router from './router'

Vue.use(VueResource);

Vue.use(VueRouter);

const route=new VueRouter({
  mode:'history',
  routes:Router
})





new Vue({
  el: '#app',
  render: h => h(App),
  router:route,
})
