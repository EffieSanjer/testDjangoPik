<template>
  <section class="section">
    <div class="container">
      <div class="level">
        <div class="level-left">
          <h1 class="title">Заявки</h1>
        </div>
      </div>

      <b-table
          :data="bookingsData"
          :loading="isLoading"
          :row-class="(row, i) => row.is_canceled && 'is-canceled'"
          hoverable
      >
        <b-table-column field="id" label="Номер" v-slot="props">
          {{ props.row.id }}
        </b-table-column>

        <b-table-column field="created_at" label="Дата создания" v-slot="props">
          {{ formatDate(props.row.created_at) }}
        </b-table-column>

        <b-table-column field="name" label="Имя" v-slot="props">
          {{ props.row.name }}
        </b-table-column>

        <b-table-column field="phone" label="Телефон" v-slot="props">
          {{ props.row.phone }}
        </b-table-column>

        <b-table-column field="email" label="Email" v-slot="props">
          {{ props.row.email }}
        </b-table-column>

        <b-table-column field="hike" label="Поход" v-slot="props">
          <nuxt-link :to="`/admin/hikes/${props.row.hike_slug}/`">
            {{ props.row.hike_title }}
          </nuxt-link>
        </b-table-column>

        <b-table-column field="canceled" label="" v-slot="props">
          <b-button type="is-ghost" class="tag is-danger is-light" @click="toggleCancel(props.row.id)">
            <span v-if="props.row.is_canceled">Восстановить</span>
            <span v-else>Отменить</span>
          </b-button>
        </b-table-column>
      </b-table>
    </div>
  </section>
</template>

<script>
import {ref, onMounted, computed, getCurrentInstance} from 'vue'
import Booking from '@/models/Booking'
import BookingCollection from '@/collections/Bookings'

export default {
  middleware: ['auth'],
  layout: 'admin',

  setup() {
    const bookings = ref(null)
    const isLoading = ref(false)
    const { $buefy } = getCurrentInstance().proxy

    const fetchBookings = async () => {
      isLoading.value = true
      try {
        bookings.value = new BookingCollection()
        await bookings.value.fetch()
      }
      catch (error) {
        $buefy.toast.open({
          message: 'Ошибка загрузки заявок',
          type: 'is-danger'
        })
      }
      finally {
        isLoading.value = false
      }
    }

    const bookingsData = computed(() => {
      return bookings.value?.map(model => model.toJSON()) || []
    })

    const toggleCancel = async (id) => {
      try {
        const booking = new Booking({ id: id })

        await booking.cancel()
        await fetchBookings()

        $buefy.toast.open({
          message: 'Успешно!',
          type: 'is-success'
        })
      }
      catch (error) {
        $buefy.toast.open({
          message: 'Ошибка!',
          type: 'is-danger'
        })
      }
    }

    const formatDate = (dateString) => {
      return new Date(dateString).toLocaleDateString()
    }

    onMounted(async () => {
      await fetchBookings()
    })

    return {
      bookingsData,
      isLoading,

      formatDate,
      toggleCancel
    }
  }
}
</script>

<style>
  tr.is-canceled {
    background-color: rgb(255 245 247);
;
;
  }
</style>
