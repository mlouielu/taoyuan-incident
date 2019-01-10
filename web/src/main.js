// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import * as VueGoogleMaps from 'vue2-google-maps'
import HighchartsVue from 'highcharts-vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import GmapCluster from 'vue2-google-maps/dist/components/cluster'

Vue.config.productionTip = false

Vue.use(HighchartsVue)
Vue.use(BootstrapVue)
Vue.use(VueAxios, axios)
Vue.use(VueGoogleMaps, {
    load: {
        key: 'AIzaSyA6DV52Q1b2ik1DK9TBSbjyeGNb2DCEdX4',
        libraries: 'places'
    },
})
Vue.component('GmapCluster', GmapCluster)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
