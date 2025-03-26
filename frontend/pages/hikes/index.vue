<template>
  <div>
    <section class="container level">
      <div class="level-left">
        <h1 class="title">
          Запланированные походы
        </h1>
      </div>
      <div class="search-box level-right">
        <b-input
            v-model="searchQuery"
            placeholder="Найти поход..."
            type="search"
            icon="magnify"
            rounded
        />
      </div>
    </section>

    <section class="container">
      <div v-if="filteredHikes.length === 0" class="has-text-grey">
        Походы не найдены
      </div>

      <div class="columns is-multiline">
        <div
            v-for="hike in filteredHikes"
            :key="hike.id"
            class="column is-12-mobile is-6-tablet is-3-desktop"
        >
          <hike-card :hike="hike"></hike-card>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import HikeCard from "@/components/HikeCard.vue";

export default {
  components: {HikeCard},

  async asyncData({ $axios }) {
    try {
      const { data } = await $axios.get('/public/hikes/')
      return { hikes: data }
    }
    catch {
      return { hikes: [] }
    }
  },

  data() {
    return {
      searchQuery: '',
      hikes: []
    }
  },

  computed: {
    filteredHikes() {
      if (!this.searchQuery) return this.hikes
      return this.hikes.filter(hike =>
          hike.title.toLowerCase().includes(this.searchQuery.toLowerCase()))
    }
  },

}
</script>

<style scoped>
.search-box {
  margin-bottom: 2rem;
}

</style>
