<template>
  <section class="section">
    <div class="container">
      <div class="level">
        <div class="level-left">
          <h1 class="title">Походы</h1>
        </div>
        <div class="level-right">
          <b-button
              tag="nuxt-link"
              to="/admin/hikes/create/"
              type="is-primary"
              icon-left="plus"
          >
            Новый поход
          </b-button>
        </div>
      </div>

      <b-table
          :data="hikesData"
          :loading="isLoading"
          hoverable
      >
        <b-table-column field="id" label="Id" v-slot="props">
          {{ props.row.id }}
        </b-table-column>

        <b-table-column field="title" label="Название" v-slot="props">
          <nuxt-link :to="`/admin/hikes/${props.row.slug}/`">
            {{ props.row.title }}
          </nuxt-link>
        </b-table-column>

        <b-table-column field="startAt" label="Дата похода" v-slot="props">
          {{ formatDate(props.row.start_at) }}
        </b-table-column>

        <b-table-column field="isPublic" label="Доступен на сайте" centered v-slot="props">
          {{ props.row.is_public ? 'Да' : 'Нет' }}
        </b-table-column>

        <b-table-column field="image" label="Изображение" v-slot="props">
          <b-image v-if="props.row.image" :src="props.row.image" ratio="5by3" width="100%" lazy></b-image>
          <span v-else>Нет</span>
        </b-table-column>

        <b-table-column field="actions" centered label="" v-slot="props">
          <div class="buttons">
            <b-button type="is-ghost" @click="confirmDelete(props.row)">
              <b-icon
                  type="is-danger"
                  size="is-regular"
                  icon="delete-outline"
              />
            </b-button>
          </div>
        </b-table-column>
      </b-table>
    </div>
  </section>
</template>

<script>
import { ref, onMounted, computed, getCurrentInstance } from 'vue'
import Hike from '@/models/Hike'
import HikeCollection from '@/collections/Hikes'

export default {
  middleware: ['auth'],
  layout: 'admin',

  setup() {
    const hikes = ref(null)
    const isLoading = ref(false)
    const { $buefy } = getCurrentInstance().proxy

    const fetchHikes = async () => {
      isLoading.value = true
      try {
        hikes.value = new HikeCollection()
        await hikes.value.fetch()

      } catch (error) {
        $buefy.toast.open({
          message: 'Ошибка загрузки походов',
          type: 'is-danger'
        })

      } finally {
        isLoading.value = false
      }
    }

    const hikesData = computed(() => {
      return hikes.value?.map(model => model.toJSON()) || []
    })

    const confirmDelete = (hike) => {
      $buefy.dialog.confirm({
        title: 'Удаление похода',
        message: `Вы уверены, что хотите удалить "${hike.title}"?`,
        confirmText: 'Удалить',
        cancelText: 'Отмена',
        type: 'is-danger',
        onConfirm: () => deleteHike(hike.slug)
      })
    }

    const deleteHike = async (slug) => {
      try {
        const hike = new Hike({ slug: slug })
        await hike.delete()
        await fetchHikes()

        $buefy.toast.open({
          message: 'Поход удален',
          type: 'is-success'
        })
      }
      catch (error) {
        $buefy.toast.open({
          message: 'Ошибка удаления',
          type: 'is-danger'
        })
      }
    }

    const formatDate = (dateString) => {
      return new Date(dateString).toLocaleDateString()
    }

    onMounted(async () => {
      await fetchHikes()
    })

    return {
      hikesData,
      isLoading,
      confirmDelete,
      formatDate
    }
  }
}
</script>
