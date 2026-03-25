# Contributing to Math Notes

> **Live site** â†’ [math.suryaraj.com](https://math.suryaraj.com) Â· **GitHub** â†’ [suryakantamangaraj/Math](https://github.com/suryakantamangaraj/Math)

Thank you for your interest in contributing! This is an open, community-driven mathematics reference built with [MyST Markdown](https://mystmd.org/) and [Jupyter Book](https://jupyterbook.org/).
Every contribution â€” however small â€” makes this a better resource for everyone.

---

## Where Contributions Are Most Needed

The sections below are **actively seeking contributors**. They have an outline but need more depth, worked examples, and/or interactive Python notebooks:

| Section | What's missing |
|---|---|
| **Linear Algebra** | Worked numerical examples, Python code for eigenvalue computation, matrix decompositions (LU, QR, SVD) |
| **Geometry** | Illustrated examples, analytic geometry problems, 3-D coordinate visualisations |
| **Number Theory** | Python implementations of sieve, GCD, modular exponentiation, RSA toy example |
| **Arithmetic & Algebra** | More NumPy examples, symbolic algebra with SymPy |
| **Any section** | Additional practice problems, proofs, real-world applications |

If you notice any errors, broken formulas, or missing references anywhere in the site, please fix or flag them â€” that counts too!

---

## Ways to Contribute

### 1. Fix a typo or formula error

1. Click the **edit** button (âœï¸) at the top of any page on [math.suryaraj.com](https://math.suryaraj.com) to edit the source directly on GitHub.
2. Commit, and open a pull request.

### 2. Add or expand content in an existing Markdown file

Topics live in `notes/content/`. Each top-level subject maps to a file:

```
notes/content/
â”œâ”€â”€ Arithmetic.ipynb        # Arithmetic & Algebra
â”œâ”€â”€ first-order.md          # 1st-order ODEs
â”œâ”€â”€ Geometry.md             # Geometry  â† needs help
â”œâ”€â”€ LinearAlgebra.md        # Linear Algebra  â† needs help
â”œâ”€â”€ NumberTheory.md         # Number Theory  â† needs help
â””â”€â”€ second-order/           # 2nd-order ODEs
    â”œâ”€â”€ analytical.ipynb
    â”œâ”€â”€ fourier-series.ipynb
    â””â”€â”€ ...
```

Edit the relevant file and submit a pull request.

### 3. Add a new Jupyter notebook

Adding Python examples as notebooks (`.ipynb`) makes content interactive and executable on Binder/Colab.

1. Place your notebook under the appropriate `notes/content/` subdirectory.
2. Add it to `notes/_toc.yml` so the build picks it up.
3. Make sure it runs top-to-bottom with `jupyter nbconvert --to notebook --execute`.

### 4. Suggest a new topic

Open an [issue](https://github.com/suryakantamangaraj/Math/issues/new) with the label **`topic request`** and describe what you'd like to see covered.

---

## Development Setup

```bash
# Clone and enter the repo
git clone https://github.com/suryakantamangaraj/Math.git
cd Math

# Create a virtual environment and install dependencies
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Build the book locally
cd notes
myst build --html               # MyST v2 (recommended)
# OR: jupyter-book build .      # legacy JupyterBook v1

# Open the result
start _build/html/index.html    # Windows
open  _build/html/index.html    # macOS / Linux
```

---

## Pull Request Guidelines

1. **Fork** the repository and create a feature branch: `git checkout -b feat/your-topic`.
2. Keep changes focused â€” one topic or fix per PR is ideal.
3. Ensure notebooks execute without errors before submitting.
4. Write a short description in the PR explaining *what* you changed and *why*.
5. Reference any related issues with `Closes #<issue-number>`.

A maintainer will review and merge your PR, usually within a few days.

---

## Community Standards

Please follow the [Code of Conduct](https://github.com/suryakantamangaraj/Math/blob/main/CODE_OF_CONDUCT.md) in all interactions.

---

## Recognition

All contributors are welcome! Significant contributions will be acknowledged in the site footer and project README.

---

*Questions?  Open an [issue](https://github.com/suryakantamangaraj/Math/issues) or reach out to [Surya Raj](https://suryaraj.com).*

