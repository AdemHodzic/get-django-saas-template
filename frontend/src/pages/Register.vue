<template>
  <div class="register">
        <div class="form-container flex flex-col gap-y-1 space-y-4 items-center justify-center sm:space-y-16 xs:space-y-16">
        <div class="text-2xl font-bold">
            Create your account
        </div>
        <div class="errors-container">
          <alert-box v-for="(error, index) in errors" :key="index" :title="error"></alert-box>
        </div>
        <form class="flex flex-col space-y-4" @submit="onSubmit">
            <label class="flex flex-col">
                <span class="text-gray-700 font-semibold pb-1">First name</span>
                <input v-model="firstName" type="text" class="form-input bg-gray-100 border-2 border-azure-200 focus:border-azure-700 focus:bg-white focus:shadow-none placeholder-gray-600 p-3 rounded-md" placeholder="Your name" autofocus>
            </label>
            <label class="flex flex-col">
                <span class="text-gray-700 font-semibold pb-1">Last name</span>
                <input v-model="lastName" type="text" class="form-input bg-gray-100 border-2 border-azure-200 focus:border-azure-700 focus:bg-white focus:shadow-none placeholder-gray-600 p-3 rounded-md" placeholder="Your name" autofocus>
            </label>
            <label class="flex flex-col">
                <span class="text-gray-700 font-semibold pb-1">Email</span>
                <input v-model="email" type="email" class="form-input bg-gray-100 border-2 border-azure-200 focus:border-azure-700 focus:bg-white focus:shadow-none placeholder-gray-600 p-3 rounded-md" placeholder="Your email">
            </label>
            <label class="flex flex-col">
                <span class="text-gray-700 font-semibold pb-1">Password</span>
                <input v-model="password" type="password" class="form-input bg-gray-100 border-2 border-azure-200 focus:border-azure-700 focus:bg-white focus:shadow-none placeholder-gray-600 p-3 rounded-md" placeholder="********">
            </label>
              <label class="flex flex-col">
                <span class="text-gray-700 font-semibold pb-1">Repeat Password</span>
                <input v-model="repeatPassowrd" type="password" class="form-input bg-gray-100 border-2 border-azure-200 focus:border-azure-700 focus:bg-white focus:shadow-none placeholder-gray-600 p-3 rounded-md" placeholder="********">
            </label>
            <button type="submit" class="bg-blue-900 text-white text-sm font-bold rounded-md p-4">Create My Account</button>
        </form>
        <div class="text-xs font-semibold text-gray-700">
            Already have an account? <router-link to="/auth/login" :query="$route.query" class="text-blue-600">Log in</router-link>
        </div>
    </div>
  </div>
</template>

<script>

import { mapGetters, mapActions } from 'vuex';

import AlertBox from '@/components/common/alert-box.vue'

export default {
  name: 'RegisterPage',
  components: {
    AlertBox,
  },
  data() {
    return {
      firstName: '',
      lastName: '',
      email: '',
      password: '',
      repeatPassowrd: '',
    };
  },
  computed: {
    ...mapGetters('auth', ['errors']),
  },
  methods: {
    ...mapActions('auth', ['register']),
    async onSubmit(event) {
      event.preventDefault();

      await this.register({
        first_name: this.firstName,
        last_name: this.lastName,
        username: `${this.lastName} ${this.firstName}`,
        email: this.email,
        password1: this.password,
        password2: this.password,
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
  .register {
    @apply bg-gray-100;
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
