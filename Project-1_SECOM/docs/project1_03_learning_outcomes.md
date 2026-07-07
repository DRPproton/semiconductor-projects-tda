# Project 1 — Learning Outcomes  
## Semiconductor Yield Prediction and Feature Selection with SECOM

This document explains what you should learn from Project 1. The goal is not to learn basic Python or machine learning. The goal is to learn how to use your existing analytics skills through a semiconductor process/yield engineering lens.

---

## 1. Main Learning Outcomes

By the end of this project, you should be able to explain and apply the following:

1. How semiconductor process data is different from normal business data.
2. Why process monitoring creates many sensor and measurement signals.
3. Why not all process signals are equally useful.
4. Why feature selection matters in semiconductor yield analytics.
5. Why yield prediction is important in manufacturing.
6. Why missing values are common in process datasets.
7. Why missingness may contain process information.
8. Why class imbalance matters in pass/fail prediction.
9. Why accuracy is not enough for manufacturing classification.
10. How to calculate and interpret balanced error rate.
11. How to evaluate a failure-prediction model.
12. How to compare all features versus selected features.
13. How to interpret model results carefully.
14. How to avoid claiming causation from correlation.
15. How to use dimensionality reduction to understand process behavior.
16. How to communicate model results to engineering teams.
17. How this project can later connect to TDA.
18. How to convert an ML result into an engineering question.

---

## 2. What You Should Learn in Each Project Stage

---

# Stage 1 — Semiconductor Manufacturing Context

## What you should learn

You should understand basic manufacturing vocabulary:

- yield,
- pass/fail,
- process variation,
- process drift,
- process window,
- yield excursion,
- process monitoring,
- out-of-control condition,
- scrap,
- rework,
- false positive,
- false negative,
- process signal,
- metrology signal,
- sensor signal,
- tool health,
- route difference.

## Why it matters

Without manufacturing context, the project becomes just another ML classification project. With manufacturing context, it becomes a semiconductor analytics project.

## Spend more time understanding

Spend extra time on:

- yield,
- process monitoring,
- yield excursions,
- process drift,
- false negatives,
- false positives,
- feature selection as engineering prioritization.

## Key understanding

A model is useful only if it supports a real manufacturing decision.

You should be able to say:

> The goal is not only to predict fail/pass. The goal is to identify useful process signals and support engineering investigation.

---

# Stage 2 — Dataset Understanding

## What you should learn

You should learn how to inspect a high-dimensional semiconductor dataset.

Important facts for this dataset:

- 1,567 examples,
- 591 features,
- 104 failures,
- -1 means pass,
- 1 means fail,
- each row is one production entity,
- each feature is an anonymized process or sensor signal,
- labels include date/time stamp,
- the dataset contains missing values.

## Why it matters

The dataset is wide, noisy, imbalanced, and anonymized. You should not jump directly into modeling.

## Spend more time understanding

Spend extra time on:

- high-dimensional data,
- anonymized features,
- noisy sensor data,
- low-variance features,
- class distribution,
- missing-value patterns,
- timestamp meaning,
- production-entity interpretation.

## Key understanding

Before modeling, you need to understand the condition and structure of the data.

You should be able to say:

> A high-dimensional process dataset must be profiled before it is modeled because data quality, missingness, and imbalance can dominate the result.

---

# Stage 3 — Missing Values

## What you should learn

You should understand that missing values are not always random.

In manufacturing, missing values may happen because:

- a sensor was unavailable,
- a process step was skipped,
- a measurement was not required,
- a tool did not record data,
- a route was different,
- a recipe was different,
- a data-collection system failed,
- a metrology step was not performed,
- a tool state was not logged,
- an upstream event prevented downstream measurement.

## Why it matters

If you handle missing values carelessly, you may remove useful information or create misleading results.

## Spend more time understanding

Spend extra time on:

- missing completely at random,
- missing at random,
- missing not at random,
- median imputation,
- missing-value indicators,
- data leakage during imputation,
- missingness by class,
- missingness by row,
- missingness as route/tool/metrology information.

## Key understanding

