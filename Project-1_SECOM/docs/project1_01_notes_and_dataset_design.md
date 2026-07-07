# Project 1 — Notes and Dataset Design  
## Semiconductor Yield Prediction and Feature Selection with SECOM

This document captures the project notes, dataset facts, manufacturing interpretation, design choices, and terminology needed before starting the code.

---

## 1. Why These Notes Matter

The SECOM project can easily become a normal data science project if you jump directly into cleaning, modeling, and scoring. That would miss the value of the dataset.

The correct framing is:

> SECOM is a semiconductor manufacturing process-monitoring dataset where the main challenge is to identify useful process/sensor signals from many noisy, irrelevant, redundant, or missing signals.

These notes are the foundation for the project report, README, and notebook introductions.

---

## 2. Dataset Identity

| Item | Description |
|---|---|
| Dataset name | SECOM |
| Source | UCI Machine Learning Repository |
| Domain | Semiconductor manufacturing |
| Main task | Classification / feature relevance |
| Examples | 1,567 |
| Features | 591 |
| Failure count | 104 |
| Label file | Contains pass/fail label and timestamp |
| Feature file | Contains process/sensor measurements |
| Missing values | Yes |
| License | CC BY 4.0 according to UCI |
| Correct positive class | Fail = 1 |
| Correct negative class | Pass = -1 |

---

## 3. Original Dataset Meaning

The dataset description says that a complex semiconductor manufacturing process is monitored through signals collected from sensors or process measurement points.

This implies:

1. Each feature is likely a process signal, sensor value, metrology value, or measurement-derived variable.
2. Some signals may be strongly related to downstream yield.
3. Some signals may be irrelevant.
4. Some signals may be redundant.
5. Some signals may be noisy.
6. Some useful signals may be buried inside noise.
7. Engineers may collect far more signals than are necessary for a particular monitoring problem.

Therefore, the dataset is fundamentally about **process monitoring and feature selection**.

---

## 4. Core Dataset Quote to Paraphrase in Your Report

Do not copy the source text directly in your final report. Paraphrase it like this:

> In modern semiconductor manufacturing, many process and sensor signals are collected to monitor production. However, not every signal is equally useful for yield monitoring. The SECOM dataset represents this type of situation: high-dimensional process data with noisy, irrelevant, and potentially useful signals mixed together. The project goal is to identify which features are most relevant for predicting pass/fail yield outcomes and which may deserve engineering review.

---

## 5. Why Feature Selection Is the Main Point

Feature selection is not a small optional step. It is one of the main reasons the dataset exists.

### Why engineers care

Feature selection can help process/yield engineers:

- reduce the number of signals they monitor,
- identify measurements that may relate to yield excursions,
- focus engineering investigation,
- reduce noise in monitoring systems,
- reduce time to learning,
- improve process understanding,
- prioritize sensor/metrology review,
- support process-control decisions.

### Project interpretation

The project should answer:

> Can a smaller group of selected process features detect rare yield failures and provide useful engineering direction?

This means you should compare:

- all cleaned features,
- top 40 features,
- top 20 features,
- top 10 features.

---

## 6. Dataset Structure Notes

SECOM has two main files:

1. `secom.data`
   - Feature matrix.
   - 1,567 rows.
   - 591 features.
   - Real-valued data.
   - Missing values represented as `NaN`.

2. `secom_labels.data`
   - Classification label.
   - Date/time stamp.
   - Label meaning:
     - `-1` = pass
     - `1` = fail

### Important design decision

Keep the original data untouched:

```text
data/raw/
```

Create cleaned or processed versions separately:

```text
data/interim/
data/processed/
```

Never overwrite the raw data.

---

## 7. Label Notes

Correct label setup:

| Raw label | Meaning | Modeling meaning |
|---:|---|---|
| -1 | Pass | Negative class |
| 1 | Fail | Positive class |

Why this matters:

- Failure is the rare class.
- Failure is the class you care most about detecting.
- Recall should be calculated for failure, not pass.
- False negatives mean actual failures predicted as pass.
- False negatives may be more dangerous in yield-screening contexts.

