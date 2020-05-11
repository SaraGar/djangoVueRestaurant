<template>
    <div>
    <b-navbar class='fixed' type="dark" variant="dark" >
        <b-navbar-nav>
            <b-navbar-brand href="/">
                <img :src="require(`@/assets/pizza-logo.png`)" :style="{ width: '30px'}" alt="">
            </b-navbar-brand>
            <b-nav-item :to="{ name: 'Home'}" >Pizzería</b-nav-item>
            <b-nav-item :to="{ name: 'Menu'}" >Menú</b-nav-item>
            
<!--             <b-nav-item href="/menu" active-class="active">Menú</b-nav-item>
 -->        </b-navbar-nav>
    </b-navbar>
    </div>
</template>

<script>

export default {
  name: 'Navbar', 
}
</script>


<style scoped>
    .exact-active{
        color: white !important;
        border-bottom: 2px solid white;
    }
    .fixed{
        width: 100%;
        position: fixed;
        z-index: 999;
    }

   

</style>