Missingness itself can sometimes contain information.

You should be able to say:

> In semiconductor data, a missing value may be a process clue, not just a data-cleaning inconvenience.

---

# Stage 4 — Class Imbalance

## What you should learn

You should understand why pass/fail datasets are often imbalanced.

In this dataset, only about 6.6% of examples are failures.

## Why it matters

A model can achieve high accuracy by predicting the majority class all the time.

For this dataset, a model that predicts every example as pass would achieve about 93.4% accuracy but detect zero failures.

## Spend more time understanding

Spend extra time on:

- minority class,
- failure-class recall,
- precision,
- F1-score,
- balanced accuracy,
- balanced error rate,
- confusion matrix,
- false-negative rate,
- precision-recall curve,
- threshold selection.

## Key understanding

Accuracy can be misleading when failures are rare.

You should be able to say:

> Accuracy is not enough because a model can predict pass for every example and still look accurate while detecting no failures.

---

# Stage 5 — Feature Selection

## What you should learn

Feature selection is one of the most important concepts in this project.

You should understand how to rank features based on their relationship with the target variable.

Feature selection can help answer:

- Which process signals are most useful?
- Can we reduce hundreds of signals to a smaller useful set?
- Do selected features improve model performance?
- Do selected features make the model easier to interpret?
- Which features should process engineers investigate?
- Are selected features stable across methods?
- Are selected features affected by missingness?
- Are selected features redundant?

## Why it matters

The original purpose of the dataset is related to identifying useful signals from many noisy or irrelevant signals.

## Spend more time understanding

Spend extra time on:

- signal-to-noise ranking,
- t-test feature ranking,
- F-test feature ranking,
- Pearson correlation ranking,
- mutual information,
- model-based feature importance,
- permutation importance,
- top 40 feature selection,
- top 20 feature selection,
- top 10 feature selection,
- feature selection versus feature extraction,
- feature-selection leakage inside cross-validation.

## Key understanding

This project is not just about prediction. It is about finding useful process signals.

You should be able to say:

> The purpose of feature selection is to identify the smallest useful group of signals that can help predict or investigate yield failure.

---

# Stage 6 — Exploratory Data Analysis

## What you should learn

You should learn how to explore whether process variables behave differently for pass and fail examples.

Important ideas:

- feature distributions,
- outliers,
- skewed variables,
- correlations,
- pass/fail comparison,
- feature ranking,
- process variation,
- missingness patterns,
- distribution shift,
- abnormal regions.

## Why it matters

EDA helps you understand the data before trusting a model.

## Spend more time understanding

Spend extra time on:

- comparing distributions,
- detecting outliers,
- understanding correlation,
- identifying variables that separate pass and fail examples,
- separating process-style interpretation from ML-style interpretation.

## Key understanding

EDA helps you find possible process signals before modeling.

You should be able to say:

> EDA is where I start translating numerical variables into possible process-signal behavior.

---

# Stage 7 — Dimensionality Reduction

## What you should learn

You should learn why high-dimensional data is hard to understand visually.

SECOM has 591 features, so you need tools like PCA to reduce the data into fewer dimensions for visualization.

## Why it matters

Dimensionality reduction can help reveal:

- clusters,
- outliers,
- process regimes,
- abnormal regions,
- whether failures are concentrated or scattered,
- whether false negatives share similar structure.

## Spend more time understanding

Spend extra time on:

- PCA,
- explained variance,
- scaling before PCA,
- PCA plots,
- process-regime interpretation,
- PCA limitations,
- failure clustering,
- error-type visualization.

## Key understanding

PCA is useful for visualization, but it does not capture every kind of structure.

You should be able to say:

> PCA is not proof of a process regime, but it can help identify regions of process space that deserve closer review.

---

# Stage 8 — Baseline Modeling

## What you should learn

You should learn why every project needs simple baselines.

A baseline helps you know whether a more complex model is actually useful.

## Why it matters

Without a baseline, you cannot prove your model adds value.

## Spend more time understanding

Spend extra time on:

