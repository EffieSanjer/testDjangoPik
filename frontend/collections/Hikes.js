import Hike from '~/models/Hike'
import BaseCollection from "./BaseCollection";

export default class HikeCollection extends BaseCollection {
  model() {
    return Hike
  }

  routes() {
    return {
      fetch: '/hikes/'
    }
  }
}
