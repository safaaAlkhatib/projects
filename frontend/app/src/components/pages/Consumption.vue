<template>
    <div>
        Consumption Page
    </div>
</template>

<script>
import router from '../../router'
export default {
  name: 'Consumption',
   mounted() {
    this.checkLoggedIn()
  },
  methods: {
    checkLoggedIn() {
      this.$session.start()
      if (!this.$session.has('token')) {
        router.push('/auth')
      }
    }
  }
}
</script>
