<script setup>
import { ref, watch } from "vue"
// import LoginPage from './components/LoginPage.vue'
// import NavBar from './components/NavBar.vue'

import SupportPage from "./Support/SupportPage.vue"
import HomePage from "./Home/HomePage.vue"
import AboutPage from "./About/AboutPage.vue"
import LibraryPage from "./Library/LibraryPage.vue"
import ShopPage from "./Shop/ShopPage.vue"

const ComponentPage = {SupportPage, HomePage, AboutPage, LibraryPage, ShopPage}
// const pageRoot = ref('HomePage')    

defineProps(['pageRoot'])

</script>

<template>
    <component :is='ComponentPage[pageRoot]'></component>
</template>