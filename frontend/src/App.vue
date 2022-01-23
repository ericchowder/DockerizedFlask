<template>
  <v-app id="inspire">

    <v-navigation-drawer permanent
    v-model="drawer"
    app
    >
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="text-h6">
            Application
          </v-list-item-title>
          <v-list-item-subtitle>
            subtext
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <v-list
        dense
        nav
      >
        <v-list-item
          v-for="item in items"
          :key="item.title"
          :to="item.to"
          link
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar
      app
      color="primary"
      dark
      src="https://picsum.photos/1920/1080?random"
      prominent
    >
      <template v-slot:img="{ props }">
        <v-img
          v-bind="props"
          gradient="to top right, rgba(19,84,122,.5), rgba(128,208,199,.8)"
        ></v-img>
      </template>

      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

      <v-app-bar-title>Title</v-app-bar-title>

      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-heart</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>
      <div>
        {{loadUser()}}
        asdfffffffffffffffffff
        {{user}}
      </div>
    </v-app-bar>

    <v-main>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>
import axios from 'axios'
//import { ref } from 'vue'

  export default {
    name: 'VueApp',
    // setup () {
    //   const hi = ref('')

    //   const loadUser = async () => {
    //     try {
    //       const response = await axios.get('localhost:5000/user')
    //       console.log("test")
    //       hi.value = response.data
    //       console.log(hi)
    //       return(hi)
    //     } catch (err) {
    //       console.log(err)
    //     }
    //   }
    //   loadUser()
    // },
    

    data: () => ({ 
      drawer: null,
      items: [
        { title: 'Home', icon: 'mdi-view-dashboard', to: '/' },
        { title: 'Users', icon: 'mdi-account', to: '/users' },
        { title: 'About', icon: 'mdi-help-box', to: '/about' },
      ],
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