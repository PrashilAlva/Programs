<template>
<formm>
 <div slot='form-header'>
  <h1>Hey</h1>
  <p>Howdy Doing</p>
  </div>
   <div slot='form-input'>
   <input type="text" placeholder="Name" required>
   <input type="password" placeholder="PassWord" required>
  </div>
   <div slot='form-button'>
   <button value="Submit" @click="respond()"></button>
  </div>
</formm>
</template>

<script>
import Form from './components/Form.vue'
export default {
  components:{
    'formm':Form
  },
  name: 'app',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  methods:{
      respond:function(){
          alert("Hey")
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
  margin-top: 60px;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
