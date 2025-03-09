<script setup>
import { ref } from 'vue';
import SvgIcon from '@jamescoyle/vue-icon';
import { mdiBookArrowLeftOutline } from '@mdi/js';

const iconBookArrowLeftOutline = ref(mdiBookArrowLeftOutline)

const pathIconBookArrowLeftOutline = iconBookArrowLeftOutline.value

</script>

<template>
    <div class="content-container">
       <div class="sub-container">
            <img src="../../assets/ximeinii9y.avif" alt="Book Cover" class="cover-book">
       </div>

       <div class="sub-container">
            <div class="details-container">
                <div class="book-details" id="title">Pulau Misterius (The Mysterious Island)</div>
                <div class="book-details" id="author">
                    <div class="sub-details-container">Author</div>
                    <div class="sub-details-container">Jules Verne</div>
                </div>
                <div class="book-details" id="publisher">
                    <div class="sub-details-container">Publisher</div>
                    <div class="sub-details-container">Gramedia Pustaka Utama</div>
                </div>
                <div class="book-details" id="publish-date">
                    <div class="sub-details-container">Tanggal Terbit</div>
                    <div class="sub-details-container">24 November 1881</div>
                </div>
                <div class="book-details" id="isbn">
                    <div class="sub-details-container">ISBN</div>
                    <div class="sub-details-container">979-602-8568-2</div>
                </div>
                <div class="book-details" id="genre">
                    <div class="sub-details-container">Genre</div>
                    <div class="sub-details-container">
                        <div class="genre-container">Fiksi</div>
                        <div class="genre-container">Novel</div>
                        <div class="genre-container">Sci-Fiction</div>
                        <div class="genre-container">Misteri</div>
                        <div class="genre-container">Survival</div>
                        <div class="genre-container">Historical</div>
                    </div>
                </div>
                <div class="book-details" id="synopsis">
                    <div class="sub-details-container">Sinopsis</div>
                    <div class="sub-details-container">
                        <p>Setelah membajak balon udara dari sebuah kamp Konfederasi, lima tawanan dan seekor anjing melarikan diri dari Perang Saudara Amerika. Sekitar delapan ribu kilometer kemudian, mereka jatuh dari awan ke sebuah pulau vulkanik yang belum dipetakan di tengah Samudra Pasifik. Melalui kerja sama, rekayasa, pengetahuan ilmiah, dan tekad, mereka berusaha membangun koloni dari nol. Namun pulau yang kaya akan sumber daya ini menyimpan rahasia gelap. Kelima orang itu mendapati mereka tidak sendirian. Seseorang mengintai mereka. Seseorang yang sudah mereka kenal dan akan berperan penting dalam nasib mereka kelak.</p>

                        <p>“Apakah kita naik lagi?” “Tidak. Sebaliknya.” “Kita sedang turun?” “Lebih gawat daripada itu, Kapten! Kita sedang jatuh!” “Demi Tuhan, buang pemberat!” “Sudah! Karung terakhir sudah kosong!” “Apakah balonnya naik?” “Tidak!” “Aku mendengar bunyi seperti debur ombak. Di bawah gondola ini ada laut! Tidak sampai 150 meter dari kita!” “Buang semua beban! … Semuanya!” Demikianlah kata-kata lantang dan mengherankan yang menggema di udara, di atas gurun air nan luas Pasifik, sekitar pukul empat sore pada tanggal 23 Maret 1865.</p>

                        <p>Sungguh tak terlupakan badai dahsyat dari timur laut yang terjadi pada hari ekuinoks tahun itu. Badai itu mengamuk tanpa jeda dari tanggal 18 sampai 26 Maret, menimbulkan kerusakan parah di Amerika, Eropa, dan Asia, meliputi jarak 3.000 kilometer dan merentang miring dari garis 35º LU hingga 40º LS. Kota porak-poranda, hutan tercerabut, pesisir luluh-lantak diterjang tsunami, kapal terdampar di pantai dalam jumlah ratusan, menurut berita terbit, berbagai daerah diratakan oleh tornado air yang menghancurkan segala sesuatu yang dilewatinya, ribuan orang binasa di darat atau tenggelam di laut; demikianlah jejak murka yang ditinggalkan oleh badai perusak ini. Badai ini melampaui bencana yang menghancurkan Havana dan Guadalupe dengan mengerikan, yang satu pada 25 Oktober 1810, satu lagi pada 26 Juli 1825.</p>
                    </div>
                </div>
            </div>
        </div>

       <div class="sub-container">
            <div class="book-borrow-container">
                <div class="borrow-details" id="count">
                    <div class="sub-details-container">Quota in Library</div>
                    <div class="sub-details-container">350</div>
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