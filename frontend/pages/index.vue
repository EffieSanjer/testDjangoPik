<template>
  <div>
    <section class="mb-6">
      <b-carousel
          :animated="'slide'"
          :interval="5000"
          has-drag
          autoplay
          repeat>

        <b-carousel-item v-for="(slide, i) in carousel" :key="i">
          <section :class="`hero is-large is-bold is-link`" :style="`background: url(${slide.src}) no-repeat center center / cover`">
            <div class="hero-body has-text-centered">
              <h2 class="title is-size-1">{{ slide.title }}</h2>
            </div>
          </section>
        </b-carousel-item>
      </b-carousel>
    </section>

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

    <section class="container mb-6">
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

    const carousel = [
      {
        title: 'Путешествуй с нами',
        src: require('@/assets/img/carousel/1.jpg')
      },
      {
        title: 'Походы с друзьями и родными',
        src: require('@/assets/img/carousel/2.jpg')
      },
      {
        title: 'Путешествие начинается с заявки',
        src: require('@/assets/img/carousel/3.jpg')
      },
      {
        title: 'Исследуй мир',
        src: require('@/assets/img/carousel/4.jpg')
      },
      {
        title: 'Поднимись на вершину',
        src: require('@/assets/img/carousel/5.jpg')
      }
    ]

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
      filteredHikes,

      carousel
    }
  }
}
</script>
