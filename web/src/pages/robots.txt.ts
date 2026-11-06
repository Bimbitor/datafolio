import type { APIRoute } from "astro";

// Se genera en lugar de vivir en public/ para que el dominio salga de SITE_URL y no quede
// escrito a mano: un valor, un solo lugar. Si la variable no esta puesta —en local, por
// ejemplo— se omite la linea del sitemap en vez de publicar una direccion inventada.
export const GET: APIRoute = () => {
  const sitio = import.meta.env.SITE_URL;
  const lineas = ["User-agent: *", "Disallow: /admin", ""];
  if (sitio) lineas.push(`Sitemap: ${sitio.replace(/\/$/, "")}/sitemap.xml`, "");

  return new Response(lineas.join("\n"), {
    headers: { "Content-Type": "text/plain; charset=utf-8" },
  });
};
