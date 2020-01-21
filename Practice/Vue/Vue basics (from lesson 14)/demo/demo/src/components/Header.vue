<template>
<header>
<h1 @click="hello()">{{title}}</h1>
</header>
</template>

<script>
import {bus} from '../main'
export default {
  props:{
    title:{
      type:String,
      required:true
    }
  },
  data () {
      return{
      }
  },
  methods:{
    hello:function(){
      this.title='Indian Khazana'
      bus.$emit('change','Indian Khazana')
    }
  }
}
</script>

<style>
<style scoped>
header{
    border:2px solid wheat;
    border-radius:2em;
}
h1{
    color:lightpink;
    text-align:center;
  font-weight: normal;

}
</style>
