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
    height: 100%;
    width: 100%;
    @apply bg-gray-100;
  }
</style>
