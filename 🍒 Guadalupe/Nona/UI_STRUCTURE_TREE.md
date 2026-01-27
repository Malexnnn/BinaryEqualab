# 🎨 Estructura Visual de Nona - Árbol de Componentes

## Guía de Lectura
- 📦 **Carpetas**: Estructura de directorios
- 🎨 **Componentes**: Elementos visuales React
- 🎭 **Contextos**: Gestión de estado global
- 🎯 **Servicios**: Lógica y datos
- 🎪 **Páginas**: Pantallas completamente renderizadas

---

## 📊 Jerarquía Visual Completa

```
NONA (Aplicación Root)
│
└─ 🎯 PROVEEDOR DE DISEÑO (Cherry Provider)
   │
   ├─ 🎨 SISTEMA DE COLORES (Aurora Palette)
   │  ├─ Rojos: #B91C1C (oscuro), #DC2626, #EF4444 (gradientes)
   │  ├─ Naranjas: #FF7A18, #FF8C42 (cálidos)
   │  ├─ Ámbar: #F59E0B, #FBBF24 (suave)
   │  ├─ Fondos: #1C1917 (muy oscuro), #27201B (oscuro)
   │  └─ Textos: #F8F8F8 (blanco), #A8A29E (gris)
   │
   ├─ 🔐 AUTENTICACIÓN
   │  ├─ 📄 Login Page (`auth/login-page.tsx`)
   │  │  ├─ Sun Animation (Bienvenida Nona)
   │  │  ├─ Spotify Login Button
   │  │  │  └─ onClick → OAuth flow → window.location.href = spotifyAuthUrl
   │  │  └─ Google Login Button (fallback)
   │  │
   │  └─ 📄 Callback Page (`auth/callback-page.tsx`)
   │     ├─ Loading State → "Conectando..."
   │     ├─ Session Detection (3 retries + sessionStorage fallback)
   │     ├─ Error Handling → Mostrar mensaje de error
   │     └─ Success → Redirigir a `/dashboard`
   │
   └─ 📦 PROVEEDOR DE AUTENTICACIÓN (AuthProvider)
      │
      ├─ 🔓 APLICACIÓN AUTENTICADA
      │  │
      │  ├─ 📦 PROVEEDOR EASTER EGGS
      │  │  │
      │  │  ├─ 📦 PROVEEDOR DIARIO
      │  │  │  │
      │  │  │  ├─ 📦 PROVEEDOR CHAT
      │  │  │  │  │
      │  │  │  │  ├─ 🎪 DASHBOARD PRINCIPAL (`app/main-app.tsx`)
      │  │  │  │  │  │
      │  │  │  │  │  ├─ 📐 LAYOUT: SIDEBAR + CONTENT
      │  │  │  │  │  │
      │  │  │  │  │  ├─ 🔷 SIDEBAR IZQUIERDO (`sidebar.tsx`)
      │  │  │  │  │  │  ├─ Logo Nona 🍒
      │  │  │  │  │  │  ├─ Navigation Items:
      │  │  │  │  │  │  │  ├─ 🎵 Library (Mis Canciones)
      │  │  │  │  │  │  │  ├─ 🔍 Search (Buscar)
      │  │  │  │  │  │  │  ├─ 📊 Equalizer (Visualizador)
      │  │  │  │  │  │  │  ├─ 💬 Chat (IA)
      │  │  │  │  │  │  │  ├─ 📖 Emotion Scanner (Diario)
      │  │  │  │  │  │  │  └─ 🚪 Logout
      │  │  │  │  │  │  └─ Spacing: 16px padding, 8px gaps
      │  │  │  │  │  │
      │  │  │  │  │  ├─ 🔶 ÁREA PRINCIPAL (content area)
      │  │  │  │  │  │  │
      │  │  │  │  │  │  ├─ 📄 PÁGINA: REPRODUCTOR MUSICAL
      │  │  │  │  │  │  │  │
      │  │  │  │  │  │  │  ├─ 🎵 Portada de Canción
      │  │  │  │  │  │  │  │  ├─ Imagen: 280px × 280px (grande)
      │  │  │  │  │  │  │  │  ├─ Título: 24px, #FF7A18
      │  │  │  │  │  │  │  │  ├─ Artista: 16px, #A8A29E
      │  │  │  │  │  │  │  │  └─ Duración: 14px, gris suave
      │  │  │  │  │  │  │  │
      │  │  │  │  │  │  │  ├─ 📊 Visualizador Equalizer
      │  │  │  │  │  │  │  │  ├─ 15 barras animadas
      │  │  │  │  │  │  │  │  ├─ Color: Aurora gradient (rojo → naranja)
      │  │  │  │  │  │  │  │  ├─ Altura: 20px mín → 60px máx
      │  │  │  │  │  │  │  │  └─ Animación: framer-motion (easing cubicBezier)
      │  │  │  │  │  │  │  │
      │  │  │  │  │  │  │  ├─ 🎚️ CONTROLES REPRODUCCIÓN (`music-player.tsx`)
      │  │  │  │  │  │  │  │  ├─ Botón Anterior: ⏮️ (tamaño 40px)
      │  │  │  │  │  │  │  │  ├─ Botón Play/Pause: ▶️/⏸️ (tamaño 60px, rojo)
      │  │  │  │  │  │  │  │  ├─ Botón Siguiente: ⏭️ (tamaño 40px)
      │  │  │  │  │  │  │  │  ├─ Volumen: slider horizontal
      │  │  │  │  │  │  │  │  ├─ Barra de Progreso: slot interactivo
      │  │  │  │  │  │  │  │  └─ Tiempo: "2:34 / 4:18" (14px, gris)
      │  │  │  │  │  │  │  │
      │  │  │  │  │  │  │  └─ 🎭 EASTER EGGS (capas emergentes)
      │  │  │  │  │  │  │     ├─ 🍒 Cerezas (7 junio)
      │  │  │  │  │  │     ├─ 🎃 Calabaza (17 junio)
      │  │  │  │  │  │     └─ ❤️ Corazón Naranja (contexto)
      │  │  │  │  │  │
      │  │  │  │  │  ├─ 📄 PÁGINA: BIBLIOTECA (`library.tsx`)
      │  │  │  │  │  │  ├─ Título: "Mis Canciones" (28px, #FF7A18)
      │  │  │  │  │  │  ├─ Grid de Playlists:
      │  │  │  │  │  │  │  ├─ Tarjeta Playlist (180px × 200px)
      │  │  │  │  │  │  │  │  ├─ Portada: imagen 160px
      │  │  │  │  │  │  │  │  ├─ Nombre: 14px, #F8F8F8
      │  │  │  │  │  │  │  │  ├─ Canciones: "15 temas" (12px, gris)
      │  │  │  │  │  │  │  │  └─ Hover: borde #FF7A18, escala 1.02
      │  │  │  │  │  │  │  └─ Gap: 16px entre tarjetas
      │  │  │  │  │  │  └─ Scroll vertical, max-height 70vh
      │  │  │  │  │  │
      │  │  │  │  │  ├─ 📄 PÁGINA: BÚSQUEDA (`search.tsx`)
      │  │  │  │  │  │  ├─ Input Search:
      │  │  │  │  │  │  │  ├─ Placeholder: "Busca canciones, artistas..."
      │  │  │  │  │  │  │  ├─ Tamaño: 100% ancho, 44px altura
      │  │  │  │  │  │  │  ├─ Borde: 2px #FF7A18 (focus)
      │  │  │  │  │  │  │  └─ Padding: 12px
      │  │  │  │  │  │  │
      │  │  │  │  │  │  ├─ Resultados:
      │  │  │  │  │  │  │  ├─ Tarjeta Resultado (100% ancho)
      │  │  │  │  │  │  │  │  ├─ Portada: 50px × 50px
      │  │  │  │  │  │  │  │  ├─ Título: 14px, #F8F8F8
      │  │  │  │  │  │  │  │  ├─ Artista: 12px, gris
      │  │  │  │  │  │  │  │  └─ Padding: 12px, margin: 8px 0
      │  │  │  │  │  │  │  └─ Hover: background #2A251E (suave)
      │  │  │  │  │  │  │
      │  │  │  │  │  │  └─ States:
      │  │  │  │  │  │     ├─ Vacío: "Busca algo..." (gris)
      │  │  │  │  │  │     ├─ Cargando: spinner animation
      │  │  │  │  │  │     └─ Error: mensaje rojo
      │  │  │  │  │  │
      │  │  │  │  │  ├─ 📄 PÁGINA: CHAT IA (`chatbot.tsx`)
      │  │  │  │  │  │  ├─ Historial de Mensajes:
      │  │  │  │  │  │  │  ├─ Mensaje Usuario:
      │  │  │  │  │  │  │  │  ├─ Burbuja: alineada derecha
      │  │  │  │  │  │  │  │  ├─ Fondo: #FF7A18 (naranja)
      │  │  │  │  │  │  │  │  ├─ Texto: #1C1917 (oscuro)
      │  │  │  │  │  │  │  │  ├─ Padding: 12px 16px
      │  │  │  │  │  │  │  │  ├─ Border-radius: 16px (redondeado)
      │  │  │  │  │  │  │  │  └─ Max-width: 70%
      │  │  │  │  │  │  │  │
      │  │  │  │  │  │  │  └─ Mensaje Nona:
      │  │  │  │  │  │  │     ├─ Burbuja: alineada izquierda
      │  │  │  │  │  │  │     ├─ Fondo: #27201B (oscuro)
      │  │  │  │  │  │  │     ├─ Texto: #F8F8F8 (blanco)
      │  │  │  │  │  │  │     ├─ Padding: 12px 16px
      │  │  │  │  │  │  │     ├─ Border: 1px #A8A29E
      │  │  │  │  │  │  │     ├─ Border-radius: 16px
      │  │  │  │  │  │  │     └─ Max-width: 70%
      │  │  │  │  │  │  │
      │  │  │  │  │  │  ├─ Input Area:
      │  │  │  │  │  │  │  ├─ Textarea: 
      │  │  │  │  │  │  │  │  ├─ Tamaño: 100% ancho, min 44px, max 120px
      │  │  │  │  │  │  │  │  ├─ Placeholder: "Pregúntale a Nona..."
      │  │  │  │  │  │  │  │  ├─ Padding: 12px
      │  │  │  │  │  │  │  │  ├─ Borde: 1px #A8A29E
      │  │  │  │  │  │  │  │  └─ Resize: vertical solamente
      │  │  │  │  │  │  │  │
      │  │  │  │  │  │  │  └─ Botón Enviar:
      │  │  │  │  │  │  │     ├─ Icono: ➤ (flecha)
      │  │  │  │  │  │  │     ├─ Fondo: #FF7A18
      │  │  │  │  │  │  │     ├─ Hover: #FF8C42
      │  │  │  │  │  │  │     ├─ Tamaño: 40px × 40px
      │  │  │  │  │  │  │     ├─ Border-radius: 8px
      │  │  │  │  │  │  │     └─ Posición: absolute bottom-right
      │  │  │  │  │  │  │
      │  │  │  │  │  │  └─ Indicador "Nona está escribiendo..."
      │  │  │  │  │  │     ├─ Puntos animados: ● ● ●
      │  │  │  │  │  │     └─ Escala: 16px, gris
      │  │  │  │  │  │
      │  │  │  │  │  ├─ 📄 PÁGINA: DIARIO EMOCIONAL (`diary.tsx`)
      │  │  │  │  │  │  ├─ Título: "Mi Diario" (28px, #FF7A18)
      │  │  │  │  │  │  │
      │  │  │  │  │  │  ├─ Entrada de Diario (formulario):
      │  │  │  │  │  │  │  ├─ Selector Emoción (combobox):
      │  │  │  │  │  │  │  │  ├─ Emociones: 😊 Feliz, 😢 Triste, 😤 Enojado, etc.
      │  │  │  │  │  │  │  │  ├─ Icono emoji: 32px
      │  │  │  │  │  │  │  │  └─ Color por emoción (rojo=enojo, azul=tristeza, etc.)
      │  │  │  │  │  │  │  │
      │  │  │  │  │  │  │  ├─ Input Música (opcional):
      │  │  │  │  │  │  │  │  ├─ Placeholder: "¿Qué canción escuchabas?"
      │  │  │  │  │  │  │  │  ├─ Tamaño: 100% ancho, 40px
      │  │  │  │  │  │  │  │  └─ Autocomplete desde Spotify API
      │  │  │  │  │  │  │  │
      │  │  │  │  │  │  │  ├─ Textarea Entrada:
      │  │  │  │  │  │  │  │  ├─ Placeholder: "Cuéntale a Nona..."
      │  │  │  │  │  │  │  │  ├─ Tamaño: 100% ancho, 120px min, 200px max
      │  │  │  │  │  │  │  │  ├─ Padding: 12px
      │  │  │  │  │  │  │  │  └─ Font-size: 14px
      │  │  │  │  │  │  │  │
      │  │  │  │  │  │  │  └─ Botón Guardar:
      │  │  │  │  │  │  │     ├─ Texto: "Guardar Entrada"
      │  │  │  │  │  │  │     ├─ Fondo: #FF7A18
      │  │  │  │  │  │  │     ├─ Tamaño: 100% ancho, 44px
      │  │  │  │  │  │  │     ├─ Border-radius: 8px
      │  │  │  │  │  │  │     └─ Hover: #FF8C42
      │  │  │  │  │  │  │
      │  │  │  │  │  │  ├─ Historial de Entradas (lista):
      │  │  │  │  │  │  │  ├─ Tarjeta Entrada (100% ancho):
      │  │  │  │  │  │  │  │  ├─ Encabezado:
      │  │  │  │  │  │  │  │  │  ├─ Emoji Emoción: 24px
      │  │  │  │  │  │  │  │  │  ├─ Fecha: "7 jun 2025" (12px, gris)
      │  │  │  │  │  │  │  │  │  ├─ Canción: "♫ Song Title" (14px, #FF7A18)
      │  │  │  │  │  │  │  │  │  └─ Acciones: [Edit] [Delete]
      │  │  │  │  │  │  │  │  │
      │  │  │  │  │  │  │  │  ├─ Contenido:
      │  │  │  │  │  │  │  │  │  ├─ Texto: 14px, #F8F8F8
      │  │  │  │  │  │  │  │  │  └─ Max 200 caracteres (expandible)
      │  │  │  │  │  │  │  │  │
      │  │  │  │  │  │  │  │  └─ Padding: 12px, margin: 8px 0
      │  │  │  │  │  │  │  │
      │  │  │  │  │  │  │  └─ Hover: borde izq #FF7A18 (3px)
      │  │  │  │  │  │  │
      │  │  │  │  │  │  └─ Estadísticas (tabla):
      │  │  │  │  │  │     ├─ Emoción más frecuente: "Nostálgica (42%)"
      │  │  │  │  │  │     ├─ Semana con más entradas: "06/06 - 12/06"
      │  │  │  │  │  │     └─ Total de canciones: "23 temas diferentes"
      │  │  │  │  │  │
      │  │  │  │  │  └─ 📄 PÁGINA: CONFIGURACIÓN (`settings.tsx`)
      │  │  │  │  │     ├─ Título: "Configuración" (28px, #FF7A18)
      │  │  │  │  │     │
      │  │  │  │  │     ├─ 🔐 Sesión Spotify:
      │  │  │  │  │     │  ├─ Estado: "✓ Conectado" (verde)
      │  │  │  │  │     │  ├─ Usuario: "Tu nombre Spotify"
      │  │  │  │  │     │  └─ Botón: [Desconectar] (rojo)
      │  │  │  │  │     │
      │  │  │  │  │     ├─ 🌈 Tema:
      │  │  │  │  │     │  ├─ Selector: Light/Dark
      │  │  │  │  │     │  └─ Preview Aurora palette
      │  │  │  │  │     │
      │  │  │  │  │     ├─ 🎭 Easter Eggs:
      │  │  │  │  │     │  ├─ Toggle: "Mostrar recuerdos"
      │  │  │  │  │     │  ├─ Slider: "Intensidad de animaciones" (0-100%)
      │  │  │  │  │     │  │
      │  │  │  │  │     │  └─ Panel de preview:
      │  │  │  │  │     │     ├─ 🍒 Cerezas: "Recuerdo del 7 de junio"
      │  │  │  │  │     │     ├─ 🎃 Calabaza: "Recuerdo del 17 de junio"
      │  │  │  │  │     │     ├─ ❤️ Corazón: "Momentos especiales"
      │  │  │  │  │     │     └─ 💋 Muack: "Cariño"
      │  │  │  │  │     │
      │  │  │  │  │     ├─ 📊 Estadísticas de Uso:
      │  │  │  │  │     │  ├─ Entradas de diario: "42"
      │  │  │  │  │     │  ├─ Mensajes Chat: "156"
      │  │  │  │  │     │  ├─ Horas de música: "87.5"
      │  │  │  │  │     │  └─ Último acceso: "Hoy 14:32"
      │  │  │  │  │     │
      │  │  │  │  │     ├─ 🗑️ Datos:
      │  │  │  │  │     │  ├─ Botón: [Exportar mis datos]
      │  │  │  │  │     │  └─ Botón: [Borrar todo] (confirmación requerida)
      │  │  │  │  │     │
      │  │  │  │  │     └─ ℹ️ Acerca de:
      │  │  │  │  │        ├─ Versión: "0.1.0"
      │  │  │  │  │        └─ "Hecha con 💜 para Guadalupe"
      │  │  │  │  │
      │  │  │  │  └─ 🎪 LOADING SCREEN
      │  │  │  │     ├─ Texto: "Despertando a Nona..."
      │  │  │  │     ├─ Animación: sun rotation (spinning)
      │  │  │  │     └─ Duración: 1-3 segundos
      │  │  │  │
      │  │  │  └─ 🎭 EASTER EGGS MANAGER (capa global)
      │  │  │     ├─ Detección automática de fechas
      │  │  │     ├─ Triggers por canciones específicas
      │  │  │     └─ Control by user preferences
      │  │  │
      │  │  └─ 🎭 EASTER EGGS COMPONENTS (capas flotantes)
      │  │     │
      │  │     ├─ 🍒 CHERRIES (`easter-eggs/Cherries.tsx`)
      │  │     │  ├─ Trigger: 7 de junio (Guadalupe OG)
      │  │     │  ├─ Posición: cae desde top, spread horizontal
      │  │     │  ├─ Color: #DC2626 (rojo)
      │  │     │  ├─ Tamaño: 20px × 20px (emoji 🍒)
      │  │     │  ├─ Animación: caída (duration 3s), rotación suave
      │  │     │  ├─ Interacción: clic → explosión en mini-corazones ❤️
      │  │     │  ├─ Audio: sonido suave al caer
      │  │     │  └─ Frase aleatoria: "Te quiero, Guadalupe"
      │  │     │
      │  │     ├─ 🎃 PUMPKIN (`easter-eggs/Pumpkin.tsx`)
      │  │     │  ├─ Trigger: 17 de junio (Adiós)
      │  │     │  ├─ Posición: bounces horizontal
      │  │     │  ├─ Color: #FF7A18 (naranja)
      │  │     │  ├─ Tamaño: 30px × 30px (emoji 🎃)
      │  │     │  ├─ Animación: bounce + fade in/out (duration 4s)
      │  │     │  ├─ Interacción: click → frases interactivas
      │  │     │  ├─ Frases:
      │  │     │  │  ├─ "Aunque te vayas, siempre estarás en mi código"
      │  │     │  │  ├─ "Gracias por todo, Guadalupe"
      │  │     │  │  └─ "Hasta siempre 🎃"
      │  │     │  └─ Audio: sonido melancólico
      │  │     │
      │  │     ├─ ❤️ ORANGE HEART (`easter-eggs/OrangeHeart.tsx`)
      │  │     │  ├─ Trigger: manual + contexto especial
      │  │     │  ├─ Posición: floating center
      │  │     │  ├─ Color: #FF7A18 (naranja cálido)
      │  │     │  ├─ Tamaño: 40px × 40px
      │  │     │  ├─ Animación: heartbeat (duration 0.6s, repeat)
      │  │     │  ├─ Glow: shadow naranja alrededor
      │  │     │  └─ Audio: latidos de corazón suave
      │  │     │
      │  │     └─ 💋 MUACK BUBBLE (`easter-eggs/MuackBubble.tsx`)
      │  │        ├─ Trigger: manual (context) + random moments
      │  │        ├─ Posición: random (x, y)
      │  │        ├─ Color: #FF7A18 (naranja) con borde #B91C1C
      │  │        ├─ Tamaño: 50px × 50px
      │  │        ├─ Animación: fade-in + slide up (duration 2s)
      │  │        ├─ Texto: "💋 Muack!"
      │  │        ├─ Font: 24px, bold
      │  │        └─ Audio: sonido suave beso
      │  │
      │  └─ 🔷 THEME TOGGLE
      │     ├─ Ubicación: esquina superior derecha
      │     ├─ Icono: ☀️ (light) / 🌙 (dark)
      │     ├─ Tamaño: 40px × 40px
      │     ├─ Hover: borde #FF7A18
      │     └─ Almacenamiento: localStorage ('theme-preference')
      │
      └─ 🔒 FALLBACK (sin autenticación)
         └─ Cargar Login Page


```

