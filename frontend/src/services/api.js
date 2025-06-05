import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:8000'
})

export const testEndpoint = () => api.get('/test')

export default api 