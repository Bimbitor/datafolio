import { defineConfig } from "astro/config";
import vercel from "@astrojs/vercel";
import tailwindcss from "@tailwindcss/vite";

// El sitio es estatico por defecto. Las rutas que necesitan servidor lo piden una por una
// con `export const prerender = false`, para no pagar latencia en las dieciocho paginas por
// resolver dos. Ver specs/001-sitio-base/research.md, D-07 y D-07 bis.
//
// El plugin de Tailwind va en vite.plugins, no en integrations: la integracion
// @astrojs/tailwind esta deprecada y su propio paquete remite aqui (research.md, D-08).
export default defineConfig({
  adapter: vercel(),
  vite: {
    plugins: [tailwindcss()],
  },
});