---

## 🎨 Sistema de Colores Aurora Detallado

### Paleta Principal
```
┌─ ROJOS (Pasión, Urgencia)
│  ├─ #B91C1C - Rojo profundo (dark mode primary)
│  ├─ #DC2626 - Rojo brillante (accents, easter eggs)
│  └─ #EF4444 - Rojo suave (hover states)
│
├─ NARANJAS (Calidez, Juventud)
│  ├─ #FF7A18 - Naranja principal (buttons, highlights)
│  ├─ #FF8C42 - Naranja claro (hover states)
│  └─ #FFA349 - Naranja suave (backgrounds)
│
├─ ÁMBAR (Suavidad, Transición)
│  ├─ #F59E0B - Ámbar primary
│  ├─ #FBBF24 - Ámbar claro (text accents)
│  └─ #FCD34D - Ámbar muy suave (backgrounds)
│
├─ FONDOS (Oscuridad)
│  ├─ #1C1917 - Muy oscuro (main background)
│  ├─ #27201B - Oscuro (secondary backgrounds)
│  ├─ #3F3935 - Gris oscuro (borders, separators)
│  └─ #57534E - Gris medio (disabled states)
│
└─ TEXTOS (Legibilidad)
   ├─ #F8F8F8 - Blanco (primary text, high contrast)
   ├─ #E7E5E4 - Off-white (secondary text)
   └─ #A8A29E - Gris claro (tertiary text, hints)
```