---

## 8. Class Imbalance Notes

The dataset contains:

```text
Total examples = 1567
Failure examples = 104
Pass examples = 1463
```

Failure rate:

```text
104 / 1567 = 0.0664 ≈ 6.6%
```

Pass rate:

```text
1463 / 1567 = 0.9336 ≈ 93.4%
```

### Why accuracy is misleading

A model that predicts every example as pass would get:

```text
1463 / 1567 ≈ 93.4% accuracy
```

But it would detect:

```text
0 failures
```

Therefore, accuracy alone is not useful.

### Better metrics

Use:

- failure recall,
- failure precision,
- F1-score,
- balanced accuracy,
- balanced error rate,
- false-negative rate,
- confusion matrix,
- precision-recall curve.

---

## 9. Balanced Error Rate Notes

Balanced Error Rate, or BER, is important because the original SECOM benchmark used it.

Balanced accuracy is:

```text
balanced accuracy = (true positive rate + true negative rate) / 2
```

Balanced Error Rate is:

```text
BER = 1 - balanced accuracy
```

Lower BER is better.

### Why BER matters here

BER is useful because it gives weight to both classes. The majority pass class cannot dominate the metric the way it dominates ordinary accuracy.

### How to explain it

Use this wording:

> Because failures are rare, ordinary accuracy can be misleading. Balanced error rate evaluates both the pass and fail classes more fairly by accounting for performance on each class.

---

## 10. Missing Value Notes

The dataset contains missing values. In manufacturing data, missing values should not be treated as only a technical cleaning problem.

Missing values may represent:

- unavailable sensor,
- skipped measurement,
- route difference,
- tool not used,
- measurement not required,
- metrology step skipped,
- data-collection failure,
- sensor logging issue,
- tool communication issue,
- recipe-specific measurement,
- downstream test point not reached.

### Project rule

Before imputing, analyze missingness.

Do not immediately drop or fill missing values without documentation.

### Missingness questions

Ask:

1. Which features have the most missing values?
2. Which rows have many missing values?
3. Are missing values more common in fail examples?
4. Are missing values concentrated in certain feature groups?
5. Do missing-value indicators help detect failure?
6. Does dropping high-missingness features improve or harm performance?
7. Could missingness represent route/tool/metrology behavior?

### Recommended first strategy

For the first version:

1. Remove constant features.
2. Remove features with extremely high missingness.
3. Use median imputation for remaining numerical features.
4. Consider missing-value indicators only after checking whether missingness is informative.
5. Perform imputation inside cross-validation folds to avoid leakage.

---

## 11. Feature Type Notes

The features are anonymized and real-valued.

Because they are anonymized:

- Do not claim physical root cause.
- Do not say “Feature 103 is etch pressure” unless the source provides that information.
- Do not say a feature caused failure.
- Do not overinterpret feature names.
- Use cautious language.

Correct wording:

- “associated with failure risk”
- “predictive signal”
- “candidate for engineering review”
- “potential process signal”
- “requires domain validation”
- “may represent a sensor/metrology/process variable”

Incorrect wording:

- “caused the failure”
- “proves the root cause”
- “this is the bad tool”
- “this is the exact process step”
- “this feature is definitely CMP pressure”

---

## 12. Process/Yield Engineering Vocabulary

Create a project glossary and use it consistently.

### Yield

The proportion of production units that pass required tests or meet specifications.

### Pass/fail test

A binary outcome used to classify a production entity as acceptable or failing.

### Process variation

Natural or abnormal changes in process outputs due to tool, material, recipe, environment, or operator factors.

### Process drift

A gradual change in process behavior over time.

### Process window

The range of process conditions where outputs remain acceptable.

### Yield excursion

A sudden or abnormal reduction in yield or increase in failure rate.

### Process monitoring

The collection and analysis of sensor, tool, recipe, and metrology data to understand or control production.

### Metrology

Measurement of wafer, film, pattern, device, or process characteristics.

### False positive

The model predicts fail, but the entity actually passes.

### False negative

The model predicts pass, but the entity actually fails.

