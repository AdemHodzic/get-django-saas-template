import axios from 'axios';

const baseUrl = 'http://localhost:8000';

const state = {
  user: null,
  errors: [],
};

const getters = {
  isLoggedIn: (state) => state.user !== null,
  errors: (state) => state.erors,
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
  async login({ commit }, payload) {
    commit('setErrors', []);
    try {
      console.log(payload)
      const { data } = await axios.post(`${baseUrl}/api/users/login`, payload);
      commit('setUser', data);
      localStorage.setItem('token', data.token)
    } catch (error) {
      console.error(error);
      commit('setErrors', error);
    }
  },
  async register({ commit }, payload) {
    commit('setErrors', []);
    try {
      const { data } = await axios.post(`${baseUrl}/api/users/register`, payload);
      commit('setUser', data);
      localStorage.setItem('token', data.token)
    } catch (error) {
      console.error(error);
      commit('setErrors', error);
    }
  },
  async getProfile ({ commit }, payload) {
    commit('setErrors', []);
    try {
      const { data } = await axios.get(`${baseUrl}/api/users/profile`);
      commit('setUser', data);
      localStorage.setItem('token', data.token)
    } catch (error) {
      localStorage.setItem('token', '')
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