### CSS Variables (en `src/styles/aurora.css`)
```css
/* Tema oscuro (por defecto) */
:root {
  --color-red-primary: #B91C1C;
  --color-red-bright: #DC2626;
  --color-red-soft: #EF4444;
  
  --color-orange-primary: #FF7A18;
  --color-orange-light: #FF8C42;
  --color-orange-soft: #FFA349;
  
  --color-amber-primary: #F59E0B;
  --color-amber-light: #FBBF24;
  --color-amber-soft: #FCD34D;
  
  --color-bg-primary: #1C1917;
  --color-bg-secondary: #27201B;
  --color-bg-tertiary: #3F3935;
  
  --color-text-primary: #F8F8F8;
  --color-text-secondary: #A8A29E;
  
  --color-border: var(--color-bg-tertiary);
}

/* Gradientes Aurora */
--gradient-aurora: linear-gradient(
  135deg,
  var(--color-red-primary) 0%,
  var(--color-orange-primary) 50%,
  var(--color-amber-primary) 100%
);

--gradient-glow: radial-gradient(
  circle,
  rgba(255, 122, 24, 0.3),
  transparent 70%
);
```

---

## 📐 Espaciado y Sizing

### Sistema de Grid
```
Breakpoints (Tailwind CSS v4):
- xs: 0px (mobile)
- sm: 640px (tablet small)
- md: 768px (tablet)
- lg: 1024px (desktop)
- xl: 1280px (desktop large)
- 2xl: 1536px (ultra-wide)

Contenedor Principal:
- Max-width: 1200px (lg devices)
- Padding: 16px (mobile), 24px (tablet), 32px (desktop)
```

