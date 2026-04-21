# Geometry

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