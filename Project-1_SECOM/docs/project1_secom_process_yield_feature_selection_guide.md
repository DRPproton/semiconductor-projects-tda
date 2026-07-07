**Project 1 Execution Guide**

*SECOM Semiconductor Yield Prediction and Feature Selection through a Process/Yield Engineer Lens*

Updated for the 8-week pre-certificate plan - Version 1.0

**Main constraint: use public data only; do not include Microchip confidential data.**

# Purpose of This Document

This document recreates and upgrades the original Project 1 plan. The old plan was already strong, but the new constraint is sharper: this project is not a generic machine learning portfolio project. It is a semiconductor manufacturing analytics project designed to help you think like a process or yield engineer before the University of Arizona semiconductor processing certificate begins.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Project identity</strong></p>
<p>A process-signal investigation using SECOM. Prediction is useful, but the main portfolio value is feature relevance, failure-risk screening, missingness interpretation, and process-engineering communication.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# What Changed from the Original Project 1 Documents

| **Old emphasis**                         | **Updated emphasis**                                                                                                                               |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Build a classifier to predict pass/fail. | Identify a small set of useful process/sensor signals and explain how they could support yield-excursion investigation.                            |
| EDA as normal data science.              | EDA as process-signal inspection: missingness, drift-like behavior, abnormal regions, stable/noisy sensors, and pass/fail signatures.              |
| Feature selection as a modeling step.    | Feature selection as the central engineering question because the dataset itself is about relevant signal discovery.                               |
| TDA as a possible early technique.       | TDA is optional and later. Mapper/process-regime discovery is the best first TDA extension for SECOM.                                              |
| Generic ML metrics.                      | Manufacturing-relevant metrics: failure recall, false-negative rate, balanced accuracy, balanced error rate, PR curve, and stability across folds. |
| Learn Python/ML while doing the project. | Do not spend time learning Python/ML. You already know that. Spend time on semiconductor interpretation and communication.                         |

# Certificate-Aware Boundary

The certificate will formally teach semiconductor processing. Your pre-work should prepare the foundations and give you a portfolio artifact. Do not try to self-teach the entire certificate. Use this project to connect data to process questions, and use Khan Academy only for missing foundational chemistry/physics concepts.

| **Certificate topic**                              | **How this project prepares you without duplicating it**                                                                                                                      |
|----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Silicon and semiconductor materials                | Treat SECOM features as anonymized process/sensor measurements connected to material and electrical outcomes.                                                                 |
| Photolithography, etch, deposition, oxidation, CMP | Build a process-variable mindset: input, tool, recipe, metrology, output, risk. Do not attempt detailed unit-process modeling from SECOM because the features are anonymized. |
| Process integration and characterization           | Practice asking what missing tool, route, lot, chamber, recipe, and metrology context you would request.                                                                      |
| Reliability and failure analysis                   | Connect false negatives and abnormal feature regions to engineering-screening risk.                                                                                           |
| Processing instrumentation and tools               | Treat feature groups as potential tool/sensor signal families and identify which signals are stable, noisy, missing, or associated with failure.                              |

# Project Summary

| **Item**                 | **Project decision**                                                                                                                                                                                            |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Project title            | Semiconductor Yield Prediction and Feature Selection with SECOM                                                                                                                                                 |
| Dataset                  | SECOM public semiconductor manufacturing dataset from UCI Machine Learning Repository.                                                                                                                          |
| Dataset shape            | 1,567 examples and 591 real-valued features.                                                                                                                                                                    |
| Label meaning            | -1 = pass; 1 = fail. Positive class is fail.                                                                                                                                                                    |
| Failure count            | 104 failures, about 6.6% of examples.                                                                                                                                                                           |
| Main problem             | Can a smaller group of process/sensor features predict yield failure and support process-engineering investigation?                                                                                             |
| Main portfolio story     | I analyzed high-dimensional semiconductor process data, selected relevant signals, evaluated rare-failure prediction using balanced metrics, and communicated findings as engineering investigation candidates. |
| Confidentiality boundary | Use only public SECOM data. Do not use Microchip internal variables, examples, charts, tool names, recipe names, or production context.                                                                         |

# Learning Outcomes

- Explain how semiconductor process data differs from normal business data.

- Explain why process monitoring produces many signals and why many are noisy or irrelevant.

