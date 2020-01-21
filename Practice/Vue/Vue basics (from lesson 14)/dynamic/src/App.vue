<template>
<div>
  <component v-bind:is="component"></component>
  <button @click='form1n()'>For Form1</button>
  <button @click="form2o()">For Form2</button>
  </div>
</template>

<script>
import Form1 from './components/Form1.vue'
import Form2 from './components/Form2.vue'
export default {
  components:{
    'form-one':Form1,
    'form-two':Form2
  },
  name: 'app',
  data(){
    return{
      component:'form-two'
    }
  },
  methods:{
    form1n:function(){
      this.component='form-one'
    },
    form2o:function(){
      this.component='form-two'
    }
  }
}
</script>

<style>
buttons{
  text-align: center;
}
</style>
