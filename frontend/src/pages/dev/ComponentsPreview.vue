<template>
  <div class="components-preview">
    <AlertBox title="This is example title">This is example body</AlertBox>
    <AtomsToastSuccess title="Success!">
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit</p>
    </AtomsToastSuccess>
    <AtomsToastDanger title="Danger!">
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit</p>
    </AtomsToastDanger>
    <AtomsToastWarning title="Warning!">
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit</p>
    </AtomsToastWarning>
    <Card>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut sem nulla pharetra diam. Pharetra vel turpis nunc eget lorem dolor sed. Et netus et malesuada fames ac. Fames ac turpis egestas sed tempus urna et pharetra pharetra. Amet venenatis urna cursus eget nunc scelerisque viverra mauris. Bibendum neque egestas congue quisque egestas diam in arcu. Augue neque gravida in fermentum et sollicitudin ac orci. Etiam erat velit scelerisque in dictum. Aliquam id diam maecenas ultricies mi eget.</p>
    </Card>
    <div class="buttons-container">
      <AtomsBaseButton>Lorem Impsum</AtomsBaseButton>
      <AtomsPrimaryButton>Lorem Impsum</AtomsPrimaryButton>
      <AtomsSuccessButton>Lorem Impsum</AtomsSuccessButton>
      <AtomsDangerButton>Lorem Impsum</AtomsDangerButton>
      <AtomsWarningButton>Lorem Impsum</AtomsWarningButton>
    </div>
    <AtomsTextInput placeholder="Elon Musk" />
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

import AtomsTextInput from '@/components/atoms/inputs/text-input.vue'

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
    AtomsTextInput,
  },
}
</script>

<style>
  .components-preview > * {
    @apply mb-4;
  }

  .buttons-container {
    @apply flex;
    gap: 8px;
  }
</style>

