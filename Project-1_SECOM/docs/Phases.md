# Document 2: Project Phases and Execution Steps

# Project 1 Execution Plan: Semiconductor Yield Prediction and Feature Selection with SECOM

## Phase 0: Semiconductor Context Setup

### Goal

Understand the semiconductor meaning of the project before analyzing the data.

### Main Idea

This is not just a machine learning project. It is a semiconductor manufacturing analytics project focused on process signals, yield failure, and feature relevance.

### Tasks

1. Define yield.
2. Define pass/fail yield testing.
3. Define process variation.
4. Define process drift.
5. Define yield excursion.
6. Define process monitoring.
7. Define false positive.
8. Define false negative.
9. Explain why false negatives may be dangerous in yield prediction.
10. Explain why engineers collect many process signals.
11. Explain why not all signals are equally useful.
12. Write a short business-context section.

### Expected Output

A section titled **Business Context**.

### Key Question

> If a yield or process engineer used this model, what decision would it support?

---

## Phase 1: Dataset Acquisition and Project Setup

### Goal

Download the SECOM dataset and organize the project professionally.

### Tasks

1. Download the SECOM dataset from a public source.
2. Save the original raw data without modification.
3. Create a separate cleaned-data location.
4. Create folders for reports, figures, notebooks, models, and documentation.
5. Create a README draft.
6. Record the dataset source.
7. Record what each file represents.
8. Record the label definition: -1 = pass, 1 = fail.
9. Confirm that no Microchip confidential data is included.

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
3. Define the positive class as failure.
4. Define the negative class as pass.
5. Write the business problem in plain English.
6. Write the machine learning problem.
7. Write the semiconductor manufacturing interpretation.
8. Explain why feature selection is part of the main problem.
9. Choose manufacturing-relevant evaluation metrics.

### Expected Output

A section titled **Problem Definition**.

### Key Question

> Are we only predicting failure, or are we also identifying useful process signals?

---

## Phase 3: Initial Data Inspection

### Goal

Understand the dataset structure and major data-quality problems.

### Tasks

1. Count the number of rows.
2. Count the number of columns.
3. Confirm that the dataset has 1,567 examples.
4. Confirm that the dataset has 591 features.
5. Count the number of pass examples.
6. Count the number of fail examples.
7. Confirm that there are 104 failures.
8. Calculate the failure percentage.
9. Count missing values per column.
10. Count missing values per row.
11. Identify columns with excessive missing values.
12. Identify columns with no variation.
13. Check for duplicate rows.
14. Check whether all features are numerical.
15. Inspect the timestamp field if available.

### Expected Output

A section titled **Data Overview**.

### Key Question

> What are the biggest data-quality problems before modeling?

---

## Phase 4: Missing Value Strategy

### Goal

Create a disciplined strategy for handling missing values.

### Main Idea

Missing values in semiconductor process data may not be random. A missing value can represent skipped measurement, unavailable sensor, different process route, tool issue, or data-collection problem.

### Tasks

1. Calculate missing percentage per feature.
2. Identify features with very high missingness.
3. Decide which features should be removed.
4. Decide whether any rows should be removed.
5. Choose an imputation strategy.
6. Decide whether to add missing-value indicators.
7. Document every cleaning decision.
8. Avoid target leakage during imputation.
9. Compare whether missingness itself appears related to failure.

### Recommended First Strategy

For the first version:

1. Remove columns with extremely high missing values.
2. Remove constant or near-constant columns.
3. Use median imputation for remaining numerical columns.
4. Add missing-value indicators only if missingness appears informative.

### Expected Output

A section titled **Data Cleaning Strategy**.

### Key Question

> Am I cleaning the data in a way that would make sense in real manufacturing analytics?

---

## Phase 5: Target Imbalance Analysis

### Goal

Understand the pass/fail class distribution.

### Main Idea

The dataset is highly imbalanced. Failures represent only about 6.6% of all examples.

### Tasks

