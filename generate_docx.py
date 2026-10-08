import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

doc = docx.Document()

# Set standard 1-inch margins
for section in doc.sections:
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(1.0)
    section.right_margin = Inches(1.0)

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
    run.font.size = Pt(18)
    run.font.bold = True
    run.font.color.rgb = RGBColor(20, 20, 20)
    title.paragraph_format.space_after = Pt(2)

    sub = doc.add_paragraph()
    sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = sub.add_run("Geothermal Power Plant Expansion & Reservoir Mapping")
    r_sub.font.size = Pt(12)
    r_sub.font.color.rgb = RGBColor(100, 100, 100)
    sub.paragraph_format.space_after = Pt(6)

    meta = doc.add_paragraph()
    meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_meta = meta.add_run("Name: Gagan  |  Roll Number: BT2024032  |  GitHub: https://github.com/gagansyam/ML-Assignment-1")
    r_meta.font.size = Pt(10)
    r_meta.font.color.rgb = RGBColor(80, 80, 80)
    meta.paragraph_format.space_after = Pt(18)

def add_heading_1(text):
    h = doc.add_paragraph()
    r = h.add_run(text)
    r.font.size = Pt(14)
    r.font.bold = True
    r.font.color.rgb = RGBColor(25, 25, 25)
    h.paragraph_format.space_before = Pt(14)
    h.paragraph_format.space_after = Pt(4)

def add_heading_2(text):
    h = doc.add_paragraph()
    r = h.add_run(text)
    r.font.size = Pt(12)
    r.font.bold = True
    r.font.color.rgb = RGBColor(40, 40, 40)
    h.paragraph_format.space_before = Pt(10)
    h.paragraph_format.space_after = Pt(3)

def add_p(text):
    p = doc.add_paragraph()
    r = p.add_run(text)
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.space_after = Pt(6)
    return p

def add_image_placeholder(label, caption):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    cell.width = Inches(6.5)
    
    # Border & light gray shading
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="F5F5F5"/>')
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
    p.paragraph_format.space_before = Pt(20)
    p.paragraph_format.space_after = Pt(8)
    
    r1 = p.add_run(f"📷 [ {label} ]\n")
    r1.font.bold = True
    r1.font.size = Pt(11)
    r1.font.color.rgb = RGBColor(70, 70, 70)
    
    r2 = p.add_run("Paste your image / screenshot here in Word")
    r2.font.italic = True
    r2.font.size = Pt(10)
    r2.font.color.rgb = RGBColor(120, 120, 120)

    # Caption below table
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_cap = p_cap.add_run(caption)
    r_cap.font.italic = True
    r_cap.font.size = Pt(9.5)
    r_cap.font.color.rgb = RGBColor(90, 90, 90)
    p_cap.paragraph_format.space_after = Pt(10)

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

    # Set column widths & borders
    for row in tbl.rows:
        for idx, width in enumerate(col_widths):
            row.cells[idx].width = width

    # Subtle gray borders
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
    doc.add_paragraph().paragraph_format.space_after = Pt(6)

# ================= BUILD CONTENT =================
add_header()

add_heading_1("1. Introduction")
add_p("For this assignment, I worked on two predictive modeling tasks as part of a geothermal power plant expansion project. The goal was to build accurate polynomial regression models using historical calibration data and spatial survey points assigned to my roll number (BT2024032).")
add_p("The project is split into two phases. In Phase 1 (var1), the objective is to model surface turbine efficiency and predict the Net Power Score (y) using 6 operational percentage adjustments (x1 through x6). In Phase 2 (var2), the objective is to map subterranean thermal reservoirs by predicting the Thermal Anomaly Score (y) across 3D spatial coordinate offsets (x1, x2, x3) relative to the survey basecamp.")
add_p("To avoid underfitting or overfitting, I used 5-fold cross-validation on the training data to evaluate different polynomial degrees and tested regularization methods (L1 Lasso and L2 Ridge). Once the best degree and penalty were selected, I trained the final models on the full dataset and generated predictions for the test sets.")

add_heading_1("2. Phase 1: Steam Turbine Optimization (var1)")
add_heading_2("Data and Baseline")
add_p("I first loaded BT2024032_train_var1.csv and BT2024032_test_var1.csv. Both datasets have exactly 1,000 rows, and there are no missing or null values. All 6 input variables (x1 to x6) are normalized percentage deviations bounded in the interval [-1.0, 1.0]. The target variable (Net Power Score) has a mean of 0.74, a standard deviation of 3.13, and values ranging from -8.83 to +11.50.")
add_p("When looking at the linear correlation between individual inputs and y, the values are quite weak to moderate. The strongest correlations were around -0.26 for x5 and -0.23 for x3, while x1 was only +0.03. This indicated that turbine power cannot be explained by individual control knobs alone, and interaction terms between pressures and valve settings are necessary.")
add_p("I trained a basic linear regression model (Degree 1) as a benchmark. Evaluated across 5-fold cross-validation, the linear baseline gave a validation MSE of 8.5302 and an R2 of 0.1248 (explaining just 12.5% of the variance). This shows high bias (underfitting), meaning a straight hyperplane is too rigid to capture the turbine's curved response.")

add_heading_2("Model Selection and Regularization")
add_p("Next, I expanded the features using polynomial terms from degree 1 up to degree 6. With 6 inputs, the number of candidate terms grows rapidly: degree 2 has 27 terms, degree 3 has 83 terms, degree 4 has 209 terms, degree 5 has 461 terms, and degree 6 has 923 terms. I evaluated standard Ordinary Least Squares (OLS), Ridge (L2), and Lasso (L1) across each degree using 5-fold cross-validation.")

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

