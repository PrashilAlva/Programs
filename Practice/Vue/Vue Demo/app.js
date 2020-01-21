new Vue({
    el:".votes",
    data:{
        heading:'Voting Machine',
        message:'Kindly cast your vote',
        bjp:0,
        cong:0,
        aap:0,
        oth:0
    },
    methods:{
        addb:function(){
            this.bjp=this.bjp+1;
        },
        addc:function(){
            this.cong=this.cong+1;
        },
        adda:function(){
            this.aap=this.aap+1;
        },
        addo:function(){
            this.oth=this.oth+1;
        }
    }
})