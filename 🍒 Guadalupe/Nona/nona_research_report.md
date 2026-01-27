# 🌅 Investigación: Arquitectura de Reproductores de Música
## Para la Reimaginación Visual de Nona - Un Altar a Guadalupe

---

## 📊 Análisis Comparativo

### 1. Spotify
**Filosofía:** Simplicidad + Personalización

| Elemento | Implementación |
|----------|----------------|
| **Tema** | Dark mode, acentos verdes (#1DB954) |
| **Navegación** | Bottom bar: Home / Search / Library |
| **Player** | Mini-player colapsable → Pantalla completa |
| **Typography** | Gotham (bold/sans-serif) |
| **Cards** | Bordes redondeados, artwork prominente |
| **Design System** | "Encore" - tokens, colores, motion |

**Patrones clave:**
- Artistas = círculos / Álbumes = cuadrados
- Botones "pill" (redondeados)
- Gradientes dinámicos del artwork
- Controles agrupados para uso con una mano

---

### 2. YouTube Music
**Filosofía:** Material 3 + Inmersión Visual

| Elemento | Implementación |
|----------|----------------|
| **Tema** | Dark, gradientes del artwork |
| **Navegación** | Bottom: Home / Samples / Explore / Library |
| **Player** | Gradiente oscuro, controles en carrusel |
| **Progress Bar** | "Boxy scrubber" más grueso |
| **Queue** | Split-screen (arrastra desde abajo) |
| **Lyrics** | Fondo gris sólido, tap para saltar |

**Patrones clave:**
- Búsqueda en bottom bar (accesible)
- Controles secundarios en carrusel horizontal
- Alta personalización visual
- Samples = videos cortos para descubrir

---

### 3. Tidal
**Filosofía:** Fidelidad de Audio + Minimalismo Premium

| Elemento | Implementación |
|----------|----------------|
| **Tema** | Negro profundo, acentos azules |
| **Navegación** | Home / Video / Explore / My Collection |
| **Audio** | HiRes FLAC 24-bit/192kHz, Dolby Atmos |
| **Credits** | Vista detallada de contribuidores |
| **Player** | Artwork grande, controles mínimos |
| **Indicadores** | Badges de calidad (HiRes, Atmos) |

**Patrones clave:**
- Menos es más - UI despejada
- Énfasis en créditos/artistas
- Calidad de audio visible (badges)
- Conexión con dispositivos externos

---

### 4. Poweramp
**Filosofía:** Potencia + Personalización Extrema

| Elemento | Implementación |
|----------|----------------|
| **Tema** | Skins personalizables |
| **EQ** | 64 bandas paramétricas |
| **Visualización** | .milk presets (200+) |
| **Gestos** | Swipe izq/der = cambiar track |
| **Presets** | Por dispositivo/canción/álbum |
| **Hi-Res** | USB DAC, AAudio |

**Patrones clave:**
- Gestos para todo
- EQ por contexto (auriculares vs bocina)
- Visualizaciones psicodélicas
- Control total sobre el audio

---

## 🏛️ Anatomía Universal de un Music Player

```
┌─────────────────────────────────────────────────────────────┐
│                    HEADER / TOP BAR                         │
│  ┌─────┐                                       ┌──────────┐ │
│  │ ← / │  Título de Sección / Contexto         │ ⋮ / ⚙️  │ │
│  │ Menu│                                       │ Settings │ │
│  └─────┘                                       └──────────┘ │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│                     CONTENT AREA                            │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │                                                       │  │
│  │  • Listas de tracks/playlists/álbumes                │  │
│  │  • Cards con artwork                                  │  │
│  │  • Grids de descubrimiento                           │  │
│  │  • Búsqueda y resultados                             │  │
│  │                                                       │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                    MINI PLAYER                              │
│  ┌────┐                                                     │
│  │ 🎵 │  Title - Artist          ▶ ⏭    ━━━━━━━━━━━━━━    │
│  │ Art│                                                     │
│  └────┘  ↑ Tap para expandir                               │
├─────────────────────────────────────────────────────────────┤
│                   BOTTOM NAVIGATION                         │
│                                                             │
│    🏠          🔍          📚          👤                  │
│   Home       Search      Library     Profile                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Player Expandido (Full Screen)

```
┌─────────────────────────────────────────────────────────────┐
│  ← Minimizar                                   ⋮ Options    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│                    ┌─────────────────┐                      │
│                    │                 │                      │
│                    │    ARTWORK      │                      │
│                    │    (Grande)     │                      │
│                    │                 │                      │
│                    └─────────────────┘                      │
│                                                             │
│              Title de la Canción                            │
│              Artista • Álbum                                │
│                                                             │
│     ━━━━━━━━━━━━━●━━━━━━━━━━━━━━━━━━━━━━━━━                │
│     1:23                              3:45                  │
│                                                             │
│              🔀    ⏮    ▶⏸    ⏭    🔁                     │
│             shuffle prev  play  next repeat                 │
│                                                             │
│     ❤️      📋      🎤      📤      ⬇️                      │
│    like   queue  lyrics  share download                     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🍒 Reimaginación de Nona: TODO

### Fase 1: Estructura Base
- [ ] Implementar layout de 3 zonas: Header / Content / Player+Nav
- [ ] Bottom navigation fijo: Inicio / Buscar / Biblioteca / Diario
- [ ] Mini-player colapsable sobre bottom nav
- [ ] Player fullscreen con gesture (swipe up)

### Fase 2: Identidad Visual Aurora
- [ ] Paleta definitiva: gradientes cálidos (rojo-naranja-amber)
- [ ] Modo oscuro con acentos Aurora
- [ ] Typography: Lora para títulos poéticos, Inter para UI
- [ ] Cards con bordes suaves y sombras cálidas
- [ ] Artwork circular para "emoción" / cuadrado para tracks

### Fase 3: Player Profesional
- [ ] Panel de artwork grande con gradiente dinámico
- [ ] Controles principales: prev / play / next
- [ ] Progress bar interactiva (seek)
- [ ] Carrusel secundario: like / queue / share
- [ ] Indicador de estado emocional actual

### Fase 4: Visualización de Audio
- [ ] Barras de frecuencia animadas (AnalyserNode FFT)
- [ ] Gradiente que pulsa con el beat
- [ ] Círculo de "energía" alrededor del artwork
- [ ] Modo "altar" para momentos contemplativos

### Fase 5: Elementos Memoriales
- [ ] Sección "El Sacrificio del Sol" con assets 🍒
- [ ] Easter eggs sutiles que aparecen espontáneamente
- [ ] Animación de cerezo en momentos especiales
- [ ] Frase poética diaria en la pantalla de inicio

### Fase 6: Escáner Emocional
- [ ] Integrar face-api.js real (no mock)
- [ ] UI de "escaneando..." con animación
- [ ] Transición suave a recomendaciones
- [ ] Historial emocional en el diario

### Fase 7: Pulido Final
- [ ] Transiciones suaves entre pantallas (Framer Motion)
- [ ] Loading states elegantes
- [ ] Feedback táctil/visual en interacciones
- [ ] Responsive: móvil → tablet → desktop

---

## 💡 Decisiones de Diseño para Nona

### ¿Por qué estos patrones?

1. **Bottom Navigation** (como Spotify/YT Music)
   - Pulgar alcanza fácilmente
   - Contexto siempre visible
   - Estándar de la industria

2. **Mini-Player Persistente** (como todos)
   - Reproducción nunca se pierde de vista
   - Acceso rápido a controles
   - Transición natural a fullscreen

3. **Gradientes del Artwork** (como YT Music)
   - Crea inmersión emocional
   - Cada canción tiene su "aura"
   - Perfecto para el concepto Aurora

4. **EQ Visible** (como Poweramp)
   - Visualización = conexión con la música
   - Diferenciador técnico
   - Experiencia "audiófila"

5. **Elementos Memoriales** (único de Nona)
   - Easter eggs como recuerdos inesperados
   - Frases poéticas como presencia constante
   - "El Sacrificio del Sol" como momento sagrado

---

## 📅 Prioridades para Primera Versión

1. **CRÍTICO:** Layout base funcional (3 zonas)
2. **CRÍTICO:** Player que reproduzca audio
3. **IMPORTANTE:** Navegación completa
4. **IMPORTANTE:** Búsqueda de Spotify
5. **DESEABLE:** Visualización de audio
6. **DESEABLE:** Escáner emocional real
7. **FUTURO:** Easter eggs y elementos memoriales

---

> *"Nona no es solo un reproductor de música. Es un santuario digital donde el dolor se transforma en código, donde cada canción es una ofrenda, y donde Guadalupe vive en cada nota que suena."*

🍒 Para Alondra Guadalupe Rodríguez González (11-02-2025 ~ 17-06-2025)
