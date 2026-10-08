import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold, cross_validate, cross_val_predict
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import RidgeCV
from sklearn.metrics import mean_squared_error, r2_score

train_df = pd.read_csv('BT2024032/BT2024032_train_var2.csv')
test_df = pd.read_csv('BT2024032/BT2024032_test_var2.csv')

features = ['x1', 'x2', 'x3']
X = train_df[features].values
y = train_df['y'].values
X_test = test_df[features].values

kf = KFold(n_splits=5, shuffle=True, random_state=42)

degrees = [1, 2, 4, 6, 8, 9, 10, 12, 14, 16]
ridge_mses = []

print("Evaluating polynomial degrees for var2:")
for deg in degrees:
    poly = PolynomialFeatures(degree=deg, include_bias=False)
    X_poly = poly.fit_transform(X)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_poly)

    ridge = RidgeCV(alphas=np.logspace(-2, 3, 20), cv=kf)
    cv_ridge = cross_validate(ridge, X_scaled, y, cv=kf, scoring={'mse': 'neg_mean_squared_error', 'r2': 'r2'})
    r_mse = -cv_ridge['test_mse'].mean()
    r_r2 = cv_ridge['test_r2'].mean()
    ridge_mses.append(r_mse)
    print(f"Degree {deg:2d} ({X_poly.shape[1]:3d} feats) -> Ridge MSE: {r_mse:.4f} | R2: {r_r2:.4f}")

poly = PolynomialFeatures(degree=12, include_bias=False)
X_train_poly = poly.fit_transform(X)
X_test_poly = poly.transform(X_test)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_poly)
X_test_scaled = scaler.transform(X_test_poly)

model = RidgeCV(alphas=np.logspace(-2, 3, 40), cv=kf)
model.fit(X_train_scaled, y)

train_preds = model.predict(X_train_scaled)
test_preds = model.predict(X_test_scaled)
oof_preds = cross_val_predict(model, X_train_scaled, y, cv=kf)

print(f"\nFinal Model (Degree 12 Ridge):")
print(f"Best Alpha: {model.alpha_:.4f}")
print(f"Train MSE:  {mean_squared_error(y, train_preds):.4f}")
print(f"Train R2:   {r2_score(y, train_preds):.4f}")
print(f"CV MSE:     {mean_squared_error(y, oof_preds):.4f}")
print(f"CV R2:      {r2_score(y, oof_preds):.4f}")

pred_df = pd.DataFrame({'y': test_preds})
pred_df.to_csv('BT2024032/BT2024032_pred_var2.csv', index=False)
print("Saved predictions to BT2024032/BT2024032_pred_var2.csv")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5))
ax1.plot(degrees, ridge_mses, 's-', color='tab:blue', label='Ridge MSE')
ax1.axvline(12, color='r', linestyle='--', label='Selected (d=12)')
ax1.set_xlabel('Degree')
ax1.set_ylabel('CV MSE')
ax1.set_title('var2: Error vs Degree')
ax1.legend()
ax1.grid(True)

residuals = y - oof_preds
ax2.scatter(oof_preds, y, alpha=0.4, color='tab:green', s=18)
ax2.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')
ax2.set_xlabel('Predicted y')
ax2.set_ylabel('Actual y')
ax2.set_title('var2: Parity Plot')
ax2.grid(True)

plt.tight_layout()
plt.savefig('var2_plot.png', dpi=200)
print("Saved plot to var2_plot.png")
