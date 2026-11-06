import { describe, expect, it } from "vitest";
import { IDIOMAS, rutaDe, rutas, type Idioma } from "../src/i18n/rutas";
import { textos } from "../src/i18n/textos";

// El mapa de rutas es la fuente de verdad de las direcciones del sitio: de el salen los
// enlaces, el selector de idioma, las etiquetas de buscador y el indice. Estas pruebas
// fijan las tres reglas que, si se rompen, lo hacen en silencio.
// Ver specs/001-sitio-base/data-model.md, seccion 2.

describe("el mapa de rutas", () => {
  it("da slug en los dos idiomas a toda seccion, y solo el inicio lo tiene vacio", () => {
    for (const ruta of rutas) {
      for (const idioma of IDIOMAS) {
        expect(ruta.slug[idioma], `${ruta.clave} no define slug en ${idioma}`).toBeTypeOf("string");
        if (ruta.clave !== "inicio") {
          expect(
            ruta.slug[idioma].length,
            `${ruta.clave} tiene el slug vacio en ${idioma}`,
          ).toBeGreaterThan(0);
        }
      }
    }
    expect(rutas.find((r) => r.clave === "inicio")?.slug.en).toBe("");
  });

  it("no repite un slug dentro del mismo idioma", () => {
    for (const idioma of IDIOMAS) {
      const vistos = rutas.map((r) => r.slug[idioma]);
      expect(new Set(vistos).size, `hay slugs repetidos en ${idioma}: ${vistos.join(", ")}`).toBe(
        vistos.length,
      );
    }
  });

  it("tiene etiqueta en los dos idiomas para toda seccion del menu", () => {
    for (const ruta of rutas.filter((r) => r.enNavegacion)) {
      for (const idioma of IDIOMAS) {
        const etiqueta = textos[idioma].secciones[ruta.clave];
        expect(etiqueta, `falta la etiqueta de ${ruta.clave} en ${idioma}`).toBeTruthy();
      }
    }
  });

  it("usa slugs limpios: minusculas, sin acentos y sin espacios", () => {
    for (const ruta of rutas) {
      for (const idioma of IDIOMAS) {
        expect(ruta.slug[idioma], `${ruta.clave} en ${idioma}`).toMatch(/^[a-z0-9\-/[\]]*$/);
      }
    }
  });
});

describe("rutaDe", () => {
  it("construye la direccion con su prefijo de idioma y barra final", () => {
    expect(rutaDe("experiencia", "en")).toBe("/en/experience/");
    expect(rutaDe("experiencia", "es")).toBe("/es/experiencia/");
  });

  it("deja el inicio como la raiz del idioma", () => {
    expect(rutaDe("inicio", "en")).toBe("/en/");
    expect(rutaDe("inicio", "es")).toBe("/es/");
  });

  it("traduce de verdad: la politica no se llama igual en los dos idiomas", () => {
    expect(rutaDe("politica", "en")).toBe("/en/data-policy/");
    expect(rutaDe("politica", "es")).toBe("/es/politica-de-datos/");
  });

  it("da la equivalente en el otro idioma, que es lo que usa el selector", () => {
    for (const ruta of rutas) {
      const otra: Idioma = "es";
      expect(rutaDe(ruta.clave, otra)).toContain("/es/");
    }
  });
});

describe("el indice para buscadores", () => {
  it("deja fuera las rutas de detalle, que no tienen contenido todavia", () => {
    const indexables = rutas.filter((r) => r.enIndice).map((r) => r.clave);
    expect(indexables).not.toContain("proyecto");
    expect(indexables).not.toContain("articulo");
  });

  it("lista doce direcciones: seis secciones por dos idiomas", () => {
    const indexables = rutas.filter((r) => r.enIndice);
    expect(indexables.length * IDIOMAS.length).toBe(12);
  });
});
