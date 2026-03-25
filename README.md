# Mathematics

> **Live site → [math.suryaraj.com](https://math.suryaraj.com)**

Welcome to the **Math Notes** repository — a growing, open collection of math notes, derivations, and Python-backed examples curated by [Surya Raj](https://suryaraj.com).
Whether you are a student refreshing fundamentals, an engineer looking for quick references, or someone who simply loves mathematics, you are in the right place.

---

## What's Inside

| Topic | Status | Notes |
|---|---|---|
| **Arithmetic & Algebra** | ✅ Active | Basic operations, NumPy examples |
| **Calculus — 1st-order ODEs** | ✅ Active | Integration, separation of variables, Bernoulli |
| **Calculus — 2nd-order ODEs** | ✅ Active | Analytical, numerical, Fourier series, power series |
| **Differential Equations — BVPs** | ✅ Active | Shooting method, finite difference, eigenvalue |
| **Differential Equations — PDEs** | ✅ Active | Elliptic and parabolic types |
| **Linear Algebra** | 🚧 Needs depth | Vectors, matrices, eigenvalues, SVD — fill gaps! |
| **Geometry** | 🚧 Needs depth | Plane, coordinate, solid, trigonometry — fill gaps! |
| **Number Theory** | 🚧 Needs depth | Primes, modular arithmetic, Diophantine — fill gaps! |

> **Calling all contributors!** The Linear Algebra, Geometry, and Number Theory sections have solid outlines but need more worked examples, Python notebooks, and deeper coverage. See [Contributing](#contributing) below.

---

## How It's Built

- **Framework**: [MyST Markdown](https://mystmd.org/) + [Jupyter Book](https://jupyterbook.org/)
- **Language**: Python 3 (NumPy, SciPy, Matplotlib)
- **Hosting**: GitHub Pages at [math.suryaraj.com](https://math.suryaraj.com)
- **License**: Code — BSD 3-Clause · Text — CC-BY-4.0

---

## Running Locally

```bash
# 1. Clone and create virtual environment
git clone https://github.com/suryakantamangaraj/Math.git
cd Math
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Build the book
cd notes
myst build --html            # MyST v2
# OR: jupyter-book build .   # JupyterBook v1 (legacy)

# 4. Open in browser
open _build/html/index.html
```

---

## Contributing

Contributions are very welcome — no contribution is too small!

See [**CONTRIBUTING.md**](notes/content/contributing.md) in the book content (also rendered on the live site) for the full guide.  Quick ways to help:

- 📝 **Fill topic gaps** — add worked examples or deeper explanations to Linear Algebra, Geometry, or Number Theory
- 🐍 **Add Python notebooks** — convert existing markdown sections into interactive `.ipynb` notebooks
- 🐛 **Fix errors** — typos, wrong formulas, broken references
- 💡 **Suggest topics** — open an [issue](https://github.com/suryakantamangaraj/Math/issues) with topic requests

Please read the [Code of Conduct](CODE_OF_CONDUCT.md) before participating.

---

## Licensing

- **Code** (`.py`, `.ipynb` code cells): [BSD 3-Clause License](LICENSE.txt)
- **Text, explanations, and diagrams**: [Creative Commons Attribution 4.0 (CC-BY-4.0)](LICENSE-text.txt)