### Manufacturing screening tool

A model or analysis used to flag potentially risky units, lots, wafers, or process states for review.

---

## 13. Semiconductor Process Connections

Because the features are anonymized, you cannot map a specific SECOM feature to a known process step. However, you can discuss what types of process signals may exist in a semiconductor dataset.

| Process area | Possible signal types | Why it could affect yield |
|---|---|---|
| Oxidation | temperature, time, gas flow, film thickness, uniformity | oxide thickness/quality can affect device behavior |
| Deposition | chamber pressure, gas flow, RF power, film thickness, stress | film properties affect integration and reliability |
| Plasma etch | RF power, pressure, endpoint, gas flow, etch rate | over/under-etch can create pattern or electrical defects |
| Wet clean / wet etch | chemistry concentration, pH, bath age, time, rinse/dry | residues, particles, or surface condition affect downstream steps |
| CMP | pressure, platen speed, slurry flow, removal rate, nonuniformity | dishing, erosion, scratches, particles, thickness variation |
| Lithography | focus, exposure, CD, overlay, resist thickness | pattern fidelity affects device dimensions |
| Implant/doping | dose, energy, angle, anneal conditions | electrical properties depend on dopant behavior |
| Metrology | thickness, CD, overlay, defect count, electrical test | measurements detect process state or final quality |
| Tool health | chamber matching, maintenance age, sensor status | tool drift can create hidden process regimes |

Use this table to guide interpretation, not to assign exact physical names to anonymized features.

---

## 14. Original Benchmark Notes

The original dataset notes describe baseline results using:

- standardization,
- removal of constant features,
- feature selection,
- top 40 highest-ranked features,
- simple kernel ridge classifier,
- 10-fold cross-validation,
- balanced error rate.

Feature-selection methods mentioned in the original notes include:

- signal-to-noise,
- t-test,
- Relief,
- Pearson,
- F-test,
- Gram-Schmidt.

### What to learn from this

You do not need to reproduce the old benchmark exactly, but you should preserve the idea:

> Compare feature-selection methods using balanced metrics and cross-validation.

### Modern practical version

Use:

- signal-to-noise ranking,
- t-test ranking,
- F-test ranking,
- Pearson correlation,
- mutual information,
- tree-based importance,
- permutation importance,
- top 40 / top 20 / top 10 feature subsets,
- stratified cross-validation,
- balanced accuracy and BER.

---

## 15. Project Design Decisions

### Decision 1 — Use failure as positive class

Set:

```text
positive class = fail = 1
negative class = pass = -1
```

### Decision 2 — Use balanced metrics

Do not use accuracy as the main metric.

Main metrics:

- balanced accuracy,
- BER,
- failure recall,
- failure precision,
- F1-score,
- false-negative rate.

### Decision 3 — Compare feature sets

Compare:

- all cleaned features,
- top 40 selected features,
- top 20 selected features,
- top 10 selected features.

### Decision 4 — Use cross-validation

Use stratified cross-validation because failures are rare.

Prefer 10-fold cross-validation if practical.

### Decision 5 — Avoid leakage

Feature selection and imputation should happen inside the training fold when doing cross-validation.

### Decision 6 — Interpret carefully

Features are anonymized. Interpret them as candidate signals, not physical root causes.

### Decision 7 — Treat TDA as a later extension

For Project 1, use PCA and possibly Mapper-style thinking as preparation. Save deeper persistent homology/TDA for Project 2 or a later extension.

---

## 16. Engineering Questions to Ask Throughout the Project

Use these questions in notebooks and report sections.

### Dataset questions

1. What does one row represent?
2. What does one feature represent?
3. What does the label represent?
4. What does the timestamp allow us to test?
5. Are features independent sensors or derived measurements?
6. Are there obvious data-quality issues?

### Missingness questions

1. Which features are missing most often?
2. Which rows are missing many measurements?
3. Is missingness associated with failure?
4. Could missingness represent process route or tool availability?
5. Should missingness indicators be used?

### Feature behavior questions

