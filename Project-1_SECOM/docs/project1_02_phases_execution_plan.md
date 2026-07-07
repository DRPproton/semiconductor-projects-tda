# Project 1 — Phases and Execution Plan  
## Semiconductor Yield Prediction and Feature Selection with SECOM

This document gives the full execution plan for Project 1. It is intentionally detailed so you do not lose time deciding what to do next.

The project is organized in two ways:

1. **Project phases** — what the full project must include.
2. **Eight-week execution calendar** — what to do each week and each study day.

---

## Part A — Full Project Phases

---

# Phase 0 — Semiconductor Context Setup

## Goal

Understand the semiconductor meaning of the project before analyzing the data.

## Main idea

This is not just a machine learning project. It is a semiconductor manufacturing analytics project focused on process signals, yield failure, and feature relevance.

## Tasks

1. Define yield.
2. Define pass/fail yield testing.
3. Define process variation.
4. Define process drift.
5. Define process window.
6. Define yield excursion.
7. Define process monitoring.
8. Define sensor signal.
9. Define metrology signal.
10. Define tool/process variable.
11. Define false positive.
12. Define false negative.
13. Explain why false negatives may be dangerous in yield prediction.
14. Explain why engineers collect many process signals.
15. Explain why not all signals are equally useful.
16. Write a short business-context section.

## Expected output

A section titled:

```text
Business Context
```

## Key question

> If a yield or process engineer used this model, what decision would it support?

---

# Phase 1 — Dataset Acquisition and Project Setup

## Goal

Download the SECOM dataset and organize the project professionally.

## Tasks

1. Download the SECOM dataset from UCI.
2. Save the original raw data without modification.
3. Create a separate cleaned-data location.
4. Create folders for reports, figures, notebooks, models, and documentation.
5. Create a README draft.
6. Record the dataset source.
7. Record what each file represents.
8. Record the label definition: `-1 = pass`, `1 = fail`.
9. Confirm that no company-confidential data is included.
10. Record dataset license and citation.
11. Create a project changelog.

## Expected output

A clean project folder with:

- raw data,
- cleaned-data location,
- README draft,
- project notes,
- dataset source documentation.

## Key question

> Could another person open this project and understand what the dataset is?

---

# Phase 2 — Problem Framing

## Goal

Define the analytics problem clearly.

## Tasks

1. Identify the target variable.
2. Identify the feature matrix.
3. Define the positive class as failure.
4. Define the negative class as pass.
5. Write the business problem in plain English.
6. Write the machine learning problem.
7. Write the semiconductor manufacturing interpretation.
8. Explain why feature selection is part of the main problem.
9. Choose manufacturing-relevant evaluation metrics.
10. Define how the final results will be communicated.

## Expected output

A section titled:

```text
Problem Definition
```

## Key question

> Are we only predicting failure, or are we also identifying useful process signals?

Correct answer:

> We are doing both, but feature relevance and process/yield interpretation are central.

---

# Phase 3 — Initial Data Inspection

## Goal

Understand the dataset structure and major data-quality problems.

## Tasks

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
13. Identify columns with near-zero variation.
14. Check for duplicate rows.
15. Check whether all features are numerical.
16. Inspect the timestamp field if available.
17. Create an initial data-quality summary.

## Expected output

A section titled:

```text
Data Overview
```

## Key question

> What are the biggest data-quality problems before modeling?

---

# Phase 4 — Missing Value Strategy

## Goal

Create a disciplined strategy for handling missing values.

## Main idea

Missing values in semiconductor process data may not be random. A missing value can represent skipped measurement, unavailable sensor, different process route, tool issue, recipe difference, or data-collection problem.

## Tasks

1. Calculate missing percentage per feature.
2. Calculate missing percentage per row.
3. Identify features with very high missingness.
4. Decide which features should be removed.
5. Decide whether any rows should be removed.
6. Choose an imputation strategy.
7. Decide whether to add missing-value indicators.
8. Document every cleaning decision.
9. Avoid target leakage during imputation.
10. Compare whether missingness itself appears related to failure.
11. Compare missingness patterns in pass vs fail examples.
12. Save a missingness report.

