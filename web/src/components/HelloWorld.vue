<template>
<div>
  <div>
    <GmapMap
	  id="map"
	  ref="map"
      :center="{lat:24.9539405, lng:121.2234109}"
      :zoom="17"
      style="width: auto; height: 500px"
      >
	  <GmapInfoWindow :options="infoOptions" :position="infoWindowPos" :opened="infoWinOpen" @closeclick="infoWinOpen=false" >
		<span v-html="infoContent"></span>
	  </GmapInfoWindow>
	  <GmapCluster>
		<GmapMarker
          :key="index"
          v-for="(m, index) in incidents"
          :position="{lat: m.GPS緯度, lng: m.GPS經度}"
          :clickable="true"
          :draggable="true"
          @click="center=m.position;toggleInfoWindow(m,index)"
		  />
	  </GmapCluster>
    </GmapMap>
  </div>
  <b-container style="padding-top: 20px; padding-bottom: 20px">
	<b-row>
	  <b-col>
		<b-card border-variant="danger" header-bg-variant="danger" header-text-variant="white" header="總事故件數" align="center">
		  {{ total_incidents }} 件
		</b-card>
	  </b-col>
	</b-row>
	<b-row>
	  <b-col>
		<b-card border-variant="primary" header-bg-variant="primary" header-text-variant="white" header="事故日期區間" align="center">
		  <datepicker wrapper-class="picker-wrapper" v-model="fromDate"></datepicker>
		  <datepicker wrapper-class="picker-wrapper" v-model="toDate"></datepicker>
		</b-card>
	  </b-col>
	</b-row>
	<b-row>
	  <b-card-group columns>
		<b-card v-for="v,k in filterTypesOptions" :header="k">
		  <b-form-group>
			<b-form-checkbox-group v-model="filterTypes[k]" :options="v" v-on:input="updateIncidentByBounds"/>
		  </b-form-group>
		</b-card>
	  </b-card-group>
	</b-row>
  </b-container>
</div>
</template>

<script>
import Datepicker from 'vuejs-datepicker'
import moment from "moment"
import { extendMoment } from 'moment-range'
import {gmapApi} from 'vue2-google-maps'

function minutesOfTime(m) {
  return parseInt(m.split(':')[0]) * 60 + parseInt(m.split(':')[1])
}

export default {
  name: 'HelloWorld',
  computed: {
	google: gmapApi
  },
  components: {
	Datepicker
  },
  data() {
    return {
	  moment: extendMoment(moment),
	  incidents: [],
	  total_incidents: 0,
	  mapupdater: null,

	  infoContent: '',
	  infoWindowPos: null,
	  infoWinOpen: false,
	  infoOptions: {
		pixelOffset: {
		  width: 0,
		  height: -35
		}
	  },
	  currentMidx: null,

	  // Date picker
	  fromDate: moment(this.$route.query.from ? this.$route.query.from : '2017-01-01').toDate(),
	  toDate: moment(this.$route.query.to ? this.$route.query.to : '2018-2-28').toDate(),

	  // Filter Options
	  filterTypes: {},
	  filterTypesOptions: {}
    }
  },
  watch: {
  },
  methods: {
	toggleInfoWindow: function(marker, idx) {
	  console.log(marker.乘坐車輛的當事者區分_子類別代碼_車種)
	  this.infoWindowPos = {lat: marker.GPS緯度, lng: marker.GPS經度}

	  var content = ''
	  var value = null
	  for (var k in marker) {
		if (k in this.filterTypesOptions) {
		  value = this.filterTypesOptions[k][marker[k]]
		} else {
		  value = marker[k]
		}
		content += `${k}: ${value}\n`
	  }

	  this.infoContent = content.replace(/\n/g, "<br />");

	  if (this.currentMidx == idx) {
		this.infoWinOpen = !this.infoWinOpen
	  } else {
		this.currentMidx = idx
		this.infoWinOpen = true
	  }
	},
    updateFilterMarkers: function () {

    },
	updateIncidentByBounds: function() {
	  var lat1 = this.bounds.ma.j
	  var lat2 = this.bounds.ma.l
	  var lng1 = this.bounds.fa.j
	  var lng2 = this.bounds.fa.l
	  var url = `https://taoyuan.freeway.pw/api/incidents/${lat1}/${lng1}/${lat2}/${lng2}`

	  var self = this
	  this.axios
		.post(url, self.filterTypes, {
		  headers: {
		  }
		})
	  	.then((response) => {
		  this.incidents = response.data.data
		  this.total_incidents = response.data.total
		})
	}
  },
  mounted () {
	var self = this
	this.$refs.map.$on('bounds_changed', function(bound) {
	  clearTimeout(self.mapupdater)
	  self.mapupdater = setTimeout(self.updateIncidentByBounds, 500);
	  self.bounds = bound
	})

	this.axios.get('https://taoyuan.freeway.pw/api/filters')
	  .then((response) => {
		self.filterTypesOptions = response.data
		for (var key in self.filterTypesOptions) {
		  self.filterTypes[key] = []
		}
	  })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

.picker-wrapper {
	display: inline-block;
}

.container > .row {
	padding-top: 5px;
	padding-bottom: 5px;
}

</style>
