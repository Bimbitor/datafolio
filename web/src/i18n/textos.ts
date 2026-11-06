/**
 * Cadenas de interfaz en los dos idiomas.
 *
 * Solo texto de interfaz: etiquetas, botones, avisos. El contenido de las secciones llega
 * en la feature 02. Si una cadena aparece escrita dentro de un componente, es un defecto.
 */

import type { Clave, Idioma } from "./rutas";

interface Textos {
  /** Se usa en el atributo lang y en las etiquetas de equivalencia. */
  etiquetaIdioma: string;
  nombreIdioma: string;
  secciones: Record<Clave | "error", string>;
  navegacion: string;
  irAContenido: string;
  cambiarIdioma: string;
  cambiarTema: string;
  escribeme: string;
  pendiente: {
    titulo: string;
    cuerpo: string;
  };
  error: {
    titulo: string;
    cuerpo: string;
    volver: string;
  };
  pie: string;
}

export const textos: Record<Idioma, Textos> = {
  en: {
    etiquetaIdioma: "en",
    nombreIdioma: "English",
    secciones: {
      inicio: "Home",
      experiencia: "Experience",
      proyectos: "Projects",
      proyecto: "Project",
      blog: "Blog",
      articulo: "Article",
      contacto: "Contact",
      politica: "Data policy",
      error: "Page not found",
    },
    navegacion: "Main navigation",
    irAContenido: "Skip to content",
    cambiarIdioma: "Ver en español",
    cambiarTema: "Switch between light and dark",
    escribeme: "Email me",
    pendiente: {
      titulo: "Nothing here yet",
      cuerpo: "This section is built but still empty. The content lands in the next release.",
    },
    error: {
      titulo: "This page does not exist",
      cuerpo: "The address may be wrong, or the page may have moved.",
      volver: "Go to the home page",
    },
    pie: "Javi Giraldo — data analyst",
  },
  es: {
    etiquetaIdioma: "es",
    nombreIdioma: "Español",
    secciones: {
      inicio: "Inicio",
      experiencia: "Experiencia",
      proyectos: "Proyectos",
      proyecto: "Proyecto",
      blog: "Blog",
      articulo: "Artículo",
      contacto: "Contacto",
      politica: "Política de datos",
      error: "Página no encontrada",
    },
    navegacion: "Navegación principal",
    irAContenido: "Ir al contenido",
    cambiarIdioma: "View in English",
    cambiarTema: "Cambiar entre claro y oscuro",
    escribeme: "Escríbeme",
    pendiente: {
      titulo: "Todavía no hay nada aquí",
      cuerpo:
        "Esta sección ya está construida, pero sigue vacía. El contenido llega en la próxima entrega.",
    },
    error: {
      titulo: "Esta página no existe",
      cuerpo: "Puede que la dirección esté mal escrita, o que la página haya cambiado de sitio.",
      volver: "Ir al inicio",
    },
    pie: "Javi Giraldo — analista de datos",
  },
};
