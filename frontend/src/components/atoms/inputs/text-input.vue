<template>
  <input type="text" class="text-input" v-bind="$props">
</template>

<script>
export default {
  name: 'AtomsTextInput',
}
</script>

<style>
  .text-input {
    @apply placeholder-gray-400 rounded-md;
    @apply bg-white focus:bg-white;
    @apply border-2 border-blue-500 focus:border-blue-700;  
    @apply shadow-sm focus:shadow-none;
    @apply p-3;
  }
</style>