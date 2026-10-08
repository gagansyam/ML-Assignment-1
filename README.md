# Geothermal Power Plant Expansion: Polynomial Regression Models

**Roll Number:** BT2024032  
**Course:** Machine Learning  
**Assignment:** Polynomial Regression  

---

## 1. Project Overview

In this project, I develop and deploy two separate polynomial regression models for an expansion project at a geothermal energy generation facility:

1. **Phase 1: Power Plant Steam Turbine Optimization (`var1`)**
   - **Task:** Predict the Net Power Score ($y$) based on 6 turbine operational percentage deviations ($x_1$ through $x_6$).
   - **Model:** 5th-Degree Polynomial Regression with `StandardScaler` and **Lasso (L1) Regularization**.
   - **Validation $R^2$:** **$96.77\%$** | **Validation MSE:** **$0.3167$**

2. **Phase 2: Subterranean Thermal Reservoir Mapping (`var2`)**
   - **Task:** Predict the subterranean Thermal Anomaly Score ($y$) across 3D spatial coordinate offsets ($x_1, x_2, x_3$).
   - **Model:** 12th-Degree Polynomial Regression with `StandardScaler` and **Ridge (L2) Regularization**.
   - **Validation $R^2$:** **$99.51\%$** | **Validation MSE:** **$0.2579$**

---

## 2. Directory Structure

```text
├── BT2024032/
│   ├── BT2024032_train_var1.csv   # Historical training logs for Phase 1
│   ├── BT2024032_test_var1.csv    # Unlabeled test set for Phase 1
│   ├── BT2024032_pred_var1.csv    # Final completed predictions for Phase 1
│   ├── BT2024032_train_var2.csv   # Geological survey core samples for Phase 2
│   ├── BT2024032_test_var2.csv    # Unlabeled test drill coordinates for Phase 2
│   └── BT2024032_pred_var2.csv    # Final completed predictions for Phase 2
├── figures/
│   ├── var1_degree_curve.png      # Validation MSE vs. Degree for Phase 1
│   ├── var1_residuals.png         # Parity fit and residual distribution for Phase 1
│   ├── var2_degree_curve.png      # Validation MSE vs. Degree for Phase 2
│   └── var2_residuals.png         # Parity fit and residual distribution for Phase 2
├── train_var1.py                  # Standalone training & inference script for Phase 1
├── train_var2.py                  # Standalone training & inference script for Phase 2
├── generate_plots.py              # Script to regenerate all diagnostic plots
├── run_pipeline.py                # End-to-end master runner
├── PROBLEM_STATEMENT.md           # Assignment specification
└── README.md                      # Documentation
```

---

## 3. How to Run the Code

### Prerequisites
Make sure you have Python 3 installed along with standard scientific libraries:
```bash
pip install numpy pandas scikit-learn matplotlib scipy
```

### Reproducing Training and Generating Predictions
To train both models, execute cross-validation, and write test predictions to the `BT2024032/` directory, run:
```bash
python3 run_pipeline.py
```

Or run each phase individually:
```bash
# Phase 1: Steam Turbine Optimization
python3 train_var1.py

# Phase 2: Thermal Reservoir Mapping
python3 train_var2.py
```

### Regenerating Figures
To regenerate the high-resolution diagnostic plots used in the report:
```bash
python3 generate_plots.py
```

---

## 4. Key Results Summary

| Problem | Selected Degree | Model Architecture | Validation MSE | Validation $R^2$ | Key Feature Dynamics |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Phase 1 (`var1`)** | **Degree 5** | Polynomial + Scaler + Lasso | **$0.3167$** | **$96.77\%$** | Pruned 350 noise terms, retained 111 key operational interactions. |
| **Phase 2 (`var2`)** | **Degree 12** | Polynomial + Scaler + Ridge | **$0.2579$** | **$99.51\%$** | Global validation minimum, zero spatial bias, normal residual noise ($\sigma=0.51$). |
