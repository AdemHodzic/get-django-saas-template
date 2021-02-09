<template>
  <div class="sidebar">
    <router-link to="/">
      <h3 class="sidebar__title">Your App</h3>
    </router-link>
    <nav class="sidebar__nav">
      <router-link
        v-for="route in routes"
        :key="route.path"
        :to="route.path"
        :class="{ 'active-route': route.path === $router.currentRoute.path }">
        <font-awesome-icon :icon="route.icon" class="sidebar__link--icon"/>
        {{ route.name }}
      </router-link>
    </nav>
  </div>
</template>

<script>
export default {
  name: 'Sidebar',
  computed: {
    routes() {
      return this.$router.options.routes.find((element) => element.name === 'Default').children;
    },
  },
};
</script>

<style>
  .sidebar {
    @apply flex;
    @apply flex-col;
    @apply justify-start;
    @apply items-stretch;
    @apply border-gray-300;
    @apply px-4;
    @apply bg-white;
    border-right-width: 1px;
    gap: 16px;
  }

  .sidebar__title {
    @apply text-2xl;
    @apply my-4;
  }

  .sidebar__nav {
    @apply flex;
    @apply flex-col;
    @apply justify-start;
    @apply items-start;
    gap: 8px;
  }

  .sidebar__nav > a{
    @apply hover:underline;
  }
</style>
