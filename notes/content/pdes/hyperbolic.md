# Hyperbolic Partial Differential Equations

Hyperbolic PDEs describe wave propagation and vibrations. The classic example is the 1D wave equation.

## 1D Wave Equation

$$
\frac{\partial^2 u}{\partial t^2} = c^2 \frac{\partial^2 u}{\partial x^2}
$$

- $u(x, t)$: displacement
- $c$: wave speed

## General Solution

The general solution is:
$$
u(x, t) = f(x - ct) + g(x + ct)$$
where $f$ and $g$ are determined by initial and boundary conditions.

## Example: Vibrating String

A string of length $L$ fixed at both ends:
- $u(0, t) = u(L, t) = 0$
- Initial displacement $u(x, 0) = f(x)$
- Initial velocity $u_t(x, 0) = g(x)$

Solution (Fourier series):
$$
u(x, t) = \sum_{n=1}^\infty \left[A_n \cos\left(\frac{n\pi c t}{L}\right) + B_n \sin\left(\frac{n\pi c t}{L}\right)\right] \sin\left(\frac{n\pi x}{L}\right)$$

## Python Example

```python
import numpy as np
import matplotlib.pyplot as plt
L = 1
c = 1
x = np.linspace(0, L, 100)
t = 0.5
u = np.sin(np.pi * x) * np.cos(np.pi * c * t)
plt.plot(x, nu)
plt.xlabel('x')
plt.ylabel('u(x, t)')
plt.title('Vibrating String at t=0.5')
plt.show()
```

---

*Expand this section with d'Alembert's solution, characteristics, higher dimensions, and numerical methods (finite difference, finite element, etc.).*
