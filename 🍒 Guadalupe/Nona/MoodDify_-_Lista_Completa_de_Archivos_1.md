# MoodDify - Lista Completa de Archivos

## 📁 Archivos de Configuración (Raíz)
- `package.json` - Dependencias y scripts del proyecto
- `vite.config.ts` - Configuración de Vite (puerto 4200)
- `tsconfig.json` - Configuración TypeScript principal
- `tsconfig.node.json` - Configuración TypeScript para Node
- `tailwind.config.js` - Configuración Tailwind CSS
- `postcss.config.js` - Configuración PostCSS
- `index.html` - HTML principal de la aplicación

## 📁 src/ (Código Fuente)
- `main.tsx` - Punto de entrada de React
- `App.tsx` - Componente principal (⚠️ necesita refactoring)

## 📁 src/components/ (Componentes React)

### 🎨 UI Components (Base)
- `ui/alert.tsx` - Componente de alertas
- `ui/avatar.tsx` - Componente de avatar
- `ui/badge.tsx` - Componente de badges/etiquetas
- `ui/breadcrumb.tsx` - Navegación breadcrumb
- `ui/button.tsx` - Botones base
- `ui/calendar.tsx` - Componente calendario
- `ui/card.tsx` - Tarjetas/cards
- `ui/carousel.tsx` - Carrusel de elementos
- `ui/chart.tsx` - Gráficos y charts
- `ui/checkbox.tsx` - Checkboxes
- `ui/collapsible.tsx` - Elementos colapsables
- `ui/command.tsx` - Paleta de comandos
- `ui/context-menu.tsx` - Menús contextuales
- `ui/dialog.tsx` - Diálogos/modales
- `ui/drawer.tsx` - Cajones laterales
- `ui/dropdown-menu.tsx` - Menús desplegables
- `ui/form.tsx` - Formularios
- `ui/hover-card.tsx` - Cards con hover
- `ui/input.tsx` - Campos de entrada
- `ui/input-otp.tsx` - Input para códigos OTP
- `ui/label.tsx` - Etiquetas de formulario
- `ui/menubar.tsx` - Barra de menú
- `ui/navigation-menu.tsx` - Menú de navegación
- `ui/pagination.tsx` - Paginación
- `ui/popover.tsx` - Popovers
- `ui/progress.tsx` - Barras de progreso
- `ui/radio-group.tsx` - Grupos de radio buttons
- `ui/resizable.tsx` - Paneles redimensionables
- `ui/scroll-area.tsx` - Áreas de scroll
- `ui/select.tsx` - Selectores/dropdowns
- `ui/separator.tsx` - Separadores
- `ui/sheet.tsx` - Hojas laterales
- `ui/sidebar.tsx` - Sidebar base
- `ui/skeleton.tsx` - Placeholders de carga
- `ui/slider.tsx` - Controles deslizantes
- `ui/sonner.tsx` - Notificaciones toast
- `ui/switch.tsx` - Interruptores
- `ui/table.tsx` - Tablas
- `ui/tabs.tsx` - Pestañas
- `ui/textarea.tsx` - Áreas de texto
- `ui/toggle.tsx` - Botones toggle
- `ui/toggle-group.tsx` - Grupos de toggle
- `ui/tooltip.tsx` - Tooltips
- `ui/use-mobile.ts` - Hook para detección móvil
- `ui/utils.ts` - Utilidades UI (cn function)

### 🔐 Autenticación
- `auth/login-page.tsx` - Página de login (solo Spotify)
- `auth/callback-page.tsx` - Callback genérico (Spotify/Google)
- `auth/google-callback-page.tsx` - Callback específico Google
- `auth/spotify-login-button.tsx` - Botón login Spotify
- `auth/google-login-button.tsx` - Botón login Google

### 🎵 Reproductor de Música
- `player/advanced-player.tsx` - Reproductor avanzado con controles

### 🧠 IA y Emociones
- `emotion-scanner/emotion-scanner.tsx` - Escáner emocional por cámara
- `chatbot.tsx` - Chatbot con IA (✅ corregido)

### 🎛️ Interfaz Principal
- `sidebar.tsx` - Barra lateral de navegación
- `library.tsx` - Biblioteca de música
- `search.tsx` - Búsqueda de música
- `equalizer.tsx` - Ecualizador de audio
- `music-player.tsx` - Reproductor básico
- `theme-toggle.tsx` - Cambio de tema
- `diagnostic-info.tsx` - Información de diagnóstico

### 🖼️ Figma Components
- `figma/ImageWithFallback.tsx` - Componente de imagen con fallback

### 🗑️ Archivos Problemáticos
- `chatbot-broken.tsx` - Versión rota del chatbot (backup)

## 📁 src/hooks/ (React Hooks)
- `use-auth.ts` - Hook de autenticación (modificado para separar Google)
- `use-theme.ts` - Hook para manejo de temas
- `use-debounce.ts` - Hook para debounce

## 📁 src/models/ (Modelos TypeScript)
- `user.model.ts` - Modelos de datos (User, Track, ChatMessage, etc.)

## 📁 src/services/ (Servicios de Negocio)
- `config.service.ts` - Configuración y variables de entorno
- `spotify.service.ts` - Integración con Spotify API (⚠️ necesita corrección)
- `deepseek.service.ts` - Integración con DeepSeek IA
- `auth-google.service.ts` - Servicio de autenticación Google (✅ creado)
- `face.service.ts` - Servicio de detección facial
- `initialization.service.ts` - Inicialización de servicios

## 📁 src/styles/ (Estilos)
- `globals.css` - Estilos globales con Tailwind (✅ corregido)

## 🔧 Estado de Archivos

### ✅ Completamente Funcionales
- Todos los componentes UI base
- Configuración del proyecto
- Servicios de configuración
- Modelos de datos
- Hooks básicos

### ⚠️ Necesitan Corrección
- `App.tsx` - Estructura principal
- `spotify.service.ts` - Flujo de autenticación
- `use-auth.ts` - Integración con nuevos servicios

### ✅ Recientemente Creados/Corregidos
- `auth-google.service.ts` - Nuevo servicio Google
- `google-callback-page.tsx` - Nueva página callback
- `chatbot.tsx` - Corregido errores de sintaxis
- `globals.css` - Agregadas directivas Tailwind

## 📊 Estadísticas del Proyecto

**Total de Archivos**: ~80 archivos
- **Componentes UI**: 45+ archivos
- **Componentes Funcionales**: 15 archivos
- **Servicios**: 6 archivos
- **Hooks**: 3 archivos
- **Configuración**: 7 archivos

**Líneas de Código Estimadas**: ~15,000 líneas
- **TypeScript/TSX**: ~12,000 líneas
- **CSS**: ~2,000 líneas
- **Configuración**: ~1,000 líneas

## 🎯 Archivos Críticos para Revisión

### Prioridad Alta
1. `App.tsx` - Estructura principal
2. `spotify.service.ts` - Autenticación Spotify
3. `use-auth.ts` - Hook de autenticación

### Prioridad Media
1. `login-page.tsx` - Flujo de login
2. `deepseek.service.ts` - Integración IA
3. `emotion-scanner.tsx` - Detección emocional

### Prioridad Baja
1. Componentes UI (ya funcionales)
2. Estilos y configuración
3. Modelos de datos

## 📝 Notas Importantes

1. **Origen Figma**: Los componentes UI provienen de exportación Figma
2. **Dependencias**: Todas instaladas y configuradas
3. **Tokens**: Configuración real para desarrollo
4. **Estructura**: Sigue patrones React modernos
5. **TypeScript**: Tipado completo implementado

