<template>
  <div class="container">
      <div class="columns is-centered">
        <h1 class="title mb-4">Войти</h1>
      </div>

    <div class="columns is-centered">
      <div class="column is-5">
        <form @submit.prevent="userLogin">
          <b-field label="Email">
            <b-input v-model="login.email" type="email" required />
          </b-field>

          <b-field label="Пароль">
            <b-input v-model="login.password" type="password" required />
          </b-field>

          <b-button native-type="submit" type="is-primary" class="mt-4" expanded>
            Войти
          </b-button>

        </form>
      </div>
    </div>
  </div>
</template>

<script>
import {getCurrentInstance, reactive, onMounted} from "vue";

export default {
  setup() {
    const { $buefy, $router, $auth } = getCurrentInstance().proxy

    const login = reactive({
      email: '',
      password: ''
    })

    const userLogin = async () => {
      try {
        await $auth.loginWith('local', {
          data: login
        })

        await $router.push('/admin/hikes/')

      }
      catch (err) {
        $buefy.toast.open({
          message: 'Неверный email или пароль',
          type: 'is-danger'
        })
      }
    }

    onMounted(() => {
      if ($auth.loggedIn) {
        $router.push('/admin/hikes/')
      }
    })

    return {
      login,
      userLogin
    }
  }
}
</script>
