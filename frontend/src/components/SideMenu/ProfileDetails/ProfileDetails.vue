<script setup>
import { useRouter } from "vue-router"

const router = useRouter()

async function LogoutSubmit(){
    const url = 'http://127.0.0.1:8000/api/v1/accounts/logout'
    const response = await fetch(url,{
        method : 'GET',
        headers : {
            'accept' : 'application/json'
        },
        credentials : 'include'
    })
    if(response.ok){
        console.log('Logged out successfully')
        setTimeout(() => {
            router.replace({path : '/'}).then(() =>{
                window.location.reload()
            })
        }, 2000)
    }else{
        console.log('Failed to log out')
    }
}

</script>

<template>
    <button @click="LogoutSubmit">Logout</button>
</template>