- majority-class baseline,
- logistic regression,
- random forest,
- gradient boosting,
- train/test split,
- stratified split,
- selected features versus all features,
- model comparison,
- reproducible pipelines.

## Key understanding

A complex model is only valuable if it performs better than simple alternatives.

You should be able to say:

> The baseline is the reference point that tells me whether the model is actually detecting failures or only reflecting the class imbalance.

---

# Stage 9 — Balanced Error Rate

## What you should learn

Balanced Error Rate is central to the original SECOM benchmark.

Balanced accuracy is the average of the true positive rate and true negative rate.

Balanced Error Rate is:

```text
BER = 1 - balanced accuracy
```

Lower BER is better.

## Why it matters

BER is useful when the classes are imbalanced because it gives weight to both pass and fail performance.

## Spend more time understanding

Spend extra time on:

- true positive rate,
- true negative rate,
- balanced accuracy,
- balanced error rate,
- why BER is better than accuracy here,
- why BER should be reported with recall and precision.

## Key understanding

BER helps evaluate both failure detection and pass detection fairly.

You should be able to explain:

> BER is useful here because it evaluates performance across both the pass and fail classes instead of letting the majority class dominate the metric.

---

# Stage 10 — Cross-Validation

## What you should learn

You should understand why the original benchmark used 10-fold cross-validation.

Because the dataset has only 104 failures, one train/test split may be unstable.

## Why it matters

Cross-validation gives a more reliable estimate of model performance.

## Spend more time understanding

Spend extra time on:

- stratified cross-validation,
- 10-fold cross-validation,
- mean performance,
- performance variation,
- leakage prevention,
- feature selection inside cross-validation,
- imputation inside cross-validation,
- comparing feature sets across folds.

## Key understanding

Feature selection should be performed carefully so test-fold information does not leak into training.

You should be able to say:

> If feature selection is done before cross-validation, the test folds can influence the selected features, making the performance look better than it really is.

---

# Stage 11 — Manufacturing-Focused Evaluation

## What you should learn

You should learn how to evaluate models based on manufacturing risk.

Important metrics:

- recall,
- precision,
- F1-score,
- balanced accuracy,
- BER,
- confusion matrix,
- false-negative rate,
- precision-recall curve,
- threshold analysis.

## Why it matters

In yield prediction, missing a real failure may be more important than flagging a good unit, depending on the use case.

## Spend more time understanding

Spend extra time on:

- confusion matrix,
- false negatives,
- false positives,
- recall versus precision,
- threshold selection,
- engineering screening use case,
- cost of missed failures,
- cost of unnecessary review.

## Key understanding

The best model is not always the model with the highest accuracy.

You should be able to say:

> A model with slightly lower precision may be acceptable if it catches more real failures and is used only as an engineering screening tool.

---

# Stage 12 — Feature Importance and Causality Limits

## What you should learn

You should learn how to identify which variables influence model predictions while avoiding causal overclaims.

Important ideas:

- feature importance,
- permutation importance,
- correlation,
- association,
- causation,
- engineering validation,
- anonymized-feature limitation,
- correlated-feature distortion.

## Why it matters

Feature selection and feature importance can suggest what engineers should investigate, but they do not prove root cause.

## Spend more time understanding

Spend extra time on:

- feature importance limitations,
- correlated features,
- avoiding causal claims,
- communicating uncertainty,
- difference between predictive feature and causal factor.

## Key understanding

Feature importance can suggest what to investigate, but it does not prove root cause.

You should be able to say:

> This feature is associated with failure risk and may be worth engineering review, but the anonymized dataset does not allow me to claim physical causality.

---

# Stage 13 — Process-Regime Thinking

## What you should learn

You should learn to think in terms of process regimes.

A process regime can be:

- normal stable behavior,
- abnormal process state,
- tool-specific behavior,
- drift condition,
- hidden production route,
- outlier group,
- chamber-matching issue,
- maintenance-related state,
- recipe-related state.

## Why it matters

Failures may not be randomly distributed. They may occur more often in certain process regions.

## Spend more time understanding

Spend extra time on:

