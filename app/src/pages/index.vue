<template>
  <div>
    <h1>{{ hello }}</h1>
    <v-btn @click="logout">ログアウト</v-btn>
  </div>
</template>

<script>
export default {
  data() {
    return {
      hello: ""
    }
  },
  async created() {
    const response = await this.$axios.get("/api/hello")
    this.hello = response.data.hello
  },
  methods: {
    async logout() {
      await this.$auth.logout()
    }
  }
}
</script>
