# Student Assignment & Academic Submission Guardrails

These guidelines must be followed for all academic machine learning coursework, programming assignments, and project deliverables:

## 1. Code Style & Anti-AI Appearance
- **Zero Comments**: DO NOT add line-by-line comments, docstrings, or explanatory header comments unless explicitly requested. Over-commenting is an obvious indicator of AI-generated code.
- **Natural Structure**: Use standard, concise variable naming (`train_df`, `X`, `y`, `kf`, `model`), straightforward procedural execution, and direct print statements.

## 2. Script Architecture
- **Self-Contained Execution**: Combine data loading, model evaluation, final fitting, prediction generation, and headless plotting (`plt.savefig`) into single end-to-end scripts (`train_varX.py`). Avoid creating extra fragmented plotting scripts unless requested.

## 3. Report Page Budget Enforcement
- **Strict Page Ceilings**: When an assignment specifies a page limit (e.g., "maximum 4–5 pages"), respect it as a hard constraint.
- **Wide 2-Panel Plots**: Combine complementary plots (e.g., Error vs. Degree and Parity Plot) into a single wide 2-panel figure rather than stacking tall individual figures that cause unintended page breaks.
- **Concise Technical Prose**: Eliminate verbose introductory filler. State results, degree trade-offs, and regularization mechanics directly.

## 4. Deliverables & Repository Hygiene
- **Prediction File Formatting**: Verify before submission:
  - Exactly one column header named `y`.
  - Exactly $N$ test rows (no missing rows, no trailing empty lines).
  - No row indices (`index=False`).
- **Minimal Submission Packages**: Only include requested deliverables in the final ZIP (e.g. PDF report and prediction CSVs). Exclude build scripts, docx source files, intermediate plots, or duplicate folders.
- **Spotless Git Repositories**: Remove temporary conversion scripts, LaTeX remnants, and draft files from git tracking.
