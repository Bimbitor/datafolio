# Feature Specification: Sitio base

**Feature Branch**: `001-sitio-base`

**Created**: 2026-11-05

**Status**: Draft

**Input**: Feature 1 de la división en `docs/historico/project-brief.md` §12. Alcance: prueba de despliegue conjunto, monorepo, enrutado bilingüe con slugs traducidos, archivo único de tokens, modo claro y oscuro, navegación por teclado, responsive, rutas estáticas contra renderizadas, tarea programada de salud, SEO y despliegue. Sin animaciones.

## Clarifications

### Session 2026-11-05

- Q: ¿El sitio debe ser visible para los buscadores desde el primer despliegue, aunque sus secciones todavía no tengan contenido real? → A: No. Se publica bloqueado a buscadores y el bloqueo se retira cuando el contenido real esté puesto, en la feature 02.
- Q: ¿Esta feature crea ya el proyecto de base de datos, aunque esté vacío, para que la comprobación diaria tenga algo que consultar? → A: Sí. Se crea vacío en esta feature y la comprobación lo consulta desde el primer despliegue; el esquema llega en la feature 03.
- Q: ¿Cómo se entera el titular de que la comprobación diaria falló, si el panel de administración no existe hasta la feature 03? → A: Por correo. La comprobación avisa al titular cuando falla, así que el canal de correo se configura en esta feature.
- Q: ¿Con qué método se comprueba que el sitio cumple los números de rendimiento del criterio de aceptación? → A: Con una auditoría de laboratorio sobre el sitio desplegado, perfil de móvil y red simulada, tomando la mediana de tres ejecuciones, antes de integrar a `main`.

## User Scenarios & Testing _(mandatory)_

### User Story 1 - El sitio y su API pueden convivir en un mismo despliegue (Priority: P1)

Antes de construir nada, el titular necesita saber que las páginas del portafolio y las funciones de servidor que más adelante atenderán el panel pueden desplegarse juntas y responder bajo el mismo dominio. De eso depende que la sesión del administrador funcione, porque su cookie solo viaja si ambas partes comparten origen.

**Why this priority**: Es la única incógnita que puede obligar a rehacer trabajo ya hecho. Si se descubre tarde, hay que reescribir la autenticación entera. Todo lo demás de esta feature se construye encima de la respuesta.

**Independent Test**: Se despliega un sitio mínimo con una sola página y un solo endpoint de servidor, y se comprueba desde un navegador que las dos direcciones responden bajo el mismo dominio.

**Acceptance Scenarios**:

1. **Given** un despliegue con una página y un endpoint de servidor, **When** se abre la página en el navegador, **Then** responde correctamente bajo el dominio del sitio.
2. **Given** ese mismo despliegue, **When** se solicita el endpoint de servidor, **Then** responde correctamente bajo **el mismo dominio**, sin redirección a otro host.
3. **Given** que las dos direcciones comparten origen, **When** el endpoint devuelve una cookie, **Then** el navegador la envía de vuelta en la siguiente petición a ese dominio.
4. **Given** que la convivencia no fuera posible, **When** se aplique la disposición alternativa prevista, **Then** el navegador sigue viendo un único origen para ambas partes.

---

### User Story 2 - Un visitante recorre el sitio publicado (Priority: P2)

Cualquier persona con el enlace abre el portafolio en internet y llega a cualquiera de sus secciones, en su propia dirección, desde cualquier dispositivo.

**Why this priority**: Es el esqueleto sobre el que se cuelga todo el contenido de las features siguientes, y es lo primero que convierte el proyecto en algo que se puede enseñar.

**Independent Test**: Se abre la dirección pública y se visita cada sección desde el menú, en móvil y en escritorio, comprobando que cada una tiene su propia dirección enlazable.

**Acceptance Scenarios**:

1. **Given** la dirección pública del sitio, **When** un visitante la abre, **Then** ve el inicio con una navegación que lleva a todas las secciones.
2. **Given** cualquier sección, **When** el visitante copia su dirección y la abre en otra pestaña, **Then** llega directamente a esa sección sin pasar por el inicio.
3. **Given** cualquier página, **When** el visitante quiere contactar, **Then** alcanza un canal de contacto en un solo clic.
4. **Given** una pantalla de móvil, de tableta o de escritorio, **When** se recorre el sitio, **Then** el contenido se lee sin desbordes horizontales y la navegación sigue siendo utilizable.
5. **Given** una dirección que no existe, **When** el visitante la abre, **Then** ve una página de error con salida hacia el inicio, en su idioma.

