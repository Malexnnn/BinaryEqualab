"""
EquaCore - High-performance symbolic and numerical computation
Python wrapper for C++ engine using GiNaC and Eigen
"""

try:
    from ._equacore import (
        Expr,
        symbol,
        matrix,
        vector,
        add,
        multiply,
        scale,
        transpose,
        inverse,
        determinant,
        rank,
        lu,
        qr,
        svd,
        eigen,
        solve,
        rref,
        null_space,
        column_space,
        __version__,
    )
    
    NATIVE_ENGINE = True
    
except ImportError:
    # Fallback to SymPy if C++ engine not compiled
    import warnings
    warnings.warn("EquaCore C++ engine not found, falling back to SymPy (slower)")
    
    from sympy import (
        Symbol as symbol,
        expand,
        simplify,
        factor,
        diff,
        integrate,
        solve,
        latex,
    )
    import numpy as np
    
    NATIVE_ENGINE = False
    __version__ = "1.0.0-fallback"
    
    # Provide compatible API using SymPy/NumPy
    class Expr:
        """SymPy-based fallback for Expression class"""
        def __init__(self, expr_str_or_val):
            if isinstance(expr_str_or_val, str):
                from sympy.parsing.sympy_parser import parse_expr
                self._expr = parse_expr(expr_str_or_val)
            else:
                from sympy import sympify
                self._expr = sympify(expr_str_or_val)
        
        def expand(self): return Expr(self._expr.expand())
        def simplify(self): return Expr(self._expr.simplify())
        def factor(self): return Expr(self._expr.factor())
        def diff(self, var, n=1): return Expr(self._expr.diff(Symbol(var), n))
        def integrate(self, var): return Expr(self._expr.integrate(Symbol(var)))
        def subs(self, var, val): return Expr(self._expr.subs(Symbol(var), val))
        def to_latex(self): return latex(self._expr)
        def __str__(self): return str(self._expr)
        def __repr__(self): return f"Expr({self._expr})"
    
    # NumPy-based matrix functions (fallback)
    def matrix(data): return np.array(data)
    def vector(data): return np.array(data)
    def add(a, b): return a + b
    def multiply(a, b): return a @ b
    def scale(m, s): return m * s
    def transpose(m): return m.T
    def inverse(m): return np.linalg.inv(m)
    def determinant(m): return np.linalg.det(m)
    def rank(m): return np.linalg.matrix_rank(m)
    def lu(m):
        from scipy.linalg import lu as scipy_lu
        return scipy_lu(m)
    def qr(m): return np.linalg.qr(m)
    def svd(m): return np.linalg.svd(m)
    def eigen(m): return np.linalg.eigh(m)
    def solve(a, b): return np.linalg.solve(a, b)
    def rref(m):
        from sympy import Matrix
        return np.array(Matrix(m).rref()[0].tolist(), dtype=float)
    def null_space(m):
        from scipy.linalg import null_space as scipy_null
        return scipy_null(m)
    def column_space(m):
        q, r = np.linalg.qr(m)
        return q[:, :np.linalg.matrix_rank(m)]


# Convenience exports
__all__ = [
    'Expr',
    'symbol',
    'matrix',
    'vector',
    'add',
    'multiply', 
    'scale',
    'transpose',
    'inverse',
    'determinant',
    'rank',
    'lu',
    'qr',
    'svd',
    'eigen',
    'solve',
    'rref',
    'null_space',
    'column_space',
    'NATIVE_ENGINE',
    '__version__',
]
