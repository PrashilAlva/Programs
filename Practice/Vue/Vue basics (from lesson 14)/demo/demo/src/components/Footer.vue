<template>
<footer>
<h1>&copy; {{title}}</h1>
</footer>
</template>

<script>
export default {
  data () {
      return{
              title:'2019 Prashil Alva Dept.of Food'
      }
  },
created(){
  bus.$on('change',(data)=>{
    this.title=data
  })
}
}
</script>
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