- Inspect missing values as possible process/data-collection information, not only as cleaning problems.

- Explain why rare failures make accuracy misleading.

- Use balanced accuracy and balanced error rate for imbalanced manufacturing classification.

- Compare all features versus top 40, top 20, and top 10 selected features.

- Translate important anonymized features into careful engineering questions rather than root-cause claims.

- Use PCA and optional Mapper to ask whether failures occur in process regimes or abnormal regions.

- Write a final report that a yield engineer, process engineer, or manufacturing manager could understand quickly.

# Eight-Week Integration Plan

Project 1 runs mainly during Weeks 1-6 of the prep plan. Weeks 7-8 are for Project 2 and final synthesis. The schedule below assumes your two long weekly blocks plus short evening review sessions.

| **Prep week** | **Science/Khan checkpoint**                                     | **Project 1 milestone**                                                                   | **Engineering output**                                                 |
|---------------|-----------------------------------------------------------------|-------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Week 1        | Atoms, electrons, charge, conductors/insulators.                | Load SECOM; inspect shape, labels, timestamps, missingness, and class balance.            | Notebook section: SECOM as a manufacturing process dataset.            |
| Week 2        | Periodicity, bonding, current, resistance, Ohm law.             | Profile missingness, constant features, and feature availability.                         | Missingness report: what could missingness mean in a fab data context? |
| Week 3        | Moles, molarity, dilution, basic circuit laws.                  | Create signal behavior taxonomy: stable, sparse, noisy, outlier-heavy, pass/fail-shifted. | Process signal inventory table.                                        |
| Week 4        | pH, acids/bases, electric fields, surface preparation.          | Compare pass/fail distributions and identify candidate signatures.                        | Candidate process-signature memo.                                      |
| Week 5        | Redox, oxidation, doping, PN junction intuition.                | Run feature-selection methods and compare top 40/20/10 feature sets.                      | Feature relevance benchmark table.                                     |
| Week 6        | Kinetics, equilibrium, heat, pressure, CMP/thin-film intuition. | Build balanced evaluation, error analysis, and final SECOM memo.                          | Project 1 report draft and GitHub README.                              |
| Week 7        | Gases, plasma intuition, optics/lithography.                    | Light cleanup only. Do not expand Project 1 endlessly.                                    | Move effort to Project 2.                                              |
| Week 8        | Integration and certificate readiness.                          | Finalize Project 1 README and cross-link to Project 2.                                    | Portfolio-ready Project 1 package.                                     |

# Recommended Project Folder

project-1-secom-yield-feature-selection/

data/raw/ \# original SECOM files only

data/processed/ \# cleaned matrices, split files, feature sets

notebooks/ \# 01_data_context.ipynb, 02_missingness.ipynb, etc.

reports/ \# final report, engineering memo, README assets

figures/ \# charts saved from notebooks

src/ \# reusable project utilities

references/ \# source notes and citations

README.md

# Phase-by-Phase Execution Plan

## Phase 0: Semiconductor Context Setup

**Goal:** Understand the semiconductor meaning before touching the data.

**Tasks:**

- Define yield, pass/fail yield testing, process variation, drift, excursion, process monitoring, false positive, and false negative.

- Write why false negatives can be dangerous in a yield-screening context.

- Write why engineers collect many process signals and why only some are useful.

- Write a short business-context section that uses manufacturing language.

**Expected output:** Business Context section.

**Key question:** If a yield or process engineer used this analysis, what decision would it support?

**Stop condition:** Do not model until you can explain the manufacturing decision.

## Phase 1: Dataset Acquisition and Project Setup

**Goal:** Download and organize the public data professionally.

**Tasks:**

- Download SECOM from UCI using either the browser or ucimlrepo.

- Save raw data without modification.

- Create raw, processed, notebooks, figures, reports, and src folders.

- Document the source, license, files, row/column counts, and label meaning.

- Confirm in the README that no Microchip confidential data is included.

**Expected output:** Clean project folder and README draft.

**Key question:** Could another person open the repo and understand the dataset?

**Stop condition:** Raw data is stored separately and never overwritten.

## Phase 2: Problem Framing

**Goal:** Define the business, ML, and semiconductor versions of the problem.

**Tasks:**

- Target variable: fail/pass yield label.

- Positive class: fail = 1. Negative class: pass = -1.

