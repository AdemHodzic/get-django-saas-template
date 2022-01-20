import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../pages/Home.vue';
import Login from '../pages/Login.vue';
import Register from '../pages/Register.vue';

import AuthLayout from '../layouts/auth.vue';
import DefaultLayout from '../layouts/default.vue';

import store from '@/store'

Vue.use(VueRouter);

const routes = [
  {
    path: '/auth',
    name: 'Auth',
    component: AuthLayout,
    children: [
      {
        path: 'login',
        name: 'Auth_login',
        component: Login,
      },
      {
        path: 'register',
        name: 'Auth_register',
        component: Register,
      },
    ],
    beforeEnter: async  (to, from, next) => {
      if (store.getters['auth/isLoggedIn']) {
        next('/');
      } else {
        await store.dispatch('auth/getProfile');
        if (store.getters['auth/isLoggedIn']) {
          next('/');
        } else {
          next();
        }
      }
    }
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
      {
        path: '/components',
        name: 'Components',
        component: () => import(/* webpackChunkName: "components" */ '../pages/dev/ComponentsPreview.vue'),
        // beforeEnter: async (to, from, next) => {
        //   const user =  store.getters['auth/getUser']

        //   if (!user.is_admin) {
        //     next({ name: 'Home' })
        //   } else {
        //     next()
        //   }
        // },
        adminOnly: true,
      }
    ],
    beforeEnter: async  (to, from, next) => {
      if (store.getters['auth/isLoggedIn']) {
        next();
      } else {
        await store.dispatch('auth/getProfile');
        if (store.getters['auth/isLoggedIn']) {
          next();
        } else {
          next({
            name: 'Auth_login',
            query: {
              redirectFrom: to.fullPath
            }
          });
        }
      }
    }
  },
];

const router = new VueRouter({
  mode: 'history',
  routes,
});

export default router;
