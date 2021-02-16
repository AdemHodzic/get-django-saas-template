<template>
  <div class="alert-box" role="alert">
    <p class="alert-box__title">{{ title }}</p>
    <p class="alert-box__body">
      <slot></slot>
    </p>
  </div>
</template>

<script>
export default {
  name: 'alert-box',
  props: [
    'title',
  ],
}
</script>

<style>
  .alert-box {
    @apply bg-yellow-500;
    @apply border-l-4;
    @apply border-yellow-600;
    @apply text-black;
    @apply p-4;
  }

  .alert-box__title {
    @apply font-bold;
  }

  .alert-box__body {
    @apply pt-2;
  }
</style>