- Define the business problem in plain English.

- Define the modeling problem in technical language.

- Define the process/yield interpretation: relevant signal discovery and rare-failure screening.

- Select evaluation metrics before building models.

**Expected output:** Problem Definition section.

**Key question:** Are we only predicting failure, or are we identifying useful process signals?

**Stop condition:** The problem statement includes both prediction and feature relevance.

## Phase 3: Initial Data Inspection

**Goal:** Understand structure and data-quality problems.

**Tasks:**

- Count rows, columns, pass examples, fail examples, and failure percentage.

- Confirm 1,567 examples, 591 features, and 104 failures.

- Count missing values per feature and per row.

- Identify constant and near-constant features.

- Check duplicate rows and feature types.

- Inspect the timestamp field and decide how to use it later.

**Expected output:** Data Overview section.

**Key question:** What are the biggest data-quality problems before modeling?

**Stop condition:** You can describe the dataset without reading code.

## Phase 4: Missingness as Process Information

**Goal:** Handle missing values without destroying possible engineering signal.

**Tasks:**

- Calculate missing percentage per feature.

- Flag very high missingness features.

- Compare missingness rates between pass and fail groups.

- Decide which features to drop and which to impute.

- Use median imputation inside a pipeline to prevent leakage.

- Add missing-value indicators only when missingness appears informative.

- Document every cleaning decision.

**Expected output:** Data Cleaning Strategy and Missingness Report.

**Key question:** Is missingness random noise, process route information, or data-collection behavior?

**Stop condition:** Cleaning decisions are documented and reproducible.

## Phase 5: Target Imbalance and Manufacturing Risk

**Goal:** Evaluate the rare-failure problem correctly.

**Tasks:**

- Calculate pass and fail percentages.

- Create class-distribution chart.

- Calculate majority-class baseline accuracy and explain why it is misleading.

- Define false negative and false positive from a manufacturing viewpoint.

- Choose recall, precision, F1, balanced accuracy, BER, confusion matrix, and PR curve.

**Expected output:** Class Imbalance section.

**Key question:** Can the analysis detect failures, or does it hide behind the majority class?

**Stop condition:** Accuracy is not used as the main success metric.

## Phase 6: Process-Oriented EDA

**Goal:** Explore features as process/sensor signals.

**Tasks:**

- Profile each feature: mean, median, std, min, max, missing rate, skew, outliers.

- Compare selected feature distributions for pass versus fail examples.

- Identify low-variance features and high-noise features.

- Identify features where failures appear in extreme ranges.

- Group variables by behavior instead of only ranking by model importance.

**Expected output:** Exploratory Data Analysis section.

**Key question:** Which variables behave differently between passing and failing examples?

**Stop condition:** You have a process-signal taxonomy table.

## Phase 7: Feature Selection Benchmark

**Goal:** Make feature selection the project center.

**Tasks:**

- Rank features using signal-to-noise, t-test, F-test, Pearson correlation, model-based importance, and permutation importance.

- Select top 40, top 20, and top 10 features.

- Compare overlap across ranking methods.

- Study distribution and missingness for top-ranked features.

- Create a table of features consistently important across methods.

**Expected output:** Feature Selection Benchmark section.

**Key question:** Can a small set of features perform almost as well as all features and be easier to discuss?

**Stop condition:** Top feature lists are reproducible and compared across methods.

## Phase 8: Dimensionality Reduction and Process Structure

**Goal:** Ask whether the data contains abnormal regions or process regimes.

**Tasks:**

- Scale cleaned data.

- Apply PCA to all cleaned features and selected feature sets.

- Color plots by pass/fail label, prediction, and error type.

- Look for clusters, outliers, and abnormal regions.

- Explain PCA limitations and why nonlinear tools may help later.

**Expected output:** Dimensionality Reduction and Process Structure section.

**Key question:** Are failures scattered randomly or concentrated in regions?

**Stop condition:** You can explain what PCA shows and what it cannot show.

## Phase 9: Baseline Modeling

**Goal:** Build only enough models to support the engineering analysis.

**Tasks:**

- Use stratified train/test split.

- Build majority-class baseline.

- Train logistic regression, random forest, gradient boosting, and optional SVM/SGD.

- Train each model on all features, top 40, top 20, and top 10 feature sets.

- Save results in a comparison table.

