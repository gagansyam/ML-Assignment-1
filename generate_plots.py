import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold, cross_val_predict
from sklearn.linear_model import RidgeCV, LassoCV
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
import warnings
warnings.filterwarnings('ignore')

os.makedirs('figures', exist_ok=True)
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams.update({'font.size': 11, 'figure.autolayout': True})

# ==========================================
# FIGURE 1 & 2: PHASE 1 (var1)
# ==========================================
print("Generating Phase 1 plots...")
train1 = pd.read_csv('BT2024032/BT2024032_train_var1.csv')
X1 = train1[['x1', 'x2', 'x3', 'x4', 'x5', 'x6']].values
y1 = train1['y'].values
kf = KFold(n_splits=5, shuffle=True, random_state=42)

# Degree progression data from experiments
degrees_var1 = [1, 2, 3, 4, 5, 6]
ols_val_mse = [8.530, 2.905, 1.022, 0.752, 1.284, 3.810] # OLS explodes after deg 4
ridge_val_mse = [8.532, 2.902, 1.013, 0.705, 0.441, 0.529]
lasso_val_mse = [8.530, 2.900, 1.011, 0.628, 0.315, 0.320]

fig, ax1 = plt.subplots(figsize=(8, 4.8), dpi=300)
ax1.plot(degrees_var1, ols_val_mse, 'o--', color='#d9534f', linewidth=2, label='OLS (Unregularized)')
ax1.plot(degrees_var1, ridge_val_mse, 's-', color='#337ab7', linewidth=2, label='Ridge (L2 Regularized)')
ax1.plot(degrees_var1, lasso_val_mse, '^-.', color='#5cb85c', linewidth=2.5, label='Lasso (L1 Feature Selection)')

ax1.axvline(x=5, color='black', linestyle=':', alpha=0.7, label='Optimal Degree (d = 5)')
ax1.set_xlabel('Polynomial Degree (d)', fontsize=12, fontweight='bold')
ax1.set_ylabel('5-Fold Cross-Validation MSE', fontsize=12, fontweight='bold')
ax1.set_title('Phase 1 (var1): Model Validation Error vs. Polynomial Degree', fontsize=13, fontweight='bold')
ax1.set_xticks(degrees_var1)
ax1.set_ylim(0, 9)
ax1.legend(loc='upper right', frameon=True)
ax1.grid(True, linestyle='--', alpha=0.6)
plt.savefig('figures/var1_degree_curve.png', dpi=300)
plt.close()

# Residual Plot for Phase 1 (Lasso Degree 5)
poly1 = PolynomialFeatures(degree=5, include_bias=False)
scaler1 = StandardScaler()
X1_scaled = scaler1.fit_transform(poly1.fit_transform(X1))
lasso1 = LassoCV(alphas=np.logspace(-3, 1, 30), cv=5, max_iter=20000, random_state=42)
oof_y1 = cross_val_predict(lasso1, X1_scaled, y1, cv=kf)
res1 = y1 - oof_y1

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5), dpi=300)
ax1.scatter(oof_y1, y1, alpha=0.45, color='#2b5c8f', edgecolors='none', s=25)
ax1.plot([y1.min(), y1.max()], [y1.min(), y1.max()], 'r--', linewidth=2, label='Ideal 1:1 Fit')
ax1.set_title('Phase 1: Predicted vs. Actual (R2 = 96.8%)', fontweight='bold')
ax1.set_xlabel('Out-of-Fold Predicted Power Score')
ax1.set_ylabel('Actual Power Score')
ax1.legend()
ax1.grid(True, linestyle='--', alpha=0.6)

ax2.hist(res1, bins=30, color='#337ab7', edgecolor='black', alpha=0.7, density=True)
mu, std = np.mean(res1), np.std(res1)
x_norm = np.linspace(res1.min(), res1.max(), 100)
p_norm = (1 / (std * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x_norm - mu) / std) ** 2)
ax2.plot(x_norm, p_norm, 'r-', linewidth=2, label=f'Normal Fit (std={std:.2f})')
ax2.set_title('Phase 1: Residual Distribution (Mean ~ 0)', fontweight='bold')
ax2.set_xlabel('Residual Error (Actual - Predicted)')
ax2.set_ylabel('Density')
ax2.legend()
ax2.grid(True, linestyle='--', alpha=0.6)
plt.savefig('figures/var1_residuals.png', dpi=300)
plt.close()

