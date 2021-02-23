<template>
  <div class="toast-success">
    <h2 class="toast-success__title">
      {{ title }}      
    </h2>
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: 'AtomsToastSuccess',
  props: ['title']
}
</script>

<style>
  .toast-success {
    /* width: 100px; */
    @apply border-l-8 p-4 border-l-green-500;
    @apply bg-white rounded max-w-xl;
  }

  .toast-success__title {
    @apply font-semibold text-lg;
  }
</style>