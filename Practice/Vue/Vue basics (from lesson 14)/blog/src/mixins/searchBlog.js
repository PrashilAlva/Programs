export default{
    computed:{
        filteredBlogs:function(){
            return this.blog.filter((blogg)=>{
                return blogg.title.match(this.search)
            });
    }
}
}