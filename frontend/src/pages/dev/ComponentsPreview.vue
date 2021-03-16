<template>
  <div class="components-preview">
    <h1 class="area-title">Alerts</h1>
    <hr />
    <AlertBox title="This is example title">This is example body</AlertBox>

    <h1 class="area-title">Toasts</h1>
    <hr />
    <AtomsToastSuccess title="Success!">
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit</p>
    </AtomsToastSuccess>
    <AtomsToastDanger title="Danger!">
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit</p>
    </AtomsToastDanger>
    <AtomsToastWarning title="Warning!">
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit</p>
    </AtomsToastWarning>

    <h1 class="area-title">Card</h1>
    <hr />
    <Card>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut sem nulla pharetra diam. Pharetra vel turpis nunc eget lorem dolor sed. Et netus et malesuada fames ac. Fames ac turpis egestas sed tempus urna et pharetra pharetra. Amet venenatis urna cursus eget nunc scelerisque viverra mauris. Bibendum neque egestas congue quisque egestas diam in arcu. Augue neque gravida in fermentum et sollicitudin ac orci. Etiam erat velit scelerisque in dictum. Aliquam id diam maecenas ultricies mi eget.</p>
    </Card>

    <h1 class="area-title">Buttons</h1>
    <hr />
    <div class="elements-container">
      <AtomsBaseButton>Lorem Impsum</AtomsBaseButton>
      <AtomsPrimaryButton>Lorem Impsum</AtomsPrimaryButton>
      <AtomsSuccessButton>Lorem Impsum</AtomsSuccessButton>
      <AtomsDangerButton>Lorem Impsum</AtomsDangerButton>
      <AtomsWarningButton>Lorem Impsum</AtomsWarningButton>
    </div>

    <h1 class="area-title">Inputs</h1>
    <hr />
    <div class="elements-container">
      <AtomsBaseInput type="text" placeholder="Elon Musk" />
      <AtomsBaseInput type="number" placeholder="42" />
      <AtomsBaseInput type="password" placeholder="*******" />
      <AtomsBaseInput type="textarea" placeholder="lorem ipsum dorem sit amet" />
      <AtomsCheckbox>Lorem ipsum</AtomsCheckbox>
      <AtomsSliderInput min="1" max="100" value="50" />
    </div>
    <h1 class="area-title">Table</h1>
    <hr />
    <AtomsTable>
      <template v-slot:thead>
          <th>ID</th>
          <th>Name</th>
          <th>Email</th>
      </template>
      <tr>
        <td>1</td>
        <td>Adem #1</td>
        <td>adem@test.com</td>
      </tr>
      <tr>
        <td>2</td>
        <td>Adem #2</td>
        <td>adem@test.com</td>
      </tr>
      <tr>
        <td>3</td>
        <td>Adem #3</td>
        <td>adem@test.com</td>
      </tr>
      <tr>
        <td>4</td>
        <td>Adem #4</td>
        <td>adem@test.com</td>
      </tr>
    </AtomsTable>

    <h1 class="area-title">Calendar</h1>
    <span>Check <a class="v-calendar-docs-link" target="_blank" href="https://vcalendar.io/">v-calendar documentation</a></span>
    <hr />
    <div class="elements-container">
      <template v-for="color in colors">
        <div class="elements-container" :key="color">
          <v-date-picker v-model="date" :color="color" />
          <v-date-picker v-model="date" :color="color" is-dark/>
        </div>
      </template>
    </div>

    <h1 class="area-title">Tab bar</h1>
    <hr />
    <AtomsTabBar :tabs="['first', 'second', 'third']">
      <template v-slot:first>
        <h1>
          First Slot Content
        </h1>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut sem nulla pharetra diam. Pharetra vel turpis nunc eget lorem dolor sed. Et netus et malesuada fames ac. Fames ac turpis egestas sed tempus urna et pharetra pharetra. Amet venenatis urna cursus eget nunc scelerisque viverra mauris. Bibendum neque egestas congue quisque egestas diam in arcu. Augue neque gravida in fermentum et sollicitudin ac orci. Etiam erat velit scelerisque in dictum. Aliquam id diam maecenas ultricies mi eget.</p>

      </template>

      <template v-slot:second>
      <h1>
          Second Slot Content
        </h1>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut sem nulla pharetra diam. Pharetra vel turpis nunc eget lorem dolor sed. Et netus et malesuada fames ac. Fames ac turpis egestas sed tempus urna et pharetra pharetra. Amet venenatis urna cursus eget nunc scelerisque viverra mauris. Bibendum neque egestas congue quisque egestas diam in arcu. Augue neque gravida in fermentum et sollicitudin ac orci. Etiam erat velit scelerisque in dictum. Aliquam id diam maecenas ultricies mi eget.</p>
      </template>

      <template v-slot:third>
      <h1>
          Third Slot Content
        </h1>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut sem nulla pharetra diam. Pharetra vel turpis nunc eget lorem dolor sed. Et netus et malesuada fames ac. Fames ac turpis egestas sed tempus urna et pharetra pharetra. Amet venenatis urna cursus eget nunc scelerisque viverra mauris. Bibendum neque egestas congue quisque egestas diam in arcu. Augue neque gravida in fermentum et sollicitudin ac orci. Etiam erat velit scelerisque in dictum. Aliquam id diam maecenas ultricies mi eget.</p>
      </template>

    </AtomsTabBar>
  </div>
</template>

<script>

import AlertBox from '@/components/common/alert-box.vue'
import Card from '@/components/atoms/card.vue'
import AtomsToastSuccess from '@/components/atoms/toast-success.vue'
import AtomsToastDanger from '@/components/atoms/toast-danger.vue'
import AtomsToastWarning from '@/components/atoms/toast-warning.vue'

import AtomsBaseButton from '@/components/atoms/buttons/base-button.vue'
import AtomsPrimaryButton from '@/components/atoms/buttons/primary-button.vue'
import AtomsSuccessButton from '@/components/atoms/buttons/success-button.vue'
import AtomsDangerButton from '@/components/atoms/buttons/danger-button.vue'
import AtomsWarningButton from '@/components/atoms/buttons/warning-button.vue'
import AtomsTable from '@/components/atoms/table/table.vue'

import AtomsBaseInput from '@/components/atoms/inputs/base-input.vue'
import AtomsCheckbox from '@/components/atoms/inputs/checkbox.vue'
import AtomsSliderInput from '@/components/atoms/inputs/slider-input.vue'

import AtomsTabBar from '@/components/atoms/tab-bar.vue'


export default {
  name: 'ComponentsPreviewPage',
  components: {
    AlertBox,
    Card,
    AtomsToastSuccess,
    AtomsToastDanger,
    AtomsToastWarning,
    AtomsBaseButton,
    AtomsPrimaryButton,
    AtomsSuccessButton,
    AtomsDangerButton,
    AtomsWarningButton,
    AtomsBaseInput,
    AtomsCheckbox,
    AtomsSliderInput,
    AtomsTable,
    AtomsTabBar,
  },
  data() {
    return {
      date: new Date(),
      colors: ["gray", "red", "orange", "yellow", "green", "teal", "blue", "indigo", "purple", "pink"]
    };
  },
}
</script>

<style>
  .components-preview > * {
    @apply mb-4;
  }

  .elements-container {
    @apply flex flex-wrap;
    gap: 8px;
  }

  .area-title {
    @apply font-bold text-4xl;
  }

  .v-calendar-docs-link {
    @apply text-blue-500;
  }

  .v-calendar-docs-link:hover {
    @apply text-blue-700 underline;
  }
</style>

