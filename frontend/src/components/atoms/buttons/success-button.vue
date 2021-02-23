<template>
  <AtomsBaseButton class="success-button">
    <slot></slot>
  </AtomsBaseButton>
</template>

<script>

import AtomsBaseButton from './base-button'
export default {
  name: 'AtomsSuccessButton',
  components: {
    AtomsBaseButton,
  }
}
</script>

<style>
  .success-button {
    @apply bg-green-500 text-white
  }
</style>