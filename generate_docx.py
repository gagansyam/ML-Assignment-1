import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

doc = docx.Document()

# Set standard 0.85-inch margins
for section in doc.sections:
    section.top_margin = Inches(0.85)
    section.bottom_margin = Inches(0.85)
    section.left_margin = Inches(0.85)
    section.right_margin = Inches(0.85)

# Configure default font to Calibri
style = doc.styles['Normal']
font = style.font
font.name = 'Calibri'
font.size = Pt(11)
font.color.rgb = RGBColor(30, 30, 30)

def add_header():
    title = doc.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = title.add_run("Assignment 1: Polynomial Regression Report")
    run.font.size = Pt(17)
    run.font.bold = True
    run.font.color.rgb = RGBColor(20, 20, 20)
    title.paragraph_format.space_after = Pt(1)

    sub = doc.add_paragraph()
    sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = sub.add_run("Geothermal Power Plant Expansion & Reservoir Mapping")
    r_sub.font.size = Pt(11.5)
    r_sub.font.color.rgb = RGBColor(100, 100, 100)
    sub.paragraph_format.space_after = Pt(4)

    meta = doc.add_paragraph()
    meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_meta = meta.add_run("Name: Gagan  |  Roll Number: BT2024032  |  GitHub: https://github.com/gagansyam/ML-Assignment-1")
    r_meta.font.size = Pt(9.5)
    r_meta.font.color.rgb = RGBColor(80, 80, 80)
    meta.paragraph_format.space_after = Pt(12)

def add_heading_1(text):
    h = doc.add_paragraph()
    r = h.add_run(text)
    r.font.size = Pt(13)
    r.font.bold = True
    r.font.color.rgb = RGBColor(25, 25, 25)
    h.paragraph_format.space_before = Pt(10)
    h.paragraph_format.space_after = Pt(3)

def add_heading_2(text):
    h = doc.add_paragraph()
    r = h.add_run(text)
    r.font.size = Pt(11.5)
    r.font.bold = True
    r.font.color.rgb = RGBColor(40, 40, 40)
    h.paragraph_format.space_before = Pt(8)
    h.paragraph_format.space_after = Pt(2)

def add_p(text):
    p = doc.add_paragraph()
    r = p.add_run(text)
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.space_after = Pt(4.5)
    return p

def add_image_placeholder(label, caption):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    cell.width = Inches(6.5)
    
    # Border & light gray shading
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="F8F8F8"/>')
    cell._tc.get_or_add_tcPr().append(shd)
    
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = parse_xml(f'''
        <w:tcBorders {nsdecls("w")}>
            <w:top w:val="dashed" w:sz="6" w:space="0" w:color="A0A0A0"/>
            <w:left w:val="dashed" w:sz="6" w:space="0" w:color="A0A0A0"/>
            <w:bottom w:val="dashed" w:sz="6" w:space="0" w:color="A0A0A0"/>
            <w:right w:val="dashed" w:sz="6" w:space="0" w:color="A0A0A0"/>
        </w:tcBorders>
    ''')
    tcPr.append(tcBorders)

    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(16)
    p.paragraph_format.space_after = Pt(8)
    
    r1 = p.add_run(f"📷 [ {label} ]\n")
    r1.font.bold = True
    r1.font.size = Pt(11)
    r1.font.color.rgb = RGBColor(60, 60, 60)
    
    r2 = p.add_run("Paste your image / screenshot here in Word")
    r2.font.italic = True
    r2.font.size = Pt(9.5)
    r2.font.color.rgb = RGBColor(120, 120, 120)

    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_cap = p_cap.add_run(caption)
    r_cap.font.italic = True
    r_cap.font.size = Pt(9)
    r_cap.font.color.rgb = RGBColor(90, 90, 90)
    p_cap.paragraph_format.space_after = Pt(8)

