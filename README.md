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

# Option A: pip (virtualenv)
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Option B: conda
conda env create -f environment.yml
conda activate mathematics

# 2. Build the book (MyST v2)
cd notes
myst build --html

# 3. Open in browser
open _build/html/index.html      # macOS/Linux
start _build/html/index.html     # Windows
```

---

## Makefile Targets

A `Makefile` is provided for common tasks (requires `make`):

```bash
make install   # Install dependencies for Jupyter Book
make book      # Build the book (HTML)
make runall    # Run all notebooks and capture outputs
make clean     # Remove build artifacts
make serve     # Serve locally with Jekyll (requires Ruby)
make site      # Build and serve with Jekyll
```

You can also clean build artifacts directly:

```bash
python scripts/clean.py
```

> On Windows, use `make` via WSL or Git Bash, or run the equivalent commands manually.

---

## Topics Covered

| Topic | Status | Highlights |
|---|---|---|
| **Arithmetic & Algebra** | ✅ Active | Basic operations, NumPy examples |
| **Calculus** | ✅ Active | First-order ODEs; second-order ODEs (analytical, numerical, Fourier & power series) |
| **Differential Equations** | ✅ Active | BVPs (shooting, finite difference, eigenvalue); PDEs (elliptic, parabolic, hyperbolic) |
| **Linear Algebra** | 🚧 In progress | Vectors, matrices, eigenvalues, SVD |
| **Geometry** | 🚧 In progress | Plane, coordinate, solid geometry, trigonometry |
| **Number Theory** | 🚧 In progress | Primes, modular arithmetic, Diophantine equations |

Additional topics (Trigonometry, Combinatorics, Topology, …) may be added in the future.

> **Calling all contributors!** Linear Algebra, Geometry, and Number Theory need more worked examples and Python notebooks. See [Contributing](#contributing).

---

## How It's Built

- **Framework:** [MyST Markdown](https://mystmd.org/) (v2) + [Jupyter Book](https://jupyterbook.org/)
- **Language:** Python 3 — NumPy, SciPy, Matplotlib, SymPy
- **Hosting:** GitHub Pages → [math.suryaraj.com](https://math.suryaraj.com)
- **Config:** `notes/myst.yml` (project & TOC) · `notes/_toc.yml` (legacy TOC reference)
- **License:** Code — BSD 3-Clause · Text — CC-BY-4.0

---

## Interactive Notebooks

Many sections include Jupyter notebooks (`.ipynb`) in `notes/content/` and subfolders (`bvps/`, `pdes/`, `second-order/`).
You can run and modify them locally after installing dependencies.

---

## Contributing

Contributions are very welcome — no contribution is too small!

See [**contributing.md**](notes/content/contributing.md) (also on the [live site](https://math.suryaraj.com)) for the full guide. Quick ways to help:

- 📝 **Fill topic gaps** — add worked examples or deeper explanations to Linear Algebra, Geometry, or Number Theory
- 🐍 **Add Python notebooks** — convert markdown sections into interactive `.ipynb` notebooks
- 🐞 **Fix errors** — typos, wrong formulas, broken references
- 💡 **Suggest topics** — open an [issue](https://github.com/suryakantamangaraj/Math/issues)

Please read the [Code of Conduct](CODE_OF_CONDUCT.md) before participating.

---

## Licensing

- **Code** (`.py`, `.ipynb` code cells): [BSD 3-Clause License](LICENSE.txt)
- **Text, explanations, and diagrams**: [Creative Commons Attribution 4.0 (CC-BY-4.0)](LICENSE-text.txt)

---

## Support

For questions, suggestions, or issues, please [open an issue](https://github.com/suryakantamangaraj/Math/issues) or reach out via [suryaraj.com](https://suryaraj.com).

