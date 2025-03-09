<script setup>
import { ref, watch, computed, onMounted} from "vue"
import { useRouter } from "vue-router"
import LoginPage from './components/LoginPage.vue'
import NavBar from './components/NavBar.vue'
import MenuBar from "./components/Utilities/MenuBar.vue"

const ComponentsMenu = ref('HomePage')
const shownMenuState = ref(false);
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
    console.log(newValue)
    // router.push({ path: '/', query: { pageRoot: ComponentsMenu.value } });
  }
})


</script>

<template>
  <LoginPage v-if="isLoginPage"/>
  <div v-else class="main-app-container">
    <NavBar v-model:selectedComponent="ComponentsMenu" v-model:showMenu="shownMenuState"/>
    <router-view :key="$route.fullPath"></router-view>
    <MenuBar :style="{ width: shownMenuState ? '300px' : '0' }" />
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