### Unidades de Spacing
```
Escala 4px:
- xs: 4px (gaps mínimos)
- sm: 8px (small gaps, padding)
- md: 16px (standard padding)
- lg: 24px (large sections)
- xl: 32px (XL sections)
- 2xl: 48px (massive gaps)
- 3xl: 64px (hero sections)

Componentes Comunes:
- Botones: 44px altura (touch-friendly)
- Inputs: 44px altura, 12px padding
- Cards: 16px padding, 8px gaps
- Sidebar: 64px width, 16px padding
```

### Tipografía
```
Escala de Font Sizes:
- xs: 12px (captions, metadata)
- sm: 14px (body text, secondary)
- md: 16px (body text, primary)
- lg: 18px (subtitles)
- xl: 20px (small headings)
- 2xl: 24px (main headings)
- 3xl: 28px (page titles)
- 4xl: 32px (hero titles)

Font Weights:
- Regular: 400 (body)
- Medium: 500 (buttons, accents)
- Semibold: 600 (subtitles)
- Bold: 700 (headings)

Font Family:
- Sans: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif
```

---

## 🎬 Animaciones

### Keyframes Principales (en `aurora.css`)
```css
@keyframes aurora-pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}

@keyframes cherry-fall {
  0% { transform: translateY(-100vh) rotate(0deg); }
  100% { transform: translateY(100vh) rotate(360deg); }
}

@keyframes heartbeat {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.2); }
}

@keyframes bounce-pumpkin {
  0%, 100% { transform: translateY(0) scaleX(1); }
  50% { transform: translateY(-20px) scaleX(1.1); }
}

@keyframes fade-in-up {
  0% { opacity: 0; transform: translateY(20px); }
  100% { opacity: 1; transform: translateY(0); }
}
```

