<template>
  <div class="admin-layout">
    <header>
      <b-navbar class="p-3 container">
        <template #brand>
          <logo/>
        </template>

        <template #start>
          <b-navbar-item tag="nuxt-link" to="/admin/hikes/">
            Походы
          </b-navbar-item>
          <b-navbar-item tag="nuxt-link" to="/admin/bookings/">
            Заявки
          </b-navbar-item>
        </template>

        <template #end>
          <b-navbar-item tag="div">
            <b-button @click="logout" type="is-dark">Выйти</b-button>
          </b-navbar-item>
        </template>
      </b-navbar>
    </header>

    <main class="main-content">
      <nuxt />
    </main>

  </div>
</template>

<script>
import { getCurrentInstance } from 'vue'
import Logo from "@/components/Logo.vue";

export default {
  components: { Logo },

  setup() {
    const { $router, $auth } = getCurrentInstance().proxy

    const logout = async () => {
      await $auth.logout()
      await $router.push('/')
    }

    return { logout }
  }
}
</script>

<style scoped>
.admin-layout {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}
</style>
