<template>
  <section class="section">
    <div class="container">
      <div class="level">
        <div class="level-left">
          <h1 class="title">Редактировать поход</h1>
        </div>
        <div class="level-right">
          <b-button
              tag="nuxt-link"
              :to="`/admin/hikes/`"
              type="is-light"
              icon-left="arrow-left"
          >
            Назад
          </b-button>
        </div>
      </div>


      <div>
        <admin-hike-form :hike="hike" @submit="submitForm"></admin-hike-form>
      </div>

      <b-loading :is-full-page="true" :active="isLoading" />

    </div>
  </section>
</template>

<script>
import { ref, onMounted, getCurrentInstance } from 'vue'
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

    const loadHike = async () => {
      try {
        isLoading.value = true
        hike.value = new Hike({ slug: hikeSlug })
        await hike.value.fetch()
      }
      catch (error) {
        $buefy.toast.open({
          message: 'Ошибка загрузки данных похода',
          type: 'is-danger'
        })

        $router.push('/admin/hikes/')
      }
      finally {
        isLoading.value = false
      }
    }

    const submitForm = async (formData) => {
      hike.value.slug = hikeSlug
      await hike.value.save({
        data: formData,
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
    }

    onMounted(loadHike)

    return {
      isLoading,
      hikeSlug,
      hike,

      submitForm
    }
  }
}
</script>
