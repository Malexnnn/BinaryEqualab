# 🎨 Guía de Diseño UI/UX - Binary EquaLab

## Inspiración de Apps de Calculadora Científica

### Apps con Mejor UI (2024):
| App                             | Lo que hace bien                                                        |
| ------------------------------- | ----------------------------------------------------------------------- |
| **HiPER Scientific Calculator** | Temas personalizables, escritura natural de expresiones, alta precisión |
| **iOS 18 Calculator**           | Diseño minimalista, "Math Notes" (escribes y resuelve en tiempo real)   |
| **TechniCalc**                  | Interfaz limpia, resultados en vivo, tamaño de entrada grande           |
| **Calculator+**                 | Animaciones suaves, sin necesidad de rotar para funciones científicas   |

### Elementos de Diseño Clave:
1. **Botones grandes y táctiles** (min 48x48px)
2. **Tipografía clara para resultados** (texto grande para output)
3. **Colores de acento para funciones especiales** (derivada, integral = color destacado)
4. **Feedback visual inmediato** (animaciones sutiles al presionar)

---

## Fuentes Recomendadas

### Para Código/Consola:
| Fuente             | Descripción                                          | Instalación                                          |
| ------------------ | ---------------------------------------------------- | ---------------------------------------------------- |
| **Fira Code** ⭐    | Ligaduras (!=, ===, =>), muy legible                 | [GitHub](https://github.com/tonsky/FiraCode)         |
| **JetBrains Mono** | Diseñada por JetBrains, excelente a tamaños pequeños | [JetBrains](https://www.jetbrains.com/lp/mono/)      |
| **Cascadia Code**  | Microsoft, incluye Powerline symbols                 | [GitHub](https://github.com/microsoft/cascadia-code) |
| **Consolas**       | Ya instalada en Windows, buena fallback              | Sistema                                              |

### Para Interfaz/Títulos:
| Fuente       | Estilo             | Uso                                            |
| ------------ | ------------------ | ---------------------------------------------- |
| **Inter**    | Sans-serif moderna | Botones, labels, texto general                 |
| **Lora**     | Serif elegante     | Títulos poéticos ("El álgebra también siente") |
| **Segoe UI** | Windows nativa     | Fallback limpio                                |

---

## Paleta de Colores "Aurora" (Actual)

```
Fondo Principal:    #1C1917 (Stone 900)
Fondo Secundario:   #292524 (Stone 800)
Fondo Oscuro:       #0C0A09 (Stone 950)

Primario:           #B91C1C (Rojo Profundo)
Secundario:         #EA580C (Naranja)
Acento:             #D97706 (Ámbar)

Texto Principal:    #F5F5F4 (Blanco roto)
Texto Secundario:   #A8A29E (Gris cálido)
Bordes:             #44403C (Stone 700)
```

---

## Mejoras Propuestas para Binary EquaLab

### Inmediatas:
1. [ ] **Instalar fuente Fira Code** para la consola (ligaduras)
2. [ ] **Aumentar tamaño de botones** (de 48x40 → 56x48)
3. [ ] **Hacer que `cos(3x)` → `cos(3*x)` automáticamente** (parseo inteligente)

### Próximas:
1. [ ] Agregar animaciones sutiles al presionar botones
2. [ ] Modo "Math Notes" estilo iOS 18 (escribir y ver resultado en tiempo real)
3. [ ] Gráficos integrados tipo GeoGebra
4. [ ] Exportar historial como archivo

---

*Inspirado en: HiPER, iOS 18 Calculator, Spyder IDE, Wolfram Mathematica*