def format_table(tbl, col_widths, headers, data):
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr_row = tbl.rows[0]
    for idx, name in enumerate(headers):
        cell = hdr_row.cells[idx]
        cell.text = name
        cell.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        cell.paragraphs[0].runs[0].font.bold = True
        cell.paragraphs[0].runs[0].font.size = Pt(9.5)
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="EAEAEA"/>')
        cell._tc.get_or_add_tcPr().append(shd)

    for row_data in data:
        row = tbl.add_row()
        for idx, val in enumerate(row_data):
            cell = row.cells[idx]
            cell.text = str(val)
            cell.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
            cell.paragraphs[0].runs[0].font.size = Pt(9.5)

    for row in tbl.rows:
        for idx, width in enumerate(col_widths):
            row.cells[idx].width = width

    tblBorders = parse_xml(f'''
        <w:tblBorders {nsdecls("w")}>
            <w:top w:val="single" w:sz="6" w:space="0" w:color="CCCCCC"/>
            <w:bottom w:val="single" w:sz="6" w:space="0" w:color="CCCCCC"/>
            <w:insideH w:val="single" w:sz="4" w:space="0" w:color="E0E0E0"/>
            <w:insideV w:val="none"/>
            <w:left w:val="none"/>
            <w:right w:val="none"/>
        </w:tblBorders>
    ''')
    tbl._tbl.tblPr.append(tblBorders)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

# ================= BUILD CONTENT =================
add_header()

add_heading_1("1. Introduction")
add_p("For this assignment, I acted as the Lead Renewable Energy Engineer managing a multi-stage geothermal power plant expansion project. The objective was to build accurate polynomial regression models to predict continuous target variables for two assigned problems using datasets tailored to my roll number (BT2024032).")
add_p("The expansion is structured in two distinct phases:")
add_p("Phase 1: Power Plant Steam Turbine Optimization (var1). Before drilling new wells, the surface generation facility must be tuned. Plant turbine efficiency is governed by six operational percentage deviation parameters (x1: high-pressure steam valve, x2: condenser coolant flow rate, x3: re-injection pump hydraulic pressure, x4: turbine blade pitch angle, x5: non-condensable gas exhaust valve rate, and x6: steam inlet pressure). The goal is to predict the Net Power Score (y), which can be modeled using a polynomial of moderate degree (up to degree 10).")
add_p("Phase 2: Subterranean Thermal Reservoir Mapping (var2). After surface optimization, the engineering team must locate coordinates for drilling new production wells. Using seismic and thermal probe sensors across a 3D survey grid, spatial offsets in meters from the basecamp landmark are recorded (x1: East-West offset, x2: North-South offset, x3: vertical depth offset). The goal is to predict the Thermal Anomaly Score (y) across planned drilling sites, which resembles a high-degree polynomial (up to degree 20).")
add_p("Per the assignment definition, a polynomial of degree d means that for each term, the sum of powers of features adds up to at most d. Models are evaluated using Mean Squared Error (MSE = sum((y - y_hat)^2)/n) and Coefficient of Determination (R2 = 1 - sum((y - y_hat)^2)/sum((y - y_bar)^2)). I used 5-fold cross-validation on the training sets to prevent underfitting and overfitting, and final predictions are formatted to match the required submission template.")

add_heading_1("2. Phase 1: Steam Turbine Optimization (var1)")
add_heading_2("Data Inspection and Baseline Model")
add_p("I first inspected BT2024032_train_var1.csv and BT2024032_test_var1.csv. Both datasets have exactly 1,000 samples and zero missing or null entries. All six inputs (x1 to x6) are normalized percentage deviations bounded in [-1.0, 1.0]. The target variable y (Net Power Score) has a mean of 0.74, a standard deviation of 3.13, and spans from -8.83 to +11.50.")
add_p("Linear correlation analysis showed that individual features have weak to moderate linear associations with y (the strongest being -0.26 with x5 and -0.23 with x3, while x1 was only +0.03). This confirms that turbine efficiency does not depend on parameters independently, and higher-order polynomial interaction terms are necessary.")
add_p("I trained an Ordinary Least Squares (OLS) linear model (Degree 1) as a performance baseline. Evaluated using 5-fold cross-validation, it achieved a validation MSE of 8.5302 and an R2 score of only 0.1248 (capturing just 12.5% of variance). This represents high bias (underfitting), demonstrating that a flat linear plane is inadequate for multi-stage turbine aerodynamics.")

add_heading_2("Degree Exploration and Model Selection")
add_p("I systematically generated polynomial expansions from degree 1 to degree 6 (up to degree 10 is permitted, but term counts grow to 1,715 at degree 7 and 8,007 at degree 10). For each degree, I standardized the polynomial features using StandardScaler and evaluated unregularized OLS, Ridge (L2), and Lasso (L1) with 5-fold cross-validation.")