## Recommended first strategy

For the first version:

1. Remove columns with extremely high missing values.
2. Remove constant or near-constant columns.
3. Use median imputation for remaining numerical columns.
4. Add missing-value indicators only if missingness appears informative.
5. Build cleaning with a scikit-learn pipeline so cross-validation is safe.

## Expected output

A section titled:

```text
Data Cleaning Strategy
```

## Key question

> Am I cleaning the data in a way that would make sense in real manufacturing analytics?

---

# Phase 5 — Target Imbalance Analysis

## Goal

Understand the pass/fail class distribution.

## Main idea

The dataset is highly imbalanced. Failures represent only about 6.6% of all examples.

## Tasks

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
11. Explain why failure recall matters.
12. Explain why precision still matters.
13. Decide how to present threshold tradeoffs.

## Recommended metrics

Use:

- failure-class recall,
- failure-class precision,
- F1-score,
- balanced accuracy,
- balanced error rate,
- confusion matrix,
- false-negative rate,
- precision-recall curve.

## Expected output

A section titled:

```text
Class Imbalance
```

## Key question

> Can the model detect failures, or is it only predicting the majority class?

---

# Phase 6 — Exploratory Data Analysis

## Goal

Explore how process features behave for pass and fail examples.

## Tasks

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
11. Separate feature behavior categories:
    - stable,
    - noisy,
    - missing-heavy,
    - low-variance,
    - high-variance,
    - fail-separated,
    - correlated/redundant.
12. Write process-style interpretation for each behavior group.

## What to look for

Look for features where:

- failures have different values,
- failures appear in outlier regions,
- missingness may be related to failure,
- feature distributions differ by class,
- groups of variables appear correlated,
- a small number of variables may carry much of the predictive signal.

## Expected output

A section titled:

```text
Exploratory Data Analysis
```

## Key question

> Which variables behave differently between passing and failing examples?

---

# Phase 7 — Feature Selection Benchmark

## Goal

Rank features according to their relevance for predicting yield failure.

## Main idea

Feature selection is central to this dataset. The original benchmark selected the top 40 features using several feature-selection methods. This project should reproduce that idea in a modern, practical way.

## Tasks

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
12. Measure agreement between feature-selection methods.
13. Check selected features for missingness problems.
14. Check selected features for high correlation.

## Possible feature-selection methods

Use a practical mix of:

- signal-to-noise ranking,
- t-test ranking,
- F-test ranking,
- Pearson correlation ranking,
- mutual information,
- random forest importance,
- gradient boosting importance,
- permutation importance.

## Expected output

A section titled:

```text
Feature Selection Benchmark
```

## Key question

> Can a smaller set of process signals predict failures almost as well as, or better than, the full feature set?

---

# Phase 8 — Dimensionality Reduction and Process Structure

## Goal

Understand the high-dimensional structure of the data.

## Tasks

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
11. Optionally compare PCA using all features vs selected features.
12. Optionally use UMAP only as exploratory visualization.

## Expected output

A section titled:

```text
Dimensionality Reduction and Process Structure
```

## Key question

> Does the data appear to have process regimes or abnormal regions?

---

# Phase 9 — Baseline Modeling

## Goal

Build simple baseline models before using advanced methods.

## Tasks

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
11. Keep models interpretable enough to explain.

## Models to compare

Use:

- majority-class baseline,
- logistic regression,
- random forest,
- gradient boosting,
- optional SGD classifier,
- optional support vector machine,
- optional XGBoost/LightGBM.

## Feature sets to compare

Compare:

- all cleaned features,
- top 40 selected features,
- top 20 selected features,
- top 10 selected features.

## Expected output

A section titled:

```text
Baseline Model Results
```

## Key question

> Which model and feature set performs best for detecting failures?

---

