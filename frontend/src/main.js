import Vue from 'vue';

import { library } from '@fortawesome/fontawesome-svg-core';
import { faUser, faHome } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import VCalendar from 'v-calendar';

import App from './App.vue';
import router from './router';
import store from './store';
import setupInterceptors from './interceptors';

import '@/assets/css/base.css';
import '@/assets/css/tailwind.css';

library.add(faUser, faHome);

Vue.component('font-awesome-icon', FontAwesomeIcon);

Vue.config.productionTip = false;

Vue.use(VCalendar, {})
setupInterceptors();

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
