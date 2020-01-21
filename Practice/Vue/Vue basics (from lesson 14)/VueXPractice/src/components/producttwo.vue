<template>
  <div id="pro2">
      <h2>Product Two</h2>
      <div v-for="ele in saleProductus">
          <h1><b>{{ele.name}}</b></h1>
          <p>Rs.{{ele.price}}</p>
        </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
    }
  },
  computed:{
      product(){
          return this.$store.state.items;
      },
      saleProductus(){
        return this.$store.getters.saleProducts;
      }
  }
}
</script>

<style scoped>
#pro2{
    background-color:black;
    color:wheat;
}
</style>
