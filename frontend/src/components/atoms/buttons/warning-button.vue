<template>
  <AtomsBaseButton class="warning-button">
    <slot></slot>
  </AtomsBaseButton>
</template>

<script>

import AtomsBaseButton from './base-button'
export default {
  name: 'AtomsWarningButton',
  components: {
    AtomsBaseButton,
  }
}
</script>

<style>
  .warning-button {
    @apply bg-yellow-500 text-white
  }
</style>