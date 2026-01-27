
#!/usr/bin/env python3
"""
EquaPy - Mini symbolic calculator (Tkinter + SymPy + Matplotlib)
Designed for Linux (Kali) / Python3.
Save as equapy_calc.py and run: python3 equapy_calc.py

Features:
- Enter a symbolic expression (use 't' as the time variable by default).
- Buttons: Simplify, Expand, Factor, Derivative, Integral, Laplace, Inverse Laplace, Evaluate (numeric), Plot.
- Uses SymPy for symbolic work and Matplotlib for plotting (embedded in Tkinter).
- Minimal error handling and helpful messages in the output panel.

Notes:
- Requires: sympy, matplotlib, numpy
  Install with: pip3 install sympy matplotlib numpy
- For Laplace transforms we use sympy.laplace_transform and inverse_laplace_transform.
- This is a lightweight educational tool — not a full MATLAB replacement.
"""

import sys
import traceback
import math
import threading

try:
    import tkinter as tk
    from tkinter import ttk, messagebox
except Exception as e:
    print("Tkinter is required. On Debian/Ubuntu/Kali: sudo apt-get install python3-tk")
    raise

try:
    import sympy as sp
except Exception as e:
    print("SymPy is required. Install with: pip3 install sympy")
    raise

try:
    import numpy as np
    import matplotlib
    matplotlib.use('TkAgg')
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    from matplotlib.figure import Figure
except Exception as e:
    print("Matplotlib / NumPy are required. Install with: pip3 install matplotlib numpy")
    raise

# Symbols
t, s = sp.symbols('t s')

