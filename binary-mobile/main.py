
import flet as ft
import sys
import os

# Add binary-cli to path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
cli_path = os.path.join(project_root, "binary-cli")
sys.path.append(cli_path)

try:
    from binary_equalab.engine import MathEngine
    HAS_ENGINE = True
except ImportError:
    HAS_ENGINE = False

from theme import AuroraTheme

class CalculatorView(ft.Column):
    def __init__(self):
        super().__init__()
        # Init Engine
        self.engine = MathEngine() if HAS_ENGINE else None
        
        # UI Elements
        self.result_text = ft.Text(value="0", size=48, text_align="right", weight=ft.FontWeight.BOLD, color=AuroraTheme.TEXT)
        self.formula_text = ft.Text(value="", size=24, text_align="right", color=AuroraTheme.TEXT_DIM, font_family="Roboto Mono")
        
        self.expand = True # Column expands
        self.alignment = ft.MainAxisAlignment.END # Align content to bottom? No, mixed.
        
        # Build UI immediately
        self._build_ui()

    def _build_ui(self):
        # Button Logic
        def on_click(e):
            data = e.control.data
            if data == "AC":
                self.formula_text.value = ""
                self.result_text.value = "0"
            elif data == "⌫":
                self.formula_text.value = self.formula_text.value[:-1]
            elif data == "=":
                try:
                    if self.engine:
                        res = self.engine.evaluate(self.formula_text.value)
                        self.result_text.value = str(res)
                    else:
                        self.result_text.value = "No Engine"
                except:
                    self.result_text.value = "Error"
            else:
                self.formula_text.value += data
            self.update()

        # Grid Definition
        buttons_layout = [
            ["AC", "⌫", "^", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "x", "="],
             ["sin(", "cos(", "tan(", "pi"],
            ["integrar(", "derivar(", "recta(", ")"]
        ]

        grid = ft.Column(spacing=12)

        for row in buttons_layout:
            row_controls = []
            for btn_text in row:
                # Style logic
                bg_color = AuroraTheme.SURFACE_2
                text_color = AuroraTheme.TEXT
                
                if btn_text in ["=", "AC"]:
                    bg_color = AuroraTheme.PRIMARY
                    text_color = "#ffffff"
                elif btn_text in ["/", "*", "-", "+", "^"]:
                    bg_color = AuroraTheme.SURFACE
                    text_color = AuroraTheme.PRIMARY

                row_controls.append(
                    ft.Container(
                        content=ft.Text(value=btn_text, size=22, color=text_color),
                        width=72,
                        height=72,
                        alignment=ft.Alignment(0, 0),
                        bgcolor=bg_color,
                        border_radius=36,
                        on_click=on_click,
                        data=btn_text,
                        ink=True,
                        animate=ft.Animation(100, ft.AnimationCurve.EASE_OUT),
                    )
                )
            grid.controls.append(ft.Row(controls=row_controls, alignment=ft.MainAxisAlignment.CENTER, spacing=12))

        # Define Controls of this Column
        self.controls = [
            ft.Container(
                content=ft.Column(
                    controls=[self.formula_text, self.result_text],
                    alignment=ft.MainAxisAlignment.END,
                    horizontal_alignment=ft.CrossAxisAlignment.END,
                ),
                padding=20,
                height=200,
            ),
            ft.Container(
                content=grid,
                padding=10,
                expand=True,
                alignment=ft.Alignment(0, 1) # Bottom align
            )
        ]

import matplotlib
matplotlib.use("Agg") # Non-interactive backend, faster
import matplotlib.pyplot as plt
import numpy as np
import io
import base64

class GraphView(ft.Column):
    def __init__(self):
        super().__init__()
        self.engine = MathEngine() if HAS_ENGINE else None
        self.expand = True
        
        # Input
        self.input = ft.TextField(
            label="f(x) =", 
            value="sin(x)", 
            color=AuroraTheme.TEXT, 
            border_color=AuroraTheme.PRIMARY,
            on_submit=self.plot
        )
        
        # Chart Container (Image)
        self.chart = ft.Image(
            src="",
            width=400,
            height=300,
            fit="contain",
            visible=False # Hide until plotted
        )
        
        # Init controls
        self.controls = [
            ft.Container(content=self.input, padding=10),
            ft.Container(content=self.chart, expand=True, padding=10, alignment=ft.Alignment(0,0)), 
            ft.Container(
                content=ft.ElevatedButton("Graficar", on_click=self.plot, bgcolor=AuroraTheme.PRIMARY, color="white"),
                alignment=ft.Alignment(0, 0),
                padding=10
            )
        ]
        
    def plot(self, e=None):
        if not self.engine: return
        
        try:
            expr_str = self.input.value
            
            # Use engine parser logic manual
            from sympy import symbols, lambdify
            x = symbols('x')
            expr = self.engine.parse(expr_str)
            f = lambdify(x, expr, modules=['numpy'])
            
            # Generate Data
            x_vals = np.linspace(-10, 10, 400)
            y_vals = f(x_vals) # Might fail for some funcs
            
            # Plot
            fig, ax = plt.subplots(figsize=(8, 6))
            # Style
            fig.patch.set_facecolor(AuroraTheme.SURFACE)
            ax.set_facecolor(AuroraTheme.SURFACE_2)
            ax.tick_params(colors=AuroraTheme.TEXT_DIM, labelcolor=AuroraTheme.TEXT_DIM)
            for spine in ax.spines.values():
                spine.set_color(AuroraTheme.TEXT_DIM)
                
            ax.grid(True, color="#333333", linestyle="--")
            ax.plot(x_vals, y_vals, color=AuroraTheme.PRIMARY, linewidth=2)
            
            # Save to buffer
            buf = io.BytesIO()
            fig.savefig(buf, format="png", bbox_inches='tight')
            plt.close(fig) # Close to free memory
            
            # Update Image
            data = base64.b64encode(buf.getvalue()).decode('utf-8')
            self.chart.src_base64 = data
            self.chart.visible = True
            
            self.update()
            
        except Exception as err:
            self.input.error_text = f"Error: {str(err)}"
            self.input.update()
            print(err)

def main(page: ft.Page):
    # App logic remains
    page.title = "Binary Pocket"
    page.theme = AuroraTheme.theme()
    page.bgcolor = AuroraTheme.BACKGROUND
    page.padding = 0 
    
    # Views
    # Instantiate Views ONCE for performance (Cached Views)
    calc_view = CalculatorView()
    graph_view = GraphView() 
    settings_view = ft.Container(content=ft.Text("Settings", size=20, color="white"), alignment=ft.Alignment(0,0))

    body = ft.Container(content=calc_view, expand=True)

    def change_tab(e):
        idx = e.control.selected_index
        # Manual routing/switching
        new_content = None
        if idx == 0: new_content = calc_view
        elif idx == 1: new_content = graph_view
        elif idx == 2: new_content = settings_view
        
        if new_content != body.content:
            body.content = new_content
            body.update()

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon="calculate_outlined", selected_icon="calculate", label="Calc"),
            ft.NavigationBarDestination(icon="show_chart", label="Graph"),
            ft.NavigationBarDestination(icon="settings_outlined", selected_icon="settings", label="Settings"),
        ],
        on_change=change_tab,
        bgcolor=AuroraTheme.SURFACE,
        indicator_color=AuroraTheme.PRIMARY_DIM,
    )

    page.add(body)

if __name__ == "__main__":
    ft.app(main)
