/**
 * EquaCore - Python Bindings
 * Uses pybind11 to expose C++ functions to Python
 */

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/eigen.h>

#include "equacore/symbolic.hpp"
#include "equacore/linear.hpp"

namespace py = pybind11;

// Wrapper class for GiNaC expressions to expose to Python
class PyExpression {
public:
    GiNaC::ex expr;
    static GiNaC::symtab symbols;
    
    PyExpression() : expr(0) {}
    PyExpression(const GiNaC::ex& e) : expr(e) {}
    PyExpression(const std::string& s) : expr(equacore::parse(s, symbols)) {}
    PyExpression(double val) : expr(val) {}
    
    static GiNaC::symbol get_symbol(const std::string& name) {
        if (symbols.find(name) == symbols.end()) {
            symbols[name] = GiNaC::symbol(name);
        }
        return GiNaC::ex_to<GiNaC::symbol>(symbols[name]);
    }
    
    PyExpression expand() const { return PyExpression(equacore::expand(expr)); }
    PyExpression simplify() const { return PyExpression(equacore::simplify(expr)); }
    PyExpression factor() const { return PyExpression(equacore::factor(expr)); }
    
    PyExpression diff(const std::string& var, int n = 1) const {
        return PyExpression(equacore::diff(expr, get_symbol(var), n));
    }
    
    PyExpression integrate(const std::string& var) const {
        return PyExpression(equacore::integrate(expr, get_symbol(var)));
    }
    
    PyExpression subs(const std::string& var, double value) const {
        return PyExpression(equacore::substitute(expr, get_symbol(var), value));
    }
    
    std::string to_latex() const { return equacore::to_latex(expr); }
    std::string __str__() const { return equacore::to_string(expr); }
    std::string __repr__() const { return "Expr(" + equacore::to_string(expr) + ")"; }
    
    // Arithmetic operators
    PyExpression operator+(const PyExpression& other) const {
        return PyExpression(expr + other.expr);
    }
    PyExpression operator-(const PyExpression& other) const {
        return PyExpression(expr - other.expr);
    }
    PyExpression operator*(const PyExpression& other) const {
        return PyExpression(expr * other.expr);
    }
    PyExpression operator/(const PyExpression& other) const {
        return PyExpression(expr / other.expr);
    }
    PyExpression operator-() const {
        return PyExpression(-expr);
    }
    PyExpression pow(const PyExpression& exp) const {
        return PyExpression(GiNaC::pow(expr, exp.expr));
    }
};

GiNaC::symtab PyExpression::symbols;

PYBIND11_MODULE(_equacore, m) {
    m.doc() = "EquaCore - High-performance symbolic and numerical computation";
    
    // Expression class
    py::class_<PyExpression>(m, "Expr")
        .def(py::init<>())
        .def(py::init<const std::string&>())
        .def(py::init<double>())
        .def("expand", &PyExpression::expand, "Expand expression")
        .def("simplify", &PyExpression::simplify, "Simplify expression")
        .def("factor", &PyExpression::factor, "Factor expression")
        .def("diff", &PyExpression::diff, "Differentiate", 
             py::arg("var"), py::arg("n") = 1)
        .def("integrate", &PyExpression::integrate, "Integrate")
        .def("subs", &PyExpression::subs, "Substitute value")
        .def("to_latex", &PyExpression::to_latex, "Convert to LaTeX")
        .def("__str__", &PyExpression::__str__)
        .def("__repr__", &PyExpression::__repr__)
        .def("__add__", &PyExpression::operator+)
        .def("__sub__", &PyExpression::operator-)
        .def("__mul__", &PyExpression::operator*)
        .def("__truediv__", &PyExpression::operator/)
        .def("__neg__", &PyExpression::operator-)
        .def("__pow__", &PyExpression::pow);
    
    // Convenience function to create symbols
    m.def("symbol", [](const std::string& name) {
        return PyExpression(PyExpression::get_symbol(name));
    }, "Create a symbolic variable");
    
    // Linear algebra functions (direct NumPy interop via Eigen)
    m.def("matrix", &equacore::create_matrix, "Create matrix from 2D list");
    m.def("vector", &equacore::create_vector, "Create vector from list");
    m.def("add", py::overload_cast<const equacore::MatrixXd&, const equacore::MatrixXd&>(&equacore::add), "Matrix addition");
    m.def("multiply", py::overload_cast<const equacore::MatrixXd&, const equacore::MatrixXd&>(&equacore::multiply), "Matrix multiplication");
    m.def("scale", &equacore::scale, "Scalar multiplication");
    m.def("transpose", &equacore::transpose, "Matrix transpose");
    m.def("inverse", &equacore::inverse, "Matrix inverse");
    m.def("determinant", &equacore::determinant, "Matrix determinant");
    m.def("rank", &equacore::rank, "Matrix rank");
    m.def("lu", &equacore::lu_decomposition, "LU decomposition, returns (L, U, P)");
    m.def("qr", &equacore::qr_decomposition, "QR decomposition, returns (Q, R)");
    m.def("svd", &equacore::svd, "SVD, returns (U, S, V)");
    m.def("eigen", &equacore::eigen_symmetric, "Eigenvalues/vectors for symmetric matrix");
    m.def("solve", &equacore::solve_linear, "Solve linear system Ax = b");
    m.def("rref", &equacore::rref, "Reduced row echelon form");
    m.def("null_space", &equacore::null_space, "Null space (kernel)");
    m.def("column_space", &equacore::column_space, "Column space (image)");
    
    // Version info
    m.attr("__version__") = "1.0.0";
}
