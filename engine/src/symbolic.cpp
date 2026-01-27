/**
 * EquaCore - Symbolic Mathematics Implementation
 * Uses GiNaC for high-performance symbolic computation
 */

#include "equacore/symbolic.hpp"
#include <sstream>
#include <ginac/ginac.h>

namespace equacore {

ex parse(const std::string& expr_str, const GiNaC::symtab& symbols) {
    GiNaC::parser reader(symbols);
    return reader(expr_str);
}

ex expand(const ex& e) {
    return GiNaC::expand(e);
}

ex simplify(const ex& e) {
    // GiNaC doesn't have a direct simplify(), use normal() for rational expressions
    return e.normal();
}

ex factor(const ex& e) {
    return GiNaC::factor(e);
}

ex diff(const ex& e, const symbol& s, int n) {
    ex result = e;
    for (int i = 0; i < n; ++i) {
        result = result.diff(s);
    }
    return result;
}

ex integrate(const ex& e, const symbol& s) {
    // Indefinite integral
    return GiNaC::integral(s, e);
}

ex integrate(const ex& e, const symbol& s, const ex& a, const ex& b) {
    // Definite integral - evaluate the indefinite integral at bounds
    ex indefinite = GiNaC::integral(s, e);
    return indefinite.subs(s == b) - indefinite.subs(s == a);
}

std::vector<ex> solve(const ex& eq, const symbol& s) {
    // GiNaC's solve returns a list of solutions
    GiNaC::lst solutions = GiNaC::lsolve(eq, s);
    std::vector<ex> result;
    for (size_t i = 0; i < solutions.nops(); ++i) {
        result.push_back(solutions.op(i));
    }
    return result;
}

ex substitute(const ex& e, const symbol& s, const ex& value) {
    return e.subs(s == value);
}

std::string to_latex(const ex& e) {
    std::ostringstream oss;
    oss << GiNaC::latex << e;
    return oss.str();
}

std::string to_string(const ex& e) {
    std::ostringstream oss;
    oss << e;
    return oss.str();
}

std::pair<std::vector<ex>, std::vector<ex>> 
fourier_coefficients(const ex& f, const symbol& x, const ex& period, int n_terms) {
    std::vector<ex> a_coeffs, b_coeffs;
    
    symbol n("n");
    ex L = period / 2;
    ex pi = GiNaC::Pi;
    
    // a_0 coefficient (special case)
    ex a0 = integrate(f, x, -L, L) / period;
    a_coeffs.push_back(a0);
    
    // Compute a_n and b_n for n = 1 to n_terms
    for (int k = 1; k <= n_terms; ++k) {
        ex kval = GiNaC::numeric(k);
        
        // a_n = (2/L) * integral(f * cos(n*pi*x/L), x, -L, L)
        ex cos_term = GiNaC::cos(kval * pi * x / L);
        ex a_n = (2 / period) * integrate(f * cos_term, x, -L, L);
        a_coeffs.push_back(a_n);
        
        // b_n = (2/L) * integral(f * sin(n*pi*x/L), x, -L, L)
        ex sin_term = GiNaC::sin(kval * pi * x / L);
        ex b_n = (2 / period) * integrate(f * sin_term, x, -L, L);
        b_coeffs.push_back(b_n);
    }
    
    return {a_coeffs, b_coeffs};
}

} // namespace equacore
