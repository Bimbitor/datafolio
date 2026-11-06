import { defineConfig } from "vitest/config";

// Las pruebas del sitio son de logica pura: el mapa de rutas y la negociacion de idioma.
// No hay navegador ni componentes renderizados, por decision explicita (research.md, D-13).
export default defineConfig({
  test: {
    include: ["tests/**/*.test.ts"],
  },
});