1. Count pass examples.
2. Count fail examples.
3. Calculate pass percentage.
4. Calculate fail percentage.
5. Create a class-distribution chart.
6. Explain why normal accuracy is misleading.
7. Define the majority-class baseline.
8. Define false-negative risk.
9. Define false-positive risk.
10. Select evaluation metrics.

### Recommended Metrics

Use:

* failure-class recall,
* failure-class precision,
* F1-score,
* balanced accuracy,
* balanced error rate,
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

Explore how process features behave for pass and fail examples.

### Tasks

1. Analyze feature distributions.
2. Compare selected features for pass versus fail examples.
3. Identify skewed features.
4. Identify outliers.
5. Identify low-variance features.
6. Identify highly correlated features.
7. Compare feature averages between pass and fail groups.
8. Identify features with strong distribution differences.
9. Look for features where failures appear in extreme ranges.
10. Create visual summaries for important candidate features.

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

## Phase 7: Feature Selection Benchmark

### Goal

Rank features according to their relevance for predicting yield failure.

### Main Idea

Feature selection is central to this dataset. The original benchmark selected the top 40 features using several feature-selection methods. This project should reproduce that idea in a modern, practical way.

### Tasks

1. Rank features using simple statistical methods.
2. Compare pass/fail separation for each feature.
3. Rank features using model-based importance.
4. Rank features using permutation importance if possible.
5. Select top 40 features.
6. Select top 20 features.
7. Select top 10 features.
8. Compare models trained on all features versus selected features.
9. Identify features that appear consistently important across methods.
10. Create a feature-ranking table.
11. Explain selected features as candidates for process review.

### Possible Feature Selection Methods

Use a practical mix of:

* signal-to-noise ranking,
* t-test ranking,
* F-test ranking,
* Pearson correlation ranking,
* random forest importance,
* gradient boosting importance,
* permutation importance.

### Expected Output

A section titled **Feature Selection Benchmark**.

### Key Question

> Can a smaller set of process signals predict failures almost as well as, or better than, the full feature set?

---

## Phase 8: Dimensionality Reduction and Process Structure

### Goal

Understand the high-dimensional structure of the data.

### Tasks

1. Use scaled cleaned features.
2. Apply PCA for visualization.
3. Color PCA plots by pass/fail label.
4. Color PCA plots by model prediction.
5. Color PCA plots by prediction error type.
6. Look for possible clusters.
7. Look for possible abnormal regions.
8. Decide whether failures appear scattered or concentrated.
9. Explain PCA limitations.
10. Explain how this phase prepares the project for Mapper or TDA later.

### Expected Output

A section titled **Dimensionality Reduction and Process Structure**.

### Key Question

> Does the data appear to have process regimes or abnormal regions?

---

## Phase 9: Baseline Modeling

### Goal

Build simple baseline models before using advanced methods.

### Tasks

1. Split the data into training and testing sets.
2. Preserve class distribution during splitting.
3. Create a majority-class baseline.
4. Train a simple linear model.
5. Train a tree-based model.
6. Train a boosting model.
7. Train models on all cleaned features.
8. Train models on selected feature sets.
9. Compare results using the same metrics.
10. Save results in a model-comparison table.

### Models to Compare

Use:

* majority-class baseline,
* logistic regression,
* random forest,
* gradient boosting,
* optional SGD classifier,
* optional support vector machine.

### Feature Sets to Compare

Compare:

* all cleaned features,
* top 40 selected features,
* top 20 selected features,
* top 10 selected features.

### Expected Output

A section titled **Baseline Model Results**.

### Key Question

> Which model and feature set performs best for detecting failures?

---

## Phase 10: Cross-Validation and Balanced Error Rate

### Goal

Evaluate models in a way that aligns with the original SECOM benchmark.

### Main Idea

The original dataset description suggests 10-fold cross-validation and Balanced Error Rate. This project should include cross-validation so the results are more reliable than a single train/test split.

### Tasks

