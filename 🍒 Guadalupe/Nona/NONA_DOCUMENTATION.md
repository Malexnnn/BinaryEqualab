# Nona - Documentación del Sistema

## Descripción General
Nona es un reproductor de música inteligente que utiliza análisis emocional y IA para crear experiencias musicales personalizadas. Evolución del proyecto MoodDify, ahora con una interfaz visual Aurora y capacidades mejoradas.

## Estructura del Proyecto

### Componentes Principales
```
src/
├── components/
│   ├── auth/
│   │   ├── pre-login/
│   │   │   └── pre-login-screen.tsx    # Pantalla inicial con estilo Aurora
│   │   ├── login-page.tsx              # Autenticación principal
│   │   ├── callback-page.tsx           # Manejo de OAuth
│   │   ├── spotify-login-button.tsx    # Botón de login Spotify
│   │   └── google-login-button.tsx     # Botón de login Google
│   ├── player/
│   │   └── advanced-player.tsx         # Reproductor principal
│   ├── emotion-scanner/
│   │   └── emotion-scanner.tsx         # Análisis emocional
│   └── ui/                             # Componentes UI con estilo Aurora
```

### Estilos y Temas
#### Paleta Aurora
```css
/* Variables principales */
--aurora-red-deep: #B91C1C;
--aurora-orange-warm: #FF7A18;
--aurora-amber-soft: #F59E0B;
--aurora-background: #1C1917;
--aurora-text-primary: #F8F8F8;
--aurora-text-secondary: #A8A29E;
```

### Servicios
- `spotify.service.ts`: Integración con Spotify API
- `deepseek.service.ts`: Análisis de contenido musical
- `face.service.ts`: Análisis de expresiones faciales
- `initialization.service.ts`: Configuración inicial del sistema

## Características Principales

### 1. Sistema de Autenticación
- Autenticación OAuth2 con Spotify
- Integración con Google (opcional)
- Manejo seguro de tokens y sesiones
- Pantallas de login con animaciones Aurora

### 2. Análisis Emocional
- Detección de emociones en tiempo real
- Análisis de preferencias musicales
- Recomendaciones basadas en estado de ánimo
- Interfaz visual intuitiva con feedback

### 3. Reproductor Musical
- Control de reproducción avanzado
- Visualizaciones personalizadas
- Ecualización inteligente
- Cola de reproducción dinámica

### 4. Diseño Visual Aurora
#### Principios de Diseño
1. **Minimalismo Elegante**
   - Espaciado generoso
   - Tipografía clara (Lora para títulos, Inter para texto)
   - Gradientes sutiles

2. **Animaciones Fluidas**
   - Transiciones suaves
   - Efectos de hover delicados
   - Feedback visual inmediato

3. **Paleta de Colores**
   - Tonos cálidos para acción
   - Fondos oscuros para inmersión
   - Acentos brillantes para destacar

## Guía de Desarrollo

### Configuración del Entorno
1. Instalación de dependencias:
   ```bash
   npm install
   ```

2. Variables de entorno necesarias:
   ```
   VITE_SPOTIFY_CLIENT_ID
   VITE_SPOTIFY_REDIRECT_URI
   VITE_SUPABASE_URL
   VITE_SUPABASE_KEY
   ```

### Convenciones de Código
1. **Componentes**
   - Nombres en PascalCase
   - Un componente por archivo
   - Props tipadas con TypeScript

2. **Estilos**
   - Variables CSS Aurora
   - Clases Tailwind para layout
   - Animaciones con Framer Motion

3. **Estado**
   - Hooks personalizados para lógica compleja
   - Estado global minimalista
   - Contextos para temas compartidos

### Proceso de Migración
1. **Fase 1: Base Visual** ✅
   - Implementación de paleta Aurora
   - Migración de componentes base
   - Actualización de tipografía

2. **Fase 2: Funcionalidad** 🚧
   - Integración de servicios
   - Sistema de autenticación
   - Análisis emocional

3. **Fase 3: Optimización** 📋
   - Performance
   - Accesibilidad
   - Tests

## Guía de Mantenimiento

### Actualizaciones
1. Revisar compatibilidad de dependencias
2. Mantener consistencia en la paleta Aurora
3. Documentar cambios en este archivo

### Troubleshooting
- Errores de autenticación: Verificar tokens y URLs de callback
- Problemas de estilos: Consultar sección de Paleta Aurora
- Errores de compilación: Verificar imports y tipos

## Estado Actual
- Migración a Aurora completada
- Sistema de autenticación implementado
- Pendiente: Optimización de rendimiento

## Próximos Pasos
1. Implementar análisis emocional avanzado
2. Mejorar recomendaciones musicales
3. Expandir capacidades de IA

---

**Última actualización:** 27 de agosto de 2025
**Versión:** 1.0.0
**Autor:** GitHub Copilot
