<template>
  <div class="users">
    <!-- FORM -->
    <v-form v-model="valid">
      <v-container>
        <h1>
          Create New User Here
        </h1>
        <p>
          All Fields are required. Start up backend to see backend logs.
          <br>
          Create User: uses fields to create new user in db
          <br>
          Load Last User: loads most recently added user
          <br>
          List Form: displays stringified json of current fields
        </p>
        <v-row>
          <v-col
            cols="12"
            md="4"
          >
            <v-text-field
              v-model="username"
              :rules="nameRules"
              :counter="10"
              label="Username"
              required
            ></v-text-field>
          </v-col>

          <v-col
            cols="12"
            md="4"
          >
            <v-text-field
              v-model="password"
              :rules="nameRules"
              :counter="10"
              label="Password"
              required
            ></v-text-field>
          </v-col>

          <!-- <v-col
            cols="12"
            md="4"
          >
            <v-text-field
              v-model="email"
              :rules="emailRules"
              label="E-mail"
              required
            ></v-text-field>
          </v-col> -->
        </v-row>
      </v-container>
      <v-container>
        <v-row>
          <v-col
            cols="12"
            md="4"
          >
            <v-text-field
              v-model="id"
              :rules="idRules"
              :counter="3"
              label="Id"
              required
            ></v-text-field>
          </v-col>

          <v-col
            cols="12"
            md="4"
          >
            <v-text-field
              v-model="public_id"
              :rules="idRules"
              :counter="5"
              label="Public ID"
              required
            ></v-text-field>
          </v-col>

          <v-col
            cols="12"
            md="4"
          >
            <v-checkbox
              v-model="admin"
              label="Admin"
            ></v-checkbox>
          </v-col>
        </v-row>
        <v-btn
        @click="createUser"
        elevation="2"
      >Create User</v-btn>
      </v-container>
    </v-form>
    <!-- FORM END -->

    <!-- LOAD USERS -->
    <v-container>
      <h1>This is an users page</h1>
      <p>
        <v-btn
          @click="listJson"
        >List Form</v-btn>
        {{formUser}}
      </p>
      <p>
        <v-btn
          @click="loadUser"
          elevation="2"
        >Load Last User</v-btn>
      Name: {{user}}
      </p>
      <p disabled>
        <v-btn
          @click="loadAllUsers"
          elevation="2"
        >
        Load All Users
        </v-btn>
        <br>
        <!-- {{allUsers}} -->
        <ul>
        <li v-for="(user, idx) in allUsers"
          :key="idx">
          {{user}}
        </li>
        </ul>
      </p>
    </v-container>
    <!-- LOAD USERS END -->
  </div>
</template>

<script>
import axios from 'axios'
  export default {

    data: () => ({
      user: '',
      allUsers: '',
      formUser: '',

      // FORM STUFF
      valid: false,
      username: '',
      password: '',
      nameRules: [
        v => !!v || 'Name is required',
        v => v.length <= 10 || 'Name must be less than 10 characters',
      ],
      id: '',
      public_id: '',
      idRules: [
        v => !!v || 'ID is required',
        v => Number.isInteger(v) || 'ID must be a number value',
      ],
      admin: false
      // email: '',
      // emailRules: [
      //   v => !!v || 'E-mail is required',
      //   v => /.+@.+/.test(v) || 'E-mail must be valid',
      // ],
      // FORM STUFF END
    }),

    methods: {
      async loadUser(){
        try {
          const response = await axios.get('http://localhost:5000/user')
          //console.log("test")
          this.user = response.data[response.data.length - 1].name
          //console.log(user)
        } catch (err) {
          console.log(err)
        }
      },

      async loadAllUsers(){
        try {          
          const headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            Accept: "application/json"
          }
          const response = await axios.get('/user',
          { headers })
          //console.log("test")
          this.allUsers = response.data
          //console.log(user)
        } catch (err) {
          console.log(err)
        }
      },

      async createUser(){
        try {
          const headers = {
            "Content-Type": "application/json"
          }
          const response = await axios.post('http://localhost:5000/user', 
          JSON.stringify({
            id: this.id,
            public_id: this.public_id,
            name: this.username,
            password: this.password,
            admin: this.admin
          }),
          { headers })
          console.log(response)
        } catch (err) {
          console.log(err)
        }
      },

      async listJson(){
        try {
          this.formUser =
          JSON.stringify({
            id: this.id,
            public_id: this.public_id,
            name: this.username,
            password: this.password,
            admin: this.admin
          })
          console.log(this.formUser)
        } catch (err) {
          console.log(err)
        }
      }


    }
    
  }
</script>
