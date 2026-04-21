# Number Theory

<<<<<<< HEAD
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
=======
Number theory is the branch of pure mathematics studying the integers and integer-valued functions.
Classical results about primes and divisibility underlie modern cryptography and computer science.

---

## 1. Integers and Divisibility

For integers $a$ and $b$ with $b \neq 0$, we say $b$ **divides** $a$ (written $b \mid a$) if there exists an integer $k$ such that $a = kb$.

### 1.1 Division Algorithm

For any integers $a$ and $b > 0$, there exist **unique** integers $q$ (quotient) and $r$ (remainder) with $0 \leq r < b$ such that:
\begin{equation}
a = qb + r
\end{equation}

### 1.2 Greatest Common Divisor (GCD)

The **GCD** of two integers $a, b$ (not both zero) is the largest positive integer dividing both.

**Euclidean algorithm** — the most efficient classical method:
\begin{align}
\gcd(a, b) &= \gcd(b,\; a \bmod b) \\
\gcd(a, 0) &= a
\end{align}

**Least Common Multiple**:
\begin{equation}
\operatorname{lcm}(a, b) = \frac{|ab|}{\gcd(a, b)}
\end{equation}

**Bézout's identity**: There always exist integers $s, t$ such that
\begin{equation}
\gcd(a, b) = sa + tb
\end{equation}
These coefficients are found by the **extended Euclidean algorithm**.

---

## 2. Prime Numbers

An integer $p > 1$ is **prime** if its only positive divisors are $1$ and $p$ itself.  Otherwise $n > 1$ is **composite**.

### 2.1 Fundamental Theorem of Arithmetic

Every integer $n > 1$ has a unique **prime factorisation**:
\begin{equation}
n = p_1^{e_1} p_2^{e_2} \cdots p_k^{e_k}, \quad p_1 < p_2 < \cdots < p_k \text{ prime},\quad e_i \geq 1
\end{equation}

### 2.2 Density of Primes — Prime Number Theorem

