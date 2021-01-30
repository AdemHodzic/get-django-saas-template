<template>
  <div class="app">
    <Sidebar class="sidebar"/>
    <router-view class="router"/>
  </div>
</template>

<script>
import Sidebar from '@/components/common/sidebar.vue';

export default {
  name: 'App',
  components: {
    Sidebar,
  },
};
</script>

<style>
  .app {
    @apply flex;
    @apply justify-start;
    @apply items-stretch;
    @apply bg-gray-100;
    height: 100vh;
    width: 100vw;
  }

  .sidebar {
    flex: 1;
  }

  .router {
    flex: 6;
  }
</style>
