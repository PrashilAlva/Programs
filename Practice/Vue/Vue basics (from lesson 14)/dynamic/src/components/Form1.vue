<template>
<div id="form1">
  <div slot="form-heading">
  <h1>{{msg}}</h1>    
  <p>Please Enter the following Details</p>
  </div>
  <div slot="form-inputs">
  <label>Firstname:</label>
  <input type="text" value="Firstname">
  <br>
    <label>LastName:</label>
  <input type="text" value="Lastname">
  <br>
  <label>Hobbies:</label>
    <textarea></textarea>
  </div>
  <div slot="form-buttons">
      <button @click="message()">Submit</button>
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
        msg:'Hello World'
    }
  },
  methods:{
      message:function(){
          alert("Your response has been recorded!")
      }
  }
}
</script>

<style>
#form1{
  text-align: center;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  border:5px solid black;
  border-radius:2em;
}
</style>