# Phase 10 — Cross-Validation and Balanced Error Rate

## Goal

Evaluate models in a way that aligns with the original SECOM benchmark.

## Main idea

The original dataset description suggests 10-fold cross-validation and Balanced Error Rate. This project should include cross-validation so results are more reliable than a single train/test split.

## Tasks

1. Use stratified cross-validation.
2. Compare models using 10-fold cross-validation if practical.
3. Calculate balanced accuracy.
4. Calculate balanced error rate.
5. Compare mean performance across folds.
6. Compare variation across folds.
7. Report whether selected features improve stability.
8. Compare your results with the original baseline conceptually.
9. Ensure feature selection happens inside cross-validation when possible.
10. Document any simplified evaluation choices.

## Expected output

A section titled:

```text
Cross-Validation and Balanced Error Rate
```

## Key question

> Does the model perform consistently across folds, or is performance unstable because failures are rare?

---

# Phase 11 — Manufacturing-Focused Model Evaluation

## Goal

Evaluate models in a way that makes sense for yield and process teams.

## Tasks

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
12. Explain the operational meaning of threshold choices.

## Expected output

A section titled:

```text
Model Evaluation
```

## Key question

> Would this model be useful as an engineering screening tool?

---

# Phase 12 — Feature Importance and Process Interpretation

## Goal

Identify which features are most associated with failure predictions.

## Tasks

1. Extract feature importance from tree-based models.
2. Compare important features across models.
3. Compare selected features across feature-selection methods.
4. Study the distributions of top features.
5. Check whether important features are correlated.
6. Check whether important features have missing-value problems.
7. Write careful interpretations.
8. Avoid causal claims.
9. Create a table of candidate engineering-review features.
10. Write follow-up questions for process engineers.

## Correct language

Use:

- “associated with failure risk,”
- “candidate for engineering review,”
- “may indicate abnormal process behavior,”
- “requires domain validation.”

Avoid:

- “this caused the failure,”
- “this is the root cause,”
- “the model proves the process problem.”

## Expected output

A section titled:

```text
Feature Importance and Process Insight
```

## Key question

> Which variables would I ask a process engineer to investigate first?

---

# Phase 13 — Error Analysis

## Goal

Study the model’s mistakes.

## Tasks

1. Identify false positives.
2. Identify false negatives.
3. Compare their feature distributions.
4. Check whether errors are near decision boundaries.
5. Check whether errors have more missing values.
6. Check whether errors appear in unusual PCA regions.
7. Compare errors against correctly classified examples.
8. Write possible explanations.
9. Identify what additional data would help explain errors.
10. Decide whether threshold tuning would reduce false negatives.

## Expected output

A section titled:

```text
Error Analysis
```

## Key question

> What kinds of cases does the model misunderstand?

---

# Phase 14 — Optional Time-Aware Validation

## Goal

Use the timestamp to evaluate whether the model can generalize over time.

## Main idea

Random cross-validation is useful for benchmarking, but semiconductor processes can drift over time. A time-aware validation asks whether earlier data can predict later failures.

## Tasks

1. Inspect the timestamp field.
2. Sort examples by time.
3. Train on earlier examples.
4. Test on later examples.
5. Compare with random cross-validation.
6. Discuss whether performance changes over time.
7. Explain how time drift could affect real deployment.
8. Look for changes in missingness or feature distributions over time.
9. Discuss limitations of timestamp granularity.

## Expected output

An optional section titled:

```text
Time-Aware Validation
```

## Key question

> Does the model still work when tested on later production examples?

---

# Phase 15 — Final Model and Feature Set Selection

## Goal

Choose the best model and feature set.

## Tasks

1. Compare all models in one table.
2. Compare all feature sets in one table.
3. Choose the best model.
4. Choose the best feature-selection strategy.
5. Explain why it is best.
6. Discuss tradeoffs.
7. Include limitations.
8. Recommend next steps.
9. Explain what would be required for real deployment.
10. Identify what engineering metadata should be added.

