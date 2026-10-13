


UCI Wine Quality Dataset: Exploratory Data Analysis (EDA)

1. Project Overview
This project presents a rigorous technical and statistical exploration of the 
UCI Vinho Verde red wine quality dataset. It focuses on developing foundational 
data science competencies, transitioning from descriptive data querying to critical 
statistical reasoning about observational data, class distributions, and the hazards 
of misinterpreting correlation as causation.

2. Dataset
File Used: winequality-red.csv
Dimensions: 1,599 rows and 12 columns 
Features: 
A. fixed acidity, 
volatile acidity, 
citric acid, 
residual sugar, 
chlorides, 
free sulfur dioxide, 
total sulfur dioxide, 
density, pH, sulphates, 
alcohol, 
and quality.

3. Tools and Techniques
Language & Libraries: Python using pandas for data manipulation, cleaning, and metric calculations.
Data Inspection: Inspected data structures, checked for missing values (isna().sum()), and analyzed value counts for the target variable (quality).
Data Visualization: Utilized scatter plots and bar charts to evaluate relationships between continuous variables and discrete quality ratings.
Statistical Reasoning: Addressed core machine learning principles, distinguishing between association and causation.

4. Key Findings
Severe Class Imbalance: Quality scores 5 and 6 dominate the dataset, accounting for approximately 82.5% of all observations. This heavy skew can limit a model's ability to accurately predict minority classes.
Quality Score Trend: Quality score 8 has the highest mean alcohol content (12.09), while quality score 5 exhibits a mean alcohol content of 9.90.
Upward Trend Interruption: Mean alcohol levels generally scale upward from score 3 (9.96) to score 8 (12.1), though the trend dips temporarily at score 5 before continuing upward.
Association vs. Causation: The observed positive relationship between higher alcohol content and top ratings demonstrates an association, not a causal relationship.


5. Visualisations
Bar Charts: Used to map group averages of alcohol content across discrete quality scores and to display the class distribution frequency.
Scatter Plots: Used to inspect feature correlations and examine individual data points across continuous chemical measurements.


6. Limitations
Class Imbalance Distortion: Uneven distribution creates high statistical noise and uncertainty for rare scores (like 3, 4, and 8).
Confounded Variables: Focusing solely on alcohol ignores how interacting chemical properties—such as acidity, volatile compounds, or sugar—drive overall quality.
Lack of Causal Proof: Observational trends do not prove that altering a wine's alcohol level will directly cause its quality score to change.
Masked Variation via Group Averages: Summary statistics like group means collapse diverse data points into a single number, hiding the wide spread and significant overlap of individual wine values across categories.
Visual Limitations: Relying exclusively on high-level visual plots can mask underlying data distributions, making it risky to draw broad conclusions.


7. How to Run the Notebook
To reproduce this analysis locally, follow these steps:
Clone the Repository:
git clone https://github.com/your-username/al-ml-engineering-journey.git
cd al-ml-engineering-journey/wine_quality


Ensure Dependencies Are Installed: Make sure you have Python, pandas and matplotlib installed in your environment:
pip install pandas
pip install matplotlib

- **Required Dataset File**: Ensure `winequality-red.csv` is placed inside a `./wine_quality/` directory relative to your script or notebook.


Run the Notebook: Open Jupyter Notebook or Jupyter Lab and run wine_quailty_data_analysis.ipynb sequentially to execute the EDA pipeline.
