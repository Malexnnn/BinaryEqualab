#pragma once
/**
 * EquaCore - Linear Algebra Engine
 * Wrapper around Eigen for high-performance matrix operations
 */

#include <Eigen/Dense>
#include <Eigen/Sparse>
#include <vector>
#include <tuple>

namespace equacore {

// Type aliases for common matrix types
using MatrixXd = Eigen::MatrixXd;
using VectorXd = Eigen::VectorXd;
using SparseMatrix = Eigen::SparseMatrix<double>;

/**
 * Create matrix from nested vector
 */
MatrixXd create_matrix(const std::vector<std::vector<double>>& data);

/**
 * Create vector from flat vector
 */
VectorXd create_vector(const std::vector<double>& data);

/**
 * Matrix addition
 */
MatrixXd add(const MatrixXd& a, const MatrixXd& b);

/**
 * Matrix multiplication
 */
MatrixXd multiply(const MatrixXd& a, const MatrixXd& b);

/**
 * Matrix-vector multiplication
 */
VectorXd multiply(const MatrixXd& a, const VectorXd& v);

/**
 * Scalar multiplication
 */
MatrixXd scale(const MatrixXd& m, double scalar);

/**
 * Transpose
 */
MatrixXd transpose(const MatrixXd& m);

/**
 * Matrix inverse
 */
MatrixXd inverse(const MatrixXd& m);

/**
 * Determinant
 */
double determinant(const MatrixXd& m);

/**
 * Matrix rank
 */
int rank(const MatrixXd& m);

/**
 * LU decomposition
 * @return tuple of (L, U, P) matrices where PA = LU
 */
std::tuple<MatrixXd, MatrixXd, MatrixXd> lu_decomposition(const MatrixXd& m);

/**
 * QR decomposition
 * @return tuple of (Q, R) matrices where A = QR
 */
std::tuple<MatrixXd, MatrixXd> qr_decomposition(const MatrixXd& m);

/**
 * Singular Value Decomposition
 * @return tuple of (U, S, V) where A = U * diag(S) * V^T
 */
std::tuple<MatrixXd, VectorXd, MatrixXd> svd(const MatrixXd& m);

/**
 * Eigenvalue decomposition for symmetric matrices
 * @return tuple of (eigenvalues, eigenvectors)
 */
std::tuple<VectorXd, MatrixXd> eigen_symmetric(const MatrixXd& m);

/**
 * Solve linear system Ax = b
 */
VectorXd solve_linear(const MatrixXd& a, const VectorXd& b);

/**
 * Reduced Row Echelon Form (RREF)
 */
MatrixXd rref(const MatrixXd& m);

/**
 * Null space (kernel) of matrix
 */
MatrixXd null_space(const MatrixXd& m);

/**
 * Column space (range) of matrix
 */
MatrixXd column_space(const MatrixXd& m);

} // namespace equacore
