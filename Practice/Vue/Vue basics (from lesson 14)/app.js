Vue.component('Hello',{
    template:'<p>Hello World,{{name}}<br><button @click="changeName">Change my name</button>',
    data:function(){
        return{
            name:'Prashil'
        }
    },
    methods:{
        changeName:function(){
            this.name='Alva'
        }
    }
});


var one=new Vue({
    el:'#app-one',
    data:{
        title:"App ONE"
    },
    methods:{

    },
    computed:{
        greet:function(){
            return "Howdy ho! We are in App-ONE"
        }
    }
})

var two =new Vue({
    el:'#app-two',
    data:{
        title:"App TWO",
        title1:'',
        food:'none'
    },
    methods:{
        changeTitle:function(){
            one.title=this.title1;
            alert("Title of app one changed")
        },
        food_add:function(){
            this.food=this.$refs.food.value
            console.log(this.$refs)
        }
    },
    computed:{
        greet:function(){
            return "Howdy ho! We are in App-TWo"
        }
    }
})