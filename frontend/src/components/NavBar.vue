<script setup>
import LoginRibbon from "./LoginRibbon.vue";
import { ref, onMounted } from "vue"
import SvgIcon from "@jamescoyle/vue-icon";
import { mdiHomeVariantOutline } from '@mdi/js';
import { mdiLibraryOutline } from '@mdi/js';
import { mdiStoreSettingsOutline } from '@mdi/js';
import { mdiInformationOutline } from '@mdi/js';
import { mdiFaceAgent } from '@mdi/js';
import { mdiLogin } from '@mdi/js';
import { mdiMenu } from '@mdi/js';

const IconHome = ref(mdiHomeVariantOutline);
const IconLibrary = ref(mdiLibraryOutline);
const IconStore = ref(mdiStoreSettingsOutline);
const IconAbout = ref(mdiInformationOutline);
const IconSupport = ref(mdiFaceAgent);
const IconLogin = ref(mdiLogin);
const IconMenu = ref(mdiMenu);

const pathIconHome = IconHome.value;
const pathIconLibrary = IconLibrary.value;
const pathIconStore = IconStore.value;
const pathIconAbout = IconAbout.value;
const pathIconSupport = IconSupport.value;
const pathIconLogin = IconLogin.value;
const pathIconMenu = IconMenu.value;

const loginUserSetting = ref(false)
const showMenu = ref(false);

const emit = defineEmits(['update:selectedComponent', 'update:showMenu']);

// function loginUserSettingState (){
//     loginUserSetting.value =!loginUserSetting.value;
//     console.log(loginUserSetting.value);
// }

function handleShowMenuClick() {
  showMenu.value = !showMenu.value;  // Toggle showMenu    
  console.log(`showMenu changed to: ${!showMenu.value}`);
  emit('update:showMenu', showMenu.value)
}


defineProps(["selectedComponent", 'isLogin']);


</script>
<template>
    <div id="nav-container">
        <div class="menu-button" id="menu-sandwich" @click="handleShowMenuClick" v-if="isLogin">
            <svg-icon type="mdi" :path="pathIconMenu" class="logo-nav"></svg-icon>
        </div>
        <div class="menu-button" @click="$emit('update:selectedComponent', 'HomePage')">
            <svg-icon type="mdi" :path="pathIconHome" class="logo-nav"></svg-icon>
            Home
        </div>
        <div class="menu-button" @click="$emit('update:selectedComponent', 'LibraryPage')">
            <svg-icon type="mdi" :path="pathIconLibrary"class="logo-nav"></svg-icon>
            Library
        </div>
        <div class="menu-button" @click="$emit('update:selectedComponent', 'ShopPage')">
            <svg-icon type="mdi" :path="pathIconStore"class="logo-nav"></svg-icon>
            Shop
        </div>
        <div class="menu-button" @click="$emit('update:selectedComponent', 'AboutPage')">
            <svg-icon type="mdi" :path="pathIconAbout"class="logo-nav"></svg-icon>
            About
        </div>
        <div class="menu-button" @click="$emit('update:selectedComponent', 'SupportPage')">
            <svg-icon type="mdi" :path="pathIconSupport"class="logo-nav"></svg-icon>    
            Support
        </div>
        
        <router-link to = '/login' class="menu-button" id="login-button" v-if="!isLogin">
            <svg-icon type="mdi" :path="pathIconLogin" class="logo-nav"></svg-icon>
            Login
        </router-link>


        <!-- <div id="login-user-setting" :style="{ height:loginUserSetting ? '100px':'0px', border: loginUserSetting ? '2px solid black' : 'none'}">
            <LoginRibbon/>
        </div> -->
    </div>
</template>

<style scoped>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display&display=swap');
    


    #nav-container {
        background-color: white;
        color: black;
        border: 2px solid black;
        /* padding: 10px; */
        display: flex;
        box-sizing: border-box;
        /* height: 60px; */
        height: 100%;
        align-items: center;
        justify-content: center;
        font-family: 'Playfair Display', serif;
        position: relative;
        /* font-size: medium; */
    }

    .menu-button {
        margin-right: 20px;
        cursor: pointer;
        /* border: 2px solid black; */
        width: 100px;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        /* border-radius: 4px; */
        transition: 0.5s;
        z-index: 2;
        color: black;
    }
    .menu-button:hover {
        background-color: black;
        color: white;
        transition: 0.5s;
    }

   .logo-nav {
    margin-right: 5px;
   }

    #login-user-setting {
        /* display: none; */
        position: absolute;
        /* background-color: white; */
        width: 200px;
        height: fit-content;
        right: -2px;
        bottom: -102px;
        z-index: 3;
        background-color: white;
        display: grid;
        /* padding: 10px; */
        box-sizing: border-box;
        /* transition: 0.5s; */
        overflow: auto;
    }

    #login-user-setting::-webkit-scrollbar{
        display: none;
    }

    #login-button {
        position: absolute;
        right: 0px;
        margin-right: 0px;
    }

    #menu-sandwich {
        position: absolute;
        left: 0px;
        cursor: pointer;
    }
</style>