**Expected output:** Baseline Model Results section.

**Key question:** Which model and feature set best detects failures without becoming impossible to explain?

**Stop condition:** Models are useful supporting evidence, not the project story by themselves.

## Phase 10: Cross-Validation and Balanced Error Rate

**Goal:** Evaluate consistently despite rare failures.

**Tasks:**

- Use stratified cross-validation, preferably 10 folds if practical.

- Calculate balanced accuracy and balanced error rate.

- Report mean and variation across folds.

- Run feature selection inside cross-validation when benchmarking to prevent leakage.

- Compare performance stability across feature sets.

**Expected output:** Cross-Validation and BER section.

**Key question:** Does performance hold across folds or depend on a lucky split?

**Stop condition:** BER is computed and explained in the report.

## Phase 11: Manufacturing-Focused Evaluation

**Goal:** Select a model based on engineering risk.

**Tasks:**

- Create confusion matrices.

- Compare failure-class recall and false-negative rate.

- Compare failure precision and false-positive burden.

- Inspect precision-recall curves.

- Evaluate threshold adjustments for screening use cases.

**Expected output:** Model Evaluation section.

**Key question:** Would this be useful as a yield-screening tool?

**Stop condition:** You can explain the tradeoff between catching more failures and flagging more good examples.

## Phase 12: Feature Importance and Process Interpretation

**Goal:** Translate important features into engineering questions, not causal claims.

**Tasks:**

- Extract feature importance from tree models.

- Run permutation importance on final candidates.

- Compare important features across methods and models.

- Check correlation among important features.

- Write cautious interpretations using association language.

**Expected output:** Feature Importance and Process Insight section.

**Key question:** Which variables would I ask a process engineer to investigate first?

**Stop condition:** No causal/root-cause claims are made from anonymized observational data.

## Phase 13: Error Analysis

**Goal:** Study what the model misunderstands.

**Tasks:**

- Identify false positives and false negatives.

- Compare error examples against correctly classified examples.

- Check whether errors have more missingness.

- Plot errors in PCA space.

- Write possible manufacturing explanations without overclaiming.

**Expected output:** Error Analysis section.

**Key question:** What kinds of cases does the model misunderstand?

**Stop condition:** False negatives receive special attention.

## Phase 14: Optional Time-Aware Validation

**Goal:** Test sensitivity to time ordering if the timestamp is usable.

**Tasks:**

- Parse and sort by timestamp.

- Train on earlier examples and test on later examples.

- Compare time-aware performance with random cross-validation.

- Discuss drift risk in real deployment.

**Expected output:** Optional Time-Aware Validation section.

**Key question:** Would the model still work if process behavior changes over time?

**Stop condition:** Time-aware validation is included only if timestamps are reliable enough.

## Phase 15: Optional TDA/Mapper Extension

**Goal:** Use topology only after the classical process analysis is strong.

**Tasks:**

- Do not begin with persistent homology on individual tabular rows.

- Use Mapper to visualize process-regime structure in selected feature space.

- Compare pass/fail density across Mapper nodes.

- Compare Mapper with PCA and clustering.

- Frame TDA as nonlinear process-state discovery, not magic feature engineering.

**Expected output:** Optional TDA Extension section.

**Key question:** Does topology reveal abnormal process neighborhoods that PCA misses?

**Stop condition:** Only add TDA if the baseline report is already complete.

## Phase 16: Final Report

**Goal:** Create a professional engineering report.

**Tasks:**

- Write executive summary, business context, data overview, data quality, class imbalance, EDA, feature selection, modeling, BER, evaluation, feature insight, error analysis, limitations, recommendations, and next steps.

- Keep the report readable in five minutes.

- Include charts that support the story, not every chart generated.

**Expected output:** Final report in Markdown, PDF, or notebook form.

**Key question:** Can someone understand the value of the project in five minutes?

**Stop condition:** Report has an executive summary and explicit limitations.

## Phase 17: Portfolio README

**Goal:** Make the project GitHub-ready.

**Tasks:**

- Add project title, short description, dataset, label explanation, feature-selection story, methods, main results, charts, lessons, limitations, and how to run.

- Use careful semiconductor language.

- Link to Project 2 as the wafer-map/TDA companion project.

**Expected output:** GitHub README.

**Key question:** Would this README help you explain your value to Microchip or another semiconductor employer?

