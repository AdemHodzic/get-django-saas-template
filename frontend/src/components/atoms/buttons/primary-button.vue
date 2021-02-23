<template>
  <AtomsBaseButton class="primary-button">
    <slot></slot>
  </AtomsBaseButton>
</template>

<script>

import AtomsBaseButton from './base-button'
export default {
  name: 'AtomsPrimaryButton',
  components: {
    AtomsBaseButton,
  }
}
</script>

<style>
  .primary-button {
    @apply bg-gray-900 text-white
  }
</style>