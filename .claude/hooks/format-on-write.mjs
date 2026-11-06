// Formatea con Prettier el archivo que Claude acaba de escribir o editar.
// Lo invoca el hook PostToolUse de .claude/settings.json.
// Recibe por entrada estandar el JSON del hook y nunca falla: si algo sale mal,
// termina en silencio y deja el archivo como estaba.

import { readFile, writeFile } from "node:fs/promises";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const raizProyecto = resolve(dirname(fileURLToPath(import.meta.url)), "..", "..");

async function leerEntrada() {
  const partes = [];
  for await (const trozo of process.stdin) partes.push(trozo);
  return Buffer.concat(partes).toString("utf8");
}

try {
  const entrada = await leerEntrada();
  const evento = JSON.parse(entrada);
  const archivo = evento?.tool_response?.filePath ?? evento?.tool_input?.file_path;
  if (!archivo) process.exit(0);

  const prettier = await import("prettier");

  // Respeta .prettierignore y salta lo que Prettier no sabe formatear.
  const info = await prettier.getFileInfo(archivo, {
    ignorePath: join(raizProyecto, ".prettierignore"),
  });
  if (info.ignored || !info.inferredParser) process.exit(0);

  const original = await readFile(archivo, "utf8");
  const config = await prettier.resolveConfig(archivo);
  const formateado = await prettier.format(original, { ...config, filepath: archivo });

  if (formateado !== original) await writeFile(archivo, formateado, "utf8");
} catch {
  // Silencio deliberado: un fallo al formatear nunca debe interrumpir el trabajo.
}

process.exit(0);
