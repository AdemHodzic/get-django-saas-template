<template>
  <AtomsBaseButton class="danger-button">
    <slot></slot>
  </AtomsBaseButton>
</template>

<script>

import AtomsBaseButton from './base-button'
export default {
  name: 'AtomsDangerButton',
  components: {
    AtomsBaseButton,
  }
}
</script>

<style>
  .danger-button {
    @apply bg-red-500 text-white
  }
</style>