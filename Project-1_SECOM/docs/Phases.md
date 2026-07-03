# Document 2: Project Phases and Execution Steps

# Project 1 Execution Plan: Semiconductor Yield Prediction with SECOM

## Phase 0: Semiconductor Context Setup

### Goal

Understand the semiconductor meaning of the project before analyzing the data.

### Main Idea

This is not just a machine learning project. It is a manufacturing analytics project.

You need to understand what the model would mean in a yield or process environment.

### Tasks

1. Define what yield means.
2. Define what pass/fail means in manufacturing.
3. Define what process variation means.
4. Define what process drift means.
5. Define what an excursion means.
6. Define what a false positive means.
7. Define what a false negative means.
8. Decide which error is more serious in a yield-screening context.
9. Write a short business-context section.

### Expected Output

A short section titled **Business Context**.

### Key Question

> If a yield engineer used this model, what decision would it support?

---

## Phase 1: Dataset Acquisition and Project Setup

### Goal

Download the SECOM dataset and organize the project professionally.

### Tasks

1. Download the SECOM dataset from a public source.
2. Save the original raw data without modification.
3. Create a separate cleaned-data location.
4. Create folders for reports, figures, notebooks, and documentation.
5. Create a README draft.
6. Record the dataset source.
7. Record what each file represents.
8. Confirm that no Microchip confidential data is included.

### Expected Output

A clean project folder with:

* raw data,
* cleaned data location,
* README draft,
* project notes,
* dataset source documentation.

### Key Question

> Could another person open this project and understand what the dataset is?

---

## Phase 2: Problem Framing

### Goal

Define the analytics problem clearly.

### Tasks

1. Identify the target variable.
2. Identify the feature matrix.
3. Define the positive class.
4. Decide whether the class of interest is pass or fail.
5. Write the business problem in plain English.
6. Write the machine learning problem.
7. Write the semiconductor manufacturing interpretation.
8. Choose the metrics that matter most.

### Expected Output

A section titled **Problem Definition**.

### Key Question

> What exactly are we predicting, and why does it matter?

---

## Phase 3: Initial Data Inspection

### Goal

Understand the dataset structure and major data-quality problems.

### Tasks

1. Count the number of rows.
2. Count the number of columns.
3. Identify the target values.
4. Count missing values per column.
5. Count missing values per row.
6. Identify columns with excessive missing values.
7. Identify columns with no variation.
8. Check for duplicate rows.
9. Check whether all features are numerical.
10. Check the pass/fail class distribution.

### Expected Output

A section titled **Data Overview**.

### Key Question

> What are the biggest data-quality problems before modeling?

---

## Phase 4: Missing Value Strategy

### Goal

Create a disciplined strategy for handling missing values.

### Tasks

1. Calculate missing percentage per feature.
2. Identify features with very high missingness.
3. Decide which features should be removed.
4. Decide whether any rows should be removed.
5. Choose an imputation strategy.
6. Decide whether to add missing-value indicators.
7. Document every cleaning decision.
8. Make sure the target variable is not used during cleaning in a way that creates leakage.

### Recommended First Strategy

For the first version:

1. Remove columns with extremely high missing values.
2. Remove columns with almost no variation.
3. Use median imputation for remaining numerical columns.
4. Add missing indicators only if missingness appears useful.

### Expected Output

A section titled **Data Cleaning Strategy**.

### Key Question

> Am I cleaning the data in a way that would make sense in real manufacturing analytics?

---

## Phase 5: Target Imbalance Analysis

### Goal

Understand the class distribution.

### Tasks

1. Count pass examples.
2. Count fail examples.
3. Calculate the failure percentage.
4. Create a class-distribution chart.
5. Explain why accuracy may be misleading.
6. Define the false-negative risk.
7. Define the false-positive risk.
8. Select evaluation metrics.

### Recommended Metrics

Use:

* failure-class recall,
* failure-class precision,
* F1-score,
* balanced accuracy,
* confusion matrix,
* false-negative rate,
* precision-recall curve.

### Expected Output

A section titled **Class Imbalance**.

### Key Question

> Can the model detect failures, or is it only predicting the majority class?

---

## Phase 6: Exploratory Data Analysis

### Goal

Explore how the process features behave.

### Tasks

1. Analyze feature distributions.
2. Compare selected features for pass vs fail examples.
3. Identify skewed features.
4. Identify outliers.
5. Identify low-variance features.
6. Identify highly correlated features.
7. Compare feature averages between pass and fail groups.
8. Create visual summaries for important features.

### What to Look For

Look for features where:

* failures have different values,
* failures appear in outlier regions,
* missingness may be related to failure,
* feature distributions differ by class,
* groups of variables appear correlated.

### Expected Output

A section titled **Exploratory Data Analysis**.

### Key Question

> Which variables behave differently between passing and failing examples?

---

## Phase 7: Dimensionality Reduction and Process Structure

### Goal

Understand the high-dimensional structure of the data.

### Tasks

