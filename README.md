# Mathematics

> **Live site → [math.suryaraj.com](https://math.suryaraj.com)**

Welcome to the **Math Notes** repository — a growing, open collection of math notes, derivations, and Python-backed examples curated by [Surya Raj](https://suryaraj.com).
Whether you are a student refreshing fundamentals, an engineer looking for quick references, or someone who simply loves mathematics, you are in the right place.

---

<<<<<<< HEAD

## Branches of Mathematics

1. **Arithmetic**: Basic numerical operations and foundation for advanced concepts.
2. **Algebra**: Generalizes formulas, solves equations and inequalities.
3. **Geometry**: Shapes, sizes, and properties of figures.
4. **Calculus**: Rates of change, limits, derivatives, and integrals.
5. **Number Theory**: Properties of integers and primes.
6. **Linear Algebra**: Matrices, operations, and applications.

Other topics (Trigonometry, Combinatorics, Topology) may be added in the future.

# Mathematics

> **Live site → [math.suryaraj.com](https://math.suryaraj.com)**

Welcome to the **Math Notes** repository — a growing, open collection of math notes, derivations, and Python-backed examples curated by [Surya Raj](https://suryaraj.com).
Whether you are a student refreshing fundamentals, an engineer looking for quick references, or someone who simply loves mathematics, you are in the right place.

---

## Quick Start

**Clone and build the book locally:**

```bash
# 1. Clone and create a Python environment
git clone https://github.com/suryakantamangaraj/Math.git
cd Math
# Option 1: pip (virtualenv)
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
# Option 2: conda
conda env create -f environment.yml
conda activate mathematics

# 2. Build the book
cd notes
myst build --html            # MyST v2
# OR: jupyter-book build .   # JupyterBook v1 (legacy)

# 3. Open in browser
# Linux/macOS:
open _build/html/index.html
# Windows:
start _build/html/index.html
```

---

## Makefile Usage (Recommended)

This repo provides a `Makefile` for common tasks (requires `make`):

```bash
make install   # Install dependencies for Jupyter Book
make book      # Build the book (HTML)
make runall    # Run all notebooks and capture outputs
make clean     # Remove build artifacts
make serve     # Serve locally with Jekyll (requires Ruby)
make site      # Build and serve with Jekyll
```

On Windows, use `make` via WSL, Git Bash, or run the equivalent commands manually.

---

## Cleaning Build Artifacts

To remove all build files, run:

```bash
make clean
# or
python scripts/clean.py
```

---

## Topics Covered

The book covers the following topics (see `notes/_toc.yml` for full structure):

- **Introduction**
- **Arithmetic & Algebra**
- **Calculus**
	- First-order ODEs
	- Second-order ODEs (analytical, numerical, Fourier/power series)
- **Differential Equations**
	- Boundary Value Problems (shooting, finite difference, eigenvalue)
	- Partial Differential Equations (elliptic, parabolic)
- **Linear Algebra**
- **Geometry**
- **Number Theory**

Other topics (e.g., Trigonometry, Combinatorics, Topology) may be added in the future.

## What's Inside

| Topic | Status | Notes |
|---|---|---|
| **Arithmetic & Algebra** | ✅ Active | Basic operations, NumPy examples |
| **Calculus (ODEs)** | ✅ Active | 1st/2nd order, analytical, numerical, series |
| **Differential Equations** | ✅ Active | BVPs, PDEs, shooting, finite difference |
| **Linear Algebra** | 🚧 Needs depth | Vectors, matrices, eigenvalues, SVD |
| **Geometry** | 🚧 Needs depth | Plane, coordinate, solid, trigonometry |
| **Number Theory** | 🚧 Needs depth | Primes, modular arithmetic, Diophantine |

> **Calling all contributors!** Linear Algebra, Geometry, and Number Theory need more worked examples and Python notebooks. See [Contributing](#contributing).

---

## How It's Built

- **Framework:** [MyST Markdown](https://mystmd.org/) + [Jupyter Book](https://jupyterbook.org/)
- **Language:** Python 3 (NumPy, SciPy, Matplotlib, SymPy)
- **Hosting:** GitHub Pages ([math.suryaraj.com](https://math.suryaraj.com))
- **Config:** See `notes/myst.yml` and `notes/_toc.yml` for book structure and settings
- **License:** Code — BSD 3-Clause · Text — CC-BY-4.0

---

## Interactive Notebooks

Many sections include interactive Jupyter notebooks (`.ipynb`) in `notes/content/` and subfolders (e.g., `bvps/`, `pdes/`, `second-order/`).
You can run and modify these locally after installing dependencies.

---

## Contributing

Contributions are very welcome — no contribution is too small!

See [**contributing.md**](notes/content/contributing.md) in the book content (also rendered on the live site) for the full guide. Quick ways to help:

- 📝 **Fill topic gaps** — add worked examples or deeper explanations to Linear Algebra, Geometry, or Number Theory
- 🐍 **Add Python notebooks** — convert markdown sections into interactive `.ipynb` notebooks
- 🐞 **Fix errors** — typos, wrong formulas, broken references
- 💡 **Suggest topics** — open an [issue](https://github.com/suryakantamangaraj/Math/issues) with topic requests

Please read the [Code of Conduct](CODE_OF_CONDUCT.md) before participating.

---

## Licensing

- **Code** (`.py`, `.ipynb` code cells): [BSD 3-Clause License](LICENSE.txt)
- **Text, explanations, and diagrams**: [Creative Commons Attribution 4.0 (CC-BY-4.0)](LICENSE-text.txt)

---

## Advanced / Contributors

- **Configuration:**
	- Book structure: `notes/_toc.yml`
	- Book/project settings: `notes/myst.yml`
- **Manual cleaning:** `python scripts/clean.py`
- **Notebooks:** All interactive content is in `notes/content/` and subfolders.

---

## Support / Contact

For questions, suggestions, or issues, please [open an issue](https://github.com/suryakantamangaraj/Math/issues) or contact [Surya Raj](https://suryaraj.com).

