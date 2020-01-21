<template>
<div>
<nav-blog></nav-blog>
<router-view></router-view>
</div>
</template>

<script>
import addBlog from './components/blogInsert.vue'
import viewBlog from './components/blogView.vue'
import navBlog from './components/blogNav.vue'
export default {
  components:{
    'add-Blog':addBlog,
    'view-blog':viewBlog,
    'nav-blog':navBlog
  },
  name: 'app',
  data () {
    return {
    }
  }
}
</script>

<style>
body {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}


</style>
