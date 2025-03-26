<template>
  <div class="card hike-card">
    <div class="card-image" @click="$router.push(`/hikes/${hike.slug}/`)">
      <b-image v-if="hike.image" :src="hike.image" alt="hike image" ratio="10by7" lazy></b-image>
      <img v-else src="~assets/img_placeholder.png" alt="hike image"/>
    </div>

    <div class="card-content">
      <p class="title is-4">{{ hike.title }}</p>

      <nuxt-link :to="`/hikes/${hike.slug}/`" class="">
        Перейти
      </nuxt-link>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    hike: {
      type: Object,
      required: true
    }
  }
}
</script>


<style>
.hike-card {
  margin-bottom: 1.5rem;
  height: 100%;
  transition: transform 0.3s;
  cursor: pointer;
}

.hike-card:hover {
  transform: translateY(-5px);
}
</style>