1. Use stratified cross-validation.
2. Compare models using 10-fold cross-validation if practical.
3. Calculate balanced accuracy.
4. Calculate balanced error rate.
5. Compare mean performance across folds.
6. Compare variation across folds.
7. Report whether selected features improve stability.
8. Compare your results with the original baseline conceptually.

### Expected Output

A section titled **Cross-Validation and Balanced Error Rate**.

### Key Question

> Does the model perform consistently across folds, or is performance unstable because failures are rare?

---

## Phase 11: Manufacturing-Focused Model Evaluation

### Goal

Evaluate models in a way that makes sense for yield and process teams.

### Tasks

1. Create confusion matrices.
2. Compare recall for the failure class.
3. Compare precision for the failure class.
4. Compare F1-score.
5. Compare balanced accuracy.
6. Compare balanced error rate.
7. Analyze false positives.
8. Analyze false negatives.
9. Consider threshold adjustment.
10. Explain the precision-recall tradeoff.
11. Select the best model for a yield-screening use case.

### Expected Output

A section titled **Model Evaluation**.

### Key Question

> Would this model be useful as an engineering screening tool?

---

## Phase 12: Feature Importance and Process Interpretation

### Goal

Identify which features are most associated with failure predictions.

### Tasks

1. Extract feature importance from tree-based models.
2. Compare important features across models.
3. Compare selected features across feature-selection methods.
4. Study the distributions of top features.
5. Check whether important features are correlated.
6. Check whether important features have missing-value problems.
7. Write careful interpretations.
8. Avoid causal claims.

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

## Phase 13: Error Analysis

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

## Phase 14: Optional Time-Aware Validation

### Goal

Use the timestamp to evaluate whether the model can generalize over time.

### Main Idea

Random cross-validation is useful for benchmarking, but semiconductor processes can drift over time. A time-aware validation asks whether earlier data can predict later failures.

### Tasks

1. Inspect the timestamp field.
2. Sort examples by time.
3. Train on earlier examples.
4. Test on later examples.
5. Compare with random cross-validation.
6. Discuss whether performance changes over time.
7. Explain how time drift could affect real deployment.

### Expected Output

An optional section titled **Time-Aware Validation**.

### Key Question

> Does the model still work when tested on later production examples?

---

## Phase 15: Final Model Selection

### Goal

Choose the best model and feature set.

### Tasks

1. Compare all models in one table.
2. Compare all feature sets in one table.
3. Choose the best model.
4. Choose the best feature-selection strategy.
5. Explain why it is best.
6. Discuss tradeoffs.
7. Include limitations.
8. Recommend next steps.

### Selection Criteria

Consider:

* failure-class recall,
* failure-class precision,
* balanced accuracy,
* balanced error rate,
* interpretability,
* stability across cross-validation,
* usefulness for engineering investigation.

### Expected Output

A section titled **Final Model Selection**.

### Key Question

> Which model and feature set would I present to a yield or process team, and why?

---

## Phase 16: Final Report

### Goal

Create a polished professional report.

### Recommended Report Structure

1. Executive Summary
2. Business Problem
3. Dataset Description
4. Data Quality Issues
5. Class Imbalance
6. Exploratory Data Analysis
7. Feature Selection
8. Modeling Approach
9. Cross-Validation and BER
10. Model Evaluation
11. Feature Importance
12. Error Analysis
13. Limitations
14. Recommendations
15. Next Steps

### Expected Output

A final project report in Markdown, PDF, or notebook form.

### Key Question

> Can someone understand the value of this project in five minutes?

---

## Phase 17: Portfolio README

### Goal

Create a clean GitHub README.

### README Structure

1. Project title
2. Short description
3. Business problem
4. Dataset
5. Label explanation
6. Why feature selection matters
7. Methods used
8. Main results
9. Key charts
10. Lessons learned
11. Limitations
12. Next steps
13. How to run the project

### Expected Output

A GitHub-ready README.

### Key Question

> Would this README help me explain my value to Microchip or another semiconductor employer?