headers_1 = ["Degree", "Features", "OLS Val MSE", "OLS Val R2", "Ridge Val MSE", "Lasso Val MSE", "Lasso Val R2"]
widths_1 = [Inches(0.8), Inches(0.8), Inches(1.0), Inches(0.9), Inches(1.0), Inches(1.0), Inches(1.0)]
data_1 = [
    ["1", "6", "8.530", "0.125", "8.532", "8.530", "0.125"],
    ["2", "27", "2.905", "0.699", "2.902", "2.900", "0.699"],
    ["3", "83", "1.022", "0.894", "1.013", "1.011", "0.895"],
    ["4", "209", "0.752", "0.922", "0.705", "0.628", "0.935"],
    ["5", "461", "1.284 (overfits)", "0.869", "0.441", "0.3151", "0.9671"],
    ["6", "923", "3.810 (blows up)", "0.612", "0.529", "0.3203", "0.9666"],
]
tbl_1 = doc.add_table(rows=1, cols=7)
format_table(tbl_1, widths_1, headers_1, data_1)

add_p("As shown in Table 1, unregularized OLS improves up to degree 4, but begins overfitting severely at degree 5 where validation MSE rises from 0.752 to 1.284. At degree 6, OLS explodes to 3.810. With 461 to 923 features estimated from 800 training samples per fold, variance becomes unacceptably high.")
add_p("Lasso (L1 regularization) solved this problem effectively. Because physical turbine couplings are sparse, Lasso shrank 350 unimportant polynomial terms to zero, preserving only 111 active features. This lowered validation MSE to 0.3151 and achieved an R2 score of 96.71%. Pushing to degree 6 did not improve performance (MSE increased to 0.3203), confirming Degree 5 with Lasso as the optimal model.")

add_image_placeholder("FIGURE 1 PLACEHOLDER", "Figure 1: Validation MSE vs. Polynomial Degree for Phase 1 (var1), showing OLS overfitting at degree 5 and Lasso reaching the optimal minimum.")
add_image_placeholder("FIGURE 2 PLACEHOLDER", "Figure 2: Parity plot (predicted vs. actual) and residual error distribution for Phase 1 using Degree 5 Lasso.")

add_p("In Figure 2, the out-of-fold predictions follow the 1:1 diagonal tightly. Residuals have a mean of 0.003 (zero systematic bias) and a standard deviation of 0.56, which represents the irreducible random sensor noise in the calibration facility.")

add_heading_1("3. Phase 2: Subterranean Thermal Reservoir Mapping (var2)")
add_heading_2("Data Inspection and Baseline Model")
add_p("For Phase 2, the dataset contains 3 spatial coordinate inputs: x1 (East-West offset), x2 (North-South offset), and x3 (vertical depth offset). All coordinates in train and test are bounded inside [-1.0, 1.0]. The target variable y (Thermal Anomaly Score) has a mean of 2.38, a standard deviation of 7.22, and ranges from -30.10 to +39.87.")
add_p("The linear correlation between x2 and y was 0.50, but correlations with x1 and x3 were near zero. The baseline linear model (Degree 1) had a validation MSE of 38.88 and an R2 of only 0.243. Because underground thermal plumes curve sharply through subterranean rock strata, a simple linear model leaves severe underfitting.")

add_heading_2("Degree Exploration and Model Selection")
add_p("In 3 variables, the number of polynomial terms grows more slowly than in 6 variables, which allowed me to test degrees from 1 up to 16 using 5-fold cross-validation with Ridge regression (L2 regularization).")

headers_2 = ["Degree", "Features", "OLS Val MSE", "OLS Val R2", "Ridge Val MSE", "Ridge Val R2", "Best Alpha"]
widths_2 = [Inches(0.8), Inches(0.8), Inches(1.0), Inches(0.9), Inches(1.0), Inches(1.0), Inches(1.0)]
data_2 = [
    ["1", "3", "38.883", "0.243", "38.880", "0.243", "0.01"],
    ["2", "9", "24.376", "0.529", "24.375", "0.529", "0.01"],
    ["4", "34", "4.016", "0.922", "4.016", "0.922", "0.01"],
    ["6", "83", "0.646", "0.987", "0.646", "0.987", "0.01"],
    ["8", "164", "0.2788", "0.994", "0.2719", "0.995", "0.07"],
    ["9", "219", "0.2939 (overfits)", "0.994", "0.2718", "0.995", "0.11"],
    ["10", "285", "0.3428 (overfits)", "0.993", "0.2589", "0.995", "0.46"],
    ["12", "454", "---", "---", "0.2579", "0.9951", "1.21"],
    ["14", "679", "---", "---", "0.2615", "0.9950", "1.96"],
    ["16", "968", "---", "---", "0.2658", "0.9949", "3.16"],
]
tbl_2 = doc.add_table(rows=1, cols=7)
format_table(tbl_2, widths_2, headers_2, data_2)

