<script setup>
import { onMounted, ref, useTemplateRef, watch } from 'vue';
import { useRouter } from 'vue-router';
import SvgIcon from '@jamescoyle/vue-icon';
import { mdiSkipNext } from '@mdi/js';
import { mdiSkipForward } from '@mdi/js';
import { mdiSkipPrevious } from '@mdi/js';
import { mdiSkipBackward } from '@mdi/js';
import ModalDonated from './ModalDonated.vue';


async function getDataOwned(valueSearch, paginationShown){
    const url = new URL('http://127.0.0.1:8000/api/v1/books/book-owned-search')
    url.searchParams.append('valueSearch',valueSearch)
    url.searchParams.append('paginationShown', paginationShown)

    const response = await fetch(url,{
        method: 'GET',
        headers: {
            'accept': 'application/json',
        },
        credentials: 'include',
    })

    if (response.ok){
        const result = await response.json()
        return result
    }
}   

const router = useRouter()

const listBook = ref()
// const numberPagination = ref(Math.floor(listBook.value.length/10+1))
const numberPagination = ref()
const paginationShown = ref()
const valueSearch = ref()

if (router.currentRoute.value.query.paginationShown === undefined){
    paginationShown.value = 1
}else{
    paginationShown.value = parseInt(router.currentRoute.value.query.paginationShown)
}

if (router.currentRoute.value.query.valueSearch === undefined){
    valueSearch.value = ''
}else{
    valueSearch.value = router.currentRoute.value.query.valueSearch
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


const itemRefs = useTemplateRef("books")


function readBook(index){
    const item = itemRefs.value[index]
    console.log(item.querySelector("#book-detail-author").innerHTML)
    console.log(item.querySelector("#book-detail-title").innerHTML)
    console.log(item.querySelector("#book-detail-publisher").innerHTML)
    stateReturnedModal.value = true
}

function donatedBook(index){
    const item = itemRefs.value[index]
    const ownedId = item.id
    const author = item.querySelector("#book-detail-author").innerHTML
    const title = item.querySelector("#book-detail-title").innerHTML
    const publisher = item.querySelector("#book-detail-publisher").innerHTML

    details.value = {author, title, publisher, ownedId}

    stateReturnedModal.value = true
}

onMounted( async() =>{
    const fetchResult = await getDataOwned(valueSearch.value, paginationShown.value)
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
    router.push({ path: '/book-owned', query: {valueSearch: valueSearch.value , paginationShown: paginationShown.value}});
}

function lastPage(){
    if (paginationShown.value === numberPagination.value) return
    paginationShown.value = numberPagination.value
    router.push({ path: '/book-owned', query: {valueSearch: valueSearch.value , paginationShown: paginationShown.value}});
}

function nextPage(){
    if (paginationShown.value === numberPagination.value) return
    paginationShown.value++
    router.push({ path: '/book-owned', query: {valueSearch: valueSearch.value , paginationShown: paginationShown.value}});
}

function previousPage(){
    if (paginationShown.value === 1) return
    paginationShown.value--
    router.push({ path: '/book-owned', query: {valueSearch: valueSearch.value , paginationShown: paginationShown.value}});
}

</script>

<template>
    <div class="item-main-container">

                <div class="item-booklist-container">

                    <div class="item-container">

                        <div class="book-item" v-for="(book,index) in listBook" ref="books" :id="book.book_detail.owned_id">
                            <div class="book-item-details">
                                <img :src="'http://127.0.0.1:8000/'+book.book_detail.cover" alt="Book Cover">
                            </div>
                            <div class="book-item-details">
                                <div id="book-detail-author" class="book-informations">{{ book.book_detail.author }}</div>
                                <div id="book-detail-title" class="book-informations">{{ book.book_detail.title }}</div>
                                <div id="book-detail-publisher" class="book-informations">{{ book.book_detail.publisher }}</div>
                            </div>
                            <div class="book-item-details">
                                <button class="book-item-actions" @click="readBook(index)">Read</button>
                                <button class="book-item-actions" @click="donatedBook(index)">Donated</button>
                            </div>
                        </div>
                        
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
<ModalDonated v-show="stateReturnedModal" v-model:stateReturned="stateReturnedModal" :detailsBook="details"/>
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