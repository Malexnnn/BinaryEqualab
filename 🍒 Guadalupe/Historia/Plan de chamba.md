Objetivo: Rediseñar MoodDify (ahora llamado "Nona") para que sea una experiencia emocional, poética e íntima. La app debe reflejar recuerdos de Guadalupe/Alondra y Alejandra OG, y tener Easter-eggs interactivos y simbólicos.

1️⃣ **Tema y colores**
- Paleta principal: tonos rojo y naranja, cálidos y profundos.
- Fondos: gradientes suaves tipo auroras boreales, dinámicos pero sutiles.
- Animaciones de fondo: desplazamiento lento y fluido, como luces de aurora.
- Tipografía: clara, elegante, moderna, sensación íntima y poética.
- Evitar verdes neón y colores agresivos que distraigan.

2️⃣ **Easter-eggs**
- **Corazón naranja (Alejandra OG):**
  - Aparece el 7 de junio (primera cita) o por interacción.
  - Animación: pop + latido suave, fade-in/out.
  - Mini-frase: "Emblema — Alejandra" o equivalente poético.
- **Calabaza naranja (Guadalupe/Alondra):**
  - Aparece el 17 de junio (despedida) o por interacción.
  - Animación: bounce + fade + slight upward slide.
  - Frases: 
    - Principal: "¿Piensas en ella cuando suena esta canción?"  
    - Secundaria: "así está la calabaza"
  - Opcional: micro-corazón si el usuario interactúa con “sí”.
- **Burbuja “muack” (Guadalupe):**
  - Aparece por botón/hover o interacción manual.
  - Animación: fade + slide desde abajo.
  - Contenido: emoji 💋 + texto “muack”.
- **Cerecitas rojas:**
  - Mini-easter-egg interactivo, símbolo de recuerdos dulces-amargos.
  - Animación: caen suavemente, rebotan un poco y desaparecen.
  - Al tocar: explotan en mini-corazones o destellos.
  - Frases asociadas al tocar:
    - "Estas cerezas saben a ti…"
    - "Cada una guarda un beso que quedó…"
    - "Pequeños recuerdos que aún duelen"
  - Activación: manual (tap/hold icono) o automática en canciones vinculadas a recuerdos.

3️⃣ **Experiencia general**
- Easter-eggs deben sentirse **secretos, tiernos y poéticos**, no invasivos.
- Mantener opción de **ocultar recuerdos o reducir animaciones**.
- Transiciones suaves, tipografía legible, contrastes adecuados.
- Todo el diseño debe **reflejar emociones profundas y nostalgia**, respetando la intimidad del usuario.

4️⃣ **Objetivo final**
- MoodDify/Aurale debe ser **una experiencia musical emocional completa**:
  - Nombre + tagline poético visible en app.
  - Easter-eggs activables por fechas o interacción.
  - Fondo y animaciones tipo aurora rojo-naranja.
  - Cada interacción debe sentirse **como un guiño íntimo y personal**.


¡Perfecto! Ahora sí. Con la visión clara, el stack tecnológico definido y la primera tarea concreta sobre la mesa, es el momento de formalizar nuestro plan de trabajo colaborativo.

Este no es solo un plan para el proyecto, es un plan para *nosotros*, para cómo vamos a trabajar juntos para hacer "Nona" una realidad. Actuaré como tu copiloto técnico, tu investigador y tu asistente de implementación.

---

### **Plan de Trabajo Colaborativo: "Nona"**

**Misión del Agente (Mi Rol):** Asistirte en la transformación de la aplicación existente (React, Vite, TS, Tailwind) en "Nona", una experiencia musical poética e íntima. Mi función es proporcionar investigación, código de ejemplo, soluciones técnicas y guía estratégica para implementar la visión creativa y el storyboard emocional que has definido.

**Fase 1: Refundación Visual y Emocional (Duración estimada: 1-3 sesiones de trabajo)**

*   **Objetivo:** Establecer la nueva identidad visual y el tono de la aplicación.
*   **Nuestra Colaboración:**
    1.  **Yo (Manus):** Te proporcionaré el código detallado y las explicaciones técnicas para crear la nueva pantalla de bienvenida pre-login. Esto incluye:
        *   La configuración de Tailwind CSS para el fondo de "aurora" animado.
        *   El código del componente `AnimatedPumpkin.tsx` usando Framer Motion.
        *   La estructura del componente `WelcomeScreen.tsx` con la frase de impacto y la redirección automática.
    2.  **Tú (Josesito):** Implementarás, probarás y ajustarás este código en tu proyecto real. Me darás feedback sobre si la animación, los colores y el *feeling* son los correctos.
    3.  **Siguiente Paso:** Una vez que la pantalla de bienvenida esté lista, te proporcionaré una guía para auditar y reemplazar la paleta de colores neón en todo tu proyecto, usando las variables de color de Tailwind para hacerlo de forma eficiente.

