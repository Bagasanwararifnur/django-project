<script setup>
import SideSearchBar from '../SideSearchBar.vue';
import OwnedContainer from './OwnedContainer.vue';
</script>

<template>
    <div class="content-container">

        <div class="sub-content-container">
            <SideSearchBar />
        </div>

        <div class="sub-content-container">
            <OwnedContainer />
        </div>

    </div>
</template>

<style scoped>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display&display=swap');

    .content-container {
        display: grid;
        grid-template-rows: 3em auto;
        box-sizing: border-box;
        height: 100%;
        font-family: "Playfair Display", serif;
    }

    .sub-content-container {
        /* border: 2px solid black; */
        box-sizing: border-box;
        display: flex;
    }

    .sub-content-container:first-child{
        margin-top: 10px;
        display: flex;
        justify-content: right;
        padding-right: 10px;
        border: none;
    }

    .sub-content-container:last-child{
        /* margin-top: 10px; */
        display: flex;
        justify-content: center;
        align-items: center;
    }

</style>