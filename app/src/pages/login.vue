<template>
  <div id="login">
    <v-alert v-if="errorMessage" type="error">
      {{ errorMessage }}
    </v-alert>
    <v-card class="mx-auto mt-5" max-width="400">
      <v-card-title>
        <h1 class="display-1">ログイン</h1>
      </v-card-title>
      <v-card-text>
        <v-form @submit.prevent="login">
          <v-text-field
            v-model="loginData.username"
            prepend-icon="mdi-account-circle"
            label="ユーザ名"
          />
          <v-text-field
            v-model="loginData.password"
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
      errorMessage: "",
      loginData: {
        username: null,
        password: null
      }
    }
  },
  methods: {
    async login() {
      if (!this.loginData.username || !this.loginData.password) {
        return
      }
      try {
        await this.$auth.loginWith("local", { data: this.loginData })
      } catch (err) {
        if (err.response.status === 400) {
          this.errorMessage = "ユーザー名かパスワードが違います。"
        } else {
          this.errorMessage =
            "ログインで問題が発生しました。時間をおいて試してください。"
        }
      }
    }
  }
}
</script>