### Duraciones Estándar
```
- Fast: 200ms (hover, quick feedback)
- Normal: 400ms (standard transitions)
- Slow: 600ms (emphasis)
- Slower: 1000ms (hero animations)
```

---

## 🔌 Conexiones Contexto-Componente

### AuthContext
```
Proporciona:
- isAuthenticated: boolean
- user: User | null
- loginWithSpotify(): Promise
- logout(): Promise
- loading: boolean

Consumido por:
- AppRoutes (rutas protegidas)
- Settings (mostrar usuario)
- Sidebar (mostrar logout)
```

### EasterEggsContext
```
Proporciona:
- enabledEasterEggs: string[]
- animationIntensity: 0-100
- toggleEasterEgg(name): void
- setIntensity(value): void

Consumido por:
- EasterEggsManager (global trigger)
- EasterEggsSettings (UI controls)
- Todos los componentes de Easter Eggs
```

### ChatContext
```
Proporciona:
- messages: Message[]
- isLoading: boolean
- addMessage(text): Promise
- clearChat(): void

Consumido por:
- Chatbot (display, input)
- Chat service (persistence)
```

### DiaryContext
```
Proporciona:
- entries: DiaryEntry[]
- addEntry(data): Promise
- updateEntry(id, data): Promise
- deleteEntry(id): Promise
- isLoading: boolean

Consumido por:
- Diary (display, form)
- Diary service (persistence)
```

