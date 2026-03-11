
// Plugins
import { registerPlugins } from '@/plugins'

// Components
import App from './App.vue'

// Composables
import { createApp } from 'vue'

import router from './router'

import { createVuetify } from 'vuetify'
import 'vuetify/styles'

const vuetify = createVuetify()

const app = createApp(App)

registerPlugins(app)

app.mount('#app')
app.use(vuetify)