# Linear Algebra

<<<<<<< HEAD
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
=======
Linear algebra is the branch of mathematics concerned with vector spaces, linear mappings, and systems of linear equations.
It is foundational to virtually every area of applied mathematics, data science, engineering, and physics.

---

## 1. Vectors

A **vector** $\mathbf{v} \in \mathbb{R}^n$ is an ordered $n$-tuple of real numbers.

### 1.1 Operations

For $\mathbf{u}, \mathbf{v} \in \mathbb{R}^n$ and scalar $c$:
\begin{align}
\mathbf{u} + \mathbf{v} &= (u_1+v_1,\; \ldots,\; u_n+v_n) \\
c\,\mathbf{v} &= (cv_1,\; \ldots,\; cv_n)
\end{align}

**Dot product**:
\begin{equation}
\mathbf{u} \cdot \mathbf{v} = \sum_{i=1}^n u_i v_i = \|\mathbf{u}\|\,\|\mathbf{v}\|\cos\theta
\end{equation}
where $\theta$ is the angle between the vectors.

**Euclidean norm**:
\begin{equation}
\|\mathbf{v}\| = \sqrt{\mathbf{v}\cdot\mathbf{v}} = \sqrt{v_1^2 + \cdots + v_n^2}
\end{equation}

**Cross product** (only in $\mathbb{R}^3$):
\begin{equation}
\mathbf{u} \times \mathbf{v} =
\begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3 \end{vmatrix}
\end{equation}
The magnitude $\|\mathbf{u} \times \mathbf{v}\| = \|\mathbf{u}\|\,\|\mathbf{v}\|\sin\theta$, equal to the area of the parallelogram spanned by $\mathbf{u}$ and $\mathbf{v}$.

### 1.2 Linear Independence

Vectors $\{\mathbf{v}_1, \ldots, \mathbf{v}_k\}$ are **linearly independent** if the only solution to
\begin{equation}
c_1 \mathbf{v}_1 + c_2 \mathbf{v}_2 + \cdots + c_k \mathbf{v}_k = \mathbf{0}
\end{equation}
is $c_1 = c_2 = \cdots = c_k = 0$.  Otherwise they are **linearly dependent**.

The **span** of a set of vectors is the set of all linear combinations.  A **basis** of a vector space is a linearly independent spanning set; its cardinality is the **dimension** of the space.

---

## 2. Matrices

An $m \times n$ **matrix** $A$ has $m$ rows and $n$ columns:
\begin{equation}
A = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & & \ddots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{pmatrix}
\end{equation}

### 2.1 Basic Operations

- **Addition**: $(A + B)_{ij} = a_{ij} + b_{ij}$ (same dimensions required)
- **Scalar multiplication**: $(cA)_{ij} = c\,a_{ij}$
- **Transpose**: $(A^T)_{ij} = a_{ji}$
- **Matrix multiplication**: $(AB)_{ij} = \displaystyle\sum_{k=1}^n a_{ik}b_{kj}$ (requires $A$ is $m\times n$, $B$ is $n\times p$)

### 2.2 Special Matrices

| Name | Property |
|---|---|
| Identity $I$ | $AI = IA = A$ |
| Symmetric | $A^T = A$ |
| Skew-symmetric | $A^T = -A$ |
| Orthogonal | $A^T A = I$ (preserves lengths and angles) |
| Diagonal | $a_{ij} = 0$ for $i \neq j$ |
| Triangular | All entries above (lower) or below (upper) diagonal are zero |

---

## 3. Determinants

The **determinant** $\det(A)$ (or $|A|$) is a scalar associated with a square matrix.

**$2 \times 2$ case**:
\begin{equation}
\det\begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad - bc
\end{equation}

**$3 \times 3$ case** (cofactor expansion along the first row):
\begin{equation}
\det(A) = a_{11}(a_{22}a_{33} - a_{23}a_{32}) - a_{12}(a_{21}a_{33} - a_{23}a_{31}) + a_{13}(a_{21}a_{32} - a_{22}a_{31})
\end{equation}

### Key properties

- $\det(AB) = \det(A)\det(B)$
- $\det(A^T) = \det(A)$
- $\det(A^{-1}) = 1/\det(A)$ (when $A$ is invertible)
- Swapping two rows negates the determinant
- If any row is a linear combination of the others, $\det(A) = 0$

A matrix $A$ is **invertible** (nonsingular) if and only if $\det(A) \neq 0$.
The **inverse** is then:
\begin{equation}
A^{-1} = \frac{1}{\det(A)} \operatorname{adj}(A)
\end{equation}
where $\operatorname{adj}(A)$ is the transpose of the cofactor matrix.

---

## 4. Systems of Linear Equations

A system of $m$ equations in $n$ unknowns can be written as $A\mathbf{x} = \mathbf{b}$.

### 4.1 Gaussian Elimination

Form the augmented matrix $[A \mid \mathbf{b}]$ and reduce to **row-echelon form** using:
1. Swap two rows
2. Multiply a row by a nonzero scalar
3. Add a multiple of one row to another

Continue to **reduced row-echelon form** (RREF) for a unique representation.

### 4.2 Solution Types

