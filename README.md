# ML Assignment 1: Polynomial Regression
Roll No: BT2024032

This repository contains my code, models, and predictions for Assignment 1.

## Repository Contents
- `train_var1.py`: Trains Phase 1 model (Degree 5 Lasso), outputs test predictions to `BT2024032/BT2024032_pred_var1.csv`, and saves `var1_plot.png`.
- `train_var2.py`: Trains Phase 2 model (Degree 12 Ridge), outputs test predictions to `BT2024032/BT2024032_pred_var2.csv`, and saves `var2_plot.png`.
- `BT2024032/`: Directory containing train/test datasets and generated prediction CSV files.
- `BT2024032_report.pdf`: Final 4-page report detailing methodology, bias-variance trade-offs, regularization rationale, and diagnostics.
- `BT2024032.zip`: Final submission zip containing the report and prediction CSV files.

## How to Run
Make sure `numpy`, `pandas`, `scikit-learn`, and `matplotlib` are installed.

To train the models, generate prediction CSVs, and save the evaluation plots:
```bash
python3 train_var1.py
python3 train_var2.py
```

## Results
- **Phase 1 (var1):** I selected a Degree 5 polynomial with Lasso regularization ($\alpha \approx 0.01$). It gives a 5-fold cross-validation MSE of 0.316 and an R2 score of 0.967.
- **Phase 2 (var2):** I selected a Degree 12 polynomial with Ridge regularization ($\alpha \approx 1.76$). It gives a 5-fold cross-validation MSE of 0.258 and an R2 score of 0.995.
