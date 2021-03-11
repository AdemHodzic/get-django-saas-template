<template>
  <table>
    <thead>
      <tr>
        <slot name="thead"></slot>
      </tr>
    </thead>
    <tbody>
      <slot></slot>
    </tbody>
  </table>
</template>

<script>
export default {
  name: 'AtomsTable'
}
</script>

<style>
  table {
    @apply w-full table-auto border-collapse shadow-sm;
  }

  thead tr {
    @apply text-left text-sm text-white bg-gray-700;
  }

  thead tr th,
  tbody tr td {
    @apply p-2;
  }

  tbody tr:nth-of-type(odd) {
    @apply bg-gray-200;
  }
  tbody tr:nth-of-type(even) {
    @apply bg-white;
  }
  
</style>
