/**
 * Mapa de rutas: la fuente de verdad de las direcciones del sitio.
 *
 * De aqui salen los enlaces del menu, el destino del selector de idioma, las etiquetas
 * canonicas y de equivalencia, y el indice para buscadores. Si un slug aparece escrito en
 * cualquier otro sitio del proyecto, es un defecto.
 *
 * El enrutado nativo de i18n de Astro no traduce slugs, asi que esto se construye a mano.
 * Ver specs/001-sitio-base/research.md, D-06, y data-model.md, seccion 2.
 */

export const IDIOMAS = ["en", "es"] as const;
export type Idioma = (typeof IDIOMAS)[number];

/** El ingles es el destino cuando no se puede determinar el idioma o no es espanol. */
export const IDIOMA_POR_DEFECTO: Idioma = "en";

export type Clave =
  | "inicio"
  | "experiencia"
  | "proyectos"
  | "proyecto"
  | "blog"
  | "articulo"
  | "contacto"
  | "politica";

export interface Ruta {
  clave: Clave;
  slug: Record<Idioma, string>;
  /** Si aparece en el menu. Las rutas de detalle no se enlazan desde ahi. */
  enNavegacion: boolean;
  /** Si entra en el indice para buscadores. */
  enIndice: boolean;
}

/**
 * La pagina de error NO esta aqui, y es a proposito: no tiene direccion propia. Responde a
 * cualquier direccion que no exista, asi que no es una ruta sino el destino de lo que
 * sobra. Su etiqueta vive en textos.ts como las demas.
 *
 * Las rutas de detalle llevan el parametro dentro del slug para que cada seccion tenga un
 * slug distinto; si no, `proyectos` y `proyecto` chocarian.
 */
export const rutas: readonly Ruta[] = [
  { clave: "inicio", slug: { en: "", es: "" }, enNavegacion: true, enIndice: true },
  {
    clave: "experiencia",
    slug: { en: "experience", es: "experiencia" },
    enNavegacion: true,
    enIndice: true,
  },
  {
    clave: "proyectos",
    slug: { en: "projects", es: "proyectos" },
    enNavegacion: true,
    enIndice: true,
  },
  {
    clave: "proyecto",
    slug: { en: "projects/[slug]", es: "proyectos/[slug]" },
    enNavegacion: false,
    enIndice: false,
  },
  { clave: "blog", slug: { en: "blog", es: "blog" }, enNavegacion: true, enIndice: true },
  {
    clave: "articulo",
    slug: { en: "blog/[slug]", es: "blog/[slug]" },
    enNavegacion: false,
    enIndice: false,
  },
  {
    clave: "contacto",
    slug: { en: "contact", es: "contacto" },
    enNavegacion: true,
    enIndice: true,
  },
  {
    clave: "politica",
    slug: { en: "data-policy", es: "politica-de-datos" },
    enNavegacion: true,
    enIndice: true,
  },
];

/** La direccion de una seccion en un idioma, siempre con prefijo y barra final. */
export function rutaDe(clave: Clave, idioma: Idioma): string {
  const ruta = rutas.find((r) => r.clave === clave);
  if (!ruta) throw new Error(`No existe ninguna ruta con la clave "${clave}".`);
  const slug = ruta.slug[idioma];
  return slug ? `/${idioma}/${slug}/` : `/${idioma}/`;
}

/** El otro idioma. Con dos, es el que no es. */
export function otroIdioma(idioma: Idioma): Idioma {
  return idioma === "en" ? "es" : "en";
}

/**
 * De que seccion es esta direccion, si es de alguna. Lo usa el selector de idioma para
 * llevar a la pagina equivalente en vez de al inicio.
 */
export function claveDeRuta(ruta: string): Clave | undefined {
  const limpia = ruta.replace(/\/+$/, "");
  for (const idioma of IDIOMAS) {
    for (const r of rutas) {
      const esperada = r.slug[idioma] ? `/${idioma}/${r.slug[idioma]}` : `/${idioma}`;
      if (limpia === esperada) return r.clave;
    }
  }
  return undefined;
}
