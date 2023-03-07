import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'

export default defineConfig({
  server: {
    port: parseInt(process.env.VITE_PORT),
    host: "0.0.0.0",
  },
  plugins: [react()],
})
