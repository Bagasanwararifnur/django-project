<script setup>
import { ref } from "vue"
import SvgIcon from '@jamescoyle/vue-icon';
import { mdiChevronRight } from '@mdi/js';
import { mdiChevronLeft } from '@mdi/js';

const iconChevronRight = ref(mdiChevronRight)
const iconChevronLeft = ref(mdiChevronLeft)

const pathIconRight = iconChevronRight.value
const pathIconLeft = iconChevronLeft.value

const bookContainer = ref(null)

// Fungsi untuk scroll ke kiri
const scrollLeft = () => {
  if (bookContainer.value) {
    bookContainer.value.scrollLeft -= 200; // Geser konten 200px ke kiri
  }
}

// Fungsi untuk scroll ke kanan
const scrollRight = () => {
  if (bookContainer.value) {
    bookContainer.value.scrollLeft += 200; // Geser konten 200px ke kanan
  }
}


</script>


<template>
    <div id="library-new-arival">
        <div id="button-scroll-new-arival" class="child-new-arival">
            <div id="button-container-new-arival">
                <svg-icon type="mdi" :path="pathIconLeft" class="logo-nav" @click="scrollLeft"></svg-icon>
                <svg-icon type="mdi" :path="pathIconRight" class="logo-nav" @click="scrollRight"></svg-icon>
            </div>

            <div id="caption">
                New Arival
            </div>
        </div>
        <div id="book-container-new-arival"class="child-new-arival" ref="bookContainer">
            <div class="book-item-new-arival">
                <div class="book-image-new-arival">
                    <img src="../../assets/9786024248369_TSUKURU-TAZAKI-TANPA-WARNA-DAN-TAHUN-ZIARAHNYA.avif" alt="Book Cover">
                </div>
                <div class="book-detail-new-arival">
                    <div id="book-detail-author">Haruki Murakami</div>
                    <div id="book-detail-title">Tsukuru Tazaki dan Tahun Ziarahnya</div>
                    <div id="book-detail-publisher">Kepustakaan Populer Gramedia</div>
                </div>
            </div>
            <div class="book-item-new-arival">
                <div class="book-image-new-arival">
                    <img src="../../assets/Burmese_Days_cov_1.avif" alt="Book Cover">
                </div>
                <div class="book-detail-new-arival">
                    <div id="book-detail-author">George Orwell</div>
                    <div id="book-detail-title">Burmese Days</div>
                    <div id="book-detail-publisher">Kepustakaan Populer Gramedia</div>
                </div>
            </div>
            <div class="book-item-new-arival">
                <div class="book-image-new-arival">
                    <img src="../../assets/Coming_Up_For_Air_cov.avif" alt="Book Cover">
                </div>
                <div class="book-detail-new-arival">
                    <div id="book-detail-author">George Orwell</div>
                    <div id="book-detail-title">Coming up for Air</div>
                    <div id="book-detail-publisher">Kepustakaan Populer Gramedia</div>
                </div>
            </div>
            <div class="book-item-new-arival">
                <div class="book-image-new-arival">
                    <img src="../../assets/dthbwjxghkyjxa8b2e8y9j.avif" alt="Book Cover">
                </div>
                <div class="book-detail-new-arival">
                    <div id="book-detail-author">Jules Verne</div>
                    <div id="book-detail-title">Twenty Thousand Leagues Under the Sea</div>
                    <div id="book-detail-publisher">Kepustakaan Populer Gramedia</div>
                </div>
            </div>
            <div class="book-item-new-arival">
                <div class="book-image-new-arival">
                    <img src="../../assets/e-t04tv-vd.avif" alt="Book Cover">
                </div>
                <div class="book-detail-new-arival">
                    <div id="book-detail-author">Tsubasa Yamaguchi</div>
                    <div id="book-detail-title">Blue Period</div>
                    <div id="book-detail-publisher">PGI</div>
                </div>
            </div>
            <div class="book-item-new-arival">
                <div class="book-image-new-arival">
                    <img src="../../assets/vccgnce--2.avif" alt="Book Cover">
                </div>
                <div class="book-detail-new-arival">
                    <div id="book-detail-author">Daisuke Aizawa</div>
                    <div id="book-detail-title">Light Novel The Eminence in Shadow 3 - Special Set</div>
                    <div id="book-detail-publisher">PGI</div>
                </div>
            </div>
            <div class="book-item-new-arival">
                <div class="book-image-new-arival">
                    <img src="../../assets/ximeinii9y.avif" alt="Book Cover">
                </div>
                <div class="book-detail-new-arival">
                    <div id="book-detail-author">Jules Verne</div>
                    <div id="book-detail-title">Pulau Misterius (The Mysterious Island)</div>
                    <div id="book-detail-publisher">Kepustakaan Populer Gramedia</div>
                </div>
            </div>
        </div>
    </div>
