<template>
  
  <div>
    <h1>Programación Distribuida</h1>
    <h2>Aplicación de Logeo usando contenedores</h2>
  </div>
  

  <div id="login" v-show="loginShow">
    <UserLogin @response="login"/>
  </div>
  
  <div id="signin" v-show="signShow">
    <UserSignin @back="clear"/>
  </div>



  <div id="main-page" :nombre="nombre" v-show="mainShow">
    <Main/>
    <button @click="closeSesion">Cerrar sesión</button>
  </div>

  <br>
  <div v-if="registerButton">
    <button @click="changeForm">Registrarse</button>
  </div>

  <div v-if="errorMsgShow">
    <h1>¡Usuario o contraseña incorrectos!</h1>
  </div>
  

</template>

<script>
import UserLogin from './components/UserLogin.vue'
import UserSignin from './components/UserSignin.vue'
import Main from './components/Main.vue'

export default {
  name: 'App',
  components: {
    UserLogin,
    UserSignin,
    Main,
  },

  data() {
        return {
            loginShow: true,
            signShow: false,
            mainShow: false,
            errorMsgShow: false,
            nombre: "",
            registerButton: true,
        };
    },

  methods: {
      login({nombre, response}) {  
        if (response!="Success") {
          this.loginShow = true
          this.signShow = false
          this.mainShow = false
          this.errorMsgShow = true
          this.registerButton = true
        } else {
          this.loginShow = false
          this.signShow = false
          this.mainShow = true
          this.errorMsgShow = false
          this.nombre = nombre
          this.registerButton = true
        }
      },

      closeSesion() {
        this.loginShow = true
        this.signShow = false
        this.mainShow = false
        this.errorMsgShow = false
        this.nombre = ""
      },

      clear() {
        this.loginShow = true
        this.signShow = false
        this.mainShow = false
        this.errorMsgShow = false
        this.nombre = ""
        this.registerButton = true
      },

      changeForm() {
        this.loginShow = false
        this.signShow = true
        this.mainShow = false
        this.errorMsgShow = false
        this.nombre = ""
        this.registerButton = false
      }


   }

  
}
</script>

<style>

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}



</style>
