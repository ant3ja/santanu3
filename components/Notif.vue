
<script>
import { useQuasar } from 'quasar'
import axios from 'axios'
import moment from 'moment'


export default {
  setup() {
    const $q = useQuasar()
    axios.get('http://127.0.0.1:8000/db').then(({ data }) => {
      console.log(data)

      const lenStatusGambar = data.length
      const listStatusGambar = []

      for (let item = 0; item < lenStatusGambar; item++) {
        let pathStatus = 'http://127.0.0.1:8000/status/' + data[item].file
        listStatusGambar.push(pathStatus)

        console.log(listStatusGambar)



        axios.get(pathStatus).then(({ data }) => {

          const nilaiGambar = [data]

          const hasilNilaiGambar = nilaiGambar.every((item) => {
            return item >= 25
          })
          if (hasilNilaiGambar === true) {
            $q.notify({
              message: 'Potensi Banjir daerah Bandung',
              caption: moment().format('hh:mm a'),
              icon: 'warning',
              timeout: 5000,
              color: 'warning',
              position: 'top'
            })
          } console.log(hasilNilaiGambar)
        })
      }
    })
  }
}
</script>

