<template>
  <div id="mapid"></div>
  <!-- <l-map style="height: 800px" :zoom="zoom" :center="center">
    <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
    <l-image-overlay :url="latarJangkauanRadar" :bounds="bounds" :opacity="0.15"></l-image-overlay>
    <l-image-overlay :url="imageOverlayUrl" :bounds="bounds"></l-image-overlay>
  </l-map> -->
</template>

<script>
import "leaflet/dist/leaflet.css";
import L from "leaflet";
// import {
//   LMap,
//   LTileLayer,
//   LGeoJson,
//   LCircle,
//   LImageOverlay
// } from "@vue-leaflet/vue-leaflet";
import { ref, onMounted, toRaw } from 'vue';
import axios from 'axios';
export default {
  // components: { LMap, LTileLayer, LGeoJson, LCircle, LImageOverlay },
  setup() {
    const canvas = document.createElement('canvas')
    canvas.setAttribute('width', 1000)
    canvas.setAttribute('height', 1000)
    const context = canvas.getContext('2d')
    const centerX = canvas.width / 2
    const centerY = canvas.height / 2
    const radius = 500

    context.beginPath()
    context.arc(centerX, centerY, radius, 0, 2 * Math.PI, false)
    context.fillStyle = '#333'
    context.fill()

    const latarJangkauanRadar = ref(canvas.toDataURL())

    const url = ref("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png")
    const attribution = ref('&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors')
    const zoom = ref(9)
    const center = ref([-6.894941, 107.58648])
    // const circle = ref({
    //   center: [-6.894941, 107.58648],
    //   radius: 44000,
    //   color: "green"
    // })
    const gambarRadar = ref("http://127.0.0.1:8000/dbz/datamat/santanu001_20211210_171610")
    const bounds = ref([[-7.2905, 107.982], [-6.4994, 107.191]])

    let mapDiv

    onMounted(async () => {

      mapDiv = L.map("mapid", {
        attributionControl: false,
        // zoomAnimation:false,
        zoomControl: false
      }).setView([-6.894941, 107.58648], 9)

      // const backgroundLayer = L.tileLayer(
      L.tileLayer(
        'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',

        {
          maxZoom: 18,
          minZoom: 5,
          id: 'mapbox/streets-v11'
        }
      )
        .addTo(mapDiv)

      mapDiv.createPane('panelJangkauanRadar')
      mapDiv.createPane('panelGambarRadar')
      mapDiv.getPane('panelJangkauanRadar').style.zIndex = 590
      mapDiv.getPane('panelGambarRadar').style.zIndex = 610

      const grupJangkauanRadar = L.layerGroup().addTo(toRaw(mapDiv))
      const grupGambarRadar = L.layerGroup().addTo(toRaw(mapDiv))

      L.imageOverlay(latarJangkauanRadar.value, bounds.value, {
        opacity: 0.10,
        pane: 'panelJangkauanRadar'
      }).addTo(grupJangkauanRadar)

      L.imageOverlay(
        gambarRadar.value,
        bounds.value,
        {
          pane: "panelGambarRadar",
          opacity: 0.85,
          // interactive: true,
        }
      ).addTo(grupGambarRadar)

      axios.get('http://127.0.0.1:8000/db').then(({ data }) => {
        console.log(data)

        const lenPathGambar = data.length
        const listPathGambar = []

        for (let item = 0; item < lenPathGambar; item++) {
          let pathGambar = "http://127.0.0.1:8000/dbz/datamat/" + data[item].file
          listPathGambar.push(pathGambar)
        }


        let indexPathGambar = 0
        const updateGambar = () => {

          setTimeout(() => {
            grupGambarRadar.clearLayers()

            L.imageOverlay(
              listPathGambar[indexPathGambar],
              bounds.value,
              {
                pane: "panelGambarRadar",
                opacity: 0.85,
                // interactive: true,
              }
            ).addTo(grupGambarRadar)

            indexPathGambar++
            if (indexPathGambar == lenPathGambar) indexPathGambar = 0
            updateGambar()
          }, 1000)
        }
        updateGambar()

      })

    })

    return {
      url,
      attribution,
      zoom,
      center,
      // circle,
      gambarRadar,
      bounds,
      latarJangkauanRadar,

    }
  }
  // data() {

  // return {
  // url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
  // attribution:
  //   '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
  // zoom: 9,
  // center: [-6.894941, 107.58648],
  // circle: {
  //   center: [-6.894941, 107.58648],
  //   radius: 44000,
  //   color: "green"
  // },


  //     imageOverlayUrl:
  //       "http://127.0.0.1:8000/dbz/datamat/santanu001_20211210_171610",
  //     bounds: [[-7.2905, 107.982], [-6.4994, 107.191]],
  //     latarJangkauanRadar

  //   }
  // },

};
</script>

<style>
#mapid {
  height: 800px;
  width: 100%;
}
</style>
