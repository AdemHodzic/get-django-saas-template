<template>
  <div class="login">
        <div class="form-container flex flex-col gap-y-1 space-y-4 items-center justify-center sm:space-y-16 xs:space-y-16">
        <div class="text-2xl font-bold">
            Log in
        </div>
        <div class="errors-container">
          <alert-box v-for="(error, index) in errors" :key="index" :title="error"></alert-box>
        </div>
        <form class="flex flex-col space-y-4" @submit="onSubmit">
            <label class="flex flex-col">
                <span class="text-gray-700 font-semibold pb-1">Email</span>
                <input v-model="email" type="email" class="form-input bg-gray-100 border-2 border-azure-200 focus:border-azure-700 focus:bg-white focus:shadow-none placeholder-gray-600 p-3 rounded-md" placeholder="Your email">
            </label>
            <label class="flex flex-col">
                <span class="text-gray-700 font-semibold pb-1">Password</span>
                <input v-model="password" type="password" class="form-input bg-gray-100 border-2 border-azure-200 focus:border-azure-700 focus:bg-white focus:shadow-none placeholder-gray-600 p-3 rounded-md" placeholder="********">
            </label>
            <button type="submit" class="bg-blue-900 text-white text-sm font-bold rounded-md p-4">Login</button>
        </form>
        <div class="text-xs font-semibold text-gray-700">
            Don't have an account? <router-link to="/auth/register" :query="$route.query" class="text-blue-600">Sign up</router-link>
        </div>
    </div>
  </div>
</template>

<script>

import { mapGetters, mapActions } from 'vuex';

import AlertBox from '@/components/common/alert-box.vue'

export default {
  name: 'LoginPage',
  components: {
    AlertBox,
  },
  data() {
    return {
      email: '',
      password: '',
    };
  },
  computed: {
    ...mapGetters('auth', ['errors']),
  },
  methods: {
    ...mapActions('auth', ['login']),
    async onSubmit (event) {
      event.preventDefault();
      await this.login({
        username: this.email,
        email: this.email,
        password: this.password,
      });

      if (!this.errors || this.errors.length === 0) {
        const to = this.$route.query.redirectFrom || '/';
        this.$router.push(to)
      } 
    },
  },
};
</script>

<style>
  .login {
    @apply bg-gray-100 p-4;
    @apply grid;
    grid-template-columns: 1fr 1fr 1fr;
    grid-template-rows: 1fr;
    grid-template-areas: ". form ."
  }

  .form-container {
    @apply bg-white;
    grid-area: form;
  }
</style>