- **Unique solution**: $\operatorname{rank}(A) = \operatorname{rank}([A|\mathbf{b}]) = n$
- **Infinitely many solutions**: $\operatorname{rank}(A) = \operatorname{rank}([A|\mathbf{b}]) < n$
- **No solution**: $\operatorname{rank}(A) < \operatorname{rank}([A|\mathbf{b}])$

### 4.3 Cramer's Rule ($n \times n$, $\det(A) \neq 0$)

\begin{equation}
x_i = \frac{\det(A_i)}{\det(A)}
\end{equation}
where $A_i$ is $A$ with its $i$-th column replaced by $\mathbf{b}$.

### 4.4 LU Decomposition

For an $n \times n$ matrix: $A = LU$ where $L$ is lower triangular with unit diagonal and $U$ is upper triangular.
Solve by **forward substitution** ($L\mathbf{y} = \mathbf{b}$) then **back substitution** ($U\mathbf{x} = \mathbf{y}$).
This is the basis for most numerical linear solvers.

---

## 5. Eigenvalues and Eigenvectors

A scalar $\lambda$ and nonzero vector $\mathbf{v}$ satisfy the **eigenvector equation**:
\begin{equation}
A\mathbf{v} = \lambda\mathbf{v}
\end{equation}

$\lambda$ is an **eigenvalue** of $A$ and $\mathbf{v}$ is the corresponding **eigenvector**.

### 5.1 Characteristic Equation

Eigenvalues are found by solving:
\begin{equation}
\det(A - \lambda I) = 0
\end{equation}
The left side is the **characteristic polynomial** of degree $n$, so an $n \times n$ matrix has exactly $n$ eigenvalues (counted with multiplicity, possibly complex).

### 5.2 Properties

- $\operatorname{tr}(A) = \displaystyle\sum_{i=1}^n \lambda_i$
- $\det(A) = \displaystyle\prod_{i=1}^n \lambda_i$
- If $A$ is real symmetric, all eigenvalues are real and eigenvectors of distinct eigenvalues are orthogonal

### 5.3 Diagonalization

If $A$ has $n$ linearly independent eigenvectors forming the columns of $P$:
\begin{equation}
A = P \Lambda P^{-1}
\end{equation}
where $\Lambda = \operatorname{diag}(\lambda_1, \ldots, \lambda_n)$.
This gives $A^k = P \Lambda^k P^{-1}$, which is efficient for large powers.

---

## 6. Vector Spaces and Subspaces

A **vector space** over $\mathbb{R}$ is a set $V$ closed under addition and scalar multiplication and satisfying the eight axioms (associativity, commutativity, identity, inverses, distributivity).

Important subspaces associated with an $m \times n$ matrix $A$:

| Subspace | Definition | Dimension |
|---|---|---|
| Column space $\operatorname{col}(A)$ | Span of columns of $A$ | $\operatorname{rank}(A)$ |
| Row space $\operatorname{row}(A)$ | Span of rows of $A$ | $\operatorname{rank}(A)$ |
| Null space $\operatorname{null}(A)$ | $\{\mathbf{x} : A\mathbf{x} = \mathbf{0}\}$ | $n - \operatorname{rank}(A)$ |

**Rank-Nullity Theorem**: $\operatorname{rank}(A) + \operatorname{nullity}(A) = n$.

---

## 7. Inner Product Spaces and Orthogonality

An **inner product** on $V$ generalises the dot product.  The standard inner product on $\mathbb{R}^n$ is:
\begin{equation}
\langle \mathbf{u}, \mathbf{v} \rangle = \mathbf{u}^T \mathbf{v}
\end{equation}

### Gram–Schmidt Orthogonalisation

Given a basis $\{\mathbf{v}_1, \ldots, \mathbf{v}_k\}$, produce an orthonormal basis $\{\mathbf{e}_1, \ldots, \mathbf{e}_k\}$:
\begin{align}
\mathbf{u}_1 &= \mathbf{v}_1 \\
\mathbf{u}_j &= \mathbf{v}_j - \sum_{i=1}^{j-1} \frac{\langle \mathbf{v}_j, \mathbf{u}_i \rangle}{\langle \mathbf{u}_i, \mathbf{u}_i \rangle}\,\mathbf{u}_i
\end{align}
then $\mathbf{e}_j = \mathbf{u}_j / \|\mathbf{u}_j\|$.

### QR Decomposition

Any $m \times n$ matrix $A$ (with $m \geq n$ and full column rank) can be written as $A = QR$ where $Q$ has orthonormal columns and $R$ is upper triangular.  This is useful for solving least-squares problems.

---

## 8. Singular Value Decomposition (SVD)

Every $m \times n$ real matrix $A$ can be decomposed as:
\begin{equation}
A = U \Sigma V^T
\end{equation}
where:
- $U$ is $m \times m$ orthogonal (left singular vectors)
- $\Sigma$ is $m \times n$ diagonal with non-negative entries $\sigma_1 \geq \sigma_2 \geq \cdots \geq 0$ (singular values)
- $V$ is $n \times n$ orthogonal (right singular vectors)

The SVD generalises the eigendecomposition to non-square matrices and is widely used for dimensionality reduction, pseudoinverse computation, and data compression.

The **rank** of $A$ equals the number of nonzero singular values.
The **pseudoinverse** (Moore–Penrose) is $A^+ = V \Sigma^+ U^T$.

This is a placeholder for Linear Algebra content.
>>>>>>> origin/main
