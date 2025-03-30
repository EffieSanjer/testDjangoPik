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
import {ref, getCurrentInstance, onServerPrefetch, onMounted, computed} from "vue";

export default {
  components: {HikeCard},

  setup() {
    const hikes = ref([])
    const searchQuery = ref('')
    const { $axios } = getCurrentInstance().proxy

    const fetchHikes = async () => {
      try {
        const { data } = await $axios.get('/public/hikes/')
        hikes.value = data
      } catch {
        hikes.value = []
      }
    }

    onServerPrefetch(fetchHikes)

    onMounted(() => {
      if (!hikes.value.length) fetchHikes()
    })

    const filteredHikes = computed(() => {
      if (!searchQuery.value) return hikes.value
      return hikes.value.filter(hike =>
          hike.title.toLowerCase().includes(searchQuery.value.toLowerCase())
      )
    })

    return {
      searchQuery,
      filteredHikes
    }
  }
}
</script>
