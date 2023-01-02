<template>
  <div id="signin">
    <h1>Registrarse</h1>
    <div v-show="registerFormShow">
      <label for="fname">Usuario:</label>
      <input type="text" id="fname" name="fname" v-model="user" /><br /><br />
      <label for="password">Contraseña:</label>
      <input
        type="password"
        id="password"
        name="password"
        v-model="password"
      /><br /><br />
      <button @click="doRegister">Registrarse</button>
      <button @click="goBack">Regresar</button>
    </div>
  </div>
  <div v-show="msgShow">
    <h1>Usuario registrado</h1>
    <button @click="goBack">Regresar</button>
  </div>
</template>
  
<script>
import register from "../js/signin.js";

export default {
  name: "UserLogin",

  data() {
    return {
      user: "",
      password: "",
      msgShow: false,
      registerFormShow: true
    };
  },

  methods: {
    async doRegister() {
      const body = {
        user: this.user,
        password: this.password
      };
      const data = await register(body);
      console.log(data);
      if (data["Status"] == "Usuario registrado") {
        this.user = ""
        this.password = ""
        this.msgShow = true
        this.registerFormShow = false
      }
    },

    goBack() {
        this.msgShow = false
        this.registerFormShow = true
        this.$emit('back', "ok")
    }
  },
};
</script>
  
<style>
.signin {
  align-items: center;
  display: flex;
  height: 100vh;
}
</style>