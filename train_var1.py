import numpy as np
import pandas as pd
from sklearn.model_selection import KFold, cross_validate
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LinearRegression, RidgeCV, LassoCV
from sklearn.metrics import mean_squared_error, r2_score

# Load data
train_df = pd.read_csv('BT2024032/BT2024032_train_var1.csv')
test_df = pd.read_csv('BT2024032/BT2024032_test_var1.csv')

features = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6']
X = train_df[features].values
y = train_df['y'].values
X_test = test_df[features].values

# 5-fold CV setup
kf = KFold(n_splits=5, shuffle=True, random_state=42)

print("Comparing polynomial degrees on var1:")
for deg in [1, 2, 3, 4, 5]:
    poly = PolynomialFeatures(degree=deg, include_bias=False)
    X_poly = poly.fit_transform(X)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_poly)
    
    # Check Ridge
    ridge = RidgeCV(alphas=np.logspace(-3, 2, 20), cv=kf)
    cv_res = cross_validate(ridge, X_scaled, y, cv=kf, scoring={'mse': 'neg_mean_squared_error', 'r2': 'r2'})
    
    val_mse = -cv_res['test_mse'].mean()
    val_r2 = cv_res['test_r2'].mean()
    print(f"Degree {deg}: {X_poly.shape[1]} features | Ridge Val MSE = {val_mse:.4f}, Val R2 = {val_r2:.4f}")

# Train final selected model: Degree 5 with Lasso
print("\nTraining final Degree 5 model with Lasso...")
poly = PolynomialFeatures(degree=5, include_bias=False)
X_train_poly = poly.fit_transform(X)
X_test_poly = poly.transform(X_test)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_poly)
X_test_scaled = scaler.transform(X_test_poly)

model = LassoCV(alphas=np.logspace(-3, 1, 30), cv=kf, max_iter=20000, random_state=42)
model.fit(X_train_scaled, y)

train_preds = model.predict(X_train_scaled)
test_preds = model.predict(X_test_scaled)

train_mse = mean_squared_error(y, train_preds)
train_r2 = r2_score(y, train_preds)

print(f"Best alpha: {model.alpha_:.5f}")
print(f"Non-zero coefficients: {np.sum(model.coef_ != 0)} / {X_train_poly.shape[1]}")
print(f"Train MSE: {train_mse:.4f}")
print(f"Train R2: {train_r2:.4f}")

# Save test predictions matching assignment template
pred_df = pd.DataFrame({'y': test_preds})
pred_df.to_csv('BT2024032/BT2024032_pred_var1.csv', index=False)
print("Saved predictions to BT2024032/BT2024032_pred_var1.csv")
