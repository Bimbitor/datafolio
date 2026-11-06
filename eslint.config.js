import js from "@eslint/js";

export default [
  {
    ignores: ["**/dist/", "**/.astro/", "**/.vercel/", "**/.venv/"],
  },
  js.configs.recommended,
  {
    // Los ganchos de Claude Code y los archivos de configuracion corren en Node, no en el
    // navegador, asi que sus globales no son errores.
    files: [".claude/hooks/**/*.mjs", "**/*.config.{js,mjs}"],
    languageOptions: {
      globals: {
        Buffer: "readonly",
        console: "readonly",
        process: "readonly",
        URL: "readonly",
      },
    },
  },
];
