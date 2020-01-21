<template>
<div id="foods">
<ul>
<li v-for="food in foods" @click="food.show=!food.show">
<h2>{{food.name}}</h2>
<p v-show="food.show">{{food.speciality}}</p>
</li>
</ul>
<center><button @click="deleteItem()">Delete Food</button></center>
</div>
</template>

<script>
export default {
    props:{
        foods:{
        type:Array,
        required:true
    }
    },
  data () {
      return{}
      },
  methods:{
      deleteItem(){
          this.foods.pop();
      }
  }
}
</script>

<style scoped>
#foods{
    width: 100%;
    max-width: 1200px;
    margin: 40px auto;
    padding: 0 20px;
    box-sizing: border-box;
}
ul{
    display: flex;
    flex-wrap: wrap;
    list-style-type: none;
    padding: 0;
}
li{
    flex-grow: 1;
    flex-basis: 300px;
    text-align: center;
    padding: 30px;
    border: 1px solid #222;
    margin: 10px;
    border-radius:2em;
    color:lightpink;
}
#foods button{
    width:100px;
    height:20px;
}
</style>
