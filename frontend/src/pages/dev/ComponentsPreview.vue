<template>
  <div class="components-preview">
    <AlertBox title="This is example title">This is example body</AlertBox>
    <Card>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut sem nulla pharetra diam. Pharetra vel turpis nunc eget lorem dolor sed. Et netus et malesuada fames ac. Fames ac turpis egestas sed tempus urna et pharetra pharetra. Amet venenatis urna cursus eget nunc scelerisque viverra mauris. Bibendum neque egestas congue quisque egestas diam in arcu. Augue neque gravida in fermentum et sollicitudin ac orci. Etiam erat velit scelerisque in dictum. Aliquam id diam maecenas ultricies mi eget.</p>
    </Card>
  </div>
</template>

<script>

import AlertBox from '@/components/common/alert-box.vue'
import Card from '@/components/atoms/card.vue'

export default {
  name: 'ComponentsPreviewPage',
  components: {
    AlertBox,
    Card,
  },
}
</script>

<style>
  .components-preview > * {
    @apply mb-4;
  }
</style>

