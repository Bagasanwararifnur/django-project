<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import SvgIcon from '@jamescoyle/vue-icon';
import { mdiBookArrowLeftOutline } from '@mdi/js';

async function getDetails(id){
  const url = new URL('http://127.0.0.1:8000/api/v1/books/get-byid')
  url.searchParams.append('id', id)
  const response = await fetch(url,
    { method: 'GET',
      headers: {
        'accept': 'application/json',
      },
    }
  )

  if (response.ok){
    const result = await response.json()
    return result
  }else{
    console.error('Error:', response.status)
  }

}


const router = useRouter()
const bookDetails = ref({})
const id = router.currentRoute.value.params.id

const iconBookArrowLeftOutline = ref(mdiBookArrowLeftOutline)
const pathIconBookArrowLeftOutline = iconBookArrowLeftOutline.value

onMounted(async() =>{
  const fetchResult = await getDetails(id)
  bookDetails.value = fetchResult
  console.log(fetchResult)
})


</script>

<template>
    <div class="content-container">
       <div class="sub-container">
            <img :src="'http://127.0.0.1:8000/'+bookDetails.cover" alt="Book Cover" class="cover-book">
       </div>

       <div class="sub-container">
            <div class="details-container">
                <div class="book-details" id="title">{{ bookDetails.title }}</div>
                <div class="book-details" id="author">
                    <div class="sub-details-container">Author</div>
                    <div class="sub-details-container">{{ bookDetails.author }}</div>
                </div>
                <div class="book-details" id="publisher">
                    <div class="sub-details-container">Publisher</div>
                    <div class="sub-details-container">{{ bookDetails.publisher }}</div>
                </div>
                <div class="book-details" id="publish-date">
                    <div class="sub-details-container">Tanggal Terbit</div>
                    <div class="sub-details-container">{{ bookDetails.publication_date }}</div>
                </div>
                <div class="book-details" id="isbn">
                    <div class="sub-details-container">ISBN</div>
                    <div class="sub-details-container">{{ bookDetails.isbn }}</div>
                </div>
                <div class="book-details" id="genre">
                    <div class="sub-details-container">Genre</div>
                    <div class="sub-details-container">
                        <div class="genre-container" v-for='genreItem in bookDetails.genre'>{{ genreItem }}</div>
                    </div>
                </div>
                <div class="book-details" id="synopsis">
                    <div class="sub-details-container">Sinopsis</div>
                    <div class="sub-details-container">
                      {{ bookDetails.description }}
                    </div>
                </div>
            </div>
        </div>

       <div class="sub-container">
            <div class="book-borrow-container">
                <div class="borrow-details" id="count">
                    <div class="sub-details-container">Quota in Library</div>
                    <div class="sub-details-container">{{ bookDetails.donated_count }}</div>
                </div>
                <button class="borrow-details" id="borrow-button">
                    <svg-icon type="mdi" :path="pathIconBookArrowLeftOutline"></svg-icon>
                    Borrow
                </button>
            </div>
       </div>
    </div>
</template>

<style scoped>

    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display&display=swap');

  .content-container {
    display: grid;
    grid-template-columns: 30rem 70rem auto;
    height: 100%;
    box-sizing: border-box;
    font-family: 'Playfair Display', serif;
  }

  .cover-book {
    height: 70%;
    max-width: 100%;
    object-fit: cover;
    border: 2px solid black;
  }

  .sub-container {
    /* border: 2px solid black; */
    height: 100%;
    box-sizing: border-box;
  }

  .details-container{
    /* border: 2px solid black; */
    display: grid;
    height: 90%;
    width: 90%;
    grid-template-rows: auto 2.5rem 2.5rem 2.5rem 2.5rem 10rem 20rem;
  }

  .book-details {
    border-bottom: 2px solid black;
  }

  .sub-container:first-child{
    display: flex;
    justify-content: center;
    align-items: center;
    border: none;
    /* background-color: rgb(238, 238, 238); */
  }

  .sub-container:nth-child(2){
    display: flex;
    justify-content: center;
    align-items: center;
  }

  #title{
    font-size: 30pt;
    display: flex;
    align-items: center;
  }

  #author{
    font-size: 14pt;
    display: flex;
    align-items: center;
    display: grid;
    grid-template-columns: 200px auto;
  }

  #publisher{
    font-size: 14pt;
    display: flex;
    align-items: center;
    display: grid;
    grid-template-columns: 200px auto;
  }

  #publish-date{
    font-size: 14pt;
    display: flex;
    align-items: center;
    display: grid;
    grid-template-columns: 200px auto;
  }

  #isbn{
    font-size: 14pt;
    display: flex;
    align-items: center;
    display: grid;
    grid-template-columns: 200px auto;
  }

  #genre{
    font-size: 14pt;
    display: grid;
    grid-template-rows: 2.5rem auto;
  }

  #genre .sub-details-container:first-child{
    display: flex;
    align-items: center;
  }

  #genre .sub-details-container:last-child{
    display: flex;
    flex-wrap: wrap; 
    align-items: center;
  }

  .genre-container{
    font-size: 10pt;
    border: 1px solid black;
    background-color: rgb(241, 241, 241);
    padding: 5px;
    margin-right: 10px;
    border-radius: 4px;
    transition: 0.3s;
    cursor: pointer;

  }

  .genre-container:hover{
    background-color: rgb(50, 50, 50);
    color: rgb(241, 241, 241);
    transition: 0.3s;
  }

  #synopsis{
    font-size: 14pt;
    display: grid;
    grid-template-rows: 2.5rem auto;
  }

  #synopsis .sub-details-container:first-child{
    display: flex;
    align-items: center;
    /* justify-content: center; */
  }

  #synopsis .sub-details-container:last-child{
    overflow-y: scroll;
    font-size: 12pt;
    text-align: justify;
  }

  #synopsis .sub-details-container:last-child::-webkit-scrollbar{
    display: none;
  }

  .sub-container:last-child{
    display: flex;
    justify-content: center;
    align-items: center;
    /* border: none;
    background-color: rgb(238, 238, 238); */
  }

  .book-borrow-container{
    /* border: 2px solid black; */
    height: 10%;
    width: 90%;
    display: grid;
    grid-template-rows: auto 2.5rem;
  }


  .book-borrow-container .borrow-details:first-child{
    display: grid;
    grid-template-columns: 2fr 1fr;
    font-size: 15pt;
  }

  .book-borrow-container .borrow-details:first-child .sub-details-container:last-child{
    display: flex;
    justify-content: center;
  }

  .borrow-details:last-child{
    border: 2px solid black;
    display: flex;
    border-radius: 0px;
    background-color: white;
    color: black;
    justify-content: center;
    align-items: center;
    font-size: 15pt;
    cursor: pointer;
    transition: 0.5s;
  }

  .borrow-details:last-child:hover{
    background-color: black;
    color: white;
    transition: 0.5s;
  }

  .borrow-details:last-child * {
    margin-right: 5px;
  }

</style>