<template>
  <TheLegend />
  <TheMap />
  <Notif />
</template>

<script>
import TheMap from 'src/components/TheMap.vue'
import TheLegend from 'src/components/TheLegend.vue'
import Notif from '../components/Notif.vue'
export default {
  name: 'Home',
  components: {
    TheMap,
    TheLegend,
    Notif
  }
}
</script>