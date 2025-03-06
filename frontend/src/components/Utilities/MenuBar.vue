<script setup>

</script>

<template>
    <div id="menu-container">
        <div class="menu-item-container"></div>
        <div class="menu-item-container"></div>
    </div>
</template>


<style scoped>
    #menu-container {
        height: 100vh;
        position: absolute;
        /* border: 2px solid black; */
        box-sizing: border-box;
        display: grid;
        /* width: 200px; */
        transition: 0.5s;
        grid-template-rows: 1fr 13fr;
    }

   .menu-item-container:last-child {
    border: 2px solid black;
    background-color: white;
    z-index: 2;
   }
</style>