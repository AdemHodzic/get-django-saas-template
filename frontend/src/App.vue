<template>
  <router-view class="main-router"/>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
  .main-router {
    height: 100vh;
    width: 100vw;
    @apply bg-gray-100;
  }
</style>
