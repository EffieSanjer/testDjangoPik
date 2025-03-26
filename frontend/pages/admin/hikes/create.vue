<template>
  <section class="section">
    <div class="container">
      <div class="level">
        <div class="level-left">
          <h1 class="title">Создать новый поход</h1>
        </div>
        <div class="level-right">
          <b-button
              tag="nuxt-link"
              to="/admin/hikes/"
              type="is-light"
              icon-left="arrow-left"
          >
            Назад к списку
          </b-button>
        </div>
      </div>

      <div>
        <admin-hike-form @submit="submitForm"></admin-hike-form>
      </div>

    </div>
  </section>
</template>

<script>
import { ref, getCurrentInstance } from 'vue'
import Hike from "@/models/Hike";
import AdminHikeForm from "@/components/Admin/HikeForm.vue";

export default {
  components: { AdminHikeForm },
  middleware: ['auth'],
  layout: 'admin',

  setup() {
    const { $route, $router } = getCurrentInstance().proxy

    const isLoading = ref(true)
    const hikeSlug = $route.params.slug
    const hike = ref(null)

    const submitForm = async (formData) => {
      hike.value = new Hike({ slug: null })
      await hike.value.save({
        data: formData,
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })

      await $router.push('/admin/hikes/')
    }

    return {
      isLoading,
      hikeSlug,
      hike,

      submitForm
    }
  }
}
</script>
