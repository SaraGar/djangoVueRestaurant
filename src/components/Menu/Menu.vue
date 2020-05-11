<template lang="html">
    <div >
        <Navbar></Navbar>
        <MenuList></MenuList>
        <Footer></Footer>
    </div>
</template>

<script>
import axios from 'axios';
import Navbar from '@/components/Navbar'
import MenuList from '@/components/Menu/MenuList'
import Footer from '@/components/Footer'


export default {
    components: {
        Navbar,
        MenuList,
        Footer
    }
    
}
</script>

<style lang='css' scoped>

</style>