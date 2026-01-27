"""
Binary EquaLab - Main Window (Desktop PyQt6)

Ventana principal con modos: Console (CAS), Graphing, Matrix.
Usa el motor SymPy de src/core/engine.py.
"""
import sys
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QTabWidget, QToolBar, QStatusBar, QLabel,
    QLineEdit, QTextEdit, QPushButton, QSplitter,
    QListWidget, QListWidgetItem, QStackedWidget,
    QFrame, QSizePolicy, QComboBox
)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QFont, QAction, QIcon

from src.core.engine import EquaEngine
from src.utils.constants import AppConfig, AuroraPalette


class ConsoleWidget(QWidget):
    """Widget del modo Consola (CAS interactivo)."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.engine = EquaEngine()
        self.history = []
        self._setup_ui()
    
    def _setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(12)
        
        # Header
        header = QLabel("Console Mode")
        header.setStyleSheet(f"""
            font-size: 24px;
            font-weight: bold;
            color: {AuroraPalette.SECONDARY};
            padding-bottom: 8px;
        """)
        layout.addWidget(header)
        
        # Output Area (History)
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.output.setPlaceholderText("Resultados aqui...")
        self.output.setStyleSheet(f"""
            QTextEdit {{
                font-family: 'Consolas', 'Fira Code', monospace;
                font-size: 14px;
                background-color: {AuroraPalette.BACKGROUND_DARK};
                border: 1px solid {AuroraPalette.BORDER};
                border-radius: 8px;
                padding: 12px;
            }}
        """)
        layout.addWidget(self.output, stretch=1)
        
        # Input Area
        input_frame = QFrame()
        input_frame.setStyleSheet(f"""
            QFrame {{
                background-color: {AuroraPalette.BACKGROUND_LIGHT};
                border: 1px solid {AuroraPalette.BORDER};
                border-radius: 8px;
                padding: 8px;
            }}
        """)
        input_layout = QHBoxLayout(input_frame)
        input_layout.setContentsMargins(8, 8, 8, 8)
        
        prompt_label = QLabel(">>>")
        prompt_label.setStyleSheet(f"color: {AuroraPalette.SECONDARY}; font-weight: bold;")
        input_layout.addWidget(prompt_label)
        
        self.input = QLineEdit()
        self.input.setPlaceholderText("Escribe una expresion... (ej: simplify((x^2-1)/(x-1)))")
        self.input.setStyleSheet(f"""
            QLineEdit {{
                background-color: {AuroraPalette.BACKGROUND_DARK};
                border: none;
                font-family: 'Consolas', monospace;
                font-size: 16px;
                padding: 8px;
            }}
        """)
        self.input.returnPressed.connect(self._on_submit)
        input_layout.addWidget(self.input, stretch=1)
        
        submit_btn = QPushButton("Ejecutar")
        submit_btn.setProperty("class", "primary")
        submit_btn.clicked.connect(self._on_submit)
        input_layout.addWidget(submit_btn)
        
        layout.addWidget(input_frame)
        
        # Quick Buttons Row
        quick_frame = QFrame()
        quick_layout = QHBoxLayout(quick_frame)
        quick_layout.setContentsMargins(0, 8, 0, 0)
        quick_layout.setSpacing(8)
        
        quick_commands = [
            ("simplify()", "simplify()"),
            ("expand()", "expand()"),
            ("factor()", "factor()"),
            ("diff(,x)", "diff(,x)"),
            ("integrate(,x)", "integrate(,x)"),
            ("solve(,x)", "solve(,x)"),
            ("limit(,x,0)", "limit(,x,0)"),
            ("taylor(,x,0,5)", "taylor(,x,0,5)"),
        ]
        
        for label, cmd in quick_commands:
            btn = QPushButton(label)
            btn.setFixedHeight(32)
            btn.setStyleSheet("font-size: 12px; padding: 4px 8px;")
            btn.clicked.connect(lambda checked, c=cmd: self._insert_command(c))
            quick_layout.addWidget(btn)
        
        quick_layout.addStretch()
        layout.addWidget(quick_frame)
    
    def _insert_command(self, cmd):
        """Inserta un comando en el input."""
        current = self.input.text().strip()
        if current:
            new_text = cmd.replace("()", f"({current})").replace("(,", f"({current},")
        else:
            new_text = cmd
        self.input.setText(new_text)
        self.input.setFocus()
    
    def _on_submit(self):
        """Procesa el input del usuario."""
        expr_str = self.input.text().strip()
        if not expr_str:
            return
        
        self.history.append(expr_str)
        result = self._evaluate(expr_str)
        
        self.output.append(f">>> {expr_str}")
        self.output.append(f"    {result}")
        self.output.append("")
        
        self.input.clear()
    
    def _evaluate(self, expr_str):
        """Evalua la expresion usando el engine."""
        try:
            if expr_str.startswith("simplify("):
                inner = expr_str[9:-1]
                return str(self.engine.simplify(inner))
            elif expr_str.startswith("expand("):
                inner = expr_str[7:-1]
                return str(self.engine.expand(inner))
            elif expr_str.startswith("factor("):
                inner = expr_str[7:-1]
                return str(self.engine.factor(inner))
            elif expr_str.startswith("diff("):
                parts = expr_str[5:-1].rsplit(",", 1)
                if len(parts) == 2:
                    return str(self.engine.derivative(parts[0].strip(), parts[1].strip()))
                return str(self.engine.derivative(parts[0].strip()))
            elif expr_str.startswith("integrate("):
                parts = expr_str[10:-1].rsplit(",", 1)
                if len(parts) == 2:
                    return str(self.engine.integral(parts[0].strip(), parts[1].strip()))
                return str(self.engine.integral(parts[0].strip()))
            elif expr_str.startswith("solve("):
                parts = expr_str[6:-1].rsplit(",", 1)
                if len(parts) == 2:
                    return str(self.engine.solve(parts[0].strip(), parts[1].strip()))
                return str(self.engine.solve(parts[0].strip()))
            elif expr_str.startswith("limit("):
                parts = expr_str[6:-1].split(",")
                if len(parts) >= 3:
                    return str(self.engine.limit(parts[0].strip(), parts[1].strip(), float(parts[2].strip())))
                return str(self.engine.limit(parts[0].strip()))
            elif expr_str.startswith("taylor("):
                parts = expr_str[7:-1].split(",")
                if len(parts) >= 4:
                    return str(self.engine.taylor(parts[0].strip(), parts[1].strip(), float(parts[2].strip()), int(parts[3].strip())))
                return str(self.engine.taylor(parts[0].strip()))
            elif expr_str.startswith("laplace("):
                inner = expr_str[8:-1]
                return str(self.engine.laplace(inner))
            elif expr_str.startswith("ilaplace("):
                inner = expr_str[9:-1]
                return str(self.engine.inverse_laplace(inner))
            elif expr_str.startswith("latex("):
                inner = expr_str[6:-1]
                return str(self.engine.to_latex(inner))
            else:
                result = self.engine.parse_expression(expr_str)
                return str(result)
        except Exception as e:
            return f"Error: {str(e)}"


class GraphingWidget(QWidget):
    """Widget del modo Graficas con Matplotlib."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.engine = EquaEngine()
        self.functions = []  # List of (expr_str, color)
        self._setup_ui()
    
    def _setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(12)
        
        header = QLabel("Graphing Mode")
        header.setStyleSheet(f"""
            font-size: 24px;
            font-weight: bold;
            color: {AuroraPalette.SECONDARY};
        """)
        layout.addWidget(header)
        
        # Function Input
        input_frame = QFrame()
        input_frame.setStyleSheet(f"""
            QFrame {{
                background-color: {AuroraPalette.BACKGROUND_LIGHT};
                border: 1px solid {AuroraPalette.BORDER};
                border-radius: 8px;
                padding: 8px;
            }}
        """)
        input_layout = QHBoxLayout(input_frame)
        
        label = QLabel("f(x) =")
        label.setStyleSheet(f"color: {AuroraPalette.SECONDARY}; font-weight: bold;")
        input_layout.addWidget(label)
        
        self.func_input = QLineEdit()
        self.func_input.setPlaceholderText("ej: sin(x), x^2, exp(-x^2)")
        self.func_input.setStyleSheet(f"""
            QLineEdit {{
                background-color: {AuroraPalette.BACKGROUND_DARK};
                border: none;
                font-family: 'Consolas', monospace;
                font-size: 14px;
                padding: 8px;
            }}
        """)
        self.func_input.returnPressed.connect(self._add_function)
        input_layout.addWidget(self.func_input, stretch=1)
        
        add_btn = QPushButton("Add")
        add_btn.setProperty("class", "primary")
        add_btn.clicked.connect(self._add_function)
        input_layout.addWidget(add_btn)
        
        clear_btn = QPushButton("Clear All")
        clear_btn.clicked.connect(self._clear_functions)
        input_layout.addWidget(clear_btn)
        
        layout.addWidget(input_frame)
        
        # Matplotlib Canvas
        try:
            from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
            from matplotlib.figure import Figure
            
            self.figure = Figure(figsize=(8, 6), facecolor=AuroraPalette.BACKGROUND_DARK)
            self.ax = self.figure.add_subplot(111)
            self._style_axes()
            
            self.canvas = FigureCanvasQTAgg(self.figure)
            self.canvas.setStyleSheet("border-radius: 8px;")
            layout.addWidget(self.canvas, stretch=1)
        except ImportError:
            placeholder = QLabel("Matplotlib no instalado.\npip install matplotlib")
            placeholder.setAlignment(Qt.AlignmentFlag.AlignCenter)
            placeholder.setStyleSheet(f"color: {AuroraPalette.TEXT_SECONDARY}; font-size: 16px;")
            layout.addWidget(placeholder, stretch=1)
            self.canvas = None
        
        # Functions List
        self.func_list = QListWidget()
        self.func_list.setMaximumHeight(100)
        self.func_list.setStyleSheet(f"""
            QListWidget {{
                background-color: {AuroraPalette.BACKGROUND_DARK};
                border: 1px solid {AuroraPalette.BORDER};
                border-radius: 8px;
            }}
        """)
        layout.addWidget(self.func_list)
    
    def _style_axes(self):
        """Aplica estilo Aurora al grafico."""
        self.ax.set_facecolor(AuroraPalette.BACKGROUND_DARK)
        self.ax.tick_params(colors=AuroraPalette.TEXT_SECONDARY)
        self.ax.spines['bottom'].set_color(AuroraPalette.BORDER)
        self.ax.spines['top'].set_color(AuroraPalette.BORDER)
        self.ax.spines['left'].set_color(AuroraPalette.BORDER)
        self.ax.spines['right'].set_color(AuroraPalette.BORDER)
        self.ax.grid(True, alpha=0.2, color=AuroraPalette.BORDER)
        self.ax.axhline(y=0, color=AuroraPalette.BORDER, linewidth=0.5)
        self.ax.axvline(x=0, color=AuroraPalette.BORDER, linewidth=0.5)
    
    def _add_function(self):
        """Agrega una funcion al grafico."""
        expr_str = self.func_input.text().strip()
        if not expr_str or not self.canvas:
            return
        
        import numpy as np
        colors = ['#FF6B9D', '#4ECDC4', '#FFE66D', '#95E1D3', '#F38181']
        color = colors[len(self.functions) % len(colors)]
        
        try:
            x = np.linspace(-10, 10, 500)
            expr = self.engine.parse_expression(expr_str)
            from sympy import lambdify, Symbol
            x_sym = Symbol('x')
            f = lambdify(x_sym, expr, modules=['numpy'])
            y = f(x)
            
            self.ax.plot(x, y, color=color, linewidth=2, label=expr_str)
            self.ax.legend(loc='upper right', facecolor=AuroraPalette.BACKGROUND_LIGHT)
            self.ax.set_xlim(-10, 10)
            self.ax.set_ylim(-10, 10)
            self.canvas.draw()
            
            self.functions.append((expr_str, color))
            self.func_list.addItem(f"• {expr_str}")
            self.func_input.clear()
        except Exception as e:
            self.func_list.addItem(f"Error: {str(e)}")
    
    def _clear_functions(self):
        """Limpia todas las funciones."""
        if self.canvas:
            self.ax.clear()
            self._style_axes()
            self.canvas.draw()
        self.functions.clear()
        self.func_list.clear()


