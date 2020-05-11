<template>
    <div>
        <b-row class='footer' align-v="center">
            <b-col cols>
                Website By <a href='https://cv.saragar.now.sh/'>Sara García</a>
            </b-col>
        </b-row>  
    </div>
</template>

<script>

export default {
  name: 'Footer', 
}
</script>


<style scoped>
  .footer{
      min-height: 50px;
      background-color: #343a40 ;
      color: white;
      text-align: center;
  }
  .footer a{
      color: white;
      text-decoration: none;
  }
  .footer a:hover{
      text-decoration: none;
      color: white;
  }
</style>