- clustering,
- PCA regions,
- outlier regions,
- abnormal groups,
- process-state interpretation,
- comparing correct and incorrect predictions in process space.

## Key understanding

Manufacturing data often has hidden structure.

You should be able to say:

> A process regime is a region of data space where the manufacturing process appears to behave differently.

---

# Stage 14 — Error Analysis

## What you should learn

You should learn how to study model mistakes.

Important error types:

- false positives,
- false negatives,
- borderline cases,
- unusual feature patterns,
- missing-value-heavy cases,
- outlier-like cases,
- cases in abnormal PCA regions.

## Why it matters

Error analysis helps you understand whether the model is failing randomly or for specific types of examples.

## Spend more time understanding

Spend extra time on:

- false-negative analysis,
- false-positive analysis,
- decision boundaries,
- error distribution,
- model limitations,
- threshold tradeoffs,
- engineering follow-up data.

## Key understanding

Model mistakes often teach you more than model successes.

You should be able to say:

> False negatives are especially important because they represent actual failures that the model would fail to flag.

---

# Stage 15 — Communication

## What you should learn

You should learn how to communicate results professionally.

The report should be understandable to:

- data analysts,
- yield engineers,
- process engineers,
- manufacturing managers,
- recruiters,
- hiring managers.

## Why it matters

A technically good project is not enough. You need to explain why it matters.

## Spend more time understanding

Spend extra time on:

- executive summary,
- business problem,
- feature-selection story,
- visual storytelling,
- limitations,
- recommendations,
- next steps,
- interview explanation,
- resume translation.

## Key understanding

A strong portfolio project tells a clear technical and business story.

You should be able to say:

> I can explain what I did, why it matters for yield/process engineering, what the model can and cannot say, and what engineering follow-up would be needed.

---

## 3. Concepts You Should Spend the Most Time Understanding

---

# 1. Feature Selection

This is the most important concept in the updated project.

You should understand:

- why engineers collect many signals,
- why many signals are irrelevant or noisy,
- why fewer features can sometimes be better,
- how to rank features,
- how to compare selected features,
- how to explain selected features to engineers,
- why top 40 is a meaningful comparison for SECOM,
- why selected features need engineering validation.

You should be able to say:

> The purpose of feature selection is to identify the smallest useful group of signals that can help predict or investigate yield failure.

---

# 2. Class Imbalance

This is also central.

You should understand:

- only about 6.6% of the dataset is failure examples,
- normal accuracy is misleading,
- failure recall is important,
- false negatives matter,
- balanced metrics are needed.

You should be able to say:

> Accuracy is not enough because a model can predict pass for every example and still look accurate while detecting no failures.

---

# 3. Balanced Error Rate

Spend serious time understanding BER.

You should understand:

- true positive rate,
- true negative rate,
- balanced accuracy,
- balanced error rate,
- why lower BER is better.

You should be able to explain:

> BER is useful here because it evaluates performance across both the pass and fail classes instead of letting the majority class dominate the metric.

---

# 4. Cross-Validation

Spend time understanding cross-validation because the original benchmark used 10-fold cross-validation.

You should understand:

- why one train/test split may be unstable,
- why stratification matters,
- why feature selection should happen inside the training folds,
- how to report mean and variation,
- how cross-validation gives a more reliable performance estimate.

---

# 5. Missing Values

Spend extra time understanding missing values because semiconductor process data often has missing measurements.

You should understand:

- why missing values happen,
- when to drop features,
- when to impute,
- when missingness may be informative,
- why imputation must be done carefully,
- why missingness can represent route/tool/metrology differences.

---

# 6. False Positives vs False Negatives

A false positive means:

> The model predicts failure, but the entity actually passes.

A false negative means:

> The model predicts pass, but the entity actually fails.

In many yield-screening situations, false negatives are more dangerous because the model misses actual risky units.

---

# 7. Feature Importance Versus Root Cause

Feature importance is useful but dangerous if misunderstood.

You should understand:

- importance does not prove causation,
- correlated features can distort importance,
- selected features require engineering validation,
- anonymized features limit physical interpretation,
- predictive value is not the same as physical cause.

