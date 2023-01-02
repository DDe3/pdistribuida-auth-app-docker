<template>
  <div id="login">
  <h1>Ingresar</h1>
  <label for="fname">Usuario:</label>
  <input type="text" id="fname" name="fname" v-model="user"><br><br>
  <label for="password">Contraseña:</label>
  <input type="password" id="password" name="password" v-model="password"><br><br>
  <button @click="doLogin">Ingresar</button>

  </div>
</template>

<script>
import login from "../js/login.js"

export default {
    name: "UserLogin",

    data() {
        return {
            user: "",
            password: "",
        };
    },

    methods: {
      async doLogin() {
        const data = await login(this.user, this.password)
        console.log(data)
        this.$emit('response', { nombre: this.user, response: data['Status']})
      },
      
   }

};


</script>

<style>

.login {
   align-items: center;
   display: flex;
   height: 100vh;
}


</style>