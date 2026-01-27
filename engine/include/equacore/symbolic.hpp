#pragma once
/**
 * EquaCore - Symbolic Mathematics Engine
 * Wrapper around GiNaC for high-performance symbolic computation
 */

#include <string>
#include <vector>
#include <ginac/ginac.h>

namespace equacore {

using GiNaC::ex;
using GiNaC::symbol;
using GiNaC::parser;

/**
 * Parse a mathematical expression from string
 * @param expr_str Expression string (e.g., "x^2 + 2*x + 1")
 * @param symbols Map of symbol names to GiNaC symbols
 * @return Parsed GiNaC expression
 */
ex parse(const std::string& expr_str, 
         const GiNaC::symtab& symbols = GiNaC::symtab());

/**
 * Expand an expression (e.g., (x+y)^2 -> x^2 + 2*x*y + y^2)
 */
ex expand(const ex& e);

/**
 * Simplify an expression
 */
ex simplify(const ex& e);

/**
 * Factor an expression
 */
ex factor(const ex& e);

/**
 * Differentiate expression with respect to a symbol
 * @param e Expression to differentiate
 * @param s Symbol to differentiate with respect to
 * @param n Order of derivative (default: 1)
 */
ex diff(const ex& e, const symbol& s, int n = 1);

/**
 * Integrate expression with respect to a symbol
 */
ex integrate(const ex& e, const symbol& s);

/**
 * Compute definite integral
 */
ex integrate(const ex& e, const symbol& s, const ex& a, const ex& b);

/**
 * Solve equation for a symbol
 * @param eq Equation (left side, implicitly = 0)
 * @param s Symbol to solve for
 * @return List of solutions
 */
std::vector<ex> solve(const ex& eq, const symbol& s);

/**
 * Substitute values in expression
 */
ex substitute(const ex& e, const symbol& s, const ex& value);

/**
 * Convert expression to LaTeX string
 */
std::string to_latex(const ex& e);

/**
 * Convert expression to string
 */
std::string to_string(const ex& e);

/**
 * Compute Fourier series coefficients (for periodic functions)
 * @param f Function expression
 * @param x Variable
 * @param period Period of the function
 * @param n_terms Number of terms
 * @return Pair of (a_n coefficients, b_n coefficients)
 */
std::pair<std::vector<ex>, std::vector<ex>> 
fourier_coefficients(const ex& f, const symbol& x, const ex& period, int n_terms);

} // namespace equacore
