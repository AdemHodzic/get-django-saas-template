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
      <template v-for="tab in tabs">
        <template v-if="tab === selectedTab">
          <slot  :name="tab"></slot>
        </template>
      </template>
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