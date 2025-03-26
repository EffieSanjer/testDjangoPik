import { Collection } from 'vue-mc'
import { API_CONFIG } from '~/utils/privateApiConfig'

export default class BaseCollection extends Collection {
  createRequest( config ) {
    const token = localStorage.getItem('auth._token.local')

    config.baseURL = API_CONFIG.baseURL
    config.headers =  {
      ...API_CONFIG.headers,
      'Authorization': token ? token : ''
    }

    return super.createRequest(config);
  }
}
