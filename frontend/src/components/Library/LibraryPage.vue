<script setup>
import SearchBar from "../Utilities/SearchBar.vue"
</script>

<template>
    <div class="content-container">
        <div class="component">
            <SearchBar />
        </div>
        <div class="component">

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
    
    .component:first-child {
        display: flex;
        justify-content: center;
        align-items: center;
    }
</style>