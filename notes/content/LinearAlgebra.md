# Linear Algebra

Linear algebra is the branch of mathematics concerning linear equations, matrices, vector spaces, and linear transformations.

## Key Concepts

- **Scalars, Vectors, Matrices**
    - Scalar: A single number (e.g., $a \in \mathbb{R}$)
    - Vector: An ordered list of numbers (e.g., $\mathbf{v} = [v_1, v_2, ..., v_n]^T$)
    - Matrix: A rectangular array of numbers (e.g., $A \in \mathbb{R}^{m \times n}$)

## Matrix Operations

- **Addition**: $A + B$ (same size)
- **Multiplication**: $AB$ ($A$ is $m \times n$, $B$ is $n \times p$)
- **Transpose**: $A^T$
- **Inverse**: $A^{-1}$ (if $A$ is square and invertible)

## Systems of Linear Equations

Solve $A\mathbf{x} = \mathbf{b}$ for $\mathbf{x}$.

**Example:**

$\begin{bmatrix} 2 & 1 \\ 1 & 3 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 1 \\ 2 \end{bmatrix}$

Solution: $\mathbf{x} = A^{-1}\mathbf{b}$

## Eigenvalues and Eigenvectors

For a square matrix $A$, $A\mathbf{v} = \lambda\mathbf{v}$, where $\lambda$ is an eigenvalue and $\mathbf{v}$ is an eigenvector.

**Applications:**
- Principal component analysis
- Differential equations
- Quantum mechanics

## Python Example

```python
import numpy as np
A = np.array([[2, 1], [1, 3]])
b = np.array([1, 2])
x = np.linalg.solve(A, b)
print("Solution x:", x)
# Eigenvalues and eigenvectors
 eigvals, eigvecs = np.linalg.eig(A)
print("Eigenvalues:", eigvals)
print("Eigenvectors:\n", eigvecs)
```

---

*Expand this section with more topics: vector spaces, determinants, LU decomposition, SVD, applications...*