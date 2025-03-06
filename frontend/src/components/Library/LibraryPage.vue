<script setup>
import SearchBar from "../Utilities/SearchBar.vue"
import LibraryDashboard from "./LibraryDashboard.vue";
</script>

<template>
    <div class="content-container">
        <div class="component">
            <SearchBar />
        </div>
        <div class="component">
            <LibraryDashboard />
        </div>
    </div>
</template>

<style scoped>
    .content-container {
        /* background-color: blue; */
        margin: 0px;
        /* border: 2px solid black; */
        color: white;
        height: 100%;
        box-sizing: border-box;
        display: grid;
        grid-template-rows: 1.2fr 14fr;
    }
    .component {
        height: 100%;
        width: 100%;
        /* background-color: red; */
        /* border: 2px solid black; */
        box-sizing: border-box;
    }
    
    .component:first-child{
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 2;
    }

    .component:nth-child(2){
        display: grid;
        place-items: center;
        /* border: 2px solid red; */
        padding-top: 20px;
        max-height: 85vh;
        background-color: white;
        overflow-y: scroll
    }

    .component:nth-child(2)::-webkit-scrollbar {
        width: 8px; /* Lebar scrollbar vertikal */
        height: 8px; /* Tinggi scrollbar horizontal */
    }

    /* Gaya thumb (bagian yang bisa digeser) */
    .component:nth-child(2)::-webkit-scrollbar-thumb {
        background-color: #888; /* Warna dasar thumb */
        border-radius: 4px; /* Membuat thumb lebih rounded */
    }

    /* Track (background area) */
    .component:nth-child(2)::-webkit-scrollbar-track {
        background-color: #f0f0f0; /* Warna track */
        border-radius: 4px; /* Membuat track lebih rounded */
    }

    /* Gaya thumb saat di-hover */
    .component:nth-child(2)::-webkit-scrollbar-thumb:hover {
        background-color: #555; /* Warna thumb saat hover */
    }
</style>