---

### User Story 3 - El visitante lee el sitio en su idioma (Priority: P3)

El sitio se presenta en inglés o en español según quién lo abra, y quien quiera cambiarlo puede hacerlo en cualquier momento. Las dos versiones son páginas reales con dirección propia, no una traducción que se aplica encima.

**Why this priority**: La audiencia principal es internacional y el inglés es el idioma por defecto, pero el titular trabaja en Colombia. Sin esto, la mitad de los visitantes lee en un idioma que no es el suyo. Además condiciona la forma de todas las direcciones del sitio, así que cambiarlo después sería rehacer el enrutado.

**Independent Test**: Se abre el sitio con el navegador configurado en español y luego en otro idioma, se comprueba el destino en cada caso, y se cambia de idioma manualmente verificando que la elección sobrevive a la navegación y a la recarga.

**Acceptance Scenarios**:

1. **Given** un navegador configurado en español, **When** el visitante abre la raíz del sitio, **Then** llega a la versión en español.
2. **Given** un navegador en cualquier otro idioma, **When** el visitante abre la raíz, **Then** llega a la versión en inglés.
3. **Given** cualquier página, **When** el visitante usa el selector de idioma, **Then** llega a la página equivalente en el otro idioma, no al inicio.
4. **Given** que el visitante eligió un idioma manualmente, **When** navega a otra sección o recarga, **Then** sigue en el idioma que eligió.
5. **Given** una página en un idioma, **When** un buscador la rastrea, **Then** encuentra declarada su equivalencia con la del otro idioma y cuál es la versión por defecto.
6. **Given** el sitio publicado, **When** se consulta su índice para buscadores, **Then** aparecen las direcciones de los dos idiomas.

---

### User Story 4 - El visitante elige cómo se ve el sitio (Priority: P4)

Quien entra ve el sitio en claro o en oscuro según lo que ya tenga configurado en su dispositivo, y puede cambiarlo con un botón siempre a mano.

**Why this priority**: Es una expectativa básica en 2026 y afecta a cómo se percibe el cuidado del sitio. Depende de que los colores estén centralizados, que es una decisión estructural: hacerlo después obligaría a revisar cada componente.

**Independent Test**: Se abre el sitio con el sistema en claro y luego en oscuro, se alterna con el botón, se recarga, y se comprueba que no hay destello del tema equivocado.

**Acceptance Scenarios**:

1. **Given** un dispositivo configurado en modo oscuro, **When** el visitante abre el sitio por primera vez, **Then** lo ve en oscuro.
2. **Given** cualquier página, **When** el visitante pulsa el botón de tema, **Then** el sitio cambia de tema al instante y el botón sigue disponible.
3. **Given** que el visitante cambió el tema, **When** vuelve más tarde o recarga, **Then** el sitio respeta su elección por encima de la del sistema.
4. **Given** una página que carga, **When** el tema guardado es el oscuro, **Then** no aparece ningún destello claro antes de pintarse.
5. **Given** cualquier combinación de tema y sección, **When** se comprueba el contraste del texto sobre su fondo, **Then** cumple las reglas de contraste definidas para la paleta.

---

### User Story 5 - El sitio se puede usar solo con el teclado (Priority: P5)

Alguien que no usa ratón —por costumbre, por discapacidad o porque está en un teclado sin él— puede recorrer y operar todo el sitio.

**Why this priority**: Es un compromiso explícito del proyecto y es mucho más barato construirlo desde el esqueleto que remendarlo componente por componente.

**Independent Test**: Se recorre el sitio entero usando solo el tabulador y la tecla de entrada, comprobando que se alcanza todo elemento interactivo y que siempre se ve dónde está el foco.

**Acceptance Scenarios**:

