<template>
  <div class="users">
    <h1>This is an users page</h1>
    {{loadUser()}}
    {{user}}
  </div>
</template>

<script>
import axios from 'axios'
  export default {
    data: () => ({
      user: '',
    }),

    methods: {
      async loadUser(){
        try {
          const response = await axios.get('http://localhost:5000/user')
          //console.log("test")
          this.user = response.data[0].name
          //console.log(user)
        } catch (err) {
          console.log(err)
        }
      }
    }
  }
</script>
