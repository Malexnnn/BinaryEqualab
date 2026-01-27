/**
 * EquaCore - Linear Algebra Implementation
 * Uses Eigen for high-performance matrix operations
 */

#include "equacore/linear.hpp"
#include <Eigen/LU>
#include <Eigen/QR>
#include <Eigen/SVD>
#include <Eigen/Eigenvalues>

namespace equacore {

MatrixXd create_matrix(const std::vector<std::vector<double>>& data) {
    if (data.empty()) return MatrixXd(0, 0);
    
    int rows = static_cast<int>(data.size());
    int cols = static_cast<int>(data[0].size());
    
    MatrixXd result(rows, cols);
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            result(i, j) = data[i][j];
        }
    }
    return result;
}

VectorXd create_vector(const std::vector<double>& data) {
    VectorXd result(data.size());
    for (size_t i = 0; i < data.size(); ++i) {
        result(i) = data[i];
    }
    return result;
}

MatrixXd add(const MatrixXd& a, const MatrixXd& b) {
    return a + b;
}

MatrixXd multiply(const MatrixXd& a, const MatrixXd& b) {
    return a * b;
}

VectorXd multiply(const MatrixXd& a, const VectorXd& v) {
    return a * v;
}

MatrixXd scale(const MatrixXd& m, double scalar) {
    return m * scalar;
}

MatrixXd transpose(const MatrixXd& m) {
    return m.transpose();
}

MatrixXd inverse(const MatrixXd& m) {
    return m.inverse();
}

double determinant(const MatrixXd& m) {
    return m.determinant();
}

int rank(const MatrixXd& m) {
    Eigen::FullPivLU<MatrixXd> lu(m);
    return static_cast<int>(lu.rank());
}

std::tuple<MatrixXd, MatrixXd, MatrixXd> lu_decomposition(const MatrixXd& m) {
    Eigen::FullPivLU<MatrixXd> lu(m);
    MatrixXd L = MatrixXd::Identity(m.rows(), m.cols());
    L.triangularView<Eigen::StrictlyLower>() = lu.matrixLU();
    MatrixXd U = lu.matrixLU().triangularView<Eigen::Upper>();
    MatrixXd P = lu.permutationP();
    return {L, U, P};
}

std::tuple<MatrixXd, MatrixXd> qr_decomposition(const MatrixXd& m) {
    Eigen::HouseholderQR<MatrixXd> qr(m);
    MatrixXd Q = qr.householderQ();
    MatrixXd R = qr.matrixQR().triangularView<Eigen::Upper>();
    return {Q, R};
}

std::tuple<MatrixXd, VectorXd, MatrixXd> svd(const MatrixXd& m) {
    Eigen::JacobiSVD<MatrixXd> svd(m, Eigen::ComputeFullU | Eigen::ComputeFullV);
    return {svd.matrixU(), svd.singularValues(), svd.matrixV()};
}

std::tuple<VectorXd, MatrixXd> eigen_symmetric(const MatrixXd& m) {
    Eigen::SelfAdjointEigenSolver<MatrixXd> solver(m);
    return {solver.eigenvalues(), solver.eigenvectors()};
}

VectorXd solve_linear(const MatrixXd& a, const VectorXd& b) {
    return a.colPivHouseholderQr().solve(b);
}

MatrixXd rref(const MatrixXd& m) {
    // Gaussian elimination with partial pivoting
    MatrixXd result = m;
    int rows = static_cast<int>(result.rows());
    int cols = static_cast<int>(result.cols());
    int pivot_row = 0;
    
    for (int col = 0; col < cols && pivot_row < rows; ++col) {
        // Find pivot
        int max_row = pivot_row;
        for (int row = pivot_row + 1; row < rows; ++row) {
            if (std::abs(result(row, col)) > std::abs(result(max_row, col))) {
                max_row = row;
            }
        }
        
        if (std::abs(result(max_row, col)) < 1e-10) continue;
        
        // Swap rows
        result.row(pivot_row).swap(result.row(max_row));
        
        // Scale pivot row
        result.row(pivot_row) /= result(pivot_row, col);
        
        // Eliminate column
        for (int row = 0; row < rows; ++row) {
            if (row != pivot_row) {
                result.row(row) -= result(row, col) * result.row(pivot_row);
            }
        }
        
        ++pivot_row;
    }
    
    return result;
}

MatrixXd null_space(const MatrixXd& m) {
    Eigen::FullPivLU<MatrixXd> lu(m);
    return lu.kernel();
}

MatrixXd column_space(const MatrixXd& m) {
    Eigen::FullPivLU<MatrixXd> lu(m);
    return lu.image(m);
}

} // namespace equacore
