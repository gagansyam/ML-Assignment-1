# Assignment: Polynomial Regression

## 1. Introduction
In this assignment, you will work with two personalised datasets and develop polynomial regression models to predict a continuous target variable $y$ from the given input variables. The datasets are individually assigned to each student. Therefore, you must use the datasets corresponding to your own roll number and problem IDs.

The objective is to obtain accurate predictions on the provided test datasets using only polynomial regression.

---

## 2. Problem Statements
You are the Lead Renewable Energy Engineer managing a multi-stage geothermal power plant expansion project.

### Phase 1: Power Plant Steam Turbine Optimization (`var1`)
* **Scenario:** Before drilling new production wells, you must optimize the surface energy generation facility. Your plant operates a multi-stage steam turbine system. Due to slight variations in manufacturing tolerances and local water chemistry across regional plants, your specific plant setup behaves uniquely compared to your colleagues' facilities.
* **Input Features:** Governed by six key operational parameters $(x_1, x_2, x_3, x_4, x_5, x_6)$, representing percentage deviations:
  - $x_1$: High-pressure steam valve adjustment
  - $x_2$: Condenser coolant flow rate adjustment
  - $x_3$: Re-injection pump hydraulic pressure
  - $x_4$: Turbine blade pitch angle
  - $x_5$: Non-condensable gas exhaust valve rate
  - $x_6$: Steam inlet pressure adjustment
* **Target:** Net Power Score ($y$).
* **Model Characteristic:** The power score can be modeled using a polynomial of a moderate degree (up to degree 10) using the given parameters.
* **Task:** Using historical plant calibration logs (`train`), build a polynomial regression model to predict the Net Power Score.

---

### Phase 2: Subterranean Thermal Reservoir Mapping (`var2`)
* **Scenario:** With your surface plant optimized, Phase 2 requires you to select the exact coordinates for drilling new geothermal extraction wells. You are assigned to map a specific, high-potential geological survey block.
* **Input Features:** You deploy seismic and thermal probe sensors across a 3D grid around your central basecamp. The variables $x_1, x_2,$ and $x_3$ represent spatial coordinate offsets in meters from the site landmark:
  - $x_1$: East-West coordinate offset
  - $x_2$: North-South coordinate offset
  - $x_3$: Vertical depth offset relative to the basecamp
* **Target:** Sensor network records a Thermal Anomaly Score ($y$).
* **Model Characteristic:** Because of complex geological structures, the heat map in your sector resembles a high-degree polynomial (up to degree 20).
* **Task:** Due to survey budget limits, you have only collected physical core samples at a random scatter of 3D points (`train`). You must build a model to predict the Thermal Anomaly Score across the remaining planned drilling sites (`test`) to identify the exact coordinates and depth for drilling high-yield wells.

---

## 3. Dataset Format
Each student receives two preprocessed and cleaned datasets for two different problems. The files follow the naming convention:
`<ROLLNO>_{train/test}_var<PRBID>.csv`

For example:
- `BT2024032_train_var1.csv`
- `BT2024032_test_var1.csv`
- `BT2024032_train_var2.csv`
- `BT2024032_test_var2.csv`

Where:
- `ROLLNO` denotes the student's roll number (here: `BT2024032`).
- `train` and `test` identify the training and testing datasets respectively.
- `PRBID` identifies the assigned problem (`var1` and `var2`).
- The training and testing files corresponding to each problem must be treated as separate datasets.
- The target variable is $y$.

---

## 4. Evaluation Metrics
Predictions on the test sets will be evaluated against hidden ground truth using:
1. **Mean Squared Error (MSE):** Measures the average squared difference between predicted values and actual values.
2. **$R^2$ Score (Coefficient of Determination):** Evaluates how well the polynomial model captures the variance of the target variable.

*Note on polynomial degree definition:* You must carefully select the optimal degree for your polynomial models to avoid underfitting or overfitting. A polynomial of degree $x$ means for each term, the sum of the powers of features adds at most up to $x$.

---

## 5. Deliverables
1. **Report (PDF):** A concise write-up (max 4-5 pages) documenting approach, polynomial degree chosen for each problem, rationale behind it, and any other techniques used.
2. **Prediction Files:** Two completed test CSV files (one per problem) containing predicted values for $y$:
   - `<ROLLNO>_pred_var<PRBID>.csv` (e.g., `BT2024032_pred_var1.csv` and `BT2024032_pred_var2.csv`)
3. **Github Repo:** Containing all code used to train the models and find inference.
