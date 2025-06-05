<template>
  <div class="container">
    <img 
      src="./assets/logo.svg" 
      alt="Vue Logo" 
      class="logo"
      :class="{ 'animate-logo': isSuccess }"
    >
    <div class="content">
      <button @click="testApi">Test API</button>
      <p v-if="response">{{ response }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { testEndpoint } from './services/api'

const response = ref(null)
const isSuccess = ref(false)

const testApi = async () => {
  try {
    const res = await testEndpoint()
    response.value = res.data
    isSuccess.value = true
    setTimeout(() => {
      isSuccess.value = false
    }, 2000)
  } catch (error) {
    response.value = 'Error: ' + error.message
    isSuccess.value = false
  }
}
</script>

<style>
.container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.logo {
  width: 100px;
  margin-bottom: 2rem;
  transition: transform 0.3s ease;
}

.animate-logo {
  animation: swing 2s ease-in-out;
}

@keyframes swing {
  0% { transform: scale(1); }
  20% { transform: scale(0.8); }
  40% { transform: scale(1.1); }
  60% { transform: scale(0.9); }
  80% { transform: scale(1.05); }
  100% { transform: scale(1); }
}

.content {
  text-align: center;
}

button {
  padding: 10px 20px;
  margin: 20px;
}
</style>