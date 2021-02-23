<template>
  <div class="toast-warning">
    <h2 class="toast-warning__title">
      {{ title }}      
    </h2>
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: 'AtomsToastWarning',
  props: ['title']
}
</script>

<style>
  .toast-warning {
    /* width: 100px; */
    @apply border-l-8 p-4 border-l-yellow-500;
    @apply bg-white rounded max-w-xl;
  }

  .toast-warning__title {
    @apply font-semibold text-lg;
  }
</style>