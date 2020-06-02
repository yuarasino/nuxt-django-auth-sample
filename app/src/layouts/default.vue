<template>
  <v-app>
    <v-app-bar app dark>
      <v-toolbar-title v-text="title" />
    </v-app-bar>
    <v-content>
      <v-container>
        <nuxt />
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      title: "nuxt-django-auth-sample"
    }
  }
}
</script>