Let $\pi(x)$ denote the number of primes $\leq x$.  Then:
\begin{equation}
\lim_{x\to\infty} \frac{\pi(x)}{x / \ln x} = 1
\end{equation}
so primes become increasingly sparse, but there are **infinitely many** of them (Euclid's proof).

### 2.3 Sieve of Eratosthenes

To find all primes up to $N$:
1. List integers $2, 3, \ldots, N$.
2. Start at $p = 2$; mark all multiples of $p$ greater than $p$ as composite.
3. Move to the next unmarked number and repeat.
4. Stop when $p > \sqrt{N}$; all unmarked numbers are prime.

### 2.4 Special Primes

| Type | Definition | Examples |
|---|---|---|
| Mersenne prime | $2^p - 1$ | 3, 7, 31, 127 |
| Fermat prime | $2^{2^n} + 1$ | 3, 5, 17, 257, 65537 |
| Twin primes | $(p,\; p+2)$ both prime | (3,5), (11,13), (17,19) |
| Sophie Germain prime | $p$ and $2p+1$ both prime | 2, 3, 5, 11, 23 |

---

## 3. Modular Arithmetic

For a positive integer $m$ (the **modulus**), $a \equiv b \pmod{m}$ (read "$a$ is congruent to $b$ modulo $m$") if $m \mid (a - b)$.

Congruence behaves like equality with respect to addition and multiplication:
\begin{align}
a \equiv b \pmod{m} &\Rightarrow a + c \equiv b + c \pmod{m} \\
a \equiv b \pmod{m} &\Rightarrow ac \equiv bc \pmod{m}
\end{align}

### 3.1 Residue Classes

The integers modulo $m$ form the set $\mathbb{Z}_m = \{0, 1, \ldots, m-1\}$ with operations defined mod $m$.
$\mathbb{Z}_m$ is a **field** (every nonzero element has a multiplicative inverse) if and only if $m$ is prime.

### 3.2 Fermat's Little Theorem

If $p$ is prime and $\gcd(a, p) = 1$:
\begin{equation}
a^{p-1} \equiv 1 \pmod{p}
\end{equation}

Equivalently for any integer $a$: $a^p \equiv a \pmod{p}$.  This is the basis of the Fermat primality test and RSA encryption.

### 3.3 Euler's Theorem

For $\gcd(a, n) = 1$:
\begin{equation}
a^{\phi(n)} \equiv 1 \pmod{n}
\end{equation}
where $\phi(n)$ is **Euler's totient function** — the count of integers in $\{1, \ldots, n\}$ coprime to $n$.

For $n = p_1^{e_1} \cdots p_k^{e_k}$:
\begin{equation}
\phi(n) = n \prod_{p \mid n}\left(1 - \frac{1}{p}\right)
\end{equation}

### 3.4 Chinese Remainder Theorem (CRT)

If $m_1, m_2, \ldots, m_k$ are pairwise coprime, then for any $a_1, \ldots, a_k$ the system
\begin{align}
x &\equiv a_1 \pmod{m_1} \\
x &\equiv a_2 \pmod{m_2} \\
&\vdots \\
x &\equiv a_k \pmod{m_k}
\end{align}
has a unique solution modulo $M = m_1 m_2 \cdots m_k$.

---

## 4. Diophantine Equations

A **Diophantine equation** is a polynomial equation for which integer (or rational) solutions are sought.

### 4.1 Linear Diophantine Equations

$ax + by = c$ has integer solutions if and only if $\gcd(a, b) \mid c$.  If a solution $(x_0, y_0)$ exists, the general solution is:
\begin{equation}
x = x_0 + \frac{b}{d}t, \quad y = y_0 - \frac{a}{d}t, \quad d = \gcd(a, b), \quad t \in \mathbb{Z}
\end{equation}

### 4.2 Pythagorean Triples

All positive integer solutions to $a^2 + b^2 = c^2$ (with $a < b$, $\gcd(a,b,c) = 1$) are generated by:
\begin{equation}
a = m^2 - n^2, \quad b = 2mn, \quad c = m^2 + n^2
\end{equation}
for integers $m > n > 0$ with $\gcd(m, n) = 1$ and $m \not\equiv n \pmod{2}$.

### 4.3 Pell's Equation

$x^2 - Dy^2 = 1$ (where $D$ is a positive non-square integer) always has infinitely many solutions.  The fundamental solution $(x_1, y_1)$ is found from the continued fraction expansion of $\sqrt{D}$.

---

## 5. Number-Theoretic Functions

| Function | Symbol | Definition |
|---|---|---|
| Euler's totient | $\phi(n)$ | $\#\{k : 1 \leq k \leq n,\, \gcd(k,n)=1\}$ |
| Divisor count | $\tau(n)$ or $d(n)$ | Number of positive divisors of $n$ |
| Divisor sum | $\sigma(n)$ | Sum of all positive divisors of $n$ |
| Möbius function | $\mu(n)$ | $0$ if $p^2 \mid n$; $(-1)^k$ if $n = p_1\cdots p_k$; $1$ if $n=1$ |
| Liouville function | $\lambda(n)$ | $(-1)^{\Omega(n)}$ where $\Omega(n)$ = total prime factors with multiplicity |

All these functions are **multiplicative**: if $\gcd(a,b)=1$ then $f(ab) = f(a)f(b)$.

---

## 6. Continued Fractions

Any real number $x$ can be expressed as a **continued fraction**:
\begin{equation}
x = a_0 + \cfrac{1}{a_1 + \cfrac{1}{a_2 + \cfrac{1}{a_3 + \cdots}}}
\end{equation}
denoted $[a_0; a_1, a_2, a_3, \ldots]$, where the $a_i$ are positive integers for $i \geq 1$.

- **Rational numbers** have finite continued fractions.
- **Quadratic irrationals** (like $\sqrt{D}$) have infinite **periodic** continued fractions.
- **Transcendental numbers** like $e = [2; 1, 2, 1, 1, 4, 1, 1, 6, \ldots]$ have no periodic pattern.

The partial quotients $[a_0; a_1, \ldots, a_k] = p_k/q_k$ are called **convergents** and provide the best rational approximations to $x$.

---

## 7. Rational and Irrational Numbers

A **rational number** can be written as $p/q$ with $p, q \in \mathbb{Z}$, $q \neq 0$.  Their decimal expansions are terminating or eventually repeating.

An **irrational number** cannot be expressed as a ratio of integers.  Famous examples:
- $\sqrt{2}$ — proved irrational by Pythagoras; $\sqrt{p}$ is irrational for every prime $p$
- $\pi \approx 3.14159\ldots$ — also **transcendental** (not a root of any polynomial with integer coefficients)
- $e \approx 2.71828\ldots$ — transcendental (Hermite, 1873)

The set of real numbers is **uncountable** (Cantor's diagonal argument), while the rationals are countable.

---

## 8. Cryptographic Applications

Number theory provides the mathematical foundation for public-key cryptography.

### RSA Encryption (sketch)

1. Choose large primes $p, q$ and set $n = pq$.
2. Compute $\phi(n) = (p-1)(q-1)$.
3. Choose public exponent $e$ with $\gcd(e, \phi(n)) = 1$.
4. Find private exponent $d$ satisfying $ed \equiv 1 \pmod{\phi(n)}$.
5. Encrypt: $c \equiv m^e \pmod{n}$.  Decrypt: $m \equiv c^d \pmod{n}$.

Security rests on the difficulty of **integer factorisation** of $n$ when $p$ and $q$ are large.

### Diffie–Hellman Key Exchange (sketch)

Based on the **discrete logarithm problem**: given $g$, $p$ (prime), and $g^x \bmod p$, find $x$.  This is believed to be computationally hard for large $p$.

This is a placeholder for Number Theory content.
>>>>>>> origin/main
