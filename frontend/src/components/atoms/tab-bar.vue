<template>
  <div class="tab-bar">
    <div class="tab-bar__nav">
      <div 
        class="tab-bar__tab" 
        v-for="tab in tabs" 
        :key="tab" 
        :class="{'tab-bar__tab--active': selectedTab === tab}"
        @click="selectedTab = tab">
        <span>{{ tab }}</span>
      </div>
    </div>
    <div class="tab-bar__body">
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut sem nulla pharetra diam. Pharetra vel turpis nunc eget lorem dolor sed. Et netus et malesuada fames ac. Fames ac turpis egestas sed tempus urna et pharetra pharetra. Amet venenatis urna cursus eget nunc scelerisque viverra mauris. Bibendum neque egestas congue quisque egestas diam in arcu. Augue neque gravida in fermentum et sollicitudin ac orci. Etiam erat velit scelerisque in dictum. Aliquam id diam maecenas ultricies mi eget.</p>

      <!-- <slot v-for="tab in tabs" :key="tab" :name="tab"></slot> -->
    </div>
  </div>
</template>

<script>
export default {
  name: 'AtomsTabBar',
  props: ['tabs'],
  data() {
    return {
      selectedTab: this.tabs[0]
    }
  },
}
</script>

<style>
  .tab-bar {
    @apply bg-white rounded shadow-sm;
    @apply flex flex-col;
  }

  .tab-bar__nav {
    @apply border-b border-gray-200;
    @apply flex flex-row;
    flex: 1 1 20%;
  }

  .tab-bar__tab {
    @apply flex flex-col items-center  text-blue-600 p-4 cursor-pointer;
    @apply text-lg sm:text-sm font-semibold;
    flex-grow: 1;
  }

  .tab-bar__tab--active {
    @apply border-b-2 border-blue-600;
  }

  .tab-bar__body {
    @apply bg-white p-6;
    flex: 1 1 80%;
  }
</style>