# ==========================================
# FIGURE 3 & 4: PHASE 2 (var2)
# ==========================================
print("Generating Phase 2 plots...")
train2 = pd.read_csv('BT2024032/BT2024032_train_var2.csv')
X2 = train2[['x1', 'x2', 'x3']].values
y2 = train2['y'].values

deg2_range = list(range(1, 17))
ols_mse2 = [38.88, 24.38, 13.14, 4.02, 1.64, 0.65, 0.36, 0.279, 0.294, 0.343, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]
ridge_mse2 = [38.88, 24.37, 13.14, 4.02, 1.64, 0.65, 0.358, 0.272, 0.272, 0.259, 0.260, 0.2579, 0.2594, 0.2615, 0.2620, 0.2658]

fig, ax = plt.subplots(figsize=(8.5, 4.8), dpi=300)
ax.plot(deg2_range[:10], ols_mse2[:10], 'o--', color='#d9534f', linewidth=2, label='OLS (Unregularized - Overfits after d=8)')
ax.plot(deg2_range, ridge_mse2, 's-', color='#337ab7', linewidth=2.5, label='Ridge Regression (L2 Regularized)')
ax.axvline(x=12, color='green', linestyle=':', linewidth=2, label='Global Minimum (d = 12, MSE = 0.2579)')
ax.set_xlabel('Polynomial Degree (d)', fontsize=12, fontweight='bold')
ax.set_ylabel('5-Fold Cross-Validation MSE', fontsize=12, fontweight='bold')
ax.set_title('Phase 2 (var2): Model Validation Error vs. Polynomial Degree', fontsize=13, fontweight='bold')
ax.set_xticks(deg2_range)
ax.set_ylim(0, 15)
ax.legend(loc='upper right', frameon=True)
ax.grid(True, linestyle='--', alpha=0.6)
plt.savefig('figures/var2_degree_curve.png', dpi=300)
plt.close()

# Residual Plot for Phase 2 (Ridge Degree 12)
poly2 = PolynomialFeatures(degree=12, include_bias=False)
scaler2 = StandardScaler()
X2_scaled = scaler2.fit_transform(poly2.fit_transform(X2))

oof_y2 = np.zeros(len(y2))
for tr_idx, va_idx in kf.split(X2_scaled):
    r = RidgeCV(alphas=np.logspace(-2, 3, 25))
    r.fit(X2_scaled[tr_idx], y2[tr_idx])
    oof_y2[va_idx] = r.predict(X2_scaled[va_idx])

res2 = y2 - oof_y2

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5), dpi=300)
ax1.scatter(oof_y2, y2, alpha=0.45, color='#1b7837', edgecolors='none', s=25)
ax1.plot([y2.min(), y2.max()], [y2.min(), y2.max()], 'r--', linewidth=2, label='Ideal 1:1 Fit')
ax1.set_title('Phase 2: Predicted vs. Actual (R2 = 99.5%)', fontweight='bold')
ax1.set_xlabel('Out-of-Fold Predicted Thermal Anomaly')
ax1.set_ylabel('Actual Thermal Anomaly')
ax1.legend()
ax1.grid(True, linestyle='--', alpha=0.6)

ax2.hist(res2, bins=30, color='#2ca25f', edgecolor='black', alpha=0.7, density=True)
mu2, std2 = np.mean(res2), np.std(res2)
x_norm2 = np.linspace(res2.min(), res2.max(), 100)
p_norm2 = (1 / (std2 * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x_norm2 - mu2) / std2) ** 2)
ax2.plot(x_norm2, p_norm2, 'r-', linewidth=2, label=f'Normal Fit (std={std2:.2f})')
ax2.set_title('Phase 2: Residual Distribution (Mean ~ 0)', fontweight='bold')
ax2.set_xlabel('Residual Error (Actual - Predicted)')
ax2.set_ylabel('Density')
ax2.legend()
ax2.grid(True, linestyle='--', alpha=0.6)
plt.savefig('figures/var2_residuals.png', dpi=300)
plt.close()

print("All figures generated successfully in figures/")
