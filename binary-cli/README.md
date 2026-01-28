# Binary EquaLab CLI

> 🧮 Command-line CAS calculator with Spanish functions

## Installation

```bash
pip install binary-equalab
```

Or from source:
```bash
cd binary-cli
pip install -e .
```

## Usage

### REPL Mode
```bash
binary-math
```

This opens an interactive calculator:
```
Binary EquaLab CLI v1.0.0
>>> derivar(x^2 + 3x, x)
2*x + 3

>>> integrar(sin(x), x)
-cos(x)

>>> factorial(5)
120

>>> van(0.10, -1000, 300, 400, 500)
78.82
```

### One-liner Mode
```bash
binary-math "derivar(x^3, x)"
# Output: 3*x^2

binary-math "factorial(10)"
# Output: 3628800
```

### Available Functions

| Category           | Functions                                                                  |
| ------------------ | -------------------------------------------------------------------------- |
| **Calculus**       | `derivar()`, `integrar()`, `limite()`, `sumatoria()`                       |
| **Algebra**        | `simplificar()`, `expandir()`, `factorizar()`, `resolver()`                |
| **Statistics**     | `media()`, `mediana()`, `desviacion()`, `varianza()`                       |
| **Linear Algebra** | `matriz()`, `determinante()`, `inversa()`, `transpuesta()`                 |
| **Finance**        | `van()`, `tir()`, `depreciar()`, `interes_simple()`, `interes_compuesto()` |
| **Trigonometry**   | `sin()`, `cos()`, `tan()`, `arcsin()`, `arccos()`, `arctan()`              |

## Development

```bash
cd binary-cli
pip install -e ".[dev]"
pytest
```
