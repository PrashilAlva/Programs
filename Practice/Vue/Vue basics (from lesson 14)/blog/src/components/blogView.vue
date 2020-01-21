<template>
  <div v-change="'nibba'" id="view">
    <h1 style="background:white">View Your Blogs here:</h1>
    <div id="search"><input type="text" v-model="search" placeholder="Search Blogs..."></div>
    <div v-for="ele in filteredBlogs" class="blogss">
      <h2 v-rainbow><router-link v-bind:to="'blog/'+ele.id">{{ele.title | to-upper}}</router-link></h2>
      <article>{{ele.content | to-italic}}</article>
    </div>
  </div>
</template>

<script>
import searchBlog from '../mixins/searchBlog'
export default {
  name: "app",
  data() {
    return {
      blog: [],
      search:''
    };
  },
  methods: {},
  created() {
    this.$http
      .get("https://postblogs-83c5e.firebaseio.com/blogs.json")
      .then(function(data) {
        return data.json();
      }).then(function(data){
        for (let key in data){
          data[key].id=key;
          this.blog.push(data[key])
        }
      })
  },
  computed:{
  },
  filters:{
    'to-upper':function(data){
      return data.toUpperCase();
    },
    toItalic(data){
       return data.toLowerCase().slice(0,100)+"...";
    }
  },
  directives:{
    'rainbow':{
      bind(el,binding,vnode){
        el.style.color="#"+Math.random().toString().slice(2,8);
      }},
      'change':{
        bind(el,binding,vnode){
          if(binding.value=='change'){
            el.style.background='indigo';
          }
          else{
            el.style.background='pink'
          }
          if(binding.arg=='noChange'){
            el.style.background='yellow'
          }
        }
      }
    },
    mixins:[searchBlog]
};
</script>

<style>
#view {
  text-align: left;
  margin: 0 auto;
}

.blogss {
  padding: 20px;
  padding-top: 0px;
  box-sizing: border-box;
}
</style>
