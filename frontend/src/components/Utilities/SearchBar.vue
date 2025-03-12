<script setup>
import { ref } from "vue"
import { useRouter } from "vue-router";
import SvgIcon from "@jamescoyle/vue-icon";
import { mdiMenuDown } from '@mdi/js';
import { mdiBookSearch } from '@mdi/js';

const router = useRouter()

const Mode = ref("Author")
const inputText = ref("")

const IconMenuDown = ref(mdiMenuDown)
const IconBookSearch = ref(mdiBookSearch)

const pathMenuDown = IconMenuDown.value
const pathBookSearch = IconBookSearch.value


async function OpenDrowpdown() {
    const listItems = document.querySelectorAll('ul li');
    // console.log('Masuk')
    listItems.forEach((item, index) => {
        if (index >= 1) {
            item.style.display = 'flex';
        }
    });
}

async function SelectedDropdown(event) {
    Mode.value = event.target.innerText
    const listItems = document.querySelectorAll('ul li');
    listItems.forEach((item, index) => {
        if (index >= 1) {
            item.style.display = 'none';
        }
    });
}

function handleSubmit(){
    const getInputText = inputText.value
    const getModeValue = Mode.value
    const querySearch = router.currentRoute.value.query.pageRoot
    console.log(`Input Text: ${getInputText}, Mode: ${getModeValue}`)
    console.log(router.currentRoute.value.query.pageRoot)

    if (querySearch === 'LibraryPage'){
        router.push({ path: '/library-search', query: { modeSearch: Mode.value, valueSearch: inputText.value } });
    }
}



</script>

<template>
    <form action="#" id="search-container" @submit.prevent="handleSubmit">
        <div class="dropdown-container">
            <ul>
                <li @click="OpenDrowpdown">{{ Mode }}
                    <div id="down-container">
                        <svg-icon type="mdi" :path="pathMenuDown" class="logo-nav"></svg-icon>
                    </div>
                </li>
                <li @click="SelectedDropdown">Author</li>
                <li @click="SelectedDropdown">Publisher</li>
                <li @click="SelectedDropdown">Genre</li>
            </ul>
        </div>
        <input type="text" v-model="inputText">
        <input type="submit" value="Submit">
    </form>
</template>

<style scoped>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display&display=swap');


    #search-container{
        display: grid;
        grid-template-columns: 1fr 3fr 1fr;
        /* border: 2px solid black; */
        height: 70%;
        width: 1000px;
        box-sizing: border-box;
        font-family: "Playfair Display", serif;
    }

    #search-container * {
        height: 100%;
        box-sizing: border-box;
    }

    .dropdown-container{
        position: relative;
        box-sizing: border-box;
    }

    ul{
        list-style-type: none;
        /* border: 2px solid black; */
        margin: 0px;
        padding: 0px;
        position:absolute;
        /* width: 100px */
        width: 100%;
        /* display: flex;
        justify-content: center;
        align-items: center;         */
        box-sizing: border-box;
    }

    li{
        margin: 0px;
        padding: 0px;
        width: 100%;
        display: none;
        justify-content: center;
        align-items: center;
        background-color: white;
        box-sizing: border-box;
        color: black;
        border: 2px solid black;
    }

    li:first-child{
        display: flex;
        padding: 20px;
        justify-content: left;
        align-items: center;
        background-color: white;
        color: black;
    }

    li:hover{
        background-color: black;
        color: white;
        transition: 0.5s;
        cursor: pointer;
    }

    input{
        padding: 10px;  
        background-color: white;
        border: 2px solid black;
        color: black;
        font-family: "Playfair Display", serif;
        font-size: 14px;
    }

    input:focus{
        border: 2px solid black;
    }
/* 
    input[type="submit"]:focus{
        transition: 0.5s;
        color: white;
        background-color: black;
    } */

    #down-container{
        position: absolute;
        right: 10px;
        top: 0px;
    }
</style>