class MatrixWidget(QWidget):
    """Widget del modo Matrices con dos matrices (A y B) y operaciones combinadas."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.engine = EquaEngine()
        # Matrix A
        self.rows_a = 3
        self.cols_a = 3
        self.cells_a = []
        # Matrix B
        self.rows_b = 3
        self.cols_b = 3
        self.cells_b = []
        self._setup_ui()
    
    def _setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(12)
        
        header = QLabel("Matrix Mode")
        header.setStyleSheet(f"""
            font-size: 24px;
            font-weight: bold;
            color: {AuroraPalette.SECONDARY};
        """)
        layout.addWidget(header)
        
        # Matrices Container (A and B side by side)
        matrices_frame = QFrame()
        matrices_layout = QHBoxLayout(matrices_frame)
        matrices_layout.setSpacing(24)
        
        # Matrix A Section
        self.matrix_a_widget = self._create_matrix_section("A", "a")
        matrices_layout.addWidget(self.matrix_a_widget)
        
        # Matrix B Section
        self.matrix_b_widget = self._create_matrix_section("B", "b")
        matrices_layout.addWidget(self.matrix_b_widget)
        
        matrices_layout.addStretch()
        layout.addWidget(matrices_frame)
        
        # Build initial grids
        self._build_matrix_grid("a")
        self._build_matrix_grid("b")
        
        # Single Matrix Operations
        single_ops_label = QLabel("Single Matrix Operations:")
        single_ops_label.setStyleSheet("font-weight: bold; margin-top: 8px;")
        layout.addWidget(single_ops_label)
        
        single_ops_frame = QFrame()
        single_ops_layout = QHBoxLayout(single_ops_frame)
        single_ops_layout.setContentsMargins(0, 0, 0, 0)
        
        # Selector for which matrix
        single_ops_layout.addWidget(QLabel("On:"))
        self.matrix_selector = QComboBox()
        self.matrix_selector.addItems(["Matrix A", "Matrix B"])
        self.matrix_selector.setFixedWidth(100)
        single_ops_layout.addWidget(self.matrix_selector)
        
        single_operations = [
            ("det", self._calc_det),
            ("inv", self._calc_inv),
            ("T", self._calc_transpose),
            ("eigenvals", self._calc_eigenvals),
            ("rref", self._calc_rref),
            ("rank", self._calc_rank),
            ("trace", self._calc_trace),
        ]
        
        for label, func in single_operations:
            btn = QPushButton(label)
            btn.setProperty("class", "secondary")
            btn.setFixedWidth(70)
            btn.clicked.connect(func)
            single_ops_layout.addWidget(btn)
        
        single_ops_layout.addStretch()
        layout.addWidget(single_ops_frame)
        
        # Combined Operations (A op B)
        combined_ops_label = QLabel("Combined Operations (A ⊕ B):")
        combined_ops_label.setStyleSheet("font-weight: bold; margin-top: 8px;")
        layout.addWidget(combined_ops_label)
        
        combined_ops_frame = QFrame()
        combined_ops_layout = QHBoxLayout(combined_ops_frame)
        combined_ops_layout.setContentsMargins(0, 0, 0, 0)
        
        combined_operations = [
            ("A + B", self._calc_add),
            ("A - B", self._calc_sub),
            ("A × B", self._calc_mul),
            ("A ÷ B", self._calc_div),  # A × inv(B)
            ("A | B", self._calc_augment),  # Augmented matrix
        ]
        
        for label, func in combined_operations:
            btn = QPushButton(label)
            btn.setProperty("class", "primary")
            btn.setFixedWidth(70)
            btn.clicked.connect(func)
            combined_ops_layout.addWidget(btn)
        
        # Copy result buttons
        combined_ops_layout.addWidget(QLabel("  Copy to:"))
        copy_a_btn = QPushButton("→ A")
        copy_a_btn.clicked.connect(lambda: self._copy_result_to("a"))
        combined_ops_layout.addWidget(copy_a_btn)
        copy_b_btn = QPushButton("→ B")
        copy_b_btn.clicked.connect(lambda: self._copy_result_to("b"))
        combined_ops_layout.addWidget(copy_b_btn)
        
        combined_ops_layout.addStretch()
        layout.addWidget(combined_ops_frame)
        
        # Results Area
        self.results = QTextEdit()
        self.results.setReadOnly(True)
        self.results.setMaximumHeight(180)
        self.results.setPlaceholderText("Resultados aparecen aquí...")
        self.results.setStyleSheet(f"""
            QTextEdit {{
                font-family: 'Consolas', monospace;
                font-size: 14px;
                background-color: {AuroraPalette.BACKGROUND_DARK};
                border: 1px solid {AuroraPalette.BORDER};
                border-radius: 8px;
                padding: 8px;
            }}
        """)
        layout.addWidget(self.results)
        
        # Store last result for copy
        self.last_result = None
    
    def _create_matrix_section(self, name: str, key: str) -> QFrame:
        """Creates a matrix section with label, size controls, and grid."""
        section = QFrame()
        section.setStyleSheet(f"""
            QFrame {{
                background-color: {AuroraPalette.BACKGROUND_DARK};
                border: 1px solid {AuroraPalette.BORDER};
                border-radius: 8px;
                padding: 12px;
            }}
        """)
        layout = QVBoxLayout(section)
        layout.setSpacing(8)
        
        # Header
        header = QLabel(f"Matrix {name}")
        header.setStyleSheet(f"font-size: 16px; font-weight: bold; color: {AuroraPalette.PRIMARY};")
        layout.addWidget(header)
        
        # Size controls
        size_frame = QFrame()
        size_frame.setStyleSheet("background: transparent; border: none;")
        size_layout = QHBoxLayout(size_frame)
        size_layout.setContentsMargins(0, 0, 0, 0)
        
        rows_input = QLineEdit("3")
        rows_input.setFixedWidth(40)
        rows_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        setattr(self, f"rows_input_{key}", rows_input)
        
        cols_input = QLineEdit("3")
        cols_input.setFixedWidth(40)
        cols_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        setattr(self, f"cols_input_{key}", cols_input)
        
        size_layout.addWidget(rows_input)
        size_layout.addWidget(QLabel("×"))
        size_layout.addWidget(cols_input)
        
        apply_btn = QPushButton("✓")
        apply_btn.setFixedWidth(30)
        apply_btn.clicked.connect(lambda: self._resize_matrix(key))
        size_layout.addWidget(apply_btn)
        size_layout.addStretch()
        
        layout.addWidget(size_frame)
        
        # Grid container
        grid_container = QFrame()
        grid_container.setStyleSheet("background: transparent; border: none;")
        grid_layout = QHBoxLayout(grid_container)
        grid_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        setattr(self, f"grid_layout_{key}", grid_layout)
        setattr(self, f"grid_container_{key}", grid_container)
        
        layout.addWidget(grid_container)
        return section
    
    def _build_matrix_grid(self, key: str):
        """Builds the matrix grid for A or B."""
        rows = getattr(self, f"rows_{key}")
        cols = getattr(self, f"cols_{key}")
        cells = getattr(self, f"cells_{key}")
        grid_layout = getattr(self, f"grid_layout_{key}")
        
        # Clear existing
        for row in cells:
            for cell in row:
                cell.deleteLater()
        cells.clear()
        
        while grid_layout.count():
            item = grid_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        
        from PyQt6.QtWidgets import QGridLayout
        grid = QWidget()
        grid_inner = QGridLayout(grid)
        grid_inner.setSpacing(3)
        
        for r in range(rows):
            row_cells = []
            for c in range(cols):
                cell = QLineEdit("0")
                cell.setFixedSize(45, 35)
                cell.setAlignment(Qt.AlignmentFlag.AlignCenter)
                cell.setStyleSheet(f"""
                    QLineEdit {{
                        background-color: {AuroraPalette.BACKGROUND_LIGHT};
                        border: 1px solid {AuroraPalette.BORDER};
                        border-radius: 3px;
                        font-family: 'Consolas', monospace;
                        font-size: 12px;
                    }}
                    QLineEdit:focus {{
                        border-color: {AuroraPalette.SECONDARY};
                    }}
                """)
                grid_inner.addWidget(cell, r, c)
                row_cells.append(cell)
            cells.append(row_cells)
        
        grid_layout.addWidget(grid)
        setattr(self, f"cells_{key}", cells)
    
    def _resize_matrix(self, key: str):
        """Resizes a matrix grid."""
        try:
            rows_input = getattr(self, f"rows_input_{key}")
            cols_input = getattr(self, f"cols_input_{key}")
            rows = max(1, min(8, int(rows_input.text())))
            cols = max(1, min(8, int(cols_input.text())))
            setattr(self, f"rows_{key}", rows)
            setattr(self, f"cols_{key}", cols)
            self._build_matrix_grid(key)
        except ValueError:
            pass
    
    def _get_matrix_values(self, key: str):
        """Gets matrix values as list of lists."""
        cells = getattr(self, f"cells_{key}")
        values = []
        for row in cells:
            row_vals = []
            for cell in row:
                try:
                    row_vals.append(float(cell.text()))
                except ValueError:
                    row_vals.append(0)
            values.append(row_vals)
        return values
    
    def _get_sympy_matrix(self, key: str):
        """Gets SymPy Matrix object."""
        from sympy import Matrix
        return Matrix(self._get_matrix_values(key))
    
    def _selected_matrix_key(self) -> str:
        """Returns 'a' or 'b' based on selector."""
        return "a" if self.matrix_selector.currentIndex() == 0 else "b"
    
    def _selected_matrix_name(self) -> str:
        """Returns 'A' or 'B' based on selector."""
        return "A" if self.matrix_selector.currentIndex() == 0 else "B"
    
    # Single matrix operations
    def _calc_det(self):
        try:
            key = self._selected_matrix_key()
            name = self._selected_matrix_name()
            m = self._get_sympy_matrix(key)
            result = m.det()
            self.results.append(f">>> det({name}) = {result}\n")
        except Exception as e:
            self.results.append(f"Error: {e}\n")
    
    def _calc_inv(self):
        try:
            key = self._selected_matrix_key()
            name = self._selected_matrix_name()
            m = self._get_sympy_matrix(key)
            result = m.inv()
            self.last_result = result
            self.results.append(f">>> inv({name}) =\n{result}\n")
        except Exception as e:
            self.results.append(f"Error: {e}\n")
    
    def _calc_transpose(self):
        try:
            key = self._selected_matrix_key()
            name = self._selected_matrix_name()
            m = self._get_sympy_matrix(key)
            result = m.T
            self.last_result = result
            self.results.append(f">>> {name}ᵀ =\n{result}\n")
        except Exception as e:
            self.results.append(f"Error: {e}\n")
    
    def _calc_eigenvals(self):
        try:
            key = self._selected_matrix_key()
            name = self._selected_matrix_name()
            m = self._get_sympy_matrix(key)
            result = m.eigenvals()
            self.results.append(f">>> eigenvals({name}) = {result}\n")
        except Exception as e:
            self.results.append(f"Error: {e}\n")
    
    def _calc_rref(self):
        try:
            key = self._selected_matrix_key()
            name = self._selected_matrix_name()
            m = self._get_sympy_matrix(key)
            result, pivots = m.rref()
            self.last_result = result
            self.results.append(f">>> rref({name}) =\n{result}\nPivots: {pivots}\n")
        except Exception as e:
            self.results.append(f"Error: {e}\n")
    
    def _calc_rank(self):
        try:
            key = self._selected_matrix_key()
            name = self._selected_matrix_name()
            m = self._get_sympy_matrix(key)
            result = m.rank()
            self.results.append(f">>> rank({name}) = {result}\n")
        except Exception as e:
            self.results.append(f"Error: {e}\n")
    
    def _calc_trace(self):
        try:
            key = self._selected_matrix_key()
            name = self._selected_matrix_name()
            m = self._get_sympy_matrix(key)
            result = m.trace()
            self.results.append(f">>> trace({name}) = {result}\n")
        except Exception as e:
            self.results.append(f"Error: {e}\n")
    
    # Combined operations
    def _calc_add(self):
        try:
            a = self._get_sympy_matrix("a")
            b = self._get_sympy_matrix("b")
            result = a + b
            self.last_result = result
            self.results.append(f">>> A + B =\n{result}\n")
        except Exception as e:
            self.results.append(f"Error: {e}\n")
    
    def _calc_sub(self):
        try:
            a = self._get_sympy_matrix("a")
            b = self._get_sympy_matrix("b")
            result = a - b
            self.last_result = result
            self.results.append(f">>> A - B =\n{result}\n")
        except Exception as e:
            self.results.append(f"Error: {e}\n")
    
    def _calc_mul(self):
        try:
            a = self._get_sympy_matrix("a")
            b = self._get_sympy_matrix("b")
            result = a * b
            self.last_result = result
            self.results.append(f">>> A × B =\n{result}\n")
        except Exception as e:
            self.results.append(f"Error: {e}\n")
    
    def _calc_div(self):
        try:
            a = self._get_sympy_matrix("a")
            b = self._get_sympy_matrix("b")
            result = a * b.inv()
            self.last_result = result
            self.results.append(f">>> A × B⁻¹ =\n{result}\n")
        except Exception as e:
            self.results.append(f"Error: {e}\n")
    
    def _calc_augment(self):
        try:
            a = self._get_sympy_matrix("a")
            b = self._get_sympy_matrix("b")
            result = a.row_join(b)
            self.last_result = result
            self.results.append(f">>> [A | B] =\n{result}\n")
        except Exception as e:
            self.results.append(f"Error: {e}\n")
    
    def _copy_result_to(self, key: str):
        """Copies last result to matrix A or B."""
        if self.last_result is None:
            self.results.append("No result to copy.\n")
            return
        try:
            rows, cols = self.last_result.shape
            setattr(self, f"rows_{key}", rows)
            setattr(self, f"cols_{key}", cols)
            getattr(self, f"rows_input_{key}").setText(str(rows))
            getattr(self, f"cols_input_{key}").setText(str(cols))
            self._build_matrix_grid(key)
            
            cells = getattr(self, f"cells_{key}")
            for r in range(rows):
                for c in range(cols):
                    cells[r][c].setText(str(float(self.last_result[r, c])))
            
            name = "A" if key == "a" else "B"
            self.results.append(f"Result copied to Matrix {name}\n")
        except Exception as e:
            self.results.append(f"Error copying: {e}\n")


class Sidebar(QWidget):
    """Sidebar con navegacion de modos."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedWidth(200)
        self._setup_ui()
    
    def _setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(8, 16, 8, 16)
        layout.setSpacing(4)
        
        # Logo/Title
        title = QLabel("Binary EquaLab")
        title.setStyleSheet(f"""
            font-size: 16px;
            font-weight: bold;
            color: {AuroraPalette.SECONDARY};
            padding: 16px 8px;
        """)
        layout.addWidget(title)
        
        # Navigation List
        self.nav_list = QListWidget()
        self.nav_list.setStyleSheet(f"""
            QListWidget {{
                background: transparent;
                border: none;
            }}
            QListWidget::item {{
                padding: 12px 16px;
                border-radius: 8px;
                margin: 2px 0;
            }}
            QListWidget::item:selected {{
                background-color: {AuroraPalette.BACKGROUND_LIGHT};
                border-left: 3px solid {AuroraPalette.SECONDARY};
            }}
            QListWidget::item:hover {{
                background-color: {AuroraPalette.BACKGROUND_DARK};
            }}
        """)
        
        modes = [
            ("Console", "console"),
            ("Graphing", "graphing"),
            ("Matrix", "matrix"),
        ]
        
        for label, mode_id in modes:
            item = QListWidgetItem(label)
            item.setData(Qt.ItemDataRole.UserRole, mode_id)
            self.nav_list.addItem(item)
        
        self.nav_list.setCurrentRow(0)
        layout.addWidget(self.nav_list)
        
        layout.addStretch()
        
        # Version
        version = QLabel(f"v{AppConfig.VERSION}")
        version.setStyleSheet(f"color: {AuroraPalette.TEXT_MUTED}; font-size: 11px;")
        version.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(version)


