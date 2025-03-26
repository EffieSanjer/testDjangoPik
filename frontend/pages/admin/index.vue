<template>

</template>

<script>
  export default {
    middleware: ['auth'],
    layout: 'admin',

    mounted() {
      this.$router.push('/admin/hikes/')
    }
  }

</script>
