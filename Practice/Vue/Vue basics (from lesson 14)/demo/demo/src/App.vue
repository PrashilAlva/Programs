<template>
<div>
<app-header v-bind:title='title'></app-header>
<app-food v-bind:foods='foods'></app-food>
<app-footer></app-footer>
</div>
</template>

<script>
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'
import Food from './components/Foods.vue'
export default {
  components:{
    'app-header':Header,
    'app-footer':Footer,
    'app-food':Food
  },
  name:'app',
  data () {
    return{
          foods: [
                {name: 'Biriyani', speciality: 'Biryani, also known as biriyani, biriani, birani or briyani, is a mixed rice dish with its origins among the Muslims of the Indian subcontinent. It can be compared to mixing a curry, later combining it with semi-cooked rice separately.', show: false},
                {name: 'Gulab Jamun', speciality: 'Gulab jamun is a milk-solid-based sweet from the Indian subcontinent, popular in India, Nepal, Pakistan, the Maldives, and Bangladesh, as well as Myanmar.', show: false},
                {name: 'Kori Rotti', speciality: 'Malabar matthi curry, also known as fish curry, is an Indian dish. It consists of sardines semi-stewed in a Kerala-style curry with assorted vegetables, such as okra or onions. It is usually served with rice, naan, bread, or tapioca. ', show: false},
                {name: 'Kebab', speciality: 'Kori rotti is a spicy dish of Tulu Udupi-Mangalorean cuisine, a combination of red-chili based chicken curry and crisp, dry wafers made from boiled rice. Kori means chicken in Tulu', show: false},
                {name: 'Tandoor Roti', speciality: 'Roti is a round flatbread native to the Indian subcontinent made from stoneground wholemeal flour, traditionally known as atta, and water that is combined into a dough. ', show: false},
                {name: 'Butter Chicken', speciality: 'Butter chicken or Makhan murg is a dish, originating in Indian subcontinent, of chicken in a mildly spiced tomato sauce.', show: false}
            ],
             title:'List of Indian Foods!'
    }
  },
  beforeCreate(){
    alert("Creating...")
  },
  created(){
    alert("Created")
  },
  beforeMount(){
    alert("Mounting...")
  },
  mounted(){
    alert("Mounted")
  },
  beforeUpdate(){
    alert("Updating...")
  },
  updated(){
    alert("Updated")
  }
}
</script>

<style>
body{
    background:url(https://coolbackgrounds.io/images/backgrounds/index/disco-dba865f1.png) center no-repeat;
     font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  
}
</style>