**Stop condition:** README is understandable to data and manufacturing readers.

# Concepts to Spend the Most Time Understanding

| **Concept**               | **Why it matters**                                                                                                                    |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Feature selection         | This is the center of Project 1. The goal is to identify useful signals from hundreds of noisy or irrelevant measurements.            |
| Class imbalance           | Only a small percentage of examples are failures, so normal accuracy can be misleading.                                               |
| Balanced error rate       | BER evaluates both pass and fail performance more fairly than accuracy. Lower BER is better.                                          |
| Missing values            | Missingness may indicate skipped measurements, different routes, sensor unavailability, tool logging issues, or data-system problems. |
| False negatives           | A false negative means the model missed a failure. In yield screening, this can be more concerning than a false positive.             |
| Feature importance limits | Important features are candidates for engineering review, not proof of root cause.                                                    |
| Process regimes           | Manufacturing data may contain hidden operating states, abnormal regions, or drift conditions.                                        |
| TDA preparation           | For SECOM, the best TDA extension is Mapper/process-regime discovery after strong baselines.                                          |

# Correct Language for the Final Report

| **Use this language**                               | **Avoid this language**                         |
|-----------------------------------------------------|-------------------------------------------------|
| Feature X is associated with failure risk.          | Feature X caused the failure.                   |
| This signal may indicate abnormal process behavior. | This signal proves the root cause.              |
| This feature is a candidate for engineering review. | This feature is the process problem.            |
| The model suggests a region worth investigation.    | The model identifies the exact failing tool.    |
| More process metadata is needed for validation.     | The analysis is complete without domain review. |

# Final Report Template

1.  Executive Summary

2.  Business and Manufacturing Context

3.  Dataset Description and Source

4.  Data Quality and Missingness

5.  Class Imbalance and Manufacturing Risk

6.  Exploratory Process-Signal Analysis

7.  Feature Selection Benchmark

8.  Baseline Modeling

9.  Cross-Validation and Balanced Error Rate

10. Manufacturing-Focused Evaluation

11. Feature Importance and Process Interpretation

12. Error Analysis

13. Limitations

14. Recommendations

15. Next Steps

# GitHub README Checklist

- Project title and one-paragraph summary.

- Dataset source, license, and label meaning.

- Why feature selection matters in semiconductor process monitoring.

- How the project handles missing values and class imbalance.

- Main results table with balanced metrics.

- Feature-selection comparison table.

- Key visualizations: missingness, class balance, PCA/process structure, top-feature distributions, confusion matrix.

- Careful interpretation and limitations.

- How to reproduce the analysis.

- Connection to Project 2: wafer-map spatial pattern and TDA analysis.

# Sources and Reference Directory

Use these sources as the official public reference points for the project. The hyperlinks are intentionally placed in one section so the notebooks and README can cite them cleanly.

| **Source**                                                   | **Use in this project**                                                                        | **Link**                                                                                                                                            |
|--------------------------------------------------------------|------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| UCI Machine Learning Repository - SECOM                      | Official dataset source, dataset facts, label meaning, missing-value notes, benchmark context. | [<u>Open UCI SECOM</u>](https://archive.ics.uci.edu/dataset/179/secom)                                                                              |
| University of Arizona - Semiconductor Processing Certificate | Boundary for what the certificate teaches versus what this project prepares.                   | [<u>Open certificate page</u>](https://online.arizona.edu/programs/graduate-certificate/online-graduate-certificate-semiconductor-processing-gcert) |
| Khan Academy - High School Chemistry                         | Foundation refresh for atoms, bonding, stoichiometry, acids/bases, redox, kinetics, gases.     | [<u>Open Khan chemistry</u>](https://www.khanacademy.org/science/hs-chemistry)                                                                      |
| Khan Academy - Electrical Engineering                        | Foundation refresh for current, voltage, circuits, electrostatics, and semiconductor devices.  | [<u>Open Khan electrical engineering</u>](https://www.khanacademy.org/science/electrical-engineering)                                               |
| Micron Intro to Fabrication                                  | Free fab-process context bridge for nonconfidential semiconductor vocabulary.                  | [<u>Open Micron Educator Hub course</u>](https://www.micron.com/educatorhub/courses/intro-to-fabrication)                                           |

End of Project 1 guide.
