UCI Wine Quality Dataset: Exploratory Data Analysis (EDA)
Overview
This repository contains a rigorous technical and statistical exploration 
of the UCI Vinho Verde wine quality dataset (1,599 observations). 
The project focuses on learning data science best practices, 
moving from descriptive data querying to critical statistical reasoning 
about observational data.

**Key Activities & Techniques**
 1. Data Inspection & Querying: 
 Used ⁠pandas⁠ methods (⁠min⁠, ⁠count⁠, ⁠groupby⁠, and ⁠.mean()⁠) 
to analyze feature distributions and calculate metrics across discrete quality scores.
 2. Data Visualization:
 Constructed scatter plots to examine the relationship 
between continuous variables (e.g., alcohol content) and 
discrete outcomes (quality scores).
 Implemented bar charts to display group averages and class distributions.
 3.Statistical Reasoning: 
Addressed the critical gap between correlation and causation, 
identifying the risks of interpreting observational trends 
without controlled experiments.

**Key Limitations Identified**
 Correlation vs. Causation: Observational trends (like higher mean alcohol in top-rated wines) only show association, not that altering alcohol will cause quality to change.
 Class Imbalance: The dataset is heavily skewed toward scores 5 and 6, creating high statistical noise and uncertainty for rare scores (like 3, 4, and 8).
 Confounding Variables: Focusing on a single chemical property ignores how interacting factors (acidity, sugar, volatile compounds) drive overall quality.
 Masked Variation: Group averages and summary charts hide individual data point overlap and internal distribution spreads.


