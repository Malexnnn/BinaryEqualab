#!/bin/bash

# ═══════════════════════════════════════════════════════════════
#  BINARY - INSTALADOR MAESTRO DEFINITIVO
#  El álgebra también siente ∫✨
#  
#  Autor: José "Aldra" Avilés Cárdenas
#  Proyecto: Aldraverse
# ═══════════════════════════════════════════════════════════════

# Colores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
MAGENTA='\033[0;35m'
NC='\033[0m' # No Color

clear

echo -e "${MAGENTA}"
cat << "EOF"
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║  ██████╗ ██╗███╗   ██╗ █████╗ ██████╗ ██╗   ██╗          ║
║  ██╔══██╗██║████╗  ██║██╔══██╗██╔══██╗╚██╗ ██╔╝          ║
║  ██████╔╝██║██╔██╗ ██║███████║██████╔╝ ╚████╔╝           ║
║  ██╔══██╗██║██║╚██╗██║██╔══██║██╔══██╗  ╚██╔╝            ║
║  ██████╔╝██║██║ ╚████║██║  ██║██║  ██║   ██║             ║
║  ╚═════╝ ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝             ║
║                                                            ║
║            El álgebra también siente ∫✨                   ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}"

echo -e "${CYAN}Instalador Maestro v1.0${NC}"
echo -e "${YELLOW}Proyecto: Aldraverse - EquaLab Native${NC}"
echo ""
sleep 1

# ═══════════════════════════════════════════════════════════════
#  VERIFICACIONES PREVIAS
# ═══════════════════════════════════════════════════════════════

echo -e "${CYAN}[1/8] Verificando sistema...${NC}"

# Verificar Linux
if [[ "$OSTYPE" != "linux-gnu"* ]]; then
    echo -e "${RED}❌ Error: Este instalador es solo para Linux${NC}"
    exit 1
fi
echo -e "${GREEN}  ✓ Sistema operativo: Linux${NC}"

# Verificar Python 3
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python 3 no está instalado${NC}"
    echo -e "${YELLOW}Instala con: sudo apt install python3 python3-pip python3-venv python3-tk${NC}"
    exit 1
fi
PYTHON_VERSION=$(python3 --version | awk '{print $2}')
echo -e "${GREEN}  ✓ Python detectado: $PYTHON_VERSION${NC}"

# Verificar pip
if ! command -v pip3 &> /dev/null; then
    echo -e "${YELLOW}⚠️  pip3 no encontrado, instalando...${NC}"
    sudo apt install -y python3-pip > /dev/null 2>&1
fi
echo -e "${GREEN}  ✓ pip3 disponible${NC}"

# Verificar/Instalar Tkinter
python3 -c "import tkinter" 2>/dev/null
if [ $? -ne 0 ]; then
    echo -e "${YELLOW}⚠️  Tkinter no instalado, instalando...${NC}"
    sudo apt install -y python3-tk > /dev/null 2>&1
fi
echo -e "${GREEN}  ✓ Tkinter disponible${NC}"

echo ""

# ═══════════════════════════════════════════════════════════════
#  CREAR ESTRUCTURA DE DIRECTORIOS
# ═══════════════════════════════════════════════════════════════

echo -e "${CYAN}[2/8] Creando estructura de proyecto...${NC}"

# Crear directorio raíz si no existe
if [ ! -d "binary" ]; then
    mkdir binary
    echo -e "${GREEN}  ✓ Directorio 'binary' creado${NC}"
else
    echo -e "${YELLOW}  ⚠ Directorio 'binary' ya existe${NC}"
fi

cd binary

# Crear subdirectorios
mkdir -p core ui operations config assets
echo -e "${GREEN}  ✓ Subdirectorios creados${NC}"

# Crear archivos vacíos (se llenarán después)
touch core/__init__.py ui/__init__.py operations/__init__.py
echo -e "${GREEN}  ✓ Módulos Python inicializados${NC}"

echo ""

# ═══════════════════════════════════════════════════════════════
#  CREAR requirements.txt
# ═══════════════════════════════════════════════════════════════

echo -e "${CYAN}[3/8] Generando requirements.txt...${NC}"

cat > requirements.txt << 'EOF'
# Core científico
sympy==1.12
numpy==1.26.2
scipy==1.11.4
matplotlib==3.8.2

# GUI
pillow==10.1.0

# Tema moderno (opcional)
sv-ttk==2.6.0
EOF