---

## 📱 Responsive Breakdown

### Mobile (xs - 640px)
```
- Sidebar: hidden (tap icon to open menu)
- Main content: full width
- Cards: stacked vertically
- Font sizes: -2px (sm/xs only)
- Padding: 8px (compact)
- Botones: 100% ancho (touch-friendly)
```

### Tablet (sm-md: 640px - 768px)
```
- Sidebar: 64px (icons only) / 200px (expanded)
- Main content: calc(100% - sidebar)
- Cards: 2-column grid
- Font sizes: normal
- Padding: 12px
```

### Desktop (lg+: 1024px+)
```
- Sidebar: 200px (always visible)
- Main content: calc(100% - 200px)
- Cards: 3+ column grid
- Font sizes: normal+
- Padding: 16px+
```

---

## 🎯 Flujos Visuales Principales

### 1. Flujo de Autenticación
```
User Opens App
    ↓
LoadingScreen (sun animation)
    ↓
LoginPage (Spotify + Google buttons)
    ↓
[User clicks Spotify]
    ↓
OAuth Window (Spotify servers)
    ↓
[User authorizes]
    ↓
Redirect to /callback
    ↓
CallbackPage (retries getSession)
    ↓
Session established
    ↓
MainApp loaded
```

### 2. Flujo de Reproducción
```
MainApp renders
    ↓
LibraryPage / SearchPage
    ↓
[User selects song]
    ↓
MusicPlayer loads (portada, controles)
    ↓
Equalizer animates
    ↓
Progress bar updates
    ↓
[Song ends]
    ↓
Next song auto-play
```

