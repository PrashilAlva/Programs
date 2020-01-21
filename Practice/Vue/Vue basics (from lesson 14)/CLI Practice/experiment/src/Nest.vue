<template>
  <div id="app">
    <img src="./assets/logo.png">
    <h1>{{ msg }}</h1>
    <ul>
    <li v-for="food in foods">{{food}}</li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      msg: 'Your Favorite Foods',
      foods:['Burger','Pizza','Biriyani']
    }
  }
}
</script>

<style>
h1{
    color:pink;
}
body{
    background:url(https://coolbackgrounds.io/images/backgrounds/index/disco-dba865f1.png) center no-repeat;
}
</style>
