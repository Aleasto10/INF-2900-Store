
// Plugins
import { registerPlugins } from '@/plugins'

// Components
import App from './App.vue'
import router from './router/index.ts'

// Composables
import { createApp } from 'vue'



import { createVuetify } from 'vuetify'
import 'vuetify/styles'

const vuetify = createVuetify()

const app = createApp(App)

registerPlugins(app)

app.use(vuetify)
app.use(router)

app.mount('#app')
