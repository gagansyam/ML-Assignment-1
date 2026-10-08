---
name: ml-regression-assignment
description: >-
  Step-by-step procedural runbook for completing machine learning polynomial and non-linear regression assignments.
  Use when exploring polynomial degrees, choosing regularization (Lasso vs Ridge), conducting k-fold cross-validation,
  running residual diagnostics, and generating prediction CSVs and evaluation figures.
---

# Machine Learning Regression Assignment Workflow

This skill outlines the complete methodology for developing high-accuracy polynomial regression models for continuous target estimation and preparing academic deliverables.

---

## 1. Problem Classification & Baselines

1. **Understand Physical Nature**:
   - **Sparse Feature Dependence**: A small subset of variables or high-order interactions dominate (e.g. mechanical turbine settings). Preferred model: **Lasso (L1)**.
   - **Continuous Potential Fields**: The target varies smoothly over spatial coordinates (e.g. 3D thermal conduction, gravitational fields). Preferred model: **Ridge (L2)**.
2. **Establish Linear Baseline**:
   - Always evaluate Degree 1 linear regression using 5-fold cross-validation.
   - Low $R^2$ (< 30%) and high MSE confirm underfitting (high bias), proving non-linear polynomial features are necessary.

---

## 2. Polynomial Feature Expansion & Scaling

1. **Feature Count Growth**:
   - For $d$ variables at degree $p$, feature count is $\binom{d+p}{p} - 1$.
   - Degree searches must account for the ratio of features to sample size ($N$). When features approach or exceed $N/2$, unregularized models rapidly overfit.
2. **Mandatory Feature Standardization**:
   - **Always** standardize features (`StandardScaler()`) after `PolynomialFeatures(degree=deg, include_bias=False)`.
   - Different powers ($x^1, x^2, \dots, x^d$) have wildly different scales, which distorts $L_1$ and $L_2$ penalties if unscaled.

---

## 3. Regularization Selection & Hyperparameter Tuning

1. **Systematic Degree Sweep**:
   - Test degrees incrementally with $k$-fold cross-validation (`KFold(n_splits=5, shuffle=True, random_state=42)`).
   - Track validation MSE and $R^2$ across degrees for OLS, Ridge, and Lasso.
2. **L1 Regularization (LassoCV)**:
   - Use for feature selection.
   - Verifies that irrelevant interaction terms are forced to exact zero.
   - Inspect `np.sum(model.coef_ != 0)` to report active vs. total features.
3. **L2 Regularization (RidgeCV)**:
   - Use when all polynomial terms contribute smoothly without hard sparsity.
   - Shrinks coefficient norms smoothly, suppressing runaway oscillations near data boundaries.

---

## 4. Diagnostics & Sanity Verification

1. **Out-of-Fold Parity Plot**:
   - Scatter plot of out-of-fold predictions (`cross_val_predict`) vs. true $y$ against the 1:1 diagonal.
2. **Residual Normality & Spatial Bias**:
   - Check residual distribution: mean $\approx 0$, standard deviation matching noise floor.
   - Run Jarque-Bera test on residuals ($p > 0.05$ indicates Gaussian white noise).
   - Check correlation between residuals and inputs ($|r| < 0.02$ confirms zero systematic bias).
3. **Prediction Range Verification**:
   - Ensure test predictions $[\min(\hat{y}_{\text{test}}), \max(\hat{y}_{\text{test}})]$ stay within the observed training target envelope.

---

## 5. End-to-End Script Self-Containment

- Structure training scripts (`train_varX.py`) so they run completely end-to-end:
  1. Load train and test data.
  2. Perform cross-validation search across candidate degrees.
  3. Fit final selected model on scaled training data.
  4. Write test predictions to `<ROLLNO>_pred_varX.csv` (`index=False`, single column `y`).
  5. Generate and save headless 2-panel figure (`plt.savefig('varX_plot.png', dpi=200)`).