1. **Given** cualquier página, **When** el visitante avanza con el teclado, **Then** alcanza todos los elementos interactivos en un orden que sigue el orden visual.
2. **Given** cualquier elemento con foco, **When** se mira la pantalla, **Then** se distingue con claridad cuál es, en los dos temas.
3. **Given** el menú de navegación en móvil, **When** se abre con el teclado, **Then** se puede recorrer y cerrar sin ratón, y el foco no queda atrapado.
4. **Given** una imagen con contenido, **When** se consulta su texto alternativo, **Then** existe y describe la imagen en el idioma de la página.

---

### User Story 6 - El sitio se mantiene en pie sin vigilancia (Priority: P6)

El titular no tiene que acordarse de entrar al sitio para que siga funcionando. Una comprobación automática diaria se encarga.

**Why this priority**: Resuelve un fallo conocido y silencioso: el servicio de datos del plan gratuito se suspende tras una semana sin actividad, y un portafolio nuevo pasa semanas sin visitas. El fallo aparecería justo ante el primer visitante tras una pausa.

**Independent Test**: Se comprueba que la tarea queda registrada con ejecución diaria y que su última ejecución consta como correcta.

**Acceptance Scenarios**:

1. **Given** el sitio desplegado, **When** pasa un día, **Then** la comprobación programada se ha ejecutado y ha dejado constancia del resultado.
2. **Given** la comprobación, **When** se ejecuta, **Then** consulta el servicio de datos de forma que cuente como actividad.
3. **Given** siete días seguidos sin ninguna visita, **When** alguien abre el sitio al octavo, **Then** funciona con normalidad.
4. **Given** una comprobación fallida, **When** termina su ejecución, **Then** el titular recibe un aviso por correo que dice qué falló.
5. **Given** que el propio envío del aviso falla, **When** el titular revisa el registro de la plataforma, **Then** encuentra constancia del fallo original.

---

### Edge Cases

- **El visitante llega a una dirección sin prefijo de idioma** (por ejemplo, un enlace antiguo o escrito a mano): debe acabar en una página válida, no en un error.
- **El navegador no permite guardar preferencias** (modo privado restringido, almacenamiento bloqueado): el sitio debe funcionar igual, cayendo en el idioma por defecto y el tema del sistema, sin romperse ni mostrar errores.
- **El visitante tiene activada la preferencia de movimiento reducido**: como esta versión no lleva animaciones, no debe haber ninguna diferencia perceptible; la preferencia nunca debe degradar la usabilidad.
- **Una sección existe en un idioma y se pide en el otro**: en esta feature todas existen en ambos, pero el enrutado no debe dar un error genérico si alguna vez falta.
- **El dispositivo es muy estrecho o el texto está muy ampliado**: el contenido debe seguir leyéndose sin desbordes horizontales.
- **La comprobación programada falla varios días seguidos**: cada ejecución fallida avisa, y como corre una vez al día el aviso no se convierte en una avalancha.
- **El aviso de fallo no se puede enviar** (credenciales caducadas, proveedor de correo caído): el fallo original debe quedar igualmente registrado en la plataforma, para que no desaparezca en silencio.
- **El visitante abre una dirección de la zona de administración**, que todavía no existe: debe recibir la página de error, y esa zona no debe aparecer en los buscadores.

## Requirements _(mandatory)_

### Functional Requirements

**Despliegue y estructura**

- **FR-001**: El sitio y sus funciones de servidor MUST responder bajo un mismo dominio, de modo que el navegador los trate como un solo origen.
- **FR-002**: El proyecto MUST alojar en un único repositorio tanto el sitio como sus funciones de servidor, en carpetas separadas.
- **FR-003**: El sitio MUST estar publicado y accesible en internet al cerrar esta feature.
- **FR-004**: El coste de ejecución MUST ser cero: todo opera dentro de los planes gratuitos ya elegidos.

**Secciones y navegación**

- **FR-005**: El sitio MUST ofrecer nueve secciones con dirección propia: inicio, experiencia, proyectos, detalle de proyecto, blog, artículo, contacto, política de datos y una página de error.
- **FR-006**: Cada sección MUST ser alcanzable directamente por su dirección, sin pasar por el inicio.
- **FR-007**: Una navegación persistente MUST dar acceso a todas las secciones desde cualquier página.
- **FR-008**: Un canal de contacto MUST estar alcanzable en un clic desde cualquier página.
- **FR-009**: Las secciones cuyo contenido llega en features posteriores MUST mostrar su estructura y una indicación visible de que su contenido está pendiente, sin texto de relleno que simule contenido real.

