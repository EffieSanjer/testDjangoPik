<template>
  <form class="box" @submit.prevent="submitForm">
    <b-field label="Название похода"
             :message="errors.title"
             :type="{'is-danger': errors.title}"
    >
      <b-input v-model="form.title" required />
    </b-field>

    <b-field label="Описание">
      <b-input v-model="form.description" type="textarea" rows="4" />
    </b-field>

    <div class="columns">
      <b-field class="column" label="Дата похода">
        <b-datepicker
            v-model="form.start_at"
            placeholder="Выберите дату"
            :min-date="new Date()"
            icon="calendar"
            required
        />
      </b-field>

      <b-field class="column" label="Показывать на сайте" >
        <b-switch v-model="form.is_public">
          {{ form.is_public ? 'Да' : 'Нет' }}
        </b-switch>
      </b-field>
    </div>

    <b-field label="Изображение">
      <div class="columns">
        <div class="column">
          <b-upload v-model="form.image" accept="image/*" @input="handleImageUpload">
            <a class="button is-primary">
              <b-icon icon="upload"></b-icon>
              <span>{{ form.image ? 'Изменить фото' : 'Выберите файл' }}</span>
            </a>
          </b-upload>
        </div>
        <div v-if="imageUrl" class="mb-2 column">
          <b-image :src="imageUrl" alt="Preview" ratio="5by4" class="image-preview"></b-image>
        </div>
      </div>
    </b-field>

    <div class="buttons is-right">
      <b-button
          native-type="submit"
          type="is-primary"
          :loading="isSubmitting"
      >
        Сохранить изменения
      </b-button>
    </div>
  </form>

</template>

<script>
import { getCurrentInstance, reactive, ref, watch } from "vue";
import Hike from "@/models/Hike";

export default {
  props: {
    hike: {
      type: Hike,
      required: false
    }
  },

  setup(props, { emit }) {
    const { $buefy } = getCurrentInstance().proxy

    const imageUrl = ref(null)
    const isSubmitting = ref(false)

    const form = ref({
      title: '',
      description: '',
      image: null,
      start_at: new Date(),
      is_public: true
    })
    const errors = reactive({
      title: '',
    })

    const handleImageUpload = async (file) => {
      if (!file) return

      imageUrl.value = URL.createObjectURL(file)
      form.image = file
    }

    const validateForm = () => {
      let isValid = true
      clearErrors()

      if (!form.value.title.trim()) {
        errors.title = 'Введите название похода'
        isValid = false
      }

      return isValid
    }

    const submitForm = async () => {
      if (!validateForm()) return

      isSubmitting.value = true

      try {
        const formData = new FormData();
        formData.append('title', form.value.title);
        formData.append('description', form.value.description);
        formData.append('start_at', form.value.start_at.toISOString());
        formData.append('is_public', form.value.is_public);

        if (form.image instanceof File) {
          formData.append('image', form.image);
        }

        emit('submit', formData)

        showSuccess('Изменения сохранены!')
      }
      catch (error) {
        handleError(error)
      }
      finally {
        isSubmitting.value = false
      }
    }

    const clearErrors = () => {
      Object.keys(errors).forEach(key => {
        errors[key] = ''
      })
    }

    const handleError = (error) => {
      if (error.response?.data?.errors) {
        Object.keys(error.response.data.errors).forEach(key => {
          if (errors.hasOwnProperty(key)) {
            errors[key] = error.response.data.errors[key].join(', ')
          }
        })
      } else {
        showError('Ошибка при сохранении')
        console.error('Ошибка:', error)
      }
    }


    const showSuccess = (message) => {
      $buefy.toast.open({
        message,
        type: 'is-success',
      })
    }

    const showError = (message) => {
      $buefy.toast.open({
        message,
        type: 'is-danger',
      })
    }

    watch(() => props.hike, (newValue) => {
      imageUrl.value = newValue.image || null
      form.value = { ...form.value, ...newValue.toJSON() }
      form.value.start_at = new Date(newValue.start_at)
    }, { deep: true })

    return {
      imageUrl,
      form,
      errors,
      isSubmitting,

      handleImageUpload,
      submitForm
    }
  }
}
</script>

