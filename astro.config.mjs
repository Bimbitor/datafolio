// @ts-check
import { defineConfig } from "astro/config";

// Repo de proyecto (Bimbitor/datafolio): Pages lo sirve bajo /datafolio/.
// Todo enlace interno debe construirse con import.meta.env.BASE_URL.
// Si se configura un dominio propio, quitar `base`.
export default defineConfig({
  site: "https://bimbitor.github.io",
  base: "/datafolio",
  trailingSlash: "always",
  i18n: {
    locales: ["es", "en"],
    defaultLocale: "es",
    routing: { prefixDefaultLocale: false },
  },
});