1. Remove near-zero-variance features.
2. Identify correlated groups of variables.
3. Use PCA to visualize the data.
4. Color PCA plots by pass/fail status.
5. Look for possible clusters.
6. Look for possible abnormal regions.
7. Decide whether failures appear scattered or concentrated.
8. Explain the limitations of PCA.

### Expected Output

A section titled **Dimensionality Reduction and Process Structure**.

### Key Question

> Does the data appear to have process regimes or abnormal regions?

---

## Phase 8: Baseline Modeling

### Goal

Build simple baseline models before using advanced methods.

### Tasks

1. Split the data into training and testing sets.
2. Preserve class distribution during splitting.
3. Create a majority-class baseline.
4. Train a simple linear model.
5. Train a tree-based model.
6. Train a boosting model.
7. Compare all models using the same metrics.
8. Save results in a model-comparison table.

### Models to Compare

Use:

* majority-class baseline,
* logistic regression,
* random forest,
* gradient boosting,
* optional SGD classifier,
* optional support vector machine.

### Expected Output

A section titled **Baseline Model Results**.

### Key Question

> Which simple model performs best, and does it detect failures better than the baseline?

---

## Phase 9: Manufacturing-Focused Model Evaluation

### Goal

Evaluate models in a way that makes sense for yield and process teams.

### Tasks

1. Create confusion matrices.
2. Compare recall for the failure class.
3. Compare precision for the failure class.
4. Compare F1-score.
5. Compare balanced accuracy.
6. Analyze false positives.
7. Analyze false negatives.
8. Consider threshold adjustment.
9. Explain the precision-recall tradeoff.
10. Select the best model for a yield-screening use case.

### Expected Output

A section titled **Model Evaluation**.

### Key Question

> Would this model be useful as an engineering screening tool?

---

## Phase 10: Feature Importance and Process Interpretation

### Goal

Identify which features are most associated with failure predictions.

### Tasks

1. Extract feature importance from tree-based models.
2. Compare important features across models.
3. Study the distributions of top features.
4. Check whether important features are correlated.
5. Check whether important features have missing-value problems.
6. Write careful interpretations.
7. Avoid causal claims.

### Correct Language

Use:

* “associated with failure risk,”
* “candidate for engineering review,”
* “may indicate abnormal process behavior,”
* “requires domain validation.”

Avoid:

* “this caused the failure,”
* “this is the root cause,”
* “the model proves the process problem.”

### Expected Output

A section titled **Feature Importance and Process Insight**.

### Key Question

> Which variables would I ask a process engineer to investigate first?

---

## Phase 11: Process-Regime Analysis

### Goal

Look for groups or regions of process behavior associated with higher failure risk.

### Tasks

1. Use PCA or other visual methods to look for clusters.
2. Color visualizations by pass/fail status.
3. Identify whether failures cluster in certain regions.
4. Compare model predictions across regions.
5. Identify outlier groups.
6. Write hypotheses about possible process regimes.
7. Explain what additional real-world data would help.

### Expected Output

A section titled **Process-Regime Analysis**.

### Key Question

> Are failures randomly distributed, or do they appear concentrated in specific process regions?

---

## Phase 12: Error Analysis

### Goal

Study the model’s mistakes.

### Tasks

1. Identify false positives.
2. Identify false negatives.
3. Compare their feature distributions.
4. Check whether errors are near decision boundaries.
5. Check whether errors have more missing values.
6. Check whether errors appear in unusual PCA regions.
7. Compare errors against correctly classified examples.
8. Write possible explanations.

### Expected Output

A section titled **Error Analysis**.

### Key Question

> What kinds of cases does the model misunderstand?

---

## Phase 13: Final Model Selection

### Goal

Choose the best model and explain why.

### Tasks

1. Compare all models in one table.
2. Choose the best model.
3. Explain why it is best.
4. Discuss tradeoffs.
5. Include limitations.
6. Recommend next steps.

### Selection Criteria

Consider:

* failure-class recall,
* failure-class precision,
* balanced accuracy,
* interpretability,
* robustness,
* usefulness for engineering investigation.

### Expected Output

A section titled **Final Model Selection**.

### Key Question

> Which model would I present to a yield or process team, and why?

---

## Phase 14: Final Report

### Goal

Create a polished professional report.

### Recommended Report Structure

1. Executive Summary
2. Business Problem
3. Dataset Description
4. Data Quality Issues
5. Exploratory Data Analysis
6. Modeling Approach
7. Model Evaluation
8. Feature Importance
9. Process-Regime Analysis
10. Error Analysis
11. Limitations
12. Recommendations
13. Next Steps

### Expected Output

A final project report in Markdown, PDF, or notebook form.

### Key Question

> Can someone understand the value of this project in five minutes?

---

## Phase 15: Portfolio README

### Goal

Create a clean GitHub README.

### README Structure

1. Project title
2. Short description
3. Business problem
4. Dataset
5. Methods used
6. Main results
7. Key charts
8. Lessons learned
9. Limitations
10. Next steps
11. How to run the project

### Expected Output

A GitHub-ready README.

### Key Question

> Would this README help me explain my value to Microchip or another semiconductor employer?