</template>


<style scoped>
    @import url('https://fonts.googleapis.com/css2?family=Signika:wght@300..700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display&display=swap');


    #library-new-arival {
        margin-top: 20px;
        /* border: 2px solid black; */
        width: 80rem;
        height: 25rem;
        display: grid;
        grid-template-rows: 0.8fr 5fr;
    }

    .child-new-arival{
        border-bottom: 2px solid black;
    }

    #button-scroll-new-arival {
        position: relative;
    }

    #button-container-new-arival{
        /* border: 2px solid black; */
        height: 100%;
        width: fit-content;
        position: absolute;
        right: 0px;
        color:black;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    #caption{
        margin-left: 10px;
        /* border: 2px solid black; */
        width: fit-content;
        color: black;
        height: 100%;
        display: flex;
        /* justify-content: center; */
        align-items: center;
        font-family: 'Playfair Display';
        font-size: 30px;
    }

    .logo-nav{
        /* height: 30px; */
        width: 40px;
        /* margin: 10px; */
        transition: 0.5s;
        height: 100%;
    }

    .logo-nav:hover{
        transition: 0.5s;
        background-color: black;
        color: white;
    }

    #book-container-new-arival{
        display: flex;
        align-items: center;
        /* justify-content: center; */
        padding: 10px;
        box-sizing: border-box;
        overflow-x: auto;
        overflow-y: hidden;
        /* background-color: red; */
        scroll-behavior: smooth;
        flex-wrap: nowrap; /* Mencegah elemen membungkus */
    }

    #book-container-new-arival::-webkit-scrollbar {
        display: none;
    }

    .book-item-new-arival{
        font-family: 'Signika';
        border: 2px solid black;
        width: 12rem;
        height: 18rem;
        margin-right: 10px;
        flex-shrink: 0; /* Mencegah elemen mengecil saat konten lebih banyak */
        display: grid;
        grid-template-rows: 75% 25%;
        max-height: 18rem;
        max-width: 12rem;
    }
    .book-item-new-arival:last-child{
        margin-right: 0px;
    }

    .book-image-new-arival img {
        width: 100%;
        height: 100%;
        object-fit: cover; /* Memastikan gambar mengisi area container tanpa distorsi */
    }

    .book-detail-new-arival{
        display: grid;
        grid-template-rows: 1.2em 2em auto;
    }

    #book-detail-author{
        /* border: 2px solid black; */
        font-size: 8pt;
        color: gray;
        overflow: hidden;
        display: flex;
        align-items: center;
        padding-left: 4px;
        box-sizing: border-box;
        white-space: nowrap;
    }
    #book-detail-title{
        /* border: 2px solid black; */
        font-size: 13pt;
        color: black;
        overflow: hidden;
        display: flex;
        align-items: center;
        padding-left: 4px;
        box-sizing: border-box;
        white-space: nowrap;
    }
    #book-detail-publisher{
        /* border: 2px solid black; */
        font-size: 8pt;
        color: black;
        overflow: hidden;
        display: flex;
        align-items: center;
        padding-left: 4px;
        box-sizing: border-box;
        white-space: nowrap;
    }
</style>