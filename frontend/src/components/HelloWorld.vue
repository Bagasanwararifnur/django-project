<script setup>
import { ref } from 'vue'
const name = ref('')
const password = ref('')

async function submitButton () {
  const url = 'http://127.0.0.1:8000/api/v1/accounts/login'
  const formData = new FormData()
  formData.append('username', name.value)
  formData.append('password', password.value)
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

async function logoutButton (){
  const url ='http://127.0.0.1:8000/api/v1/accounts/logout';
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'accept': 'application/json',
    },
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


</script>

<template>
  <div id="container">

    <div id="form-container">
      <div id="side-gridcontainer">
        <div id="side-container">
          <!-- Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quisquam perferendis cupiditate ullam fugiat natus, provident commodi quasi nostrum quis! Consectetur odit ullam et labore non necessitatibus dolorem iusto nobis similique? -->
        </div>
        <div id="side-container">
          <div id="action-container">
            <div id="logo"></div>
          </div>
          <div id="action-container">
            <form @submit.prevent="submitButton" id="form-asli">
              <label>Welcome to Libraverse</label>
              <!-- <label>Login to Access</label> -->
              <label for="username" class="label-input">Username</label>
              <input type="text" v-model="name" placeholder="Enter your username" />
              <label for="password" class="label-input">Password</label>
              <input type="password" v-model="password" placeholder="Enter your password">
              <button type="submit">Login</button>
              <label class="lower-label">Don't Have Account? <a href="https://www.youtube.com/watch?v=XOKP8CMqilM&list=RDguExDl4241M&index=14&ab_channel=%E3%83%B0%E4%B8%96%E7%95%8C%E6%83%85%E7%B7%92-Isekaijoucho-" target="_blank">Create One</a></label>
            </form>
          </div>
        </div>
      </div>
      <!-- <div id="bottom-container">ppp</div> -->
    </div>

  </div>
  <!-- <form @submit.prevent="submitButton">
    <input type="text" v-model="name" placeholder="Enter your message" />
    <input type="password" v-model="password" placeholder="password">
    <button type="submit">Submit</button>
  </form>
  <p id="paragraf">Lorem, ipsum dolor sit amet consectetur adipisicing elit. Totam quod maiores assumenda placeat, aperiam mollitia quidem incidunt consequatur neque earum omnis tenetur beatae odio sit. Amet perferendis mollitia explicabo ipsa.

  </p>
  <button @click="checkButton">Click Disini</button>
  <button @click="logoutButton">Logout</button> -->
</template>


<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display&display=swap');

#paragraf {
  font-family: 'Playfair Display', serif;
}

#container {
  /* border: 2px solid red; */
  height: 100%;
  width: 100%;
  box-sizing: border-box;
  display: flex;
  justify-content: center;
  align-items: center;
}

#form-container {
  border: 2px solid black;
  width: 60%;
  height: 70%;
  border-radius: 10px;
  position: relative;
  box-sizing: border-box;
  font-family: 'Playfair Display', serif;
  overflow: hidden;
}

#side-gridcontainer {
  display: grid;
  grid-template-columns: 1fr 2fr;
  box-sizing: border-box;
  height: 100%;
}

#side-container {
  /* background-color: yellow; */
  border: 1px solid white;
  height: 100%;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  box-sizing: border-box;
}

#side-container:nth-child(1){
  border: none;
  background-color: black;
  text-align: center;
}

#side-container:nth-child(2){
  border: none;
  background-color: white;
  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: 1fr 10fr;
}

#bottom-container {
  /* background-color: green; */
  border: 1px solid white;
  height: 5%;
  width: 100%;
  box-sizing: border-box;
  position: absolute;
  bottom: 0;
  display: flex;
  justify-content: center;
  align-items: center;
}

#action-container {
  border: 1px solid black;
  /* background-color: red; */
  width: 100%;
  height: 100%;
  color: black;
}

#action-container:nth-child(1){
  position: relative;
  display: flex;
  align-items: center;
}

#action-container:nth-child(2){
  display: flex;
  align-items: center;
  justify-content: center;
}

#logo{
  border: 2px solid black;
  width: 200px;
  height: 50px;
  position: absolute;
  right: 5px;
  border-radius: 5px;
}

#form-asli {
  /* border: 2px solid black; */
  height: 70%;
  width: 50%;
  display: grid;
  gap: 10px;
  grid-template-rows: 2fr 1fr 1.5fr 1fr 1.5fr 1fr 1fr;
}

#form-asli * {
  /* border: 2px solid black; */
  height: 100%;
}

#form-asli input {
  background-color: white;
  border: 2px solid black;
  padding: 10px;
  border-radius: 5px;
  font-family: 'Playfair Display', serif;
  color: black;
  box-sizing: border-box;
}

#form-asli label:first-of-type{
  font-size: 40px;
}

.label-input{
  display: flex;
  /* justify-content: center; */
  align-items: end;
  font-size: 20px;
}

.lower-label{
  font-size: 12px;
  /* color: blue; */
  /* text-decoration:  underline; */
  /* cursor: pointer; */
  /* display: flex; */
  justify-content: center;
  /* align-items: center; */
}

</style>
