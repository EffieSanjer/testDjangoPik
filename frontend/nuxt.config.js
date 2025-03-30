
export default {
  mode: 'universal',
  ssr: true,

  env: {
    apiBaseUrl: process.env.API_BASE_URL || "http://localhost:8000"
  },

  head: {
    title: 'Походы',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: process.env.npm_package_description || '' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      {
        rel: 'stylesheet',
        href: 'https://fonts.googleapis.com/css2?family=Montserrat:wght@100..900&display=swap'
      }
    ]
  },

  loading: { color: '#fff' },
  css: [
    '@mdi/font/css/materialdesignicons.min.css',
    '@/assets/scss/main.scss'
  ],
  plugins: [
      '~/plugins/validation'
  ],
  modules: [
    '@nuxtjs/axios',
    '@nuxtjs/auth-next',
    'nuxt-buefy'
  ],
  buefy: {
    materialDesignIcons: true,
    defaultIconPack: 'mdi',
    css: true
  },
  axios: {
    baseURL: `${process.env.API_BASE_URL}/api/v1`,
    headers: {
      common: {
        'Accept': 'application/json'
      }
    }
  },
  auth: {
    strategies: {
      local: {
        token: {
          property: 'access',
          global: true,
          required: true,
          type: 'Bearer'
        },
        refreshToken: {
          property: 'refresh',
          data: 'refresh_token'
        },
        user: false,
        endpoints: {
          login: { url: '/auth/login/', method: 'post' },
          refresh: { url: '/auth/refresh/', method: 'post' },
          logout: false,
          user: false
        }
      }
    },
    redirect: {
      login: '/login/',
      logout: '/',
      home: '/admin/hikes/'
    }
  },
  build: {
    extend (config, ctx) {
    }
  }
}
