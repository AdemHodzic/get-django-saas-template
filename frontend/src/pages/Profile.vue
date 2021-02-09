<template>
  <div class="profile">
    <button class="profile__logout-btn" @click="logout">Log Out</button>
  </div>
</template>

<script>

import { mapActions, mapGetters } from 'vuex';

export default {
  name: 'Profile',
  computed: {
    ...mapGetters('auth', ['errors']),
  },
  methods: {
    ...mapActions('auth', { 'requestLogout': 'logout' }),
    async logout () {
      await this.requestLogout()

      if (!this.errors || this.errors.length === 0) {
        this.$router.push({ name: 'Auth_login' })
      } 
    }
  },
};
</script>

<style>
  .profile {
  }

  .profile__logout-btn {
    @apply px-4 py-2;
    @apply m-4;
    @apply bg-white;
    @apply rounded;
  }
</style>