## Selection criteria

Consider:

- failure-class recall,
- failure-class precision,
- balanced accuracy,
- balanced error rate,
- interpretability,
- stability across cross-validation,
- usefulness for engineering investigation.

## Expected output

A section titled:

```text
Final Model and Feature Set Selection
```

## Key question

> Which model and feature set would I present to a yield or process team, and why?

---

# Phase 16 — Final Report

## Goal

Create a polished professional report.

## Recommended report structure

1. Executive Summary
2. Business Problem
3. Dataset Description
4. Semiconductor Context
5. Data Quality Issues
6. Class Imbalance
7. Exploratory Data Analysis
8. Feature Selection
9. Modeling Approach
10. Cross-Validation and BER
11. Model Evaluation
12. Feature Importance
13. Error Analysis
14. Limitations
15. Engineering Recommendations
16. Next Steps

## Expected output

A final project report in Markdown, PDF, or notebook form.

## Key question

> Can someone understand the value of this project in five minutes?

---

# Phase 17 — Portfolio README

## Goal

Create a clean GitHub README.

## README structure

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

## Expected output

A GitHub-ready README.

## Key question

> Would this README help me explain my value to a semiconductor employer?

---

# Phase 18 — Interview and Resume Translation

## Goal

Turn the project into professional language.

## Tasks

1. Write a 30-second explanation.
2. Write a 2-minute technical explanation.
3. Write resume bullets.
4. Write LinkedIn/project description.
5. Prepare answers to likely questions.
6. Prepare limitations discussion.
7. Prepare “what I would do with real fab data” explanation.

## Expected output

A file titled:

```text
docs/interview_story.md
```

## Key question

> Can I explain this project as a process/yield analytics project, not just an ML model?

---

# Part B — Eight-Week Execution Calendar

This calendar assumes you have two long study/project blocks per week and shorter one-hour sessions on other days. Adjust the exact days to your schedule.

---

## Week 1 — Business Context and Dataset Setup

**Main goal:** Understand what the dataset represents and set up the project professionally.

| Day | Time | Work |
|---|---:|---|
| Day 1 | 4–5 hrs | Read the SECOM dataset page. Write the business context. Define yield, pass/fail, process variation, process monitoring, feature selection, and yield excursion. |
| Day 2 | 1 hr | Create glossary: yield, drift, excursion, process window, sensor signal, metrology, false positive, false negative. |
| Day 3 | 1 hr | Create repository structure and README draft. |
| Day 4 | 1 hr | Download dataset, save raw files, document source/license/citation. |
| Day 5 | 1 hr | Load data and labels. Confirm dimensions, label values, timestamp field, and missing values. |
| Day 6 | 4–5 hrs | Build notebook `01_business_context.ipynb` and `02_data_overview_missingness.ipynb` skeleton. |
| Day 7 | 30–60 min | Write weekly summary: “What SECOM represents as a semiconductor process dataset.” |

### Week 1 outputs

- Business Context section
- Dataset source note
- Repo structure
- Initial README
- Raw data preserved
- First notebook skeletons

---

## Week 2 — Data Overview, Missingness, and Imbalance

**Main goal:** Understand data quality before modeling.

| Day | Time | Work |
|---|---:|---|
| Day 1 | 4–5 hrs | Compute row/column counts, label counts, missingness per feature, missingness per row, constant features, near-constant features. |
| Day 2 | 1 hr | Create missingness charts and tables. Identify top missing features. |
| Day 3 | 1 hr | Compare missingness between pass and fail examples. |
| Day 4 | 1 hr | Analyze class imbalance. Calculate pass rate, fail rate, majority-class baseline. |
| Day 5 | 1 hr | Write metric notes: why accuracy is misleading; define recall, precision, F1, balanced accuracy, BER. |
| Day 6 | 4–5 hrs | Build cleaning strategy: remove constant features, set missingness thresholds, define imputation approach, document decisions. |
| Day 7 | 30–60 min | Write weekly summary: “Missingness as manufacturing information.” |