Use language like:

> This feature is associated with failure risk and may be worth engineering review.

Do not say:

> This feature caused the failure.

---

# 8. PCA and Process Regimes

PCA is important because it helps you visualize high-dimensional process data.

You should understand:

- why scaling matters,
- what principal components represent,
- how to read PCA plots,
- how failures may cluster in PCA space,
- why PCA may miss nonlinear structure,
- how PCA can support process-regime thinking.

This is also the bridge to TDA later.

---

# 9. TDA Preparation

For this dataset, do not start with persistent homology on individual rows.

The better future TDA extension is:

- Mapper for process-regime discovery,
- topology of high-dimensional process clouds,
- comparison of failure and pass regions,
- nonlinear structure beyond PCA.

The correct learning order is:

1. Understand the manufacturing problem.
2. Clean and analyze the data.
3. Build normal ML baselines.
4. Apply feature selection.
5. Evaluate models correctly.
6. Interpret results.
7. Then add TDA and compare.

---

## 4. Weekly Learning Outcomes

| Week | Learning outcome |
|---|---|
| Week 1 | Explain SECOM as a semiconductor process-monitoring dataset and define the business/yield problem. |
| Week 2 | Explain missingness, class imbalance, and why ordinary accuracy is misleading. |
| Week 3 | Interpret EDA as process/sensor behavior instead of generic variable summaries. |
| Week 4 | Compare feature-selection methods and explain why selected signals matter. |
| Week 5 | Build baseline models and compare all features vs selected features. |
| Week 6 | Evaluate models with cross-validation, BER, failure recall, and threshold analysis. |
| Week 7 | Analyze false positives/false negatives and convert model results into engineering questions. |
| Week 8 | Communicate the project as a professional process/yield analytics portfolio artifact. |

---

## 5. Self-Assessment Checklist

By the end of the project, you should be able to answer these without notes.

### Dataset

- [ ] What is SECOM?
- [ ] How many examples are there?
- [ ] How many features are there?
- [ ] How many failures are there?
- [ ] What does `-1` mean?
- [ ] What does `1` mean?
- [ ] Why are missing values expected in manufacturing data?

### Metrics

- [ ] Why is accuracy misleading?
- [ ] What is failure recall?
- [ ] What is failure precision?
- [ ] What is balanced accuracy?
- [ ] What is balanced error rate?
- [ ] Why is BER useful for SECOM?
- [ ] What is a false negative?
- [ ] Why do false negatives matter?

### Feature selection

- [ ] Why is feature selection central to SECOM?
- [ ] What is signal-to-noise ranking?
- [ ] What is t-test feature ranking?
- [ ] What is F-test feature ranking?
- [ ] What is permutation importance?
- [ ] Why compare top 40, top 20, and top 10 features?
- [ ] Why should feature selection happen inside cross-validation?

### Process/yield interpretation

- [ ] What is a yield excursion?
- [ ] What is process drift?
- [ ] What is a process window?
- [ ] What is a process signal?
- [ ] What is a metrology signal?
- [ ] What extra metadata would help interpret selected features?
- [ ] Why can’t anonymized features prove root cause?

### Communication

- [ ] Can I explain this project in 30 seconds?
- [ ] Can I explain this project in 2 minutes?
- [ ] Can I write one resume bullet for it?
- [ ] Can I explain limitations clearly?
- [ ] Can I describe what I would do with real fab metadata?

---

## 6. Final Learning Objective

At the end of this project, you should be able to say:

> I understand how to analyze semiconductor process data, handle missing values and class imbalance, select relevant process signals, build failure-prediction models, evaluate them using balanced manufacturing-relevant metrics, interpret feature relevance carefully, and communicate findings in a way that supports yield or process engineering work.

---

## 7. Final Portfolio Capability

After finishing Project 1, you should be able to present yourself as someone who can connect:

```text
semiconductor manufacturing context
+ process/yield thinking
+ feature selection
+ rare-event classification
+ balanced evaluation
+ engineering communication
```

That is the real value of the project.
