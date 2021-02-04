import axios from 'axios'
import store from '@/store'

export default function interceptorsSetup () {
  axios.interceptors.request.use(config => {
    const token = localStorage.getItem('token')
    if (token) {
      config.headers.Authorization = `Token ${token}`
    }

    return config
  }, error => console.error(error))
}
