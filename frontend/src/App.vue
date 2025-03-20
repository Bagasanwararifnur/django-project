<script setup>
import { ref, watch, computed, onMounted, watchEffect} from "vue"
import { useRouter } from "vue-router"
import LoginPage from './components/LoginPage.vue'
import NavBar from './components/NavBar.vue'
import MenuBar from "./components/Utilities/MenuBar.vue"

async function loginCheck(){
  const url = 'http://127.0.0.1:8000/api/v1/accounts/authorization_check'
  const response = await fetch(url, {
    method: 'GET',
    headers: {
      'accept': 'application/json',
    },
    credentials: 'include',
  })

  if (response.ok) {
    const result = await response.json()
    localStorage.setItem('isLogin',true)
  }
  else {
    localStorage.setItem('isLogin',false)
  }
}

const ComponentsMenu = ref('HomePage')
const shownMenuState = ref(false);
const isLogin = ref()
const router = useRouter();

const isLoginPage = computed(() => router.currentRoute.value.path === '/login')

watch(ComponentsMenu, (newValue) => {
  if (ComponentsMenu.value !== ''){
    router.push({ path: '/', query: { pageRoot: newValue } });

  }
});

watch(() => router.currentRoute.value.path, (newValue)=>{
  if (newValue !== '/'){
    ComponentsMenu.value = ''
    // router.push({ path: '/', query: { pageRoot: ComponentsMenu.value } });
  }
})


onMounted(async() => {
  await loginCheck()
  isLogin.value = localStorage.getItem('isLogin') === 'true'
})


</script>

<template>
  <LoginPage v-if="isLoginPage"/>
  <div v-else class="main-app-container">
    <NavBar v-model:selectedComponent="ComponentsMenu" v-model:showMenu="shownMenuState" :isLogin="isLogin"/>
    <router-view :key="$route.fullPath"></router-view>
    <MenuBar :style="{ width: shownMenuState ? '300px' : '0' }" v-if="isLogin"/>
  </div>
</template>

<style scoped>
 .main-app-container{
  height: 100vh;
  display: grid;
  grid-template-rows: 1fr 13fr;
  max-height: 100vh;
 }

</style>
