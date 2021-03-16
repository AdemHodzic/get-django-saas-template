<template>
  <div class="progress">
    <div class="progress-value" :style="{ width: value + '%'}"></div>
  </div>
</template>

<script>
export default {
  props: ['value'],
  name: 'AtomsProgressBar',
}
</script>

<style>
  .progress {
    @apply bg-white;
    @apply flex justify-start items-center;
    @apply h-10;
    border-radius: 100px;
    position: relative;
    padding: 0 5px;
    width: 500px;
  }

  .progress-value {
    @apply bg-blue-500 h-8;
    box-shadow: 0 10px 40px -10px #fff;
    border-radius: 100px;
  }
</style>