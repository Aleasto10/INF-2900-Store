
// Plugins
import { registerPlugins } from '@/plugins'

// Components
import App from './App.vue'
import router from './router/index.ts'

// Composables
import { createApp } from 'vue'

import { createVuetify } from 'vuetify'
import 'vuetify/styles'
import * as components from 'vuetify/components'

const vuetify = createVuetify({ components })

const app = createApp(App)

registerPlugins(app)

app.mount('#app')
