import BaseModel from "./BaseModel";

export default class Application extends BaseModel {
  defaults() {
    return {
      id: null,
      name: '',
      email: '',
      phone: '',
      hike_title: '',
      hike_slug: '',
      is_canceled: false,
      created_at: null
    }
  }

  options() {
    return {
      methods: {
        'cancel': 'POST'
      }
    }
  }

  routes() {
    return {
      cancel: '/bookings/{id}/cancel/'
    }
  }

  cancel() {
    let method = this.getOption('methods.cancel')
    let route = this.getRoute('cancel')
    let params = this.getRouteParameters()
    let url = this.getURL(route, params)

    return this.createRequest({method, url}).send()
  }
}