class MainWindow(QMainWindow):
    """Ventana principal de Binary EquaLab."""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle(AppConfig.APP_NAME)
        self.setMinimumSize(*AppConfig.WINDOW_SIZE)
        self._setup_ui()
    
    def _setup_ui(self):
        # Central Widget
        central = QWidget()
        self.setCentralWidget(central)
        
        main_layout = QHBoxLayout(central)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Sidebar
        self.sidebar = Sidebar()
        self.sidebar.nav_list.currentRowChanged.connect(self._on_mode_changed)
        main_layout.addWidget(self.sidebar)
        
        # Separator
        separator = QFrame()
        separator.setFixedWidth(1)
        separator.setStyleSheet(f"background-color: {AuroraPalette.BORDER};")
        main_layout.addWidget(separator)
        
        # Content Stack
        self.content_stack = QStackedWidget()
        self.content_stack.addWidget(ConsoleWidget())
        self.content_stack.addWidget(GraphingWidget())
        self.content_stack.addWidget(MatrixWidget())
        main_layout.addWidget(self.content_stack, stretch=1)
        
        # Status Bar
        self.status_bar = QStatusBar()
        self.status_bar.setStyleSheet(f"""
            QStatusBar {{
                background-color: {AuroraPalette.BACKGROUND_LIGHT};
                color: {AuroraPalette.TEXT_SECONDARY};
                font-size: 12px;
                padding: 4px 12px;
            }}
        """)
        self.status_bar.showMessage("Listo | Modo: DEG | Tu luz sigue intacta")
        self.setStatusBar(self.status_bar)
    
    def _on_mode_changed(self, index):
        """Cambia el widget visible segun el modo seleccionado."""
        self.content_stack.setCurrentIndex(index)
        modes = ["Console", "Graphing", "Matrix"]
        self.status_bar.showMessage(f"Modo: {modes[index]} | DEG | Tu luz sigue intacta")
