new Vue({
    el:'#validator',
    data:{
        title:'Validator',
        info:'Kindly Enter the Credentials...',
        name:'',
        pword:''
    },
    methods:{
        validate:function(){
            this.name=this.$refs.name.value
            this.pword=this.$refs.pword.value
            if (this.name==='Prashil' && this.pword==='1234'){
                alert("Login Successfull")
            }
            else{
                alert("Invalid Credentials")
            }
        }
    }
})