# Documentación de Nona 🍒 - Versión Final

## Descripción General
Nona es un reproductor de música inteligente que utiliza análisis emocional y IA para crear experiencias musicales personalizadas. Es la evolución del proyecto MoodDify, ahora con una interfaz visual Aurora y capacidades mejoradas de Supabase.

## Estructura del Proyecto

### Componentes Principales
```
src/
├── components/
│   ├── auth/                 # Componentes de autenticación
│   ├── player/               # Reproductor de música avanzado
│   ├── emotion-scanner/      # Análisis emocional
│   ├── easter-eggs/          # Sistema de recuerdos y Easter Eggs
│   ├── app/                  # Componentes principales de la aplicación
│   └── ui/                   # Componentes de UI con estilo Aurora
├── services/                 # Servicios de la aplicación
├── hooks/                    # Hooks personalizados
├── contexts/                 # Contextos de React
├── routes/                   # Rutas de la aplicación
├── styles/                   # Estilos globales y de componentes
└── constants/                # Constantes de la aplicación
```

### Estilos y Temas
#### Paleta Aurora
La paleta de colores Aurora se basa en tonos cálidos de rojo y naranja, creando una experiencia visual acogedora y emocional.

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
- **`spotify.service.ts`**: Integración con la API de Spotify.
- **`deepseek.service.ts`**: Análisis de contenido musical.
- **`face.service.ts`**: Análisis de expresiones faciales.
- **`initialization.service.ts`**: Configuración inicial del sistema.
- **`chatService.ts`**: Servicio de chat con Supabase.
- **`emotional-diary.service.ts`**: Servicio de diario emocional con Supabase.

## Características Principales

### 1. Sistema de Autenticación
- Autenticación OAuth2 con Spotify.
- Integración con Supabase Auth para la gestión de usuarios.
- Manejo seguro de tokens y sesiones.
- Pantallas de login con animaciones Aurora.

### 2. Diario Emocional
- Creación, lectura, actualización y eliminación de entradas de diario.
- Persistencia de datos en Supabase.
- Análisis de sentimientos de las entradas del diario mediante NLP.

### 3. Chatbot Híbrido
- Conversaciones persistentes con historial en Supabase.
- Respuestas generadas por IA (DeepSeek y GPT).
- Indicador de "Nona está escribiendo..." para una experiencia más humana.

### 4. Sistema de Easter Eggs
- Sistema de "recuerdos" desbloqueables.
- Triggers basados en fechas, interacciones, gestos y acciones.
- Control de visibilidad de los Easter Eggs por parte del usuario.

### 5. Integración con Supabase
- Uso de Supabase para la base de datos, autenticación y almacenamiento.
- Edge Functions para la interacción segura con APIs externas.

## Estado Actual
- La aplicación se compila y ejecuta correctamente en modo de desarrollo.
- La interfaz de usuario está completamente actualizada con el estilo visual de Nona.
- La autenticación de Spotify está parcialmente implementada (falta completar el flujo de callback).
- Los servicios de Supabase están creados pero no completamente integrados.

## Próximos Pasos
- Completar el flujo de autenticación de Spotify.
- Integrar completamente los servicios de diario emocional y chat con Supabase.
- Implementar la lógica de negocio para los Easter Eggs.
- Realizar pruebas exhaustivas de todas las funcionalidades.
- Optimizar el rendimiento y corregir cualquier error restante bugs.


