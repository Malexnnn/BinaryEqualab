# 📱 Binary EquaLab: Multiplatform Strategy (Flet)

## 🎯 Objetivo
Llevar la potencia de **Binary EquaLab** a dispositivos móviles (**Android/iOS**) y unificar la experiencia de escritorio sin reescribir la lógica matemática.

## 🛠️ ¿Por qué Flet?
Flet permite construir apps de **Flutter** usando **Python**.
- **Python**: Reutilizamos el 100% de `binary-cli` y `binary-desktop` (lógica de SymPy, Matplotlib).
- **UI Moderna**: Flutter ofrece controles Material Design 3 / Cupertino nativos.
- **Cross-Platform**: Compila a `.apk`, `.ipa`, `.exe`, `.app` y WebAssembly.

---

## 🏗️ Arquitectura Propuesta

### 1. Núcleo Compartido (`binary-core`)
Extraer la lógica de cálculo de `binary-cli` y `binary-desktop` a un paquete común.
- `engine.py`: Parser y solvers.
- `plotter.py`: Generador de figuras (adaptado para Flet).

### 2. Estructura del Proyecto
```
BinaryEquaLab/
├── binary-core/       # Lógica matemática pura (pip installable)
├── binary-cli/        # Interfaz Terminal (Existente)
├── binary-desktop/    # Interfaz PyQt6 (Existente - Pro Power User)
├── binary-web/        # Interfaz React (Existente - Acceso Universal)
└── binary-mobile/     # [NUEVO] App Flet (Android/iOS/Desktop Casual)
```

## 🚀 Roadmap Multiplataforma

### Fase 1: Prototipo Flet (`binary-mobile`)
- [ ] Setup de proyecto Flet.
- [ ] Portar el "Modo Consola" (Chat UI con el motor matemático).
- [ ] Compilar APK de prueba.

### Fase 2: Paridad Visual
- [ ] Implementar tema "Aurora" en Flet (Dark Glassmorphism).
- [ ] Portar gráficas (Matplotlib → Flet Image).

### Fase 3: Distribución
- [ ] GitHub Actions para generar APKs automáticamente.
- [ ] Publicación en F-Droid / Play Store (Opcional).

---

## ⚖️ PyQt6 vs Flet

| Característica  | PyQt6 (Desktop Actual)           | Flet (Mobile Futuro)         |
| :-------------- | :------------------------------- | :--------------------------- |
| **Target**      | Power Users, PC/Mac              | Casual, touch, Mobile        |
| **Performance** | Nativo C++ (Qt)                  | Flutter (Skia)               |
| **Gráficos**    | Matplotlib interactivo real      | Matplotlib (Imagen estática) |
| **Look & Feel** | Aplicación de escritorio clásica | App móvil moderna            |
| **Curva Dev**   | Alta (Qt Designer/Code)          | Baja (Python puro)           |

## 💡 Recomendación
Mantener **PyQt6** para la versión Desktop "Pro" (científica pesada) y desarrollar **Flet** para la versión Mobile/Tablet "Lite" (cálculos rápidos, consultas).
