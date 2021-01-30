import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../pages/Home.vue';
import Login from '../pages/Login.vue';

import AuthLayout from '../layouts/auth.vue';
import DefaultLayout from '../layouts/default.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/auth',
    name: 'Auth',
    component: AuthLayout,
    children: [{
      path: 'login',
      name: 'Auth_login',
      component: Login,
    }],
  },
  {
    path: '/',
    name: 'Default',
    component: DefaultLayout,
    children: [
      {
        path: '/',
        name: 'Home',
        component: Home,
        icon: ['fa', 'home'],
      },
      {
        path: '/profile',
        name: 'Profile',
        component: () => import(/* webpackChunkName: "profile" */ '../pages/Profile.vue'),
        icon: ['fa', 'user'],
      },
    ],
  },
];

const router = new VueRouter({
  routes,
});

export default router;
