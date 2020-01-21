import Vue from 'vue'
import VueX from 'vuex'

Vue.use(VueX)

export const store=new VueX.Store({
    state:{
        items:[
            {name:'Banana',price:'20'},
            {name:'Apple',price:'30'},
            {name:'Orange',price:'40'},
            {name:'Grapes',price:'50'},
            {name:'Watermelon',price:'60'}
          ]
    },
    getters:{
        saleProducts: state =>{
            var saleProduct=state.items.map( products =>{
                return {
                    name:"**"+products.name+"**",
                    price:products.price/2
                }
            })
            return saleProduct;
        }
    }
})