<template>
  <div class="container">
    <div v-if="hike" class="columns">
      <div class="column is-two-thirds">
        <div class="box">
          <h1 class="title is-2">{{ hike.title }}</h1>
          <b-image
              v-if="hike.image"
              :src="hike.image"
              ratio="16by9"
              alt="hike image"
              lazy
          />
          <img v-else src="~assets/img/img_placeholder.png" alt="hike image"/>

          <div class="content mt-4">
            <p class="subtitle is-4">{{ hike.description }}</p>
          </div>
        </div>
      </div>

      <div class="column">
        <div class="box">
          <h2 class="title is-4">Заявка на участие</h2>
          <booking-form :hikeId="hike.id" />
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import {ref, getCurrentInstance, onServerPrefetch, onMounted} from "vue";
import BookingForm from "@/components/BookingForm.vue";

export default {
  components: {BookingForm},

  setup() {
    const hike = ref(null)
    const { $axios, $route } = getCurrentInstance().proxy
    const hikeId = $route.params.slug

    const fetchHike = async () => {
      try {
        const { data } = await $axios.get(`/public/hikes/${hikeId}/`)
        hike.value = data
      } catch {
        hike.value = null
      }
    }

    onServerPrefetch(fetchHike)

    onMounted(() => {
      if (!hike.value) fetchHike()
    })

    return {
      hike
    }
  }
}
</script>