<script setup>
import { ref } from 'vue'
const name = ref('')
const password = ref('')

async function submitButton () {
  const url = 'http://127.0.0.1:8000/api/v1/accounts/login'
  const formData = new FormData()
  formData.append('name', name.value)
  formData.append('password', password.value)
  console.log(formData)
  const response = await fetch(url, {
    method: 'POST',
    body: formData
  })
  const data = await response.json()
  console.log(data)
  // If successful, clear the form and display success message
  if (data.success) {
    name.value = ''
    password.value = ''
    alert('Login successful!')
  } else {
    alert('Invalid credentials!')
  }
}


</script>

<template>
  <form action="">
    <input type="text" v-model="name" placeholder="Enter your message" />
    <input type="password" v-model="password" placeholder="password">
    <button @click="submitButton">Increment Count</button>
  </form>
</template>

<style scoped>
</style>