### Week 2 outputs

- Data Overview section
- Missingness report
- Class imbalance chart
- Metric definitions
- Cleaning Strategy section

---

## Week 3 — Process-Oriented EDA

**Main goal:** Study feature behavior as process/sensor behavior.

| Day | Time | Work |
|---|---:|---|
| Day 1 | 4–5 hrs | Analyze feature distributions: mean, std, min, max, skew, outliers, variance. |
| Day 2 | 1 hr | Create feature behavior categories: stable, noisy, low-variance, high-variance, missing-heavy. |
| Day 3 | 1 hr | Compare pass vs fail distributions for candidate features. |
| Day 4 | 1 hr | Identify features where failures appear in extreme ranges. |
| Day 5 | 1 hr | Create correlation analysis and find redundant feature groups. |
| Day 6 | 4–5 hrs | Write EDA notebook and create figures/tables for final report. |
| Day 7 | 30–60 min | Weekly summary: “Which signals behave differently in failures?” |

### Week 3 outputs

- EDA notebook
- Feature behavior taxonomy
- Candidate fail-separated features
- Correlation summary
- EDA report section

---

## Week 4 — Feature Selection Benchmark

**Main goal:** Rank features and compare selected feature groups.

| Day | Time | Work |
|---|---:|---|
| Day 1 | 4–5 hrs | Implement statistical feature rankings: signal-to-noise, t-test, F-test, Pearson correlation. |
| Day 2 | 1 hr | Add mutual information or another non-linear ranking method if useful. |
| Day 3 | 1 hr | Train tree-based model and extract feature importance. |
| Day 4 | 1 hr | Compute permutation importance for the best baseline model if practical. |
| Day 5 | 1 hr | Compare overlap among top-ranked features across methods. |
| Day 6 | 4–5 hrs | Create top 40, top 20, top 10 feature sets. Save feature-ranking tables. |
| Day 7 | 30–60 min | Weekly summary: “Which features are consistently important?” |

### Week 4 outputs

- Feature Selection notebook
- Feature-ranking tables
- Top 40 / 20 / 10 feature lists
- Method-overlap summary
- Feature Selection report section

---

## Week 5 — Baseline Modeling

**Main goal:** Build simple models and compare all features vs selected features.

| Day | Time | Work |
|---|---:|---|
| Day 1 | 4–5 hrs | Create preprocessing + modeling pipelines. Implement majority baseline, logistic regression, random forest, gradient boosting. |
| Day 2 | 1 hr | Evaluate using stratified train/test split. |
| Day 3 | 1 hr | Compare all features vs top 40 features. |
| Day 4 | 1 hr | Compare top 20 and top 10 features. |
| Day 5 | 1 hr | Create confusion matrices and precision-recall curves. |
| Day 6 | 4–5 hrs | Build model-comparison table. Select candidate best models for cross-validation. |
| Day 7 | 30–60 min | Weekly summary: “Does feature selection improve model usefulness?” |

### Week 5 outputs

- Baseline Modeling notebook
- Model comparison table
- Confusion matrices
- PR curves
- First model recommendation

---

## Week 6 — Cross-Validation, BER, and Threshold Analysis

**Main goal:** Evaluate models in a way aligned with semiconductor rare-failure detection.

| Day | Time | Work |
|---|---:|---|
| Day 1 | 4–5 hrs | Implement stratified cross-validation for candidate models and feature sets. |
| Day 2 | 1 hr | Compute balanced accuracy and BER for each fold. |
| Day 3 | 1 hr | Compare mean and standard deviation across folds. |
| Day 4 | 1 hr | Perform threshold analysis for the best model. |
| Day 5 | 1 hr | Write manufacturing interpretation of recall vs precision tradeoff. |
| Day 6 | 4–5 hrs | Finalize evaluation tables and charts. |
| Day 7 | 30–60 min | Weekly summary: “Which model would I trust most for screening?” |

