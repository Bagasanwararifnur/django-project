<script setup>
import { ref } from 'vue'
const name = ref('')
const password = ref('')

async function submitButton () {
  const url = 'http://127.0.0.1:8000/api/v1/accounts/login'
  const formData = new FormData()
  formData.append('username', name.value)
  formData.append('password', password.value)
  // console.log(formData)
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'accept': 'application/json',
    },
    body: formData,
    credentials: 'include',
  });

  if (response.ok){
    const result = await response.json()
    console.log(result)
  }
  else {
    console.error('Error:', response.status)
  }
}


async function checkButton () {
  const url = 'http://127.0.0.1:8000/api/v1/accounts/coba_authentication'
  const response = await fetch(url, {
    method: 'GET',
    headers: {
      'accept': 'application/json',
    },
    credentials: 'include',
  })

  if (response.ok){
    const result = await response.json()
    console.log(result)
  }
  else {
    console.error('Error:', response.status)
  }
}


</script>

<template>
  <form action="">
    <input type="text" v-model="name" placeholder="Enter your message" />
    <input type="password" v-model="password" placeholder="password">
    <button @click="submitButton">Submit</button>
  </form>

  <button @click="checkButton">Click Disini</button>
</template>

<style scoped>
</style>