1. Which features have almost no variation?
2. Which features have extreme outliers?
3. Which features are strongly skewed?
4. Which features differ between pass and fail?
5. Which features are redundant or correlated?

### Feature-selection questions

1. Which features are consistently ranked high?
2. Do different methods agree?
3. Are important features missing-heavy?
4. Are important features correlated with each other?
5. Can selected features match all-feature performance?

### Model evaluation questions

1. Does the model detect failures?
2. How many actual failures are missed?
3. How many good examples are incorrectly flagged?
4. Does threshold adjustment improve failure recall?
5. Is performance stable across folds?
6. Does top 40 perform better than all features?

### Engineering interpretation questions

1. Which signals would I ask a process engineer to review?
2. What additional metadata would I request?
3. Could selected signals reflect tool, route, metrology, or process state?
4. Are failures concentrated in a process region?
5. Are errors associated with missingness or outliers?

---

## 17. Data Cleaning Notes

### Do not do this

Do not write:

> I removed missing values because missing values are bad.

Better:

> I analyzed missingness first because missing values in manufacturing can reflect route differences, skipped measurements, unavailable sensors, or data-collection behavior. I then removed features with extreme missingness and imputed remaining numerical values using a strategy applied inside the training folds.

### Cleaning checklist

- [ ] Load raw data.
- [ ] Preserve raw files.
- [ ] Assign column names.
- [ ] Load labels and timestamps.
- [ ] Confirm row alignment.
- [ ] Convert labels correctly.
- [ ] Count missing values per feature.
- [ ] Count missing values per row.
- [ ] Identify constant features.
- [ ] Identify near-constant features.
- [ ] Identify duplicate rows.
- [ ] Identify extreme outliers.
- [ ] Decide missingness thresholds.
- [ ] Document decisions.
- [ ] Build preprocessing pipeline.

---

## 18. Analysis Notes

### EDA should include

- class distribution,
- missingness summary,
- feature variance summary,
- feature distribution samples,
- pass/fail distribution comparisons,
- top missing features,
- top variance features,
- top pass/fail separating features,
- correlation clusters,
- PCA visualization,
- error-type visualization after modeling.

### Feature selection should include

- simple statistical ranking,
- model-based ranking,
- permutation ranking,
- stability across folds,
- overlap between methods,
- top feature tables,
- top feature distribution plots,
- selected feature model comparison.

### Modeling should include

- majority-class baseline,
- logistic regression,
- random forest,
- gradient boosting,
- optional SVM,
- optional XGBoost/LightGBM,
- all features,
- top 40,
- top 20,
- top 10,
- stratified split,
- stratified cross-validation.

---

## 19. Report Language Guide

### Use this language

- “The model identifies features associated with failure risk.”
- “These variables are candidates for engineering review.”
- “Selected features may represent useful process signals.”
- “Because features are anonymized, physical interpretation is limited.”
- “This result suggests a possible abnormal process region.”
- “Further validation would require process metadata such as tool ID, route, recipe, chamber, maintenance history, or metrology context.”

### Avoid this language

- “This feature caused the failure.”
- “This is the root cause.”
- “The model proves the process issue.”
- “This sensor is definitely bad.”
- “The model can replace process engineers.”
- “The dataset tells us the exact failing tool.”

---

## 20. Documentation Notes

Every notebook should start with:

1. What question this notebook answers.
2. Why the question matters to process/yield engineering.
3. What inputs are used.
4. What outputs are produced.
5. What decisions are made.
6. What limitations exist.

Every notebook should end with:

1. Key findings.
2. Engineering interpretation.
3. Risks/limitations.
4. Next notebook link.
5. Questions for process/yield engineers.

---

## 21. Final Design Summary

The project should be designed around this sequence:

```text
manufacturing context
→ dataset understanding
→ missingness analysis
→ imbalance analysis
→ EDA
→ feature selection
→ baseline modeling
→ balanced evaluation
→ error analysis
→ process interpretation
→ final report
```

The main value is the translation layer:

```text
statistics / ML result
→ process signal behavior
→ yield risk interpretation
→ engineering follow-up question
```
