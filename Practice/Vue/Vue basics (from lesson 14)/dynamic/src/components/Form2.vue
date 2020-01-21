<template>
<div id="form2">
  <div slot="form-heading">
  <h1>{{msg}}</h1>    
  <p>Please Enter your credentials</p>
  </div>
  <div slot="form-inputs">
  <label>UserName:</label>
  <input type="text" value="Firstname">
  <br>
    <label>PassWord:</label>
  <input type="PassWord" value="Lastname">
  <br>
  </div>
  <div slot="form-buttons">
      <button @click="message1()">Login!</button>
      </div>
  </div>
</template>

<script>
import FormSlot from '../components/FormSlot.vue'
export default {
    components:{
        'form-slot':FormSlot
    },
  name: 'app',
  data(){
    return{
        msg:'Hello World Login'
    }
  },
  methods:{
      message:function(){
          alert("Login Successfull")
      }
  }
}
</script>

<style>
#form2{
  text-align: center;
  font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
  background-color: blueviolet;
  color:wheat;
  border:5px ridge wheat;
  border-radius:2em;
  padding:20px;
}
</style>
