<template>
  <div id="login">
    <v-card class="mx-auto mt-5" max-width="400">
      <v-card-title>
        <h1 class="display-1">ログイン</h1>
      </v-card-title>
      <v-card-text>
        <v-form @submit.prevent="login">
          <v-text-field prepend-icon="mdi-account-circle" label="ユーザ名" />
          <v-text-field
            :type="showPassword ? 'text' : 'password'"
            prepend-icon="mdi-lock"
            :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
            label="パスワード"
            @click:append="showPassword = !showPassword"
          />
          <v-btn class="info" type="submit">ログイン</v-btn>
        </v-form>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showPassword: false,
      loginData: {
        username: null,
        password: null
      }
    }
  },
  methods: {
    login() {}
  }
}
</script>
