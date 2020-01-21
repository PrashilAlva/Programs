<template>
  <div id="app">
    <product-one ></product-one>
    <product-two ></product-two>
  </div>
</template>

<script>
import ProductOne from './components/productone.vue'
import ProductTwo from './components/producttwo.vue'
export default {
  components:{
    'product-one':ProductOne,
    'product-two':ProductTwo
  },
  name: 'app',
  data () {
    return {
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
