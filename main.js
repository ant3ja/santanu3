import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from "axios"

axios.defaults.baseURL = 'http://127.0.0.1:8000';
axios.defaults.headers.post['Content-Type'] ='application/json;charset=utf-8';
  axios.defaults.headers.post['Access-Control-Allow-Origin'] = '*';
  axios.get(serviceUrl, onSuccess, onFailure)
  .then(resp => {
        let result = resp.data;
        onSuccess(result);
  })
  .catch(error => {
        if(onFailure) {
            return onFailure(error);
        }
  })

const app = createApp(App)


app.use(router)

app.mount('#app')
