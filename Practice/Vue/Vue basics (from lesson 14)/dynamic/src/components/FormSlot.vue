<template>
<div>
  <slot name="form-heading"></slot>
  <slot name="form-inputs"></slot>
  <slot name="form-button"></slot>
</div>
</template>

<script>
import Form1 from '../components/Form1.vue'
import Form2 from '../components/Form2.vue'
export default {
    components:{
        'form-one':Form1,
        'form-two':Form2
    },
  data(){
    return{}
  }
}
</script>

<style>

</style>