add_p("As shown in Table 2, unregularized OLS achieves its best error at Degree 8 (MSE = 0.2788), but then begins overfitting at degrees 9 and 10. Ridge regression (L2 penalty) prevents this by penalizing large weights. As the degree increases, Ridge automatically raises the penalty alpha from 0.07 at degree 8 to 1.21 at degree 12.")
add_p("At Degree 12 (454 features), Ridge reaches the lowest validation MSE across all experiments: 0.2579, explaining 99.51% of the total variance. Beyond degree 12, validation error creeps upward slightly (0.2615 at degree 14, 0.2658 at degree 16; at degree 20, 1,770 terms yield 0.2929 MSE), confirming Degree 12 as the optimal choice.")

add_image_placeholder("FIGURE 3 PLACEHOLDER", "Figure 3: Validation MSE vs. Polynomial Degree for Phase 2 (var2), showing OLS overfitting past degree 8 and Ridge reaching the minimum at degree 12.")
add_image_placeholder("FIGURE 4 PLACEHOLDER", "Figure 4: Parity plot (predicted vs. actual) and residual error distribution for Phase 2 using Degree 12 Ridge.")

add_p("I verified the model using several diagnostic checks. A Jarque-Bera normality test on the residuals gave a p-value of 0.66 (p > 0.05), confirming that the residuals are pure Gaussian white noise with standard deviation 0.51. Correlations between residuals and coordinates (x1, x2, x3) were all below 0.015, proving zero spatial bias. Furthermore, test predictions span [-29.51, +39.18], which matches the training range without runaway boundary spikes.")

add_heading_1("4. Discussion: Bias, Variance, and Regularization")
add_p("In both problems, finding the optimal polynomial degree required balancing bias and variance. Lower degrees (1 to 3) suffered from high bias because they lacked the capacity to capture true physical curvatures, leading to poor R2 scores. Conversely, higher-degree models without regularization suffered from high variance, attempting to fit random sensor fluctuations and causing validation errors to spike once feature counts approached sample size.")
add_p("Regularization resolved these challenges effectively according to each problem's physics. In Phase 1, Lasso (L1) worked best because the turbine control response is sparse; Lasso eliminated 350 noisy combinations and retained 111 genuine interaction terms. In Phase 2, Ridge (L2) was more appropriate because subterranean heat diffusion creates continuous, smooth potential fields across 3D coordinates. Ridge shrank all 454 coefficients smoothly, preserving fine geological contours without boundary instability.")

add_heading_1("5. Conclusion")
add_p("Table 3 summarizes the final models selected for both problems. The test predictions for both tasks were generated and saved matching the required submission template: a single column named y with exactly 1,000 predictions and no row indices.")

headers_3 = ["Problem", "Degree", "Penalty", "Terms", "CV MSE", "CV R2", "Output File"]
widths_3 = [Inches(1.0), Inches(0.8), Inches(1.2), Inches(0.9), Inches(0.9), Inches(0.9), Inches(1.8)]
data_3 = [
    ["Phase 1 (var1)", "5", "Lasso (alpha ~ 0.011)", "111 / 461", "0.3151", "96.71%", "BT2024032_pred_var1.csv"],
    ["Phase 2 (var2)", "12", "Ridge (alpha ~ 1.76)", "454 / 454", "0.2579", "99.51%", "BT2024032_pred_var2.csv"],
]
tbl_3 = doc.add_table(rows=1, cols=7)
format_table(tbl_3, widths_3, headers_3, data_3)

add_p("For Phase 1, the Degree 5 Lasso model captures non-linear turbine valve interactions while eliminating noise, predicting the Net Power Score with 96.7% accuracy. For Phase 2, the Degree 12 Ridge model maps the subterranean thermal reservoir with 99.5% accuracy, providing reliable estimates to guide well drilling. All code, datasets, and predictions are available in the GitHub repository at https://github.com/gagansyam/ML-Assignment-1.")

output_path = "report.docx"
doc.save(output_path)
print(f"Successfully generated {output_path}!")
