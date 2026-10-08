import numpy as np
import pandas as pd
from sklearn.model_selection import KFold, cross_validate
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LinearRegression, RidgeCV
from sklearn.metrics import mean_squared_error, r2_score

# Load data
train_df = pd.read_csv('BT2024032/BT2024032_train_var2.csv')
test_df = pd.read_csv('BT2024032/BT2024032_test_var2.csv')

features = ['x1', 'x2', 'x3']
X = train_df[features].values
y = train_df['y'].values
X_test = test_df[features].values

# 5-fold CV setup
kf = KFold(n_splits=5, shuffle=True, random_state=42)

print("Testing degrees on var2 with Ridge:")
for deg in [1, 4, 8, 10, 12, 14]:
    poly = PolynomialFeatures(degree=deg, include_bias=False)
    X_poly = poly.fit_transform(X)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_poly)
    
    ridge = RidgeCV(alphas=np.logspace(-2, 3, 20), cv=kf)
    cv_res = cross_validate(ridge, X_scaled, y, cv=kf, scoring={'mse': 'neg_mean_squared_error', 'r2': 'r2'})
    
    val_mse = -cv_res['test_mse'].mean()
    val_r2 = cv_res['test_r2'].mean()
    print(f"Degree {deg:2d}: {X_poly.shape[1]:3d} features | Ridge Val MSE = {val_mse:.4f}, Val R2 = {val_r2:.4f}")

# Train final selected model: Degree 12 with Ridge
print("\nTraining final Degree 12 model with Ridge...")
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

train_mse = mean_squared_error(y, train_preds)
train_r2 = r2_score(y, train_preds)

print(f"Best alpha: {model.alpha_:.4f}")
print(f"Train MSE: {train_mse:.4f}")
print(f"Train R2: {train_r2:.4f}")

# Save test predictions
pred_df = test_df.copy()
pred_df['y'] = test_preds
pred_df.to_csv('BT2024032/BT2024032_pred_var2.csv', index=False)
print("Saved predictions to BT2024032/BT2024032_pred_var2.csv")
