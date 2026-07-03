# Document 1: Project Overview and General Plan

# Project 1: Semiconductor Yield Prediction and Feature Selection with SECOM

## 1. Project Title

**Semiconductor Yield Prediction and Feature Selection Using SECOM Manufacturing Data**

---

## 2. Project Purpose

The purpose of this project is to build a realistic semiconductor manufacturing analytics portfolio project using public data.

This project uses the **SECOM dataset**, a semiconductor manufacturing dataset containing hundreds of anonymized process or sensor measurements and a pass/fail yield label.

The project is not only about building a classifier. The main purpose is to understand how process and sensor signals can be analyzed, ranked, and used to support semiconductor yield or process-engineering investigation.

The project will focus on three main ideas:

1. Predicting pass/fail yield outcome.
2. Identifying the most relevant process or sensor features.
3. Explaining how selected features could support process/yield investigation.

This project connects directly to semiconductor work because modern fabs collect many signals from tools, sensors, process steps, and measurement points. Not all of those signals are useful. Some contain real process information, some are irrelevant, and some are noise. The goal is to find which signals are most useful for identifying yield risk.

---

## 3. Main Business Problem

Modern semiconductor manufacturing processes are monitored continuously through many signals and process measurements. However, engineers often collect many more signals than they actually need for a specific monitoring or yield-improvement problem.

The business problem is:

> Can we identify a small group of process or sensor signals that help predict yield failure and support process-engineering investigation?

A process or yield engineering team may want to know:

* Which measurements are most associated with yield failure?
* Can a smaller group of signals predict failure reasonably well?
* Are failures related to specific process behavior patterns?
* Can feature selection reduce the number of signals engineers need to monitor?
* Can this reduce time to learning after a yield excursion?
* Can analytics help improve throughput and reduce production cost?

This project does **not** prove root cause. It identifies features that may be useful for further engineering review.

---

## 4. Dataset Summary

The SECOM dataset represents a semiconductor manufacturing process under surveillance using process and sensor measurements.

Each row represents:

* one production entity,
* associated measured process/sensor features,
* a date/time stamp,
* a pass/fail yield label.

The label values are:

* **-1 = pass**
* **1 = fail**

Dataset size:

* **1,567 examples**
* **591 features**
* **104 failure examples**

This means only about **6.6%** of examples are failures. The dataset is highly imbalanced.

Because the features are anonymized, we cannot identify the exact physical meaning of each variable. We can still rank features by predictive relevance and explain how this type of workflow would help process engineers in a real fab.

---

## 5. Main Machine Learning Problem

This is a **binary classification problem**.

The model uses many process/sensor features to predict whether a production entity will pass or fail.

The positive class should be defined as:

> **Positive class = fail = 1**

The negative class should be defined as:

> **Negative class = pass = -1**

The main machine learning question is:

> Can selected process/sensor features predict pass/fail yield outcome better than a simple baseline?

The main semiconductor analytics question is:

> Which signals appear most relevant to downstream yield failure?

---

## 6. Why Feature Selection Is Central

The SECOM dataset was created around the idea that semiconductor engineers may collect many signals, but only a smaller number may be useful for a specific monitoring or yield problem.

Feature selection is important because it can help:

* reduce noise,
* remove irrelevant measurements,
* identify high-value process signals,
* improve model interpretability,
* support process-engineering investigation,
* reduce time to learning after yield excursions,
* reduce monitoring complexity,
* improve production decision-making.

The original dataset benchmark used feature selection methods that selected the **top 40 features**. For that reason, this project should compare models trained on:

* all cleaned features,
* top 40 selected features,
* top 20 selected features,
* top 10 selected features.

The goal is to understand whether a smaller feature set can perform close to, equal to, or better than the full feature set.

---

## 7. Why Accuracy Is Not Enough

The dataset has 104 failures out of 1,567 examples.

That means approximately:

* **93.4% pass**
* **6.6% fail**

A model that predicts every example as “pass” would get about 93.4% accuracy, but it would detect zero failures.

For this reason, regular accuracy is not a good primary metric.

The project should focus on metrics such as:

* failure-class recall,
* failure-class precision,
* F1-score,
* balanced accuracy,
* balanced error rate,
* confusion matrix,
* false-negative rate,
* precision-recall curve.