**Idioma**

- **FR-010**: El sitio MUST existir en inglés y en español, cada idioma con direcciones propias y distinguibles.
- **FR-011**: Las direcciones de cada sección MUST estar traducidas al idioma al que pertenecen.
- **FR-012**: La raíz del sitio MUST llevar al idioma detectado en el navegador del visitante, con el inglés como destino cuando no se pueda determinar o no sea español.
- **FR-013**: Un selector de idioma MUST estar visible y MUST llevar a la página equivalente en el otro idioma, no al inicio.
- **FR-014**: La elección manual de idioma MUST persistir entre páginas y entre visitas, y MUST prevalecer sobre la detección.
- **FR-015**: Cada página MUST declarar a los buscadores su dirección canónica, su equivalencia con la del otro idioma y cuál es la versión por defecto.
- **FR-016**: El sitio MUST publicar un índice de sus direcciones para buscadores, incluyendo los dos idiomas, y MUST excluir de la indexación la zona de administración.

**Apariencia**

- **FR-017**: Todos los valores de color, tipografía, espaciado, radios y sombras MUST provenir de un único archivo de definiciones; ningún componente MUST escribir uno de esos valores directamente.
- **FR-018**: Cambiar un valor en ese archivo MUST cambiar el sitio completo sin modificar ningún componente.
- **FR-019**: El sitio MUST ofrecer modo claro y oscuro, tomando por defecto la preferencia del dispositivo.
- **FR-020**: Un botón flotante en la esquina inferior derecha MUST permitir alternar el tema desde cualquier página.
- **FR-021**: La elección de tema MUST persistir y MUST aplicarse antes del primer pintado, sin destello del tema contrario.
- **FR-022**: El sitio MUST ser utilizable y legible en móvil, tableta y escritorio, sin desbordes horizontales.
- **FR-023**: El sitio NO MUST incluir animaciones. Los cambios de estado MUST ser inmediatos o con transiciones de 150 ms como máximo.

**Accesibilidad**

- **FR-024**: Todo elemento interactivo MUST ser alcanzable y operable con el teclado, en un orden coherente con el orden visual.
- **FR-025**: El elemento con foco MUST ser visualmente identificable en los dos temas.
- **FR-026**: Toda imagen con contenido MUST tener texto alternativo en el idioma de la página; las decorativas MUST marcarse para que un lector de pantalla las omita.
- **FR-027**: El contraste de texto y de bordes de control MUST cumplir las reglas definidas para la paleta en los dos temas.

**Comportamiento de entrega**

- **FR-028**: Las secciones cuyo contenido vive en el código MUST servirse de forma estática; las que dependerán de datos administrables MUST renderizarse en servidor con caché; la zona de administración y las funciones de servidor MUST responder sin caché.
- **FR-029**: El servicio de datos MUST quedar creado en esta feature, sin esquema ni contenido, con sus credenciales disponibles para las funciones de servidor.
- **FR-030**: Una comprobación programada MUST ejecutarse a diario, consultar ese servicio de datos de forma que cuente como actividad, y dejar constancia de su resultado.
- **FR-031**: Cuando la comprobación falle, el titular MUST recibir un aviso por correo en su dirección de administración, indicando qué falló. El envío de correo desde el servidor MUST quedar configurado y verificado en esta feature.
- **FR-032**: Las credenciales del envío de correo MUST vivir únicamente en variables de entorno de la plataforma, nunca en el repositorio.

**Indexación**

- **FR-033**: Mientras alguna sección muestre la indicación de contenido pendiente de FR-009, el sitio completo MUST declararse no indexable para los buscadores. El índice de direcciones de FR-015 y FR-016 se construye y publica igual en esta feature; el bloqueo se retira en la feature 02, al publicarse el contenido real.

**Degradación**

- **FR-034**: Si el navegador no permite guardar preferencias, el sitio MUST seguir funcionando con el idioma por defecto y el tema del sistema, sin errores visibles.
- **FR-035**: Una dirección inexistente MUST llevar a la página de error en el idioma del visitante, con salida hacia el inicio.

