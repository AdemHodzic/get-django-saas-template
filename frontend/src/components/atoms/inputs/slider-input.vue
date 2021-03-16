<template>
  <input type="range" class="slider" v-bind="$props">
</template>

<script>
export default {
  name: 'AtomsSliderInput',
}
</script>

<style>
  .slider {
    @apply rounded-lg overflow-hidden appearance-none bg-white h-6 w-60;
  }

  .slider::-webkit-slider-thumb {
    @apply bg-blue-500;
  }

  @media screen and (-webkit-min-device-pixel-ratio: 0) {
    .slider::-webkit-slider-thumb {
      @apply w-6 h-6;
      -webkit-appearance: none;
      appearance: none;
      cursor: ew-resize;
      box-shadow: -405px 0 0 400px rgb(37, 99, 235);
      border-radius: 50%;
    }
  }
</style>