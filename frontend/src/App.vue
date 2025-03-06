<script setup>
import { ref, watch} from "vue"
import LoginPage from './components/LoginPage.vue'
import NavBar from './components/NavBar.vue'
import SupportPage from './components/Support/SupportPage.vue'
import HomePage from './components/Home/HomePage.vue'
import AboutPage from './components/About/AboutPage.vue'
import LibraryPage from './components/Library/LibraryPage.vue'
import ShopPage from './components/Shop/ShopPage.vue'
import MenuBar from "./components/Utilities/MenuBar.vue"

const ComponentsMenu = ref('HomePage')
const shownMenuState = ref(false);
// const percobaanValue = ref(false)

const ComponentPage = {SupportPage, HomePage, AboutPage, LibraryPage, ShopPage}

watch(shownMenuState, (newValue, oldValue) => {
  console.log(`showMenuState berubah: ${newValue}`);
}); 

</script>

<template>
  <div>
    <NavBar v-model:selectedComponent="ComponentsMenu" v-model:showMenu="shownMenuState"/>
    <component :is="ComponentPage[ComponentsMenu]" />
    <MenuBar :style="{ width: shownMenuState ? '300px' : '0' }" />
  </div>
</template>

<style scoped>
 div{
  height: 100vh;
  display: grid;
  grid-template-rows: 1fr 13fr;
  max-height: 100vh;
 }

</style>
