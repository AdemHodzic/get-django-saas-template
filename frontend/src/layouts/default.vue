<template>
  <div class="app">
    <Sidebar class="sidebar"/>
    <router-view class="router"/>
  </div>
</template>

<script>
import Sidebar from '@/components/common/sidebar.vue';

export default {
  name: 'DefaultLayout',
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
    width: 100%;
  }

  .sidebar {
    flex: 1;
  }

  .router {
    @apply py-2 px-4;
    flex: 6;
  }
</style>