### Week 6 outputs

- Cross-validation notebook
- BER table
- Threshold analysis
- Manufacturing-focused metric section
- Updated model recommendation

---

## Week 7 — Error Analysis and Process Interpretation

**Main goal:** Understand model mistakes and convert selected features into engineering questions.

| Day | Time | Work |
|---|---:|---|
| Day 1 | 4–5 hrs | Identify false positives and false negatives for the selected model. |
| Day 2 | 1 hr | Compare missingness patterns in errors vs correct predictions. |
| Day 3 | 1 hr | Compare feature distributions for false negatives, false positives, true failures, and true passes. |
| Day 4 | 1 hr | Use PCA visualization colored by error type. |
| Day 5 | 1 hr | Create engineering-review questions for top features and error groups. |
| Day 6 | 4–5 hrs | Write Feature Importance and Error Analysis report sections. |
| Day 7 | 30–60 min | Weekly summary: “What would I ask a process/yield engineer?” |

### Week 7 outputs

- Error Analysis notebook
- False negative analysis
- Feature insight table
- Engineering question list
- Interpretation section

---

## Week 8 — Final Report and Portfolio Package

**Main goal:** Turn the work into a polished portfolio project.

| Day | Time | Work |
|---|---:|---|
| Day 1 | 4–5 hrs | Write the full report: executive summary, business problem, dataset, methods, results, limitations. |
| Day 2 | 1 hr | Clean figures and tables. |
| Day 3 | 1 hr | Write GitHub README. |
| Day 4 | 1 hr | Write limitations and next steps. |
| Day 5 | 1 hr | Write resume bullets and interview explanation. |
| Day 6 | 4–5 hrs | Final repo cleanup: folders, notebooks, requirements, reproducibility check. |
| Day 7 | 30–60 min | Final reflection: “How this project supports my process/yield engineer transition.” |

### Week 8 outputs

- Final report
- README
- Clean notebooks
- Reproducible repo
- Resume bullets
- Interview story

---

# Part C — Final Report Outline

Use this structure for the final report.

```text
# Semiconductor Yield Prediction and Feature Selection with SECOM

## 1. Executive Summary

## 2. Business and Manufacturing Context

## 3. Dataset Description

## 4. Problem Definition

## 5. Data Quality and Missingness

## 6. Class Imbalance and Metric Selection

## 7. Exploratory Data Analysis

## 8. Feature Selection Benchmark

## 9. Baseline Modeling

## 10. Cross-Validation and Balanced Error Rate

## 11. Manufacturing-Focused Model Evaluation

## 12. Feature Importance and Process Interpretation

## 13. Error Analysis

## 14. Limitations

## 15. Engineering Recommendations

## 16. Next Steps

## 17. Appendix
```

---

# Part D — GitHub README Outline

```text
# Semiconductor Yield Prediction and Feature Selection with SECOM

## Overview

## Why This Project Matters

## Dataset

## Problem Statement

## Methods

## Feature Selection

## Modeling and Evaluation

## Main Results

## Engineering Interpretation

## Limitations

## Next Steps

## Repository Structure

## How to Run

## References
```

---

# Part E — Final Checklist

Before calling Project 1 complete, confirm:

- [ ] Raw data preserved.
- [ ] Dataset source documented.
- [ ] Business context written.
- [ ] Labels correctly interpreted.
- [ ] Failure class set as positive.
- [ ] Missingness analyzed.
- [ ] Class imbalance explained.
- [ ] Accuracy not used as main metric.
- [ ] BER calculated.
- [ ] Feature selection completed.
- [ ] Top 40 / 20 / 10 feature sets compared.
- [ ] Cross-validation completed.
- [ ] False negatives analyzed.
- [ ] Feature importance interpreted carefully.
- [ ] No unsupported causal claims.
- [ ] Engineering questions included.
- [ ] Final report written.
- [ ] README written.
- [ ] Resume/interview explanation prepared.