echo -e "${GREEN}  ✓ requirements.txt creado${NC}"
echo ""

# ═══════════════════════════════════════════════════════════════
#  CREAR ENTORNO VIRTUAL E INSTALAR DEPENDENCIAS
# ═══════════════════════════════════════════════════════════════

echo -e "${CYAN}[4/8] Configurando entorno virtual...${NC}"

python3 -m venv venv
echo -e "${GREEN}  ✓ Entorno virtual creado${NC}"

source venv/bin/activate
echo -e "${GREEN}  ✓ Entorno virtual activado${NC}"

echo -e "${YELLOW}  → Instalando dependencias (esto puede tardar)...${NC}"
pip install --upgrade pip --quiet
pip install -r requirements.txt --quiet

if [ $? -eq 0 ]; then
    echo -e "${GREEN}  ✓ Dependencias instaladas correctamente${NC}"
else
    echo -e "${RED}  ✗ Error instalando dependencias${NC}"
    exit 1
fi

echo ""

# ═══════════════════════════════════════════════════════════════
#  CREAR ARCHIVOS DE CONFIGURACIÓN
# ═══════════════════════════════════════════════════════════════

echo -e "${CYAN}[5/8] Creando archivos de configuración...${NC}"

# settings.json
cat > config/settings.json << 'EOF'
{
  "theme": "aurora",
  "precision": 10,
  "angle_mode": "rad",
  "history_size": 100,
  "show_steps": true,
  "font_size": 12,
  "window_width": 1200,
  "window_height": 800
}
EOF
echo -e "${GREEN}  ✓ config/settings.json${NC}"

# theme.json
cat > config/theme.json << 'EOF'
{
  "aurora": {
    "bg": "#0A0A0A",
    "fg": "#FFBF00",
    "accent1": "#FF8C42",
    "accent2": "#C41E3A",
    "secondary": "#2D2D2D",
    "text": "#FFFFFF",
    "button_bg": "#2D2D2D",
    "button_fg": "#FFBF00",
    "entry_bg": "#1A1A1A",
    "entry_fg": "#FFFFFF"
  }
}
EOF
echo -e "${GREEN}  ✓ config/theme.json${NC}"

echo ""

# ═══════════════════════════════════════════════════════════════
#  CREAR MÓDULOS CORE
# ═══════════════════════════════════════════════════════════════

echo -e "${CYAN}[6/8] Generando módulos core...${NC}"

# core/__init__.py
cat > core/__init__.py << 'EOF'
"""
Binary Core Module
Motor matemático basado en SymPy
"""

from .engine import MathEngine
from .parser import ExpressionParser

__all__ = ['MathEngine', 'ExpressionParser']
EOF

# core/engine.py
cat > core/engine.py << 'EOF'
"""
Motor matemático principal
Wrapper de SymPy para operaciones simbólicas y numéricas
"""

import sympy as sp
from sympy import symbols, latex
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application
)

class MathEngine:
    """Motor de cálculo simbólico y numérico"""
    
    def __init__(self, precision=10):
        self.precision = precision
        sp.init_printing(use_unicode=True)
        
        # Variables comunes predefinidas
        self.x, self.y, self.z = symbols('x y z', real=True)
        self.t, self.s, self.w = symbols('t s w', real=True)
        self.n = symbols('n', integer=True)
        
        # Configurar transformaciones para parser
        self.transformations = (
            standard_transformations + 
            (implicit_multiplication_application,)
        )
    
    def parse(self, expression_str):
        """Parsea string a expresión SymPy"""
        try:
            expression_str = expression_str.replace('^', '**')
            expression_str = expression_str.replace('π', 'pi')
            
            expr = parse_expr(
                expression_str,
                transformations=self.transformations,
                local_dict={
                    'x': self.x, 'y': self.y, 'z': self.z,
                    't': self.t, 's': self.s, 'w': self.w,
                    'n': self.n
                }
            )
            return expr
        except Exception as e:
            return None
    
    def to_latex(self, expr):
        """Convierte expresión a LaTeX"""
        try:
            return latex(expr)
        except:
            return str(expr)
    
    def simplify(self, expr):
        return sp.simplify(expr)
    
    def expand(self, expr):
        return sp.expand(expr)
    
    def factor(self, expr):
        return sp.factor(expr)
EOF

# core/parser.py
cat > core/parser.py << 'EOF'
"""
Parser de expresiones matemáticas
"""

import re

