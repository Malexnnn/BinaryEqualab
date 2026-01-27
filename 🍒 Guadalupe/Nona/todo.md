## Tareas para separar flujos de autenticación en MoodDify

### Fase 2: Extraer y examinar código de autenticación existente
- [x] Revisar `spotify.service.ts`
- [x] Revisar `google-login-button.tsx`
- [x] Revisar `login-page.tsx`
- [x] Revisar `use-auth.ts`

### Fase 3: Refactorizar servicio de autenticación de Spotify
- [x] Asegurar que `spotify.service.ts` solo maneje la interacción con la API de Spotify y el uso de tokens.
- [x] Confirmar que `loginWithSpotify` en `use-auth.ts` inicia el flujo OAuth de Spotify.
- [x] Verificar que `callback-page.tsx` maneje correctamente la redirección y el almacenamiento del token de Spotify.

### Fase 4: Implementar servicio de autenticación de Google separado
- [x] Crear `auth-google.service.ts` para manejar el login de Google y la gestión de tokens.
- [x] Mover la lógica de `loginWithGoogle` de `use-auth.ts` a `auth-google.service.ts`.
- [x] Adaptar `google-callback.tsx` (si existe o crear uno) para manejar la redirección de Google.
- [x] Asegurar que el estado del login de Google se mantenga en `localStorage` o `sessionStorage`.

### Fase 5: Modificar componentes para usar autenticación condicional
- [x] Modificar `login-page.tsx` para que solo muestre el botón de Spotify al inicio.
- [x] Modificar `chatbot.component.ts` para activar el login de Google si no hay sesión iniciada.
- [x] Modificar `emotion-scanner.component.ts` para activar el login de Google si no hay sesión iniciada.
- [x] Mostrar mensaje suave *"Para continuar con el chat emocional, inicia sesión con Google"*.

### Fase 6: Entregar código refactorizado y documentación
- [x] Generar un archivo ZIP con el código modificado.
- [x] Proporcionar instrucciones claras sobre cómo ejecutar el proyecto y probar los cambios.