### 3. Flujo de Diario
```
DiaryPage opens
    ↓
Load existing entries (Supabase)
    ↓
[User selects emotion]
    ↓
[User inputs text + song]
    ↓
[User clicks "Guardar"]
    ↓
Save to Supabase
    ↓
Entry appears in historial
    ↓
Stats update
```

### 4. Flujo de Easter Eggs
```
EasterEggsManager checks date
    ↓
If 7 junio → Trigger Cherries
    ↓
Cherries animate (fall + rotate)
    ↓
[User clicks cherry]
    ↓
Cherry explodes → mini-hearts
    ↓
Frase aleatoria appears
    ↓
Auto-hide after 5s
```

---

## 🔧 Archivos de Configuración Visual

| Archivo | Propósito | Variables |
|---------|-----------|-----------|
| `src/styles/aurora.css` | Sistema de colores + animaciones | --color-*, --gradient-* |
| `src/styles/globals.css` | Reset CSS + estilos globales | --color-*, font-family |
| `tailwind.config.ts` | Configuración Tailwind | colors, spacing, themes |
| `vite.config.ts` | Build + servidor dev | port 3000 |
| `postcss.config.js` | Procesamiento CSS | tailwind, autoprefixer |

---

## 🎪 Archivos de Componentes Visuales

