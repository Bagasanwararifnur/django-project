import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import './style.css'

import App from './App.vue'
import BookBorrowed from './components/SideMenu/BorrowedPage/BookBorrowed.vue'
import BookOwned from './components/SideMenu/OwnedPage/BookOwned.vue'
import ProfileDetails from './components/SideMenu/ProfileDetails/ProfileDetails.vue'
// import HomePage from './components/Home/HomePage.vue'
import RootPage from './components/RootPage.vue'
import LoginPage from './components/LoginPage.vue'
import BookDetailsLibrary from './components/Library/BookDetailsLibrary.vue'
import LibrarySearchPage from './components/Library/LibrarySearch/LibrarySearchPage.vue'

const router = createRouter({
    history : createWebHistory(),
    routes : [
        { path : '/', component: RootPage, props: route => ({ pageRoot: route.query.pageRoot || 'HomePage' })},
        { path : '/book-owned', component : BookOwned, props: route => ({ valueSearch: route.query.valueSearch || '',
            paginationShown : route.query.paginationShown || '1'
        })},
        { path : '/book-borrowed', component : BookBorrowed, props: route => ({ valueSearch: route.query.valueSearch || '',
            paginationShown : route.query.paginationShown || '1'})},
        { path : '/profile-details', component : ProfileDetails},
        { path : '/login', component: LoginPage},
        { path : '/book-details-library/:id', component: BookDetailsLibrary, props: true },
        { path : '/library-search', component: LibrarySearchPage, props: route =>({modeSearch : route.query.modeSearch, valueSearch: route.query.valueSearch,
            paginationShown : route.query.paginationShown || '1'
        })}
    ]
})

const app = createApp(App)

app.use(router)
app.mount('#app')
