import BaseModel from "./BaseModel";

export default class Hike extends BaseModel {
  options() {
    return {
      identifier: 'slug',
      methods: {
        'update': 'PATCH'
      }
    }
  }

  defaults() {
    return {
      id: null,
      title: '',
      slug: '',
      description: '',
      image: null,
      start_at: null,
      is_public: true
    }
  }

  routes() {
    return {
      fetch: '/hikes/{slug}/',
      save:  '/hikes/{slug}/',
      create:  '/hikes/create/',
      update: '/hikes/{slug}/update/',
      delete: '/hikes/{slug}/delete/'
    }
  }
}