## Success Criteria _(mandatory)_

### Measurable Outcomes

- **SC-001**: Las dieciocho direcciones públicas —nueve secciones en dos idiomas— responden correctamente al abrirlas directamente.
- **SC-002**: Desde cualquier página, un visitante alcanza cualquier otra sección en un clic, y un canal de contacto en un clic.
- **SC-003**: Medido con una auditoría de laboratorio sobre el sitio desplegado, con perfil de móvil de gama media y red móvil simulada, tomando la mediana de tres ejecuciones: el contenido principal de la página de inicio aparece en menos de 2,5 segundos y el desplazamiento involuntario de la página mientras carga se mantiene por debajo de 0,1.
- **SC-004**: En la misma auditoría, cada página pública se carga con menos de 100 KB de código ejecutable en el navegador, comprimido tal como lo sirve la plataforma.
- **SC-005**: Un visitante con el navegador en español llega a la versión en español y uno con el navegador en cualquier otro idioma llega a la inglesa, en el 100 % de los casos.
- **SC-006**: Cambiar de idioma desde cualquier sección conserva la sección; nunca devuelve al inicio.
- **SC-007**: La elección de tema y de idioma sobrevive a la navegación y a la recarga, y no se percibe ningún destello del tema contrario al cargar.
- **SC-008**: Modificar los valores del archivo de definiciones visuales cambia el aspecto de todas las secciones sin editar ningún componente, verificable en una sola prueba.
- **SC-009**: El sitio completo se recorre y se opera usando solo el teclado, sin que el foco quede atrapado ni se pierda de vista en ningún punto, en los dos temas.
- **SC-010**: El sitio permanece operativo tras siete días consecutivos sin visitas.
- **SC-011**: El sitio está publicado y el coste mensual de operarlo es cero.
- **SC-012**: Una comprobación fallida provoca un aviso por correo al titular en la misma ejecución, verificable provocando un fallo a propósito.
- **SC-013**: Mientras las secciones muestren la indicación de contenido pendiente, ninguna página del sitio se declara indexable, y el índice de direcciones existe y es válido desde el primer despliegue.

## Assumptions

- **La pila tecnológica no se decide aquí**: está fijada en `docs/historico/project-brief.md` §7 y en la constitución. Esta especificación describe qué debe lograrse; el cómo corresponde al plan.
- **El contenido real llega en la feature 02.** Esta feature entrega la estructura; las secciones muestran su armazón y una indicación de que el contenido está pendiente, nunca texto de relleno que parezca real.
- **Los valores visuales ya están decididos** en `docs/design-tokens.md`. Esta feature los implementa en un único archivo; la composición y el ritmo visual corresponden a la feature 07.
- **El sitio vive en el subdominio gratuito de la plataforma de despliegue.** No hay dominio propio y no está planeado.
- **El rendimiento se verifica en laboratorio, no con visitantes.** Todavía no hay tráfico del que sacar datos reales, y medir en el navegador del visitante chocaría con el principio de no guardar nada suyo y gastaría parte del propio presupuesto de JavaScript. La auditoría es la puerta antes de integrar a `main`.
- **Hay un único entorno de datos.** No existe base de pruebas: la verificación se hace sobre el sitio desplegado, y lo que se cree al probar se elimina.
- **El correo sale de una cuenta gratuita del titular**, con una contraseña de aplicación guardada como variable de entorno en la plataforma. La dirección de administración que recibe los avisos no es la dirección pública de contacto.
- **La comprobación programada se ejecuta una vez al día**, que es lo que permite el plan gratuito y sobra frente al umbral de suspensión de una semana.
- **Se asume que la convivencia del sitio y las funciones de servidor en un mismo despliegue es posible.** La historia P1 existe precisamente para confirmarlo antes de construir encima; si no lo fuera, se aplica la disposición alternativa ya prevista en `docs/viabilidad-tecnica.md`, que conserva el origen único.
- **El servicio de datos se crea aquí, vacío.** No tiene esquema ni contenido: el esquema llega en la feature 03. Se crea ahora porque el plazo de suspensión del plan gratuito empieza a contar desde que el proyecto existe, y porque así las credenciales y la tarea programada se verifican en el mismo despliegue de prueba de la historia P1.
