<template>
<nav>
    <ul>
        <li><router-link to="/"><h4>View Blogs</h4></router-link></li>
        <li><router-link to="/add"><h4>Add new Blogs</h4></router-link></li>
    </ul>
</nav>
</template>

<script>
export default {
  data() {
    return {
    };
  }
};
</script>

<style>
body{
  text-align: center;
}
h4{
  color:wheat;
}
nav{
  background:grey;
  padding:10px;
}
</style>
