<template>
  <div>
    <form @submit.prevent="submitForm">
      <b-field label="Имя">
        <b-input
            v-model="form.name"
            name="name"
            required
        />
      </b-field>

      <ValidationProvider rules="email" v-slot="v">
        <b-field label="Email"
                 :type="{ 'is-danger': v.errors.length > 0 }"
                 :message="v.errors[0]"
        >
          <b-input
              v-model="form.email"
              name="email"
              type="email"
              required
          />
        </b-field>
      </ValidationProvider>

      <ValidationProvider rules="phone" v-slot="v">
        <b-field label="Телефон"
                 :type="{ 'is-danger': v.errors.length > 0 }"
                 :message="v.errors"
        >
          <b-input
              v-model="form.phone"
              name="phone"
              type="tel"
              required
          />
        </b-field>
      </ValidationProvider>

      <b-button
          native-type="submit"
          type="is-primary"
          :loading="isSubmitting"
          class="mt-4"
      >
        Отправить заявку
      </b-button>
    </form>

  </div>
</template>

<script>
import { getCurrentInstance, reactive, ref } from "vue";
import { ValidationProvider } from 'vee-validate';

export default {
  components: { ValidationProvider },

  props: {
    hikeId: {
      type: Number,
      required: true
    }
  },

  setup(props) {
    const { $buefy, $axios } = getCurrentInstance().proxy

    const isSubmitting = ref(false)
    const isSuccess = ref(null)

    const form = reactive({
      name: '',
      phone: '',
      email: '',
      hike_id: props.hikeId,
    })

    const submitForm = async () => {
      isSubmitting.value = true

      try {
        await $axios.post('/public/bookings/create/', form)

        $buefy.notification.open({
          message: `Спасибо за заявку! Мы свяжемся с Вами в ближайшее время.`,
          duration: 5000,
          progressBar: true,
          type: 'is-primary',
          pauseOnHover: true
        })

        form.name = null
        form.email = null
        form.phone = null
      }
      catch (error) {
        $buefy.toast.open({
          message: 'Ошибка отправки формы',
          type: 'is-danger',
        })
      }
      finally {
        isSubmitting.value = false
      }
    }

    return {
      form,
      isSuccess,
      isSubmitting,

      submitForm
    }
  }
}
</script>
