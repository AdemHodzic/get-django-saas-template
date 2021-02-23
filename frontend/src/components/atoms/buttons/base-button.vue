<template>
  <button class="base-button">
    <slot></slot>
  </button>
</template>

<script>
export default {
  name: 'AtomsBaseButton',
}
</script>

<style>
  .base-button {
    @apply bg-white text-gray-900 px-8 py-2 rounded font-semibold
  }
</style>