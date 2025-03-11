<script setup>

import { ref, useTemplateRef } from 'vue';
import ModalReturned from './ModalReturned.vue';

const listBook = ref([
    { 'img' : "/src/assets/ximeinii9y.avif", 'author' : "Jules Verne", 'name' : "Pulau Misterius", 'publisher':'Kepustakaan Populer Gramedia'},
    { 'img' : "src/assets/dthbwjxghkyjxa8b2e8y9j.avif", 'author' : "Jules Verne", 'name' : "Twenty Thousand Under the Sea", 'publisher':'Kepustakaan Populer Gramedia'},
])
const numberPagination = ref(Math.floor(listBook.value.length/10+1))

const itemRefs = useTemplateRef("books")

const stateReturnedModal = ref(false)
const details = ref()


function readBook(index){
    const item = itemRefs.value[index]
    console.log(item.querySelector("#book-detail-author").innerHTML)
    console.log(item.querySelector("#book-detail-title").innerHTML)
    console.log(item.querySelector("#book-detail-publisher").innerHTML)
    stateReturnedModal.value = true
}

function returnedBook(index){
    const item = itemRefs.value[index]
    const author = item.querySelector("#book-detail-author").innerHTML
    const title = item.querySelector("#book-detail-title").innerHTML
    const publisher = item.querySelector("#book-detail-publisher").innerHTML

    details.value = {author, title, publisher}

    stateReturnedModal.value = true
}



</script>

<template>
    <div class="item-main-container">

                <div class="item-booklist-container">

                    <div class="item-container">

                        <div class="book-item" v-for="(book,index) in listBook" ref="books">
                            <div class="book-item-details">
                                <img :src="book.img" alt="Book Cover">
                            </div>
                            <div class="book-item-details">
                                <div id="book-detail-author" class="book-informations">{{ book.author }}</div>
                                <div id="book-detail-title" class="book-informations">{{ book.name }}</div>
                                <div id="book-detail-publisher" class="book-informations">{{ book.publisher }}</div>
                            </div>
                            <div class="book-item-details">
                                <button class="book-item-actions" @click="readBook(index)">Read</button>
                                <button class="book-item-actions" @click="returnedBook(index)">Returned</button>
                            </div>
                        </div>
                        
                    </div>

                </div>

                <div class="item-booklist-container">
                    <div class="pagination-number" v-for="pageN in numberPagination">{{ pageN }}</div>
                </div>
    </div>
<ModalReturned v-show="stateReturnedModal" v-model:stateReturned="stateReturnedModal" :detailsBook="details"/>
</template>

<style scoped>
    .item-main-container {
        /* border: 2px solid black; */
        height: 52em;
        width: 80%;
        display: grid;
        grid-template-rows: 95% auto;
    }

    .item-booklist-container {
        /* border: 2px solid black; */
    }

    .item-booklist-container:first-child {
        padding: 10px;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .item-container{
        /* border: 2px solid black; */
        /* border: 2px solid black; */
        width: 95%;
        height: 95%;
        display: grid;
        grid-template-columns: repeat(5,auto);
        grid-template-rows: repeat(2,auto);
        justify-items: center;
        align-items: center;
    }

    .item-booklist-container:last-child{
        display: flex;
        justify-content: right;
        align-items: center;
        padding-right: 20px;
        /* height: 5em; */
    }

    .pagination-number {
        border: 2px solid black;
        margin-right: 10px;
        width: 30px;
        height: 30px;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .book-item{
        /* border: 2px solid black; */
        /* background-color: black; */
        width: 15em;
        height: 22em;
        display: grid;
        grid-template-rows: 72% 22% auto;
    }

    .book-item-details:last-child{
        display: flex;
        display: grid;
        grid-template-columns: 45% 45%;
        justify-content: space-between;
    }

    .book-item-details:nth-child(2){
        display: grid;
        grid-template-rows: 25% auto 25%;
        font-size: 8pt;
    }

    .book-item-details:first-child img {
        border: 2px solid black;
        width: 100%;
        height: 100%;
        object-fit: cover;
    }

    .book-item-details:nth-child(2) *{
        /* border: 2px solid black; */
        display: flex;
        align-items: center;
        /* padding-left: 5px; */
        overflow: hidden;
        white-space: nowrap;
    }

    .book-informations:nth-child(2){
        font-size: 14pt;
    }

    .book-item-actions{
        /* border: 2px solid black; */
        height: 100%;
        padding: 0px;
        border-radius: 0px;
        font-size: 12pt;
        transition: 0.3s;
    }

    .book-item-actions:first-child{
        box-sizing: border-box;
        border: 2px solid black;
        background-color: white;
        color: black;
    }

    .book-item-actions:first-child:hover{
        box-sizing: border-box;
        border: 2px solid black;
        background-color: black;
        color: white;
        transition: 0.3s;
    }

    .book-item-actions:last-child:hover{
        box-sizing: border-box;
        border: 2px solid black;
        background-color: white;
        color: black;
        transition: 0.3s;
    }
</style>