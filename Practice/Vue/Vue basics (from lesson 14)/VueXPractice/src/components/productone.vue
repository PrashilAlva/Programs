<template>
  <div id="pro1">
      <h2>Product List One</h2>
      <ul>
          <li v-for="ele in saleProducts">
              <span>{{ele.name}}</span>
              <span>Rs.{{ele.price}}</span>
            </li>
        </ul>
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
      saleProducts(){
        return this.$store.getters.saleProducts;
      }
  }
}
</script>

<style scoped>
#pro1{
    background-color: brown;
    color:yellow;
}
</style>