class ExpressionParser:
    """Parser avanzado de expresiones"""
    
    def preprocess(self, expression):
        """Preprocesa expresión antes de parsear"""
        expression = expression.strip()
        
        replacements = {
            '^': '**',
            '÷': '/',
            '×': '*',
            'π': 'pi',
            '√': 'sqrt'
        }
        
        for old, new in replacements.items():
            expression = expression.replace(old, new)
        
        # Multiplicación implícita (2x -> 2*x)
        expression = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expression)
        
        return expression
    
    def validate(self, expression):
        """Valida sintaxis básica"""
        if not expression:
            return False, "Expresión vacía"
        
        if expression.count('(') != expression.count(')'):
            return False, "Paréntesis desbalanceados"
        
        return True, ""
EOF

echo -e "${GREEN}  ✓ Módulos core generados${NC}"
echo ""

# ═══════════════════════════════════════════════════════════════
#  CREAR MÓDULOS DE OPERACIONES
# ═══════════════════════════════════════════════════════════════

echo -e "${CYAN}[7/8] Generando módulos de operaciones...${NC}"

# operations/__init__.py
cat > operations/__init__.py << 'EOF'
"""
Operations Module
Transformadas y operaciones matemáticas avanzadas
"""

from .laplace import laplace_transform, inverse_laplace_transform

__all__ = ['laplace_transform', 'inverse_laplace_transform']
EOF

# operations/laplace.py
cat > operations/laplace.py << 'EOF'
"""
Transformadas de Laplace
"""

import sympy as sp
from sympy import symbols

def laplace_transform(expr, t_var='t', s_var='s', show_steps=False):
    """
    Calcula transformada de Laplace
    
    Args:
        expr: Expresión SymPy o string
        t_var: Variable en el dominio del tiempo
        s_var: Variable en el dominio de Laplace
        show_steps: Si mostrar pasos intermedios
    
    Returns:
        tuple: (resultado, pasos) o (resultado, None)
    """
    try:
        t = symbols(t_var, real=True, positive=True)
        s = symbols(s_var)
        
        if isinstance(expr, str):
            from sympy.parsing.sympy_parser import parse_expr
            expr = parse_expr(expr, local_dict={'t': t})
        
        result = sp.laplace_transform(expr, t, s, noconds=True)
        
        steps = None
        if show_steps:
            steps = [
                f"Expresión original: {expr}",
                f"Variable: {t_var} → {s_var}",
                f"Aplicando definición de Laplace...",
                f"Resultado: {result}"
            ]
        
        return result, steps
        
    except Exception as e:
        return None, [f"Error: {str(e)}"]

def inverse_laplace_transform(expr, s_var='s', t_var='t'):
    """Calcula transformada inversa de Laplace"""
    try:
        s = symbols(s_var)
        t = symbols(t_var, real=True, positive=True)
        
        if isinstance(expr, str):
            from sympy.parsing.sympy_parser import parse_expr
            expr = parse_expr(expr, local_dict={'s': s})
        
        result = sp.inverse_laplace_transform(expr, s, t)
        return result, None
        
    except Exception as e:
        return None, [f"Error: {str(e)}"]
EOF

echo -e "${GREEN}  ✓ Módulos de operaciones generados${NC}"
echo ""

# ═══════════════════════════════════════════════════════════════
#  CREAR SCRIPT PRINCIPAL
# ═══════════════════════════════════════════════════════════════

echo -e "${CYAN}[8/8] Creando script principal y launchers...${NC}"

# binary.py (versión simplificada para test)
cat > binary.py << 'EOF'
#!/usr/bin/env python3
"""
Binary - EquaLab Native
El álgebra también siente ∫✨

Autor: José "Aldra" Avilés Cárdenas
"""

import tkinter as tk
from tkinter import ttk, scrolledtext
import json
from core.engine import MathEngine
from operations.laplace import laplace_transform

class BinaryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Binary - El álgebra también siente ∫✨")
        self.root.geometry("800x600")
        
        # Cargar config
        with open('config/settings.json', 'r') as f:
            self.settings = json.load(f)
        
        with open('config/theme.json', 'r') as f:
            self.theme = json.load(f)['aurora']
        
        # Aplicar tema
        self.root.configure(bg=self.theme['bg'])
        
        # Motor matemático
        self.engine = MathEngine()
        
        # Crear UI
        self.create_widgets()
    
    def create_widgets(self):
        # Frame principal
        main_frame = tk.Frame(self.root, bg=self.theme['bg'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Título
        title = tk.Label(
            main_frame,
            text="Binary - Transformada de Laplace (Demo)",
            font=("Inter", 18, "bold"),
            bg=self.theme['bg'],
            fg=self.theme['fg']
        )
        title.pack(pady=10)
        
        # Input
        input_frame = tk.Frame(main_frame, bg=self.theme['bg'])
        input_frame.pack(pady=10, fill=tk.X)
        
        tk.Label(
            input_frame,
            text="Función f(t):",
            bg=self.theme['bg'],
            fg=self.theme['text'],
            font=("Inter", 12)
        ).pack(side=tk.LEFT, padx=5)
        
        self.input_entry = tk.Entry(
            input_frame,
            font=("Courier", 12),
            bg=self.theme['entry_bg'],
            fg=self.theme['entry_fg'],
            insertbackground=self.theme['fg'],
            width=40
        )
        self.input_entry.pack(side=tk.LEFT, padx=5)
        
        # Botón calcular
        calc_btn = tk.Button(
            input_frame,
            text="Calcular ℒ",
            command=self.calculate,
            bg=self.theme['button_bg'],
            fg=self.theme['button_fg'],
            font=("Inter", 10, "bold"),
            padx=15,
            pady=5
        )
        calc_btn.pack(side=tk.LEFT, padx=5)
        
        # Output
        output_frame = tk.Frame(main_frame, bg=self.theme['bg'])
        output_frame.pack(pady=10, fill=tk.BOTH, expand=True)
        
        tk.Label(
            output_frame,
            text="Resultado:",
            bg=self.theme['bg'],
            fg=self.theme['text'],
            font=("Inter", 12)
        ).pack(anchor=tk.W)
        
        self.output_text = scrolledtext.ScrolledText(
            output_frame,
            font=("Courier", 11),
            bg=self.theme['entry_bg'],
            fg=self.theme['text'],
            insertbackground=self.theme['fg'],
            height=15,
            wrap=tk.WORD
        )
        self.output_text.pack(fill=tk.BOTH, expand=True)
    
    def calculate(self):
        expr_str = self.input_entry.get()
        
        if not expr_str:
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, "⚠️ Ingresa una función\n")
            return
        
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, f"Calculando ℒ{{{expr_str}}}...\n\n")
        
        try:
            expr = self.engine.parse(expr_str)
            if expr is None:
                self.output_text.insert(tk.END, "❌ Error parseando expresión\n")
                return
            
            result, steps = laplace_transform(expr, show_steps=True)
            
            if result is None:
                self.output_text.insert(tk.END, "❌ Error calculando transformada\n")
                return
            
            # Mostrar resultado
            self.output_text.insert(tk.END, "✓ Resultado:\n\n")
            self.output_text.insert(tk.END, f"  ℒ{{{expr}}} = {result}\n\n")
            
            if steps:
                self.output_text.insert(tk.END, "Pasos:\n")
                for step in steps:
                    self.output_text.insert(tk.END, f"  • {step}\n")
        
        except Exception as e:
            self.output_text.insert(tk.END, f"❌ Error: {str(e)}\n")

def main():
    root = tk.Tk()
    app = BinaryApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
EOF

chmod +x binary.py

# Launcher bash
cat > binary.sh << 'EOF'
#!/bin/bash
cd "$(dirname "$0")"
source venv/bin/activate
python3 binary.py
EOF

chmod +x binary.sh

echo -e "${GREEN}  ✓ Scripts principales creados${NC}"
echo ""

# ═══════════════════════════════════════════════════════════════
#  FINALIZACIÓN
# ═══════════════════════════════════════════════════════════════

clear
echo -e "${GREEN}"
cat << "EOF"
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║            ✨ INSTALACIÓN COMPLETADA ✨                    ║
║                                                            ║
║  Binary está listo para usar                               ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}"

echo -e "${CYAN}Directorio de instalación:${NC} $(pwd)"
echo ""
echo -e "${YELLOW}Para ejecutar Binary:${NC}"
echo -e "  ${GREEN}cd binary${NC}"
echo -e "  ${GREEN}./binary.sh${NC}"
echo ""
echo -e "${YELLOW}O manualmente:${NC}"
echo -e "  ${GREEN}cd binary${NC}"
echo -e "  ${GREEN}source venv/bin/activate${NC}"
echo -e "  ${GREEN}python3 binary.py${NC}"
echo ""
echo -e "${CYAN}¡Que lo disfrutes, Aldra! ∫✨${NC}"
echo ""