add_p("As shown in Table 1, standard OLS works well up to degree 4, but starts overfitting heavily at degree 5 where validation MSE jumps from 0.752 to 1.284. At degree 6, OLS blows up to 3.810. Because each fold has only 800 training rows, estimating 461 to 923 unconstrained parameters creates too much variance.")
add_p("Lasso (L1 regularization) solved this cleanly. By applying an L1 penalty, Lasso forced 350 unimportant interaction terms to exactly zero, keeping only 111 active features. This brought the validation MSE down to 0.3151 and achieved an R2 score of 96.71%. Moving to degree 6 did not improve performance (Lasso MSE increased slightly to 0.3203), confirming that Degree 5 is the optimal degree.")

add_image_placeholder("FIGURE 1 PLACEHOLDER", "Figure 1: Validation MSE vs. Polynomial Degree for Phase 1 (var1), showing OLS overfitting at degree 5 and Lasso reaching the minimum.")
add_image_placeholder("FIGURE 2 PLACEHOLDER", "Figure 2: Parity plot (predicted vs. actual) and residual error distribution for Phase 1 using Degree 5 Lasso.")

add_p("In Figure 2, the predicted vs. actual points lie tightly on the 1:1 diagonal. The residuals have a mean of 0.003 (no systematic bias) and a standard deviation of 0.56, which matches the expected random sensor noise in the plant calibration logs.")

add_heading_1("3. Phase 2: Subterranean Thermal Reservoir Mapping (var2)")
add_heading_2("Data and Baseline")
add_p("For Phase 2, the dataset contains 3 spatial inputs (x1 = East-West, x2 = North-South, x3 = Depth) and one target y (Thermal Anomaly Score). All coordinates in both train and test lie within [-1.0, 1.0]. The target variable has a mean of 2.38, a standard deviation of 7.22, and ranges from -30.10 to +39.87.")
add_p("Looking at linear correlations, x2 had a moderate correlation of 0.50 with y, but x1 and x3 were close to zero. The baseline linear model (Degree 1) had a validation MSE of 38.88 and an R2 of only 0.243. Because underground thermal plumes curve sharply in 3D space, a simple linear model leaves large errors and a higher degree polynomial is required.")

add_heading_2("Model Selection and Regularization")
add_p("With 3 features, the number of polynomial terms grows more slowly than in Phase 1, allowing me to evaluate degrees from 1 up to 16 using 5-fold cross-validation with Ridge regression.")

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

add_p("As seen in Table 2, unregularized OLS reaches its minimum error at Degree 8 (MSE = 0.2788), but then starts overfitting at degrees 9 and 10. Ridge regression (L2 penalty) prevents this by penalizing large weights. As the degree increases, Ridge automatically increases the penalty alpha (from 0.07 at degree 8 to 1.21 at degree 12).")
add_p("At Degree 12 (454 features), Ridge reaches the lowest validation MSE across all experiments: 0.2579, explaining 99.51% of the total variance. Beyond degree 12, validation error creeps upward slightly (0.2615 at degree 14, 0.2658 at degree 16), which confirmed Degree 12 as the best choice.")

add_image_placeholder("FIGURE 3 PLACEHOLDER", "Figure 3: Validation MSE vs. Polynomial Degree for Phase 2 (var2), showing OLS overfitting past degree 8 and Ridge reaching the minimum at degree 12.")
add_image_placeholder("FIGURE 4 PLACEHOLDER", "Figure 4: Parity plot (predicted vs. actual) and residual error distribution for Phase 2 using Degree 12 Ridge.")

add_p("I also performed sanity checks on the predictions. A Jarque-Bera normality test on the residuals gave a p-value of 0.66 (p > 0.05), showing the errors are purely random Gaussian noise with standard deviation 0.51. Correlations between residuals and coordinates (x1, x2, x3) were all below 0.015, confirming zero spatial bias. Furthermore, test predictions span [-29.51, +39.18], which matches the training range without boundary spikes.")

add_heading_1("4. Discussion: Bias, Variance, and Regularization")
add_p("In both problems, finding the right model came down to managing the bias-variance trade-off. Lower degrees (1 to 3) suffered from high bias because they were too rigid to follow the physical curves, leading to poor R2 scores. On the other hand, high-degree models without regularization suffered from high variance, attempting to fit every random noise spike in the training folds and causing validation errors to climb.")
add_p("Regularization resolved these issues effectively. In Phase 1, Lasso (L1) worked best because the turbine formula depends on a sparse set of active interactions. Lasso dropped 350 noisy terms and retained 111 genuine features. In Phase 2, Ridge (L2) performed better because heat diffusion through rock creates continuous, smooth potential fields. L2 shrinkage smoothly controlled all 454 coefficients, keeping the 3D surface stable right up to degree 12.")

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

add_p("For Phase 1, the Degree 5 Lasso model captures non-linear turbine valve interactions while eliminating noise, achieving 96.7% accuracy. For Phase 2, the Degree 12 Ridge model maps the subterranean thermal reservoir with 99.5% accuracy, giving reliable estimates to guide well drilling. All code, datasets, and predictions are available in the GitHub repository at https://github.com/gagansyam/ML-Assignment-1.")

output_path = "report.docx"
doc.save(output_path)
print(f"Successfully generated {output_path}!")