The original dataset description uses **Balanced Error Rate**, so this project should include it as one of the main evaluation metrics.

---

## 8. Career Relevance

This project is directly relevant to your goal of moving from production toward a more technical semiconductor role.

It can support conversations for roles such as:

* Yield Analyst,
* Yield Engineering Technician,
* Process Engineering Technician,
* Manufacturing Data Analyst,
* Quality Analyst,
* Process Control Analyst,
* Failure Analysis Support,
* Manufacturing AI/ML Analyst,
* Yield Engineer path,
* Process Engineer path.

The professional story behind the project is:

> I understand production, process/yield context, and data analytics. I can take messy semiconductor manufacturing data, clean it, identify relevant signals, build predictive models, evaluate them correctly, and communicate insights that may support yield or process improvement.

---

## 9. Main Project Goals

The main goals are:

1. Understand semiconductor manufacturing data from an analytics perspective.
2. Clean a high-dimensional process dataset.
3. Handle missing values carefully.
4. Analyze severe class imbalance.
5. Understand why ordinary accuracy is misleading.
6. Use balanced metrics such as BER and balanced accuracy.
7. Build baseline classification models.
8. Apply feature selection methods.
9. Compare all features versus selected features.
10. Rank process/sensor features by predictive relevance.
11. Interpret selected features cautiously.
12. Explore whether failures appear in specific process regions.
13. Prepare the project for later TDA extension through Mapper or process-shape analysis.

---

## 10. Final Deliverables

By the end of the project, you should have the following deliverables.

### Deliverable 1: Project README

A professional GitHub README explaining:

* the business problem,
* the dataset,
* the pass/fail label structure,
* why the dataset is imbalanced,
* why feature selection matters,
* methods used,
* model results,
* limitations,
* next steps.

### Deliverable 2: Cleaned Dataset Summary

A section explaining:

* original dataset shape,
* number of rows,
* number of features,
* number of failures,
* target distribution,
* missing-value issues,
* constant features removed,
* features retained,
* cleaning decisions.

### Deliverable 3: Exploratory Data Analysis Report

A report showing:

* pass/fail distribution,
* missing-value patterns,
* feature distributions,
* outliers,
* correlations,
* differences between pass and fail examples,
* PCA visualizations,
* possible process regimes.

### Deliverable 4: Feature Selection Report

A feature-selection section showing:

* ranking methods used,
* top selected features,
* comparison between top 40, top 20, top 10, and all features,
* consistency of selected features across methods,
* feature relevance interpretation.

### Deliverable 5: Baseline Model Comparison

A comparison of models such as:

* majority-class baseline,
* logistic regression,
* random forest,
* gradient boosting,
* optional SGD classifier,
* optional support vector machine.

### Deliverable 6: Manufacturing-Focused Evaluation

A model-evaluation section using:

* balanced error rate,
* balanced accuracy,
* failure-class recall,
* failure-class precision,
* F1-score,
* confusion matrix,
* false-negative rate,
* precision-recall curve.

### Deliverable 7: Process Insight Summary

A business-focused explanation of:

* which anonymized features appear most associated with failure,
* how selected features could help process engineers,
* what further engineering validation would be needed,
* why the model does not prove root cause.

### Deliverable 8: Optional Dashboard

A simple dashboard or visual report showing:

* failure percentage,
* missing-value summary,
* top selected features,
* model comparison,
* confusion matrix,
* feature importance,
* PCA/process-regime view.

---

## 11. Recommended Project Duration

A realistic timeline is **4 to 5 weeks**.

Recommended schedule:

* **Week 1:** Dataset understanding, cleaning, missing values, target imbalance.
* **Week 2:** EDA, feature distributions, PCA, process-structure exploration.
* **Week 3:** Feature selection and baseline modeling.
* **Week 4:** Cross-validation, balanced metrics, error analysis, feature interpretation.
* **Week 5:** Final report, README, optional dashboard, optional TDA planning.

A strong first version can be completed in about **25 to 35 focused hours**.

---

## 12. Final Portfolio Message

The final message of this project should be:

> I can apply data analytics and machine learning to semiconductor manufacturing data. I understand high-dimensional process signals, missing values, class imbalance, feature selection, yield-risk modeling, balanced evaluation metrics, and careful engineering interpretation.

This project should become the first piece of a larger semiconductor analytics portfolio.
