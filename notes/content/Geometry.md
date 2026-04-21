# Geometry

<<<<<<< HEAD
Geometry is the study of shapes, sizes, and properties of figures and spaces.

## Key Concepts

- **Point**: An exact location in space (no size)
- **Line**: Infinite set of points extending in both directions
- **Plane**: Flat, two-dimensional surface
- **Angle**: Formed by two rays with a common endpoint
- **Polygon**: Closed figure with straight sides (triangle, quadrilateral, etc.)
- **Circle**: Set of points equidistant from a center

## Types of Geometry

- **Euclidean Geometry**: Flat space, parallel postulate holds
- **Analytic Geometry**: Uses coordinates (Cartesian plane)
- **Solid Geometry**: 3D shapes (cubes, spheres, cylinders)
- **Non-Euclidean Geometry**: Spherical, hyperbolic spaces

## Example: Distance Between Two Points

Given $A(x_1, y_1)$ and $B(x_2, y_2)$:

$$
d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
$$

## Python Example

```python
import numpy as np
def distance(A, B):
    return np.linalg.norm(np.array(A) - np.array(B))
A = (1, 2)
B = (4, 6)
print("Distance:", distance(A, B))
```

---

*Expand this section with more topics: transformations, area/volume, coordinate geometry, conic sections, 3D visualization...*
=======
Geometry is the branch of mathematics concerned with the properties and relations of points, lines, surfaces, and solids.
This chapter surveys the major areas of classical and coordinate geometry, with key formulas and Python examples.

---

## 1. Plane Geometry

### 1.1 Angles and Lines

Two lines are **parallel** if they never intersect and **perpendicular** if they intersect at a right angle ($90°$).
Angles are measured in degrees or radians:
\begin{equation}
\theta_{\text{rad}} = \frac{\pi}{180} \theta_{\text{deg}}
\end{equation}

Complementary angles sum to $90°$; supplementary angles sum to $180°$.

### 1.2 Triangles

For any triangle with sides $a$, $b$, $c$ and angles $A$, $B$, $C$ opposite to those sides:

- **Angle sum**: $A + B + C = 180°$
- **Area**: $\displaystyle S = \frac{1}{2}ab\sin C$
- **Perimeter**: $p = a + b + c$
- **Heron's formula**: $\displaystyle S = \sqrt{s(s-a)(s-b)(s-c)}$, where $s = p/2$

**Pythagorean theorem** (right triangle, $C = 90°$):
\begin{equation}
a^2 + b^2 = c^2
\end{equation}

**Law of cosines** (general triangle):
\begin{equation}
c^2 = a^2 + b^2 - 2ab\cos C
\end{equation}

**Law of sines**:
\begin{equation}
\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C} = 2R
\end{equation}
where $R$ is the circumradius of the triangle.

### 1.3 Circles

For a circle of radius $r$:

| Property | Formula |
|---|---|
| Circumference | $C = 2\pi r$ |
| Area | $A = \pi r^2$ |
| Arc length (central angle $\theta$) | $s = r\theta$ |
| Sector area | $A_{\text{sector}} = \frac{1}{2}r^2\theta$ |

### 1.4 Common Polygons

For a regular $n$-gon with side length $s$:
\begin{align}
\text{Interior angle} &= \frac{(n-2)\cdot 180°}{n} \\
\text{Area} &= \frac{ns^2}{4}\cot\!\left(\frac{\pi}{n}\right)
\end{align}

---

## 2. Coordinate Geometry

In the Cartesian plane, every point is given by $(x, y)$.

### 2.1 Distance and Midpoint

The **distance** between $P_1 = (x_1, y_1)$ and $P_2 = (x_2, y_2)$:
\begin{equation}
d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
\end{equation}

The **midpoint** $M$:
\begin{equation}
M = \left(\frac{x_1 + x_2}{2},\; \frac{y_1 + y_2}{2}\right)
\end{equation}

### 2.2 Lines

The equation of a line through $(x_1, y_1)$ with slope $m = \dfrac{\Delta y}{\Delta x}$:
\begin{equation}
y - y_1 = m(x - x_1) \quad \text{(point-slope form)}
\end{equation}

Standard form: $ax + by + c = 0$. The **distance from a point** $(x_0, y_0)$ to this line:
\begin{equation}
d = \frac{|ax_0 + by_0 + c|}{\sqrt{a^2 + b^2}}
\end{equation}

### 2.3 Conic Sections

Conic sections arise as the intersection of a plane with a double cone.

| Conic | Standard Equation |
|---|---|
| Circle | $x^2 + y^2 = r^2$ |
| Ellipse | $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$ |
| Parabola | $y = ax^2 + bx + c$ |
| Hyperbola | $\dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} = 1$ |

