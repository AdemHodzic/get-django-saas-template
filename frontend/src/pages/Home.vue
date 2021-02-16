<template >
  <div class="home">
    <alert-box class="home__confirm-email-alert" title="Confirm Your Account" v-if="!user.confirmed_email">
      Hey {{ user.first_name}},<br />
      Can you confirm your account?  We've sent you an email over at <strong>{{ user.email }}</strong> with instructions on how to do it.
    </alert-box>
    <span>Hello, {{ user.first_name }}</span> 
  </div>
</template>

<script>

import AlertBox from '@/components/common/alert-box.vue'

import { mapGetters } from "vuex";

export default {
  name: 'HomePage',
  components: {
    AlertBox
  },
  computed: {
    ...mapGetters('auth', {'user': 'getUser'})
  },
};
</script>

<style>
  .home {
    @apply py-2 px-4;
  }

  .home__confirm-email-alert {
    @apply my-4;
  }
</style>
