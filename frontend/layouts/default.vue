<template>
  <div class="layout">
    <header>
      <div class="container level">
        <div class="level-left">
          <logo/>
        </div>
        <div class="level-left">
          <b-button tag="nuxt-link" to="/admin/" type="is-dark is-medium">
            Панель управления
          </b-button>
        </div>
      </div>
    </header>

    <main class="main-content">
      <nuxt />
    </main>

    <footer class="footer">
      <div class="container">
        <p>&copy; Походы. Все права защищены.</p>
      </div>
    </footer>
  </div>

</template>

<script>

import Logo from "@/components/Logo.vue";

export default {
  components: {Logo}
}
</script>
