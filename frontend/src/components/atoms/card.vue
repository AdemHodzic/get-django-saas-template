<template>
  <div class="card">
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: 'AtomsCard'
}
</script>

<style>
  .card {
    @apply bg-white rounded-md shadow-xl p-16 max-w-xl
  }
</style>