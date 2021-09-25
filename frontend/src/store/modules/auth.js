import axios from 'axios';

const baseUrl = 'http://localhost:8000';

const state = {
  user: null,
  errors: [],
};

const getters = {
  getUser: state => state.user,
  isLoggedIn: state => state.user !== null,
  isAdmin: state => state.user.is_admin,
  errors: state => state.errors,
};

const mutations = {
  setUser(state, user) {
    state.user = user;
  },
  setErrors(state, errors) {
    state.errors = errors;
  },
};

const actions = {
  async login({ commit, dispatch }, payload) {
    commit('setErrors', []);
    try {
      console.log(payload)
      const { data } = await axios.post(`${baseUrl}/auth/login/`, payload);
      localStorage.setItem('token', data.key)
      dispatch('getProfile')
    } catch (error) {
      commit('setErrors', error.response.data.errors);
    }
  },
  async register({ commit, dispatch }, payload) {
    commit('setErrors', []);
    try {
      const { data } = await axios.post(`${baseUrl}/auth/registration/`, payload);
      dispatch('getProfile')
      localStorage.setItem('token', data.key)
    } catch (error) {
      commit('setErrors', error.response.data.errors);
    }
  },
  async getProfile ({ commit }) {
    try {
      const { data } = await axios.get(`${baseUrl}/auth/user/`);
      commit('setUser', data);
    } catch (error) {
      localStorage.setItem('token', '')
    }
  },
  async logout ({ commit }) {
    commit('setErrors', []);
    try {
      await axios.post(`${baseUrl}/auth/logout/`)
      commit('setUser', null);
      localStorage.removeItem('token')
    } catch (error) {
      commit('setErrors', error.response.data.errors);
    }
  }
};

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions,
};
