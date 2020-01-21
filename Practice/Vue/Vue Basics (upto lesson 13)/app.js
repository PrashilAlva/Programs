new Vue({
    el:'#main-part',
    data:{
        text:'Hello World!',
        name:'Prashil',
        Job:'Engineer',
        website:'https://github.com/PrashilAlva',
        websiteTag:' <a href="https://www.google.com">My College Page!</a>',
        age:21,
        x:0.0,
        y:0.0,
        nameee:'',
        available:false,
        error:false,
        success:false,
        elems:['loco','pubg','gameloft','ea','wwe'],
        games:[
            {comapny:'gameloft',game:'asphalt'},
            {company:'Tencent',game:'pubg'},
            {company:'ea',game:'Cricket07'},
            {company:'2k',game:'wwe'}
        ]
    },
    methods:{
        greet:function(time){
            return 'Well '+this.name+', '+time
        },
        add:function(){
            this.age++;
        },
        subtract:function(){
            this.age--;
        },
        coordinates:function(event){
            this.x=event.offsetX;
            this.y=event.offsetY;
        },
        click:function(){
            alert("You Clicked me!");
        },
        logName:function(){
            name=document.getElementById("name").value
            alert("You entered "+name)
        },
        logAge:function(){
            age=document.getElementById("age").value
           alert("You entered "+age)
        }
    }
});