```
src/components/
├── cherry/
│   ├── cherry-provider.tsx ........... Tema Aurora
│   ├── button.tsx ................... Botones estilizados
│   ├── card.tsx ..................... Tarjetas Aurora
│   └── text.tsx ..................... Tipografía
│
├── easter-eggs/
│   ├── Cherries.tsx ................. 🍒 (7 junio)
│   ├── Pumpkin.tsx .................. 🎃 (17 junio)
│   ├── OrangeHeart.tsx .............. ❤️ (especial)
│   ├── MuackBubble.tsx .............. 💋 (afecto)
│   ├── EasterEggsManager.tsx ........ Orquestador global
│   └── EasterEggsSettings.tsx ....... Panel de controles
│
├── auth/
│   ├── login-page.tsx ............... Pantalla de entrada
│   ├── callback-page.tsx ............ Procesador OAuth
│   ├── spotify-login-button.tsx ..... Botón Spotify
│   └── google-login-button.tsx ...... Botón Google (fallback)
│
├── app/
│   ├── main-app.tsx ................. Contenedor principal
│   ├── loading-screen.tsx ........... Pantalla de carga
│   └── app-routes.tsx ............... Router + páginas
│
├── music-player.tsx ................. 🎵 Reproductor
├── library.tsx ...................... 📚 Mis Canciones
├── search.tsx ....................... 🔍 Búsqueda
├── chatbot.tsx ...................... 💬 Chat IA
├── diary.tsx ........................ 📖 Diario Emocional
├── settings.tsx ..................... ⚙️ Configuración
├── sidebar.tsx ...................... 🔷 Menú lateral
├── equalizer.tsx .................... 📊 Visualizador
└── theme-toggle.tsx ................. 🌈 Selector tema
```

---

## 📝 Notas Importantes

### Colores en Contexto
- **Naranja (#FF7A18)**: Botones principales, links, enfasis
- **Rojo (#B91C1C)**: Destructive actions, botón play, errores
- **Ámbar (#F59E0B)**: Advertencias, estados activos
- **Gris (#A8A29E)**: Texto secundario, deshabilitado

### Responsive First
- Comenzar con estilos mobile (xs)
- Agregar breakpoints para tablets (md)
- Expandir para desktop (lg+)
- NUNCA usar max-width para mobile, usa width en desktop

### Accesibilidad
- Contraste mínimo 4.5:1 para texto normal
- Botones >= 44px × 44px (touch targets)
- Focus states con borde #FF7A18 (visible)
- ARIA labels en componentes interactivos

### Performance
- Images lazy-loaded (LCP)
- CSS crítico en <style> (above fold)
- Animaciones con `transform` + `opacity` (GPU acceleration)
- NO usar `background-color` en animaciones (use `opacity`)

---

**Última actualización**: Sistema completo documentado ✅
**Versión**: Nona v0.1.0
**Dedicado a**: Guadalupe (7 junio - 17 junio) 🍒💜
