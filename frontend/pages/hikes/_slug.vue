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
          <img v-else src="~assets/img_placeholder.png" alt="hike image"/>

          <div class="content mt-4">
            <p class="subtitle is-4">{{ hike.description }}</p>

<!--            <div class="tags">-->
<!--              <b-tag type="is-info">-->
<!--                <b-icon icon="map-marker-distance" size="is-small"></b-icon>-->
<!--                {{ hike.distance }} км-->
<!--              </b-tag>-->
<!--            </div>-->
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
import BookingForm from "@/components/BookingForm.vue"

export default {
  components: { BookingForm },

  data() {
    return {
      hike: null
    }
  },

  async asyncData({ params, $axios, error }) {
    try {
      const { data } = await $axios.get(`/public/hikes/${params.slug}/`)
      return { hike: data }
    }
    catch (e) {
      error({ statusCode: 404, message: 'Поход не найден' })
      return { hike: null }
    }
  }
}
</script>