class EquaPyApp:
    def __init__(self, root):
        self.root = root
        root.title("EquaPy - Mini symbolic calculator")
        root.geometry("900x600")

        # Top frame for input
        top = ttk.Frame(root, padding=8)
        top.pack(side=tk.TOP, fill=tk.X)

        ttk.Label(top, text="Expr (use 't' as variable)").pack(side=tk.LEFT)
        self.expr_var = tk.StringVar(value="sin(2*t) + t*cos(3*t)")
        self.expr_entry = ttk.Entry(top, textvariable=self.expr_var, width=60)
        self.expr_entry.pack(side=tk.LEFT, padx=6)

        ttk.Label(top, text="Variable:").pack(side=tk.LEFT, padx=(10,0))
        self.var_choice = tk.StringVar(value='t')
        ttk.Combobox(top, textvariable=self.var_choice, values=['t','x','tau']).pack(side=tk.LEFT, padx=4)

        # Buttons frame
        btns = ttk.Frame(root, padding=6)
        btns.pack(side=tk.TOP, fill=tk.X)

        actions = [
            ("Simplify", self.do_simplify),
            ("Expand", self.do_expand),
            ("Factor", self.do_factor),
            ("Derivative", self.do_diff),
            ("Integral", self.do_integrate),
            ("Laplace", self.do_laplace),
            ("Inv Laplace", self.do_ilaplace),
            ("Evaluate (num)", self.do_eval),
            ("Plot", self.do_plot)
        ]

        for (label, cmd) in actions:
            b = ttk.Button(btns, text=label, command=lambda c=cmd: threading.Thread(target=c).start())
            b.pack(side=tk.LEFT, padx=4, pady=4)

        # Output / results area
        outframe = ttk.Frame(root, padding=6)
        outframe.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        left = ttk.Frame(outframe)
        left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        ttk.Label(left, text="Result / Console").pack(anchor=tk.W)
        self.output = tk.Text(left, wrap=tk.WORD, width=55)
        self.output.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar = ttk.Scrollbar(left, command=self.output.yview)
        scrollbar.pack(side=tk.LEFT, fill=tk.Y)
        self.output['yscrollcommand'] = scrollbar.set

        # Right: plot area
        right = ttk.Frame(outframe)
        right.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        ttk.Label(right, text="Plot area (real t)").pack(anchor=tk.W)
        self.fig = Figure(figsize=(4,3))
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=right)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # status bar
        self.status = tk.StringVar(value="Ready")
        statusbar = ttk.Label(root, textvariable=self.status, relief=tk.SUNKEN, anchor=tk.W)
        statusbar.pack(side=tk.BOTTOM, fill=tk.X)

    def write(self, text):
        self.output.insert(tk.END, str(text) + "\n")
        self.output.see(tk.END)

    def clear_output(self):
        self.output.delete(1.0, tk.END)

    def parse_expr(self):
        raw = self.expr_var.get().strip()
        if not raw:
            raise ValueError("Expression empty")
        # Try to parse with sympy; sympify is powerful but be cautious with security if exposing.
        # Replace common exponent caret to **
        raw = raw.replace('^', '**')
        expr = sp.sympify(raw, locals={'t':t, 's':s, 'sin':sp.sin, 'cos':sp.cos, 'exp':sp.exp, 'sinh':sp.sinh, 'cosh':sp.cosh, 'log':sp.log, 'sqrt':sp.sqrt, 'pi':sp.pi})
        return expr

    def do_simplify(self):
        try:
            self.clear_output()
            expr = self.parse_expr()
            res = sp.simplify(expr)
            self.write("Simplified: " + str(res))
            self.status.set("Simplified")
        except Exception as e:
            self.write("Error in simplify: " + str(e))
            traceback.print_exc(file=sys.stdout)

    def do_expand(self):
        try:
            self.clear_output()
            expr = self.parse_expr()
            res = sp.expand(expr)
            self.write("Expanded: " + str(res))
            self.status.set("Expanded")
        except Exception as e:
            self.write("Error in expand: " + str(e))
            traceback.print_exc(file=sys.stdout)

    def do_factor(self):
        try:
            self.clear_output()
            expr = self.parse_expr()
            res = sp.factor(expr)
            self.write("Factored: " + str(res))
            self.status.set("Factored")
        except Exception as e:
            self.write("Error in factor: " + str(e))
            traceback.print_exc(file=sys.stdout)

    def do_diff(self):
        try:
            self.clear_output()
            expr = self.parse_expr()
            varname = self.var_choice.get().strip()
            var = t if varname=='t' else sp.symbols(varname)
            res = sp.diff(expr, var)
            self.write("d/d{}: {}".format(varname, res))
            self.status.set("Differentiated")
        except Exception as e:
            self.write("Error in derivative: " + str(e))
            traceback.print_exc(file=sys.stdout)

    def do_integrate(self):
        try:
            self.clear_output()
            expr = self.parse_expr()
            varname = self.var_choice.get().strip()
            var = t if varname=='t' else sp.symbols(varname)
            res = sp.integrate(expr, var)
            self.write("Integral wrt {}: {}".format(varname, res))
            self.status.set("Integrated")
        except Exception as e:
            self.write("Error in integrate: " + str(e))
            traceback.print_exc(file=sys.stdout)

    def do_laplace(self):
        try:
            self.clear_output()
            expr = self.parse_expr()
            # We assume time variable is t and transform variable is s
            res = sp.laplace_transform(expr, t, s, noconds=True)
            self.write("Laplace F(s): " + str(res))
            self.status.set("Laplace done")
        except Exception as e:
            self.write("Error in Laplace: " + str(e))
            traceback.print_exc(file=sys.stdout)

    def do_ilaplace(self):
        try:
            self.clear_output()
            # Parse expression in 's' (user must enter in terms of s)
            raw = self.expr_var.get().strip().replace('^','**')
            if not raw:
                raise ValueError("Expression empty")
            expr = sp.sympify(raw, locals={'s':s, 't':t, 'pi':sp.pi})
            res = sp.inverse_laplace_transform(expr, s, t)
            self.write("Inverse Laplace f(t): " + str(res))
            self.status.set("Inverse Laplace done")
        except Exception as e:
            self.write("Error in inverse Laplace: " + str(e))
            traceback.print_exc(file=sys.stdout)

    def do_eval(self):
        try:
            self.clear_output()
            expr = self.parse_expr()
            # numerical evaluation: ask user for numeric value of variable
            varname = self.var_choice.get().strip()
            val = simple_input_dialog(self.root, "Numeric evaluation", f"Value for {varname}:", "1.0")
            if val is None:
                return
            v = float(val)
            res = float(sp.N(expr.subs({t: v}))) if varname=='t' else float(sp.N(expr.subs({sp.symbols(varname):v})))
            self.write("Numeric eval at {}={}: {}".format(varname, v, res))
            self.status.set("Evaluated")
        except Exception as e:
            self.write("Error in evaluate: " + str(e))
            traceback.print_exc(file=sys.stdout)

    def do_plot(self):
        try:
            self.clear_output()
            expr = self.parse_expr()
            varname = self.var_choice.get().strip()
            var = t if varname=='t' else sp.symbols(varname)
            # Convert to a numpy-callable function
            f_lamb = sp.lambdify(var, expr, modules=['numpy','math'])
            # Domain from -10 to 10 by default, but prefer positive for many signals
            start = simple_input_dialog(self.root, "Plot range", "Start (numeric):", "0.0")
            if start is None: return
            stop = simple_input_dialog(self.root, "Plot range", "Stop (numeric):", "10.0")
            if stop is None: return
            a = float(start); b = float(stop)
            xs = np.linspace(a, b, 400)
            ys = f_lamb(xs)
            # Clear and plot
            self.ax.clear()
            self.ax.plot(xs, ys)
            self.ax.set_xlabel(varname)
            self.ax.set_title(str(expr))
            self.canvas.draw()
            self.write("Plotted on [{} , {}]".format(a, b))
            self.status.set("Plotted")
        except Exception as e:
            self.write("Error in plot: " + str(e))
            traceback.print_exc(file=sys.stdout)

def simple_input_dialog(root, title, prompt, default=""):
    dialog = tk.Toplevel(root)
    dialog.title(title)
    dialog.geometry("300x100")
    tk.Label(dialog, text=prompt).pack(pady=6)
    var = tk.StringVar(value=default)
    entry = ttk.Entry(dialog, textvariable=var)
    entry.pack(padx=8, fill=tk.X)
    result = {'value': None}

    def on_ok():
        result['value'] = var.get()
        dialog.destroy()

    def on_cancel():
        dialog.destroy()

    btns = ttk.Frame(dialog)
    btns.pack(pady=6)
    ttk.Button(btns, text="OK", command=on_ok).pack(side=tk.LEFT, padx=6)
    ttk.Button(btns, text="Cancel", command=on_cancel).pack(side=tk.LEFT, padx=6)

    dialog.transient(root)
    dialog.grab_set()
    root.wait_window(dialog)
    return result['value']

def main():
    root = tk.Tk()
    app = EquaPyApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
