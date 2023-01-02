<template>
  <div class="contenedor">
    Bienvenido {{ nombre }}
  </div>

</template>

<script>
export default {

    props: {
        nombre: {
            type: String,
            required: true
        },
    }

}
</script>

<style>

.contenedor {
  display: flex;
  justify-content: center;
}

</style>