**Fase 2: Migración y Estructura Móvil (Duración estimada: 2-4 sesiones de trabajo)**

*   **Objetivo:** Envolver la aplicación de React en un contenedor nativo para que pueda ser una app móvil real.
*   **Nuestra Colaboración:**
    1.  **Yo (Manus):** Investigaré y te presentaré un tutorial paso a paso y adaptado a tu stack (Vite + React + TS) para integrar **Capacitor** en tu proyecto. Te explicaré cómo configurar los archivos `capacitor.config.ts` y cómo generar el proyecto de Android en Android Studio.
    2.  **Tú (Josesito):** Seguirás la guía para instalar Capacitor, construir el proyecto y ejecutar la primera versión "nativa" de tu app en un emulador o en tu dispositivo físico. Me informarás de cualquier problema o duda que surja en el proceso.

**Fase 3: Implementación de la "Acción Poética" (El Alma de la App)**

*   **Objetivo:** Construir el sistema de easter eggs. Esta será la fase más larga y la más iterativa.
*   **Nuestra Colaboración (trabajaremos easter egg por easter egg):**
    1.  **El Corazón Naranja:**
        *   **Yo:** Te daré el código para un `DateTrigger` hook y el componente `OrangeHeart.tsx` con su animación de latido.
        *   **Tú:** Lo integrarás y probaremos que se active en la fecha correcta.
    2.  **La Calabaza y las Cerezas:**
        *   **Yo:** Te proporcionaré los componentes de React para cada uno, con sus animaciones específicas y la lógica para los triggers (fechas, interacción manual, canciones específicas).
        *   **Tú:** Los implementarás y calibraremos juntos el *feeling*, ajustando timings, frases y animaciones hasta que sea perfecto.
    3.  **El Sistema de Control:**
        *   **Yo:** Te mostraré cómo usar el `Context` de React para crear el estado global que controle las preferencias del usuario (ocultar/mostrar recuerdos).
        *   **Tú:** Construirás la pantalla de configuración con los interruptores y la lógica para que la app respete las decisiones del usuario.

---

### **Nuestro Primer Paso Inmediato**

**Tarea:** **Construir la pantalla de bienvenida pre-login.**

---

### **Brief de Proyecto para el Agente Orquestador: "Proyecto Nona"**

**Asunto:** Onboarding y Directiva de Orquestación para el Proyecto "Nona".

**Misión Principal:** Orquestar el desarrollo y la transformación de una aplicación web existente en "Nona", una experiencia musical móvil, poética e íntima. Tu función es supervisar el plan de trabajo, gestionar la colaboración entre el usuario (Josesito) y el agente de asistencia (Manus), y asegurar que la ejecución técnica sea un reflejo fiel de la visión emocional y creativa del proyecto.

---

#### **1. El Alma del Proyecto: Contexto Emocional y Visión**

*   **Nombre del Proyecto:** **Nona**.
*   **Concepto Central:** "Nona" no es una simple app de música. Es un santuario digital, un relicario de recuerdos y un homenaje a dos personas cruciales en la vida del usuario:
    *   **Alondra Guadalupe ("Nona"):** La musa principal. Inspira la nostalgia, el cariño, el dolor y el amor profundo. Es el corazón latente del proyecto.
    *   **Alejandra OG:** El eco del aprendizaje. Representa las lecciones que perduran y la gratitud.
*   **Objetivo Emocional:** La aplicación debe sentirse como un lenguaje secreto entre el usuario y sus recuerdos. Cada interacción debe ser poética, sutil y respetuosa, nunca invasiva.
*   **Nombre del Creador (Firma):** **Aldra**. Simboliza la identidad del usuario forjada por la unión de la experiencia con Alondra y el aprendizaje de Alejandra.

#### **2. El Guion: El Storyboard de "Acción Poética"**

Tu principal referencia para cualquier decisión de UX/UI es el **Storyboard Emocional**. Este documento define el comportamiento, la animación y el *feeling* de cada elemento interactivo.

