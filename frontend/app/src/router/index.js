import Vue from 'vue'
import Router from 'vue-router'

// salkhatib
import Auth from '@/components/pages/Auth'
import Consumption from '@/components/pages/Consumption'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Consumption',
      component: Consumption
    },
    {
      path: '/auth',
      name: 'Auth',
      component: Auth
    }
  ]
})
