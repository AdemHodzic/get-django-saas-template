<template>
  <div class="toast-danger">
    <h2 class="toast-danger__title">
      {{ title }}      
    </h2>
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: 'AtomsToastDanger',
  props: ['title']
}
</script>

<style>
  .toast-danger {
    /* width: 100px; */
    @apply border-l-8 p-4 border-l-red-500;
    @apply bg-white rounded max-w-xl;
  }

  .toast-danger__title {
    @apply font-semibold text-lg;
  }
</style>