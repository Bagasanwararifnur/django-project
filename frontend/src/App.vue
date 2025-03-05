<script setup>
import { ref } from "vue"
import LoginPage from './components/LoginPage.vue'
import NavBar from './components/NavBar.vue'
import SupportPage from './components/Support/SupportPage.vue'
import HomePage from './components/Home/HomePage.vue'
import AboutPage from './components/About/AboutPage.vue'
import LibraryPage from './components/Library/LibraryPage.vue'
import ShopPage from './components/Shop/ShopPage.vue'

const ComponentsMenu = ref('HomePage')

const ComponentPage = {SupportPage, HomePage, AboutPage, LibraryPage, ShopPage}

</script>

<template>
  <div>
    <NavBar v-model:selectedComponent="ComponentsMenu" />
    <component :is="ComponentPage[ComponentsMenu]" />
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
