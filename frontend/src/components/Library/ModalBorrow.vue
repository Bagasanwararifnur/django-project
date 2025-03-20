<script setup>


const propsLibrary = defineProps({
    message : {
        type: String,
        default : ''
    }
})

</script>


<template>
    <div class="main-container">
        <div class="modal-container">
            <div class="modal-details">
                {{ propsLibrary.message }}
            </div>
            <div class="modal-details">
                <!-- <button class="modal-buttons" id="close-button" @click="close">Close</button>
                <button class="modal-buttons" id="returned-button" @click="donated">Donate</button> -->
            </div>
        </div>
    </div>
</template>


<style scoped>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display&display=swap');

    .main-container {
        position: absolute;
        color: black;
        top: 0px;
        left: 0px;
        width: 100%;
        height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: rgba(0, 0, 0, 0.5);
        font-family: 'Playfair Display', serif;
    }

    .modal-container {
        width: 500px;
        height: 200px;
        background-color: white;
        border-top: 5px solid black;
        box-sizing: border-box;
        display: grid;
        grid-template-rows: auto 3em;
        transition: transform 0.3s ease-in-out;
    }

    /* .modal-container {
        width: 500px;
        height: 300px;
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
        overflow-y: auto;
        max-height: 80vh;
        margin-top: 100px;
        overflow-x: hidden;
        scroll-behavior: smooth;
        transition: transform 0.3s ease-in-out;
    } */

    .modal-details{
        border: 2px solid black;
    }

    .modal-details:first-child{
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 10px;
        border: 2px solid black;
    }

    .modal-details:last-child{
        display: flex;
        align-items: center;
        justify-content: right;
    }

    .modal-buttons{
        border-radius: 0px;
        padding: 0px;
        width: 90px;
        height: 30px;
        margin-right: 10px;
        transition: 0.5s;
        box-sizing: border-box;
    }

    #close-button{
        background-color: white;
        color: black;
        border: 2px solid black;
    }

    #close-button:hover{
        background-color: black;
        color: white;
        transition: 0.5s;
    }

    #returned-button:hover{
        background-color: white;
        color: black;
        border: 1px solid black;
    }
</style>