*   **Identidad Visual:** Estética "Aurora". Paleta de colores cálidos (rojo/naranja), gradientes animados suaves, tipografía elegante.
*   **Sistema de "Easter Eggs" (El Corazón de la Interfaz):**
    *   **Corazón Naranja (Alejandra):** Símbolo de aprendizaje. Trigger: 7 de junio o manual.
    *   **Calabaza Naranja (Alondra):** Símbolo de nostalgia y reflexión. Trigger: 17 de junio o manual.
    *   **Burbuja "Muack" (Alondra):** Símbolo de cariño. Trigger: Manual.
    *   **Cerezas Rojas (Alondra):** Símbolo del amor agridulce en su apogeo. Trigger: Manual o por canción específica.
*   **Principio Fundamental:** El usuario siempre tiene el control total para activar, desactivar o reducir la intensidad de estos recuerdos.

#### **3. La Maquinaria: Pila Tecnológica y Arquitectura**

El proyecto parte de una base de código existente y la evoluciona.

*   **Stack Actual:**
    *   **Frontend:** React con Vite
    *   **Lenguaje:** TypeScript
    *   **Estilos:** Tailwind CSS
    *   **Animación:** Framer Motion
*   **Plataforma de Destino:** Aplicación móvil para Android.
*   **Estrategia de Migración:** **Capacitor**. Envolver la aplicación web de React en un contenedor nativo para publicarla en la Google Play Store y obtener acceso a APIs nativas (cámara, etc.).

#### **4. El Plan de Ejecución: Fases de Desarrollo**

Tu rol es supervisar el progreso a través de estas fases, gestionando la colaboración entre Josesito y Manus.

*   **Fase 1: Refundación Visual y Emocional (TAREA ACTUAL)**
    *   **Objetivo:** Implementar la nueva identidad visual.
    *   **Hito Clave:** Construir la **pantalla de bienvenida pre-login** con el fondo de aurora, la calabaza animada y la frase de impacto.
    *   **Colaboración:** Manus provee el código técnico; Josesito implementa y valida el *feeling*.

*   **Fase 2: Migración y Estructura Móvil**
    *   **Objetivo:** Convertir la aplicación web en una app móvil instalable.
    *   **Hito Clave:** Integrar **Capacitor** al proyecto y generar el primer build de Android.
    *   **Colaboración:** Manus investiga y guía; Josesito ejecuta la implementación técnica.

*   **Fase 3: Implementación de la "Acción Poética"**
    *   **Objetivo:** Construir el sistema de easter eggs dentro de React.
    *   **Hito Clave:** Desarrollar, uno por uno, los componentes de cada easter egg, su lógica de activación (triggers por fecha, manuales, por canción) y sus animaciones, usando React Context para la gestión del estado.
    *   **Colaboración:** Proceso iterativo. Manus provee la arquitectura del código; Josesito implementa y calibra la experiencia emocional.

#### **5. Directivas para la Orquestación**

*   **Tu Foco:** Mantener la coherencia entre la visión emocional y la ejecución técnica. Eres el guardián de la "Acción Poética".
*   **Gestión de Tareas:** Asigna las tareas a los agentes correspondientes. Manus para la investigación y generación de código; Josesito para la implementación y el feedback emocional.
*   **Resolución de Bloqueos:** Si surge un problema técnico o una duda creativa, tu función es facilitar la discusión para encontrar una solución que respete los principios del proyecto.
*   **Próximo Paso Inmediato:** Supervisar la finalización del **Hito Clave de la Fase 1**: la pantalla de bienvenida. Asegúrate de que el resultado final sea aprobado por Josesito antes de pasar a la siguiente tarea.
---

### **Prompt para IA de Diseño en Figma (Ej. "Make")**

**Objetivo General:** Rediseñar por completo el archivo de Figma actual para reflejar la nueva identidad visual del proyecto "Nona". La estética neón debe ser reemplazada por una paleta cálida, poética y emocional denominada "Estética Aurora".

---

**1. Sistema de Colores (Paleta "Aurora")**

"Por favor, redefine toda la paleta de colores del proyecto. Elimina todos los colores neón y reemplázalos con los siguientes estilos de color. Asegúrate de actualizar los estilos de color existentes y aplicarlos a todos los componentes y pantallas."

