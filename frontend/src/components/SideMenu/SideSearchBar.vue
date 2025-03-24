<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter()
const inputSearch = ref('');

function searchHandle(){
    const path = router.currentRoute.value.path
    router.push({ path: path, query:{ valueSearch:inputSearch.value }})
}

</script>

<template>
    <div class="searchbar-container">
        <input type="text" placeholder="Search..." class="input-searchbar" v-model="inputSearch">
        <button class="input-searchbar" @click="searchHandle">Search</button>
    </div>
</template>

<style scoped>
    .searchbar-container {
        /* background-color: lightgray; */
        /* border: 2px solid black; */
        height: 100%;
        width: 20em;
        padding: 0px;
        display: grid;
        grid-template-columns: 15em auto;
        box-sizing: border-box;

    }

    .input-searchbar:last-child {
        /* width: 100%; */
        padding: 0px;
        border-radius: 0px;
        /* box-sizing: border-box; */
    }

    .input-searchbar:first-child{
        background-color: white;
        border: none;
        color: black;
        font-family: "Playfair Display", serif;
        border: 2px solid black;
        padding-left: 10px;
    }
</style>