# Number Theory

Number theory is the study of properties and relationships of integers.

## Key Concepts

- **Divisibility**: $a$ divides $b$ if $b = ka$ for some integer $k$
- **Prime Numbers**: Integers $>1$ with no divisors other than 1 and itself
- **Greatest Common Divisor (GCD)**: Largest integer dividing two numbers
- **Least Common Multiple (LCM)**: Smallest integer divisible by two numbers
- **Modular Arithmetic**: Arithmetic with remainders (clock arithmetic)

## Example: Euclidean Algorithm for GCD

Given integers $a$ and $b$ ($a > b$):

1. Divide $a$ by $b$, get remainder $r$
2. Replace $a$ with $b$, $b$ with $r$
3. Repeat until $r = 0$. The last nonzero $b$ is the GCD.

## Python Example

```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
print("GCD of 48 and 18:", gcd(48, 18))
```

---

*Expand this section with more topics: prime tests, modular inverses, Diophantine equations, cryptography...*