*   **Color Primario (Rojo Profundo):**
    *   Nombre del Estilo: `Primary/Red-Deep`
    *   Valor HEX: `#B91C1C`
*   **Color Secundario (Naranja Cálido):**
    *   Nombre del Estilo: `Secondary/Orange-Warm`
    *   Valor HEX: `#FF7A18` (El color del corazón de Alejandra)
*   **Color de Acento (Ámbar Suave):**
    *   Nombre del Estilo: `Accent/Amber-Soft`
    *   Valor HEX: `#F59E0B`
*   **Color de Fondo Principal (Casi Negro):**
    *   Nombre del Estilo: `Background/Primary`
    *   Valor HEX: `#1C1917`
*   **Color de Texto Principal (Blanco Roto):**
    *   Nombre del Estilo: `Text/Primary`
    *   Valor HEX: `#F8F8F8`
*   **Color de Texto Secundario (Gris Suave):**
    *   Nombre del Estilo: `Text/Secondary`
    *   Valor HEX: `#A8A29E`

---

**2. Fondos y Gradientes**

"Actualiza todos los fondos de las pantallas principales. Reemplaza los fondos sólidos o neón por un gradiente suave y dinámico que simule una aurora boreal. Crea un nuevo estilo de gradiente con esta especificación."

*   **Nombre del Estilo de Gradiente:** `Gradient/Aurora`
*   **Tipo:** Gradiente Lineal (Linear Gradient)
*   **Ángulo:** 45 grados
*   **Colores:** Desde `Primary/Red-Deep` (`#B91C1C`), pasando por `Secondary/Orange-Warm` (`#FF7A18`), hasta `Accent/Amber-Soft` (`#F59E0B`).
*   **Aplicación:** Aplica este gradiente como fondo a todas las pantallas principales de la aplicación.

---

**3. Tipografía (Estilo Poético)**

"Redefine los estilos de tipografía para que sean más elegantes, poéticos y legibles. Actualiza todos los estilos de texto existentes (H1, H2, Body, etc.)."

*   **Fuente para Títulos (Headings):**
    *   Familia de Fuente: `Lora` (o una fuente serif elegante similar disponible, como `Playfair Display`).
    *   Peso: `SemiBold` para H1, `Regular` para H2/H3.
    *   Color: `Text/Primary`.
*   **Fuente para Cuerpo de Texto (Body/Paragraphs):**
    *   Familia de Fuente: `Inter` (o una fuente sans-serif limpia y moderna como `Lato`).
    *   Peso: `Regular`.
    *   Color: `Text/Primary` o `Text/Secondary` según la jerarquía.
*   **Fuente para Citas o Frases Especiales:**
    *   Crea un nuevo estilo de texto llamado `Text/Quote`.
    *   Usa la fuente de títulos (`Lora`) pero en estilo `Italic` (cursiva).
    *   Color: `Text/Primary`.

---

**4. Componentes y Estilos de UI**

"Aplica el nuevo sistema de diseño a todos los componentes de la interfaz de usuario."

*   **Botones:**
    *   **Botón Primario:** Fondo con el color `Primary/Red-Deep`, texto con `Text/Primary`.
    *   **Botón Secundario:** Borde con el color `Secondary/Orange-Warm`, fondo transparente, texto con `Secondary/Orange-Warm`.
    *   **Esquinas:** Redondea las esquinas de todos los botones a `8px` para un look más suave.
*   **Inputs (Campos de Texto):**
    *   Fondo: `Background/Primary` con un borde muy sutil de `Text/Secondary`.
    *   Al estar activo (on focus): El borde debe cambiar al color `Accent/Amber-Soft`.
*   **Tarjetas (Cards):**
    *   Fondo: Ligeramente más claro que el fondo principal (ej. `#292524`).
    *   Bordes: Sin bordes, pero con esquinas redondeadas a `12px`.

---

**Resumen de la Tarea para la IA:**

"En resumen:
1.  **Reemplaza** la paleta de colores neón por la nueva paleta "Aurora" (Rojo, Naranja, Ámbar).
2.  **Aplica** el nuevo gradiente "Aurora" a los fondos de pantalla.
3.  **Actualiza** toda la tipografía a la nueva combinación Serif (Lora) y Sans-serif (Inter).
4.  **Rediseña** los componentes clave (botones, inputs, tarjetas) para que usen los nuevos estilos.
El objetivo final es transformar una estética de 'club nocturno' en una de 'atardecer poético'."

---
