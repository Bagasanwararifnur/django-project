<script setup>

</script>

<template>
    <div id="menu-container">
        <div class="menu-item-container"></div>
        <div class="menu-item-container">
            <router-link to='/book-owned' class="side-menu-item">Book Owned</router-link>
            <router-link to='/book-borrowed' class="side-menu-item">Book Borrowed</router-link> 
        </div>
    </div>
</template>


<style scoped>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display&display=swap');

    #menu-container {
        height: 100vh;
        position: absolute;
        /* border: 2px solid black; */
        box-sizing: border-box;
        display: grid;
        /* width: 200px; */
        transition: 0.5s;
        grid-template-rows: 1fr 13fr;
        overflow: hidden;
    }

    .side-menu-item{
        display: flex;
        height: 50px;
        white-space: nowrap;
        justify-content: center;
        align-items: center;
        transition: 0.5s;
        color: black;
        font-family: "Playfair Display",serif;
        /* border: 2px solid black; */
        /* width: inherit; */
    }

    .side-menu-item:hover{
        background-color: black;
        color: white;
        transition: 0.5s;
    }

   .menu-item-container:last-child {
    border: 2px solid black;
    background-color: white;
    /* width: 100%; */
    z-index: 2;
   }
</style>