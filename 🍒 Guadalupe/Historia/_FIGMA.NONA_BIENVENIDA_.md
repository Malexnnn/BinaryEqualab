
Título del archivo en Figma: Nona 🍒 — Welcome Animation (Web Minimalista)

Objetivo corto:
Crear una intro animada minimalista y poética: un sol que “cede” su brillo a un par de cerezas; las cerezas caen, rebotan y revelan el texto de bienvenida. Exportable como SVG + CSS/JS (web) y con opción a Lottie. Accesible (reduced-motion).

Canvas: 720 × 480 px (hero web).


---

Assets obligatorios (crear como componentes)

BG_Aurora — Rect 720×480, gradiente (top #1F1B24 → bottom #3C2C42).

Sol_Component

Sol_Circle (circle r=44, fill #FF6B35).

Sol_Rayo_# (8 rects 28×7 rx=3) agrupados en Sol_Rayos.


Cerezas_Component

Cereza_Left (circle r=14 fill #E63946, highlight ellipse #FFD3B6 op 45%).

Cereza_Right (igual).

Stem (path stroke #6C2D5A w=2). Agrupar todo en Cerezas_Grupo.


Floor_Invisible — guía Y = 380 px (no visible en export, sirve para posición de impacto).

Texto_Bienvenida — Inter Medium 20px, color #FAF8F6. Copia: Cada día, cada vez, podemos hacer algo mucho mejor.


Nomenclatura de capas (exacta):
BG_Aurora, Sol_Component/Sol_Circle, Sol_Component/Sol_Rayos, Cerezas_Grupo/Cereza_Left, Cerezas_Grupo/Cereza_Right, Floor_Invisible, Texto_Bienvenida.


---

Timeline detallado (números exactos — pega tal cual)

Duración total sugerida: 0.0s → 5.0s (la parte visual principal: 0–4.0s; transición 4.0–5.0s).

Frame 1 — El Sol Radiante (0.000s → 1.000s)

Acción: sol “vivo” que pulsa y emite aura.

Animaciones:

scale del grupo Sol_Component: 1 → 1.05 → 1. Duración: 1000ms. Easing: ease-in-out.

outer-glow (animar opacidad 0.0 → 0.4 → 0.0) radio 18–22 px sincronizado con el scale.



Frame 2 — El Sacrificio del Sol (1.000s → 1.500s)

Acción clave: sol se apaga; del centro nacen las cerezas.

Animaciones:

Sol_Component color/opacity: fill #FF6B35 → #CC5A28 y opacity 1 → 0.32. Duración: 500ms, easing ease-out.

Cerezas_Grupo aparece con scale 0 → 1 en 300ms (start = 1.05s, end = 1.35s), easing back-out ligero.

Al aparecer, Cerezas_Grupo aplica aura temporal (fill overlay #FF6B35 op 0.5 → 0) por 500ms para indicar que “heredaron brillo”.



Frame 3 — La Caída Brillante (1.500s → 2.500s)

Acción: las cerezas caen desde posición del sol hasta Y ≈ 380 px.

Animaciones:

translateY para cada cereza: Y_start = sol_center_y (≈170) → Y_end = 380.

Curva: cubic-bezier(0.25, 0.46, 0.45, 0.94) (sensación natural de gravedad).

Duración por caída: 1000ms por cereza; Cereza_Right inicia con delay 80ms para ligera separación.

Trail: añadir una máscara o shape con opacity 40% → 0 a lo largo de la trayectoria (250–600ms después del inicio) — sutil, como una estela.



Frame 4 — El Rebote y la Bienvenida (2.500s → 4.000s)

Acción: impacto + rebotes (spring) + texto.

Animaciones:

Impacto en Floor_Invisible (Y=380).

Rebotes secuenciales (usar física tipo spring):

bounce 1: offset -40 px, duración 260ms (overshoot 1.08), damping: 0.6.

bounce 2: offset -18 px, duración 200ms (damping 0.7).

bounce 3: offset -6 px, duración 160ms (damping 0.85).


Al primer rebote: aplicar un compress/strecth sutil en cada cereza (scaleY 0.88 → 1) para sensación orgánica.

Partícula/spark: un círculo pequeño #FFD3B6 aparece (scale 0→1, opacity 0→1→0) en el punto de impacto, duración 220–300ms.

Texto (Texto_Bienvenida) aparece 200ms después del último rebote con fade-in + slide-up (opacity 0→1, translateY 12px → 0). Duración: 600ms, easing ease-out.



Frame 5 — Transición (4.000s → 5.000s)

Acción: fade-out y redirección a Login.

Animación:

opacity de todo el canvas 100% → 0% en 1000ms.

Trigger: al finalizar fade-out, cambiar a pantalla Login.




---

Easing / Physics recomendados (copiar directo)

Pulsos / entradas: ease-in-out

Caída: cubic-bezier(0.25,0.46,0.45,0.94)

Rebote (spring): tension ~ 300, friction ~ 22 (o damping 0.6 en motores que lo soporten)

Aparición de texto: ease-out (0.22, 1, 0.36, 1)



---

Entregables y exportación (qué esperamos del agente)

1. Figma file con frames: Welcome_anim (animado) + Welcome_static (static fallback).


2. JSON Figmotion (si se usa Figmotion) o Lottie JSON (si se exporta vía LottieFiles).


3. SVG exportable con keyframes/CSS mapping (si se quiere extraer a web).


4. Guía pequeña (README en canvas) con: instrucciones de integración (IDs de layers, coordenadas Y, easing, reduced-motion flag).


5. Variants: animated / reduced-motion / static.




---

Accesibilidad & Calidad (no negociable)

Implementar variant reduced-motion (frame estático con sol atenuado + cerezas ya en piso + texto visible). Respetar prefers-reduced-motion.

Incluir botón "Saltar animación" en top-right (visible en prototipo).

Asegurar contraste de texto (WCAG AA) sobre BG_Aurora.

Añadir aria-label descriptivo: "Animación de bienvenida: sol y cerezas — Nona".



---

Plugins / workflow recomendado (para el agente)

Web minimal: Figmotion → export SVG + Figmotion JSON + CSS keyframes.

Opcional Lottie: diseñar vectores y exportar a AE con AEUX → After Effects (animar partículas/glow si hace falta) → Bodymovin (Lottie JSON).

Naming y estructura: respetar exactamente la nomenclatura de capas provista arriba.



---

Checklist para revisar antes de cerrar (marca cada punto)

[ ] Fondo BG_Aurora con gradiente correcto.

[ ] Sol_Component con rayos y glow.

[ ] Cerezas_Grupo como componente emergente.

[ ] Animaciones con timing exacto y easing especificado.

[ ] Trail/estela sutil durante la caída.

[ ] Rebote con physics spring y squash/stretch.

[ ] Spark particles en impacto.

[ ] Texto aparece con delay y fade-in.

[ ] Variant reduced-motion y botón Skip.

[ ] Export: SVG, Figmotion JSON, notas README.

