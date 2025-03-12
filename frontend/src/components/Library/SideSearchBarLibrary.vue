<script setup>
import { ref } from "vue"
import { useRouter } from "vue-router";
import SvgIcon from "@jamescoyle/vue-icon";
import { mdiMenuDown } from '@mdi/js';
import { mdiBookSearch } from '@mdi/js';

const router = useRouter()
const searchMode = router.currentRoute.value.query.modeSearch

const Mode = ref(searchMode)
const inputText = ref("")

const IconMenuDown = ref(mdiMenuDown)
const IconBookSearch = ref(mdiBookSearch)

const pathMenuDown = IconMenuDown.value
const pathBookSearch = IconBookSearch.value

async function OpenDrowpdown() {
    const listItems = document.querySelectorAll('ul li');
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
    console.log(`Input Text: ${getInputText}, Mode: ${getModeValue}`)
    console.log(router.currentRoute.value.query.pageRoot)

    router.push({ path: '/library-search', query: { modeSearch: Mode.value, valueSearch: inputText.value } });
}

</script>

<template>
    <div class="searchbar-container">
        <div class="input-searchbar">
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
        <input type="text" placeholder="Search..." class="input-searchbar" v-model="inputText">
        <button class="input-searchbar" @click="handleSubmit">Search</button>
    </div>
</template>

<style scoped>
    .searchbar-container {
        /* background-color: lightgray; */
        /* border: 2px solid black; */
        height: 100%;
        width: 40em;
        padding: 0px;
        display: grid;
        grid-template-columns: 10em auto 10em;
        box-sizing: border-box;
        position: relative;
        /* border: 2px solid red; */

    }

    .input-searchbar:first-child{
        /* border: 2px solid black; */
        height: 100%;
        position: relative;
        box-sizing: border-box;
    }

    ul{
        margin: 0px;
        list-style-type: none;
        position: absolute;
        /* top: 0px; */
        /* left: 0px; */
        /* border: 2px solid black; */
        padding: 0px;
        width: 100%;
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
        padding: 5px;
    }

    li:first-child{
        display: flex;
        padding: 5px;
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

    li:first-child{
        display: flex;
        height: 100%;
    }

    #down-container {
        position: absolute;
        right: 10px;
    }

    .input-searchbar:last-child {
        width: 100%;
        padding: 0px;
        border-radius: 0px;
        box-sizing: border-box;
    }

    .input-searchbar:nth-child(2){
        background-color: white;
        border: none;
        color: black;
        font-family: "Playfair Display", serif;
        border: 2px solid black;
        padding-left: 10px;
    }
</style>