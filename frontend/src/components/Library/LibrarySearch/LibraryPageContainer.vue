<script setup>
import { onMounted, ref, useTemplateRef, watch } from 'vue';
import { useRouter } from 'vue-router';
import SvgIcon from '@jamescoyle/vue-icon';
import { mdiSkipNext } from '@mdi/js';
import { mdiSkipForward } from '@mdi/js';
import { mdiSkipPrevious } from '@mdi/js';
import { mdiSkipBackward } from '@mdi/js';

async function getData(modeSearch, valueSearch, paginationShown) {
    const url = new URL('http://127.0.0.1:8000/api/v1/books/list');
    url.searchParams.append('modeSearch',modeSearch);
    url.searchParams.append('valueSearch', valueSearch);
    url.searchParams.append('paginationShown', paginationShown);

    const response = await fetch(url, {
    method: 'GET',
    headers: {
      'accept': 'application/json',
    }});

    if (response.ok){
        const result = await response.json()
        return result
    }
    else {
        console.error('Error:', response.status)
    }
}


const router = useRouter()
const Mode = router.currentRoute.value.query.modeSearch
const valueSearch = router.currentRoute.value.query.valueSearch

const listBook = ref([
    { 'img' : "src/assets/dthbwjxghkyjxa8b2e8y9j.avif", 'author' : "Jules Verne", 'name' : "Twenty Thousand Under the Sea", 'publisher':'Kepustakaan Populer Gramedia'},
    { 'img' : "/src/assets/ximeinii9y.avif", 'author' : "Jules Verne", 'name' : "Pulau Misterius", 'publisher':'Kepustakaan Populer Gramedia'},
])
// const numberPagination = ref(Math.floor(listBook.value.length/10+1))
const numberPagination = ref()
const paginationShown = ref()

if (router.currentRoute.value.query.paginationShown === undefined){
    paginationShown.value = 1
}else{
    paginationShown.value = parseInt(router.currentRoute.value.query.paginationShown)
}

const stateReturnedModal = ref(false)
const details = ref()

const iconSkipNext = ref(mdiSkipNext)
const iconSkipForward = ref(mdiSkipForward)
const iconSkipPrevious = ref(mdiSkipPrevious)
const iconSkipBackward = ref(mdiSkipBackward)

const pathSkipNext = iconSkipNext.value
const pathSkipForward = iconSkipForward.value
const pathSkipPrevious = iconSkipPrevious.value
const pathSkipBackward = iconSkipBackward.value

onMounted( async() =>{
    const fetchResult = await getData(Mode, valueSearch, paginationShown.value)
    listBook.value = fetchResult.listBook
    numberPagination.value = fetchResult.number

    const buttonNext = document.querySelector("#next-button")
    const buttonLast = document.querySelector("#last-button")
    const buttonPrev = document.querySelector("#previous-button")
    const buttonFirst = document.querySelector("#first-button")

    if(paginationShown.value === 1 && paginationShown.value === numberPagination.value){
        buttonPrev.disabled = true
        buttonFirst.disabled = true
        buttonNext.disabled = true
        buttonLast.disabled = true
    }
    else if(paginationShown.value === 1 && numberPagination.value !== 1){
        buttonPrev.disabled = true
        buttonFirst.disabled = true
        buttonNext.disabled = false
        buttonLast.disabled = false
        
    }
    else if(paginationShown.value === numberPagination.value){
        buttonNext.disabled = true
        buttonLast.disabled = true
        buttonPrev.disabled = false
        buttonFirst.disabled = false
    }
    else{
        buttonNext.disabled = false
        buttonLast.disabled = false
        buttonPrev.disabled = false
        buttonFirst.disabled = false
    }
})


function firstPage(){
    if (paginationShown.value === 1) return
    paginationShown.value = 1
    router.push({ path: '/library-search', query: { modeSearch: Mode, valueSearch: valueSearch , paginationShown: paginationShown.value}});
}

function lastPage(){
    if (paginationShown.value === numberPagination.value) return
    paginationShown.value = numberPagination.value
    router.push({ path: '/library-search', query: { modeSearch: Mode, valueSearch: valueSearch , paginationShown: paginationShown.value}});
}

function nextPage(){
    if (paginationShown.value === numberPagination.value) return
    paginationShown.value++
    router.push({ path: '/library-search', query: { modeSearch: Mode, valueSearch: valueSearch , paginationShown: paginationShown.value}});
}

function previousPage(){
    if (paginationShown.value === 1) return
    paginationShown.value--
    router.push({ path: '/library-search', query: { modeSearch: Mode, valueSearch: valueSearch , paginationShown: paginationShown.value}});
}

</script>

<template>
    <div class="item-main-container">

                <div class="item-booklist-container">

                    <div class="item-container">

                        <router-link :to="'book-details-library/'+book.id" class="book-item" v-for="(book,index) in listBook" ref="index">
                            <div class="book-item-details">
                                <img :src="'http://127.0.0.1:8000/'+book.cover" alt="Book Cover">
                            </div>
                            <div class="book-item-details">
                                <div id="book-detail-author" class="book-informations">{{ book.author }}</div>
                                <div id="book-detail-title" class="book-informations">{{ book.title }}</div>
                                <div id="book-detail-publisher" class="book-informations">{{ book.publisher }}</div>
                            </div>
                        </router-link>
                        
                    </div>

                </div>

                <div class="item-booklist-container">
                    <button class="pagination-container" id="first-button">
                        <svg-icon type="mdi" :path="pathSkipBackward" class="logo-nav" @click="firstPage"></svg-icon>
                    </button>
                    <button class="pagination-container" id="previous-button">
                        <svg-icon type="mdi" :path="pathSkipPrevious" class="logo-nav" @click="previousPage"></svg-icon>
                    </button>

                    <div class="pagination-container">{{ paginationShown }}</div>
                    
                    <button class="pagination-container" id="next-button">
                        <svg-icon type="mdi" :path="pathSkipNext" class="logo-nav" @click="nextPage"></svg-icon>
                    </button>
                    <button class="pagination-container" id="last-button">
                        <svg-icon type="mdi" :path="pathSkipForward" class="logo-nav" @click="lastPage"></svg-icon>
                    </button>
                </div>
    </div>
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
        grid-template-columns: repeat(5,1fr);
        grid-template-rows: repeat(2,1fr);
        /* justify-items: center; */
        /* align-items: center; */
    }

    .item-booklist-container:last-child{
        display: flex;
        justify-content: right;
        align-items: center;
        padding-right: 20px;
        /* height: 5em; */
    }

    .pagination-container {
        border: 2px solid black;
        margin-right: 10px;
        width: 30px;
        height: 30px;
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 0px;
    }

    button.pagination-container{
        border-radius: 0px;
    }

    button.pagination-container:disabled{
        background-color: gray;
        color: lightgray;
        cursor: not-allowed;
    }

    .book-item{
        /* border: 2px solid black; */
        /* background-color: black; */
        width: 15em;
        height: 22em;
        display: grid;
        grid-template-rows: 75% auto;
    }


    .book-item-details:nth-child(2){
        display: grid;
        grid-template-rows: 25% auto 25%;
        font-size: 8pt;
        color:black
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

    #book-detail-author{
        color: gray;
    }
</style>