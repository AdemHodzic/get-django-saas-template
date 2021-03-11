<template>
  <label class="inline-flex items-center mt-3">
    <input type="checkbox" class="cursor-pointer form-checkbox h-5 w-5 text-teal-600" v-bind="$props">
    <span class="ml-2 text-gray-700"><slot></slot></span>
  </label>
</template>

<script>
export default {
  name: 'AtomsCheckbox',
}
</script>