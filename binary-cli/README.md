# Binary EquaLab CLI - Aurora v2.0

<p align="center">
  <img src="https://raw.githubusercontent.com/Malexnnn/BinaryEqualab/main/docs/banner_cli.png" alt="Binary EquaLab CLI" width="500">
</p>

<p align="center">
  <em>"Las matemáticas también sienten, pero estas no se equivocan."</em>
</p>

---

## 🚀 Instalación
```bash
pip install binary-equalab
```

### 👩‍💻 Modo Desarrollador (Local)
Si quieres editar el código y probar tus cambios al instante:
```bash
git clone https://github.com/Malexnnn/BinaryEqualab.git
cd BinaryEqualab/binary-cli
pip install -e .
```

---

## 🐚 Uso y Aliases
Puedes invocar la herramienta con cualquiera de estos comandos:
- `binary-equalab` (Estándar)
- `bneqls` (Corto)
- `beq` (Ultra corto)
- `binary-math` (Legacy)

### REPL Mode (Interactivo)
Entra al modo interactivo con historial y autocompletado:
```bash
bneqls
```

```text
╔══════════════════════════════════════════════════════════╗
║    Binary EquaLab CLI   Aurora v2.0                      ║
║    "Las matemáticas también sienten,                     ║
║     pero estas no se equivocan."                         ║
╚══════════════════════════════════════════════════════════╝

>>> derivar(x^2 + 3x, x)
→ 2*x + 3
```

### One-liner Mode
```bash
bneqls "derivar(x^3, x)"
# Output: 3*x^2
```

---

## ✨ Novedades v2.0 (Aurora)

### 🎵 Sonificación (Audio)
Convierte funciones matemáticas en archivos de audio `.wav`.
```python
>>> sonify(sin(440*2*pi*t))  # Genera una onda pura a 440Hz
>>> sonify(x * sin(x))       # Genera algo más experimental
```

### 📐 Geometría Analítica
```python
>>> distancia((0,0), (3,4))
→ 5
>>> recta((0,0), (1,1))
→ y = x
>>> pendiente((0,0), (1,1))
→ 1
```

### 🥚 Easter Eggs
El sistema tiene "alma". Intenta escribir estos comandos en el REPL:
- `binary`
- `aldra`
- `lupe`

---

## 🔢 Funciones Clave

### Cálculo
| Función     | Ejemplo                    | Resultado |
| :---------- | :------------------------- | :-------- |
| `derivar`   | `derivar(x^2, x)`          | `2*x`     |
| `integrar`  | `integrar(sin(x), x)`      | `-cos(x)` |
| `limite`    | `limite(sin(x)/x, x, 0)`   | `1`       |
| `sumatoria` | `sumatoria(n^2, n, 1, 10)` | `385`     |

### Finanzas
`van`, `tir`, `depreciar`, `interes_compuesto`.

### Estadística
`media`, `mediana`, `desviacion`, `varianza`.

---

## 📱 Mobile App (Binary Pocket)
Esta versión incluye el código base para la app móvil en `binary-mobile/` (construida con Flet).
¡Próximamente en tiendas!

---

*Hecho con ❤️ por Malexnnn.*
