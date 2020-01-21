<template>
    <div>
        <h1 >{{blog.title | to-uppercase}}</h1>
        <article>{{blog.content}}</article>
        <p style="text-align:center"><b>Author</b>:{{blog.author}}</p>
        <ul>
            <li v-for="ele in blog.categories" style="padding-left:5px">{{ele}}</li>
        </ul>
    </div>
</template>


<script>
export default {
    data(){
        return{
            blog:{
            },
            id:this.$route.params.id
        }
    },
    created(){
        this.$http.get("https://postblogs-83c5e.firebaseio.com/blogs/"+this.id+".json").then(function(data){
            return data.json()
        }).then(function(data){
            this.blog=data
            console.log(this.blog)
        })
    },
    filters:{
        toUppercase:function(data){
            return data.toUpperCase();
        }
    }
}
</script>


<style scoped>
h1{
    text-align:center;
}
</style>