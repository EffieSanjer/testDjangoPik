import Booking from '~/models/Booking'
import BaseCollection from "./BaseCollection";

export default class BookingCollection extends BaseCollection {
  model() {
    return Booking
  }

  routes() {
    return {
      fetch: '/bookings/'
    }
  }
}
