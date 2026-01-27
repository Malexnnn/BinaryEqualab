# Triggers de Easter Eggs por Canción - Guía de Implementación

## Concepto

Cada Easter Egg puede ser activado automáticamente cuando se reproduce una canción específica vinculada a él.

**Ejemplo:**
- Canción "Aurora" → Mostrar Corazón Naranja
- Canción "Calabaza" → Mostrar Calabaza
- Cualquier canción de Alondra → Mostrar Cerezas

## Estructura de Datos

### 1. Modelo de Canción Especial

```typescript
// src/models/special-track.model.ts

export interface SpecialTrack {
  spotifyId: string;
  title: string;
  artist: string;
  easterEggType: 'heart' | 'pumpkin' | 'cherries' | 'muack';
  meaning: string; // Contexto emocional
  triggerBehavior: 'auto' | 'manual'; // Auto: se muestra siempre, Manual: requiere confirmación
  duration?: number; // Duración del Easter Egg en ms
}

export const SPECIAL_TRACKS: SpecialTrack[] = [
  {
    spotifyId: 'spotify:track:...',
    title: 'Aurora',
    artist: 'Artista',
    easterEggType: 'heart',
    meaning: 'Emblema de Alejandra',
    triggerBehavior: 'auto',
    duration: 3000,
  },
  {
    spotifyId: 'spotify:track:...',
    title: 'Nombre de la canción de Lupe',
    artist: 'Artista',
    easterEggType: 'cherries',
    meaning: 'Recuerdos de Alondra',
    triggerBehavior: 'manual',
  },
];
```

### 2. Servicio de Tracks Especiales

```typescript
// src/services/special-tracks.service.ts

import { SpecialTrack, SPECIAL_TRACKS } from '../models/special-track.model';

class SpecialTracksService {
  private specialTracks: SpecialTrack[] = SPECIAL_TRACKS;

  /**
   * Busca si una canción es especial por su Spotify ID
   */
  findBySpotifyId(spotifyId: string): SpecialTrack | null {
    return this.specialTracks.find(
      track => track.spotifyId === spotifyId
    ) || null;
  }

  /**
   * Busca por título (más flexible)
   */
  findByTitle(title: string): SpecialTrack | null {
    return this.specialTracks.find(
      track => track.title.toLowerCase().includes(title.toLowerCase())
    ) || null;
  }

  /**
   * Obtiene todas las canciones de un Easter Egg específico
   */
  getTracksByEasterEgg(
    easterEggType: SpecialTrack['easterEggType']
  ): SpecialTrack[] {
    return this.specialTracks.filter(
      track => track.easterEggType === easterEggType
    );
  }

  /**
   * Agrega una nueva canción especial
   */
  addSpecialTrack(track: SpecialTrack): void {
    if (!this.findBySpotifyId(track.spotifyId)) {
      this.specialTracks.push(track);
      console.log(`Track especial agregado: ${track.title}`);
    }
  }
}

export const specialTracksService = new SpecialTracksService();
```

### 3. Hook para Detección Automática

```typescript
// src/hooks/use-track-easter-eggs.ts

import { useEffect } from 'react';
import { useEasterEggsAPI } from './use-easter-eggs-api';
import { specialTracksService } from '../services/special-tracks.service';

export function useTrackEasterEggs(currentTrack: SpotifyTrack | null) {
  const easter = useEasterEggsAPI();

  useEffect(() => {
    if (!currentTrack) return;

    // Buscar si la canción actual es especial
    const specialTrack = specialTracksService.findBySpotifyId(
      currentTrack.id
    ) || specialTracksService.findByTitle(currentTrack.name);

    if (!specialTrack) return;

    console.log(`🎵 Canción especial detectada: ${specialTrack.title}`);

    // Mostrar el Easter Egg correspondiente
    switch (specialTrack.easterEggType) {
      case 'heart':
        if (specialTrack.triggerBehavior === 'auto') {
          easter.showHeart(specialTrack.duration);
        }
        break;

      case 'pumpkin':
        if (specialTrack.triggerBehavior === 'auto') {
          easter.showPumpkin(specialTrack.duration);
        }
        break;

      case 'cherries':
        if (specialTrack.triggerBehavior === 'auto') {
          easter.showCherries(specialTrack.duration);
        }
        break;

      case 'muack':
        if (specialTrack.triggerBehavior === 'auto') {
          easter.showMuack(specialTrack.duration);
        }
        break;
    }
  }, [currentTrack?.id, easter]);
}
```

### 4. Integración en Reproductor de Música

```typescript
// src/components/music-player.tsx

import { useTrackEasterEggs } from '@/hooks/use-track-easter-eggs';
import { useCurrentTrack } from '@/hooks/use-current-track'; // Hook que obtienes de tu contexto de música

export function MusicPlayer() {
  const currentTrack = useCurrentTrack(); // Tu hook para obtener canción actual

  // Activar Easter Eggs automáticamente
  useTrackEasterEggs(currentTrack);

  return (
    <div className="music-player">
      {/* Tu UI del reproductor */}
      {currentTrack && (
        <div className="track-info">
          <h3>{currentTrack.name}</h3>
          <p>{currentTrack.artist}</p>
        </div>
      )}
    </div>
  );
}
```

## Configuración

### Paso 1: Definir Canciones Especiales

Edita `src/models/special-track.model.ts` y agrega las IDs de Spotify de tus canciones especiales.

Para obtener el Spotify ID de una canción:
1. Abre en Spotify (en navegador)
2. Click derecho → "Copy Spotify URI"
3. Tiene formato: `spotify:track:XXXXXXXXXXXXXXXXXXXXXXXX`

### Paso 2: Elegir Comportamiento

- **auto**: Se muestra automáticamente cuando suena
- **manual**: Se ofrece un botón (opcional)

### Paso 3: Configurar Duración

- **heart**: 3000ms (3 segundos)
- **pumpkin**: 3000ms
- **cherries**: 0 (indefinido, el usuario la cierra)
- **muack**: 2000ms

## Ejemplo Completo

```typescript
// Step 1: Definir canciones
// En special-track.model.ts

export const SPECIAL_TRACKS: SpecialTrack[] = [
  {
    spotifyId: 'spotify:track:5V6CXzZx74KrJwJtF5GQGa',
    title: 'Recuerdos de Junio',
    artist: 'Artist Name',
    easterEggType: 'cherries',
    meaning: 'Canción vinculada a Alondra',
    triggerBehavior: 'auto',
  },
  {
    spotifyId: 'spotify:track:...',
    title: 'Aurora',
    artist: 'Artist Name',
    easterEggType: 'heart',
    meaning: 'Emblema de Alejandra',
    triggerBehavior: 'auto',
  },
];

// Step 2: Usar en componente
function MusicPlayer() {
  const currentTrack = useCurrentTrack();
  useTrackEasterEggs(currentTrack);
  
  return <div className="player">...</div>;
}

// ¡Listo! Los Easter Eggs aparecerán automáticamente
```

## Ventajas

✅ Triggers automáticos por contexto musical  
✅ Flexible (configurable por track)  
✅ No intrusivo (puede deshabilitarse)  
✅ Extensible (agregar más canciones fácilmente)  

## Mejoras Futuras

- [ ] Admin panel para agregar canciones sin editar código
- [ ] Sincronización con Supabase de tracks especiales
- [ ] Analytics: cuándo se activan los Easter Eggs
- [ ] Playlist especial de canciones vinculadas
- [ ] Sistema de "unlock" de canciones especiales

---

**Esta funcionalidad conecta la música con la emoción de Nona** 🎵🍒