For an ellipse, the **eccentricity** $e = c/a$ where $c^2 = a^2 - b^2$ ($a > b$). When $e = 0$ it is a circle; as $e \to 1$ it becomes a parabola.

---

## 3. Transformations

A **geometric transformation** maps points in the plane to new positions.

### 3.1 Translation

Shift every point by $(\Delta x, \Delta y)$:
\begin{equation}
\begin{pmatrix} x' \\ y' \end{pmatrix}
= \begin{pmatrix} x \\ y \end{pmatrix}
+ \begin{pmatrix} \Delta x \\ \Delta y \end{pmatrix}
\end{equation}

### 3.2 Rotation

Rotate by angle $\theta$ about the origin:
\begin{equation}
\begin{pmatrix} x' \\ y' \end{pmatrix}
= \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}
\begin{pmatrix} x \\ y \end{pmatrix}
\end{equation}

### 3.3 Reflection

Reflection across the $x$-axis: $(x, y) \mapsto (x, -y)$.
Reflection across the line $y = x$: $(x, y) \mapsto (y, x)$.

### 3.4 Scaling (Dilation)

Scale by factor $k$ from the origin:
\begin{equation}
(x, y) \mapsto (kx,\; ky)
\end{equation}

---

## 4. Solid Geometry

### 4.1 Common 3-D Volumes and Surface Areas

| Solid | Volume | Surface Area |
|---|---|---|
| Cube (side $a$) | $a^3$ | $6a^2$ |
| Rectangular box | $\ell w h$ | $2(\ell w + \ell h + wh)$ |
| Sphere (radius $r$) | $\dfrac{4}{3}\pi r^3$ | $4\pi r^2$ |
| Cylinder ($r$, $h$) | $\pi r^2 h$ | $2\pi r(r + h)$ |
| Cone ($r$, $h$) | $\dfrac{1}{3}\pi r^2 h$ | $\pi r(r + l)$, $l = \sqrt{r^2 + h^2}$ |
| Tetrahedron (side $a$) | $\dfrac{a^3}{6\sqrt{2}}$ | $a^2\sqrt{3}$ |

### 4.2 Coordinates in 3-D

**Cartesian**: $(x, y, z)$.  Euclidean distance:
\begin{equation}
d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2 + (z_2-z_1)^2}
\end{equation}

**Spherical** $(r, \theta, \phi)$:
\begin{align}
x &= r\sin\phi\cos\theta \\
y &= r\sin\phi\sin\theta \\
z &= r\cos\phi
\end{align}

**Cylindrical** $(\rho, \theta, z)$:
\begin{align}
x &= \rho\cos\theta \\
y &= \rho\sin\theta \\
z &= z
\end{align}

---

## 5. Trigonometry

### 5.1 Right-Triangle Definitions

For angle $\theta$ in a right triangle (opposite $o$, adjacent $a$, hypotenuse $h$):
\begin{equation}
\sin\theta = \frac{o}{h}, \quad
\cos\theta = \frac{a}{h}, \quad
\tan\theta = \frac{o}{a}
\end{equation}

### 5.2 Key Identities

\begin{align}
\sin^2\theta + \cos^2\theta &= 1 \\
\sin(\alpha \pm \beta) &= \sin\alpha\cos\beta \pm \cos\alpha\sin\beta \\
\cos(\alpha \pm \beta) &= \cos\alpha\cos\beta \mp \sin\alpha\sin\beta \\
\tan(\alpha + \beta) &= \frac{\tan\alpha + \tan\beta}{1 - \tan\alpha\tan\beta}
\end{align}

**Double-angle formulas**:
\begin{align}
\sin 2\theta &= 2\sin\theta\cos\theta \\
\cos 2\theta &= \cos^2\theta - \sin^2\theta = 1 - 2\sin^2\theta
\end{align}

### 5.3 Inverse Trig Functions

| Function | Range |
|---|---|
| $\arcsin x$ | $[-\pi/2,\; \pi/2]$ |
| $\arccos x$ | $[0,\; \pi]$ |
| $\arctan x$ | $(-\pi/2,\; \pi/2)$ |

---

## 6. Geometric Inequalities

- **Triangle inequality**: $|a - b| < c < a + b$
- **AM–GM inequality**: $\dfrac{a+b}{2} \geq \sqrt{ab}$ for $a, b \geq 0$
- **Isoperimetric inequality**: Among all plane figures with perimeter $L$, the circle has the maximum area $A = L^2 / (4\pi)$.

This is a placeholder for Geometry content.
>>>>>>> origin/main
