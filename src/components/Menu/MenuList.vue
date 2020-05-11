<template lang="html">
    <div class=' row'>
        <div class='container menu-main col text-left'>
            <center>
                <h2>Nuestra carta</h2>
                <br>
                <br>
                <!-- <img class='icon' :src="require('@/assets/m.png')"> --> 
                <p class='menu-desc'>
                    Permítenos que sorprendamos tu paladar con las mejores delicias 100% vegetales
                </p>
            </center>           
      
            <div class='col-md-12 '>
                <div class='menu slit-in-vertical' v-for="menu in menus">
                    <center>
                        <h3> {{ menu.name }} </h3>
                        <img class='icon' :src="require(`@/assets/${menu.image}`)" alt='Menu icon'>
                    </center>
                    <div v-for="menuItem in menuItems" >
                        <div class='row menu-item' v-if="menuItem.menu == menu.id">
                            <div class='col-xs-12 col-sm-12 col-md-3 col-lg-2'>
                               <img class='icon-food' :src="[ `${menuItem.image}`.includes('http') ?  `${menuItem.image}` : require(`@/assets/${menuItem.image}`) ]" alt='Food image'>
                            </div>
                            <div class='col-xs-12 col-sm-12 col-md-9 col-lg-10'>
                                <b>{{ menuItem.name }}</b> <br> 
                                <i> {{menuItem.description}} <br>
                                {{ menuItem.price }} €</i>
                            </div>
                        </div>
                    </div>
                </div>
             <!--   <b-table striped hover :items="menus" :fields="fields">
                </b-table>  -->  
            </div>              
        </div>
    </div>
    <!--  Iconos diseñados por eucalyp, smalllikeart y freepik en www.flaticon.es</a> -->
</template>

<script>
import axios from 'axios';


export default {
    data(){
        return{
           /*  fields: [
                { key: 'name', label: 'Nombre'},
                { key: 'description', label: 'Descripción'},
                { key: 'price', label: 'Precio'},
            ], */ 
            menus: [],
            menuItems: []
        }
    }, 
    methods: {
        getMenus(){
            const path = process.env.API_URL + '/api/menus/'

            axios.get(path).then((response) => {
                this.menus = response.data
                this.getMenuItems()
            })
            .catch((error)=>{
                console.log(error)
            })
        },  
        getMenuItems(){
            const path = process.env.API_URL + '/api/menuItems/'

            axios.get(path).then((response) => {
                this.menuItems = response.data
            })
            .catch((error)=>{
                console.log(error)
            })
        }     
    },
    created(){
        this.getMenus()
    }
    
}
</script>

<style lang='css' scoped>
    
    .container{
        color: #303e4c;
        font-family: 'Josefin Sans', Tahoma, sans-serif;
        margin: 20px;
    }
    .menu-desc{
        text-align: center;
        font-style: italic;
    }
     .menu-main{
        margin-top: 56px;
    }
    h3{
        text-align: center;
        margin-top: 20px;
    }
    h2{
        margin: auto;
        text-align: center;
        margin-top: 25px;
        position: relative;
        display: inline-block;
    }
    h2:after {
        content: '';
        background: #fcba03;
        width: 100%;
        height: 2px;
        display: block;
    
    }
    .icon{
        width: 60px;
        margin: 10px;
    }
    .icon-food{
        width: 100%;
        margin: 0px 10px;
        border: 2px solid #d1a773;
    }
    .menu{
        border:1px solid #ddd;
        margin: 20px;
        padding: 50px;
    }
    .menu-item{
        margin: 20px 0px;
    }

   .slit-in-vertical {
	    -webkit-animation: slit-in-vertical 0.45s ease-out both;
	    animation: slit-in-vertical 0.45s ease-out both;
    }

    @-webkit-keyframes slit-in-vertical {
        0% {
            -webkit-transform: translateZ(-800px) rotateY(90deg);
                    transform: translateZ(-800px) rotateY(90deg);
            opacity: 0;
        }
        54% {
            -webkit-transform: translateZ(-160px) rotateY(87deg);
                    transform: translateZ(-160px) rotateY(87deg);
            opacity: 1;
        }
        100% {
            -webkit-transform: translateZ(0) rotateY(0);
                    transform: translateZ(0) rotateY(0);
        }
    }
    @keyframes slit-in-vertical {
        0% {
            -webkit-transform: translateZ(-800px) rotateY(90deg);
                    transform: translateZ(-800px) rotateY(90deg);
            opacity: 0;
        }
        54% {
            -webkit-transform: translateZ(-160px) rotateY(87deg);
                    transform: translateZ(-160px) rotateY(87deg);
            opacity: 1;
        }
        100% {
            -webkit-transform: translateZ(0) rotateY(0);
                    transform: translateZ(0) rotateY(0);
        }

    }

   
</style>