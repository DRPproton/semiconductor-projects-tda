# Document 1: Project Overview and General Plan

# Project 1: Semiconductor Yield Prediction with SECOM

## 1. Project Title

**Semiconductor Yield Prediction and Process-Regime Analysis Using SECOM Data**

---

## 2. Project Purpose

The purpose of this project is to build a realistic semiconductor manufacturing analytics portfolio project using public data.

This project will simulate the kind of analytics work that could be useful in a semiconductor yield, process, manufacturing, quality, or production engineering environment.

The main objective is to analyze semiconductor process data and predict whether a production example is likely to pass or fail final yield testing.

This project uses the **SECOM dataset**, a public semiconductor manufacturing dataset with many anonymized sensor or process measurements.

The project is designed to connect your background in:

* data analytics,
* machine learning,
* statistics,
* production experience,
* previous process/yield technician experience,
* semiconductor manufacturing,
* future topological data analysis.

The goal is not only to build a machine learning model. The goal is to understand how manufacturing data behaves and how analytics can support yield and process improvement.

---

## 3. Main Business Problem

In semiconductor manufacturing, many process steps happen before final testing. If a unit fails at the end of the process, the company may have already spent significant time, labor, materials, equipment usage, and inspection resources.

The business problem is:

> Can we use process and sensor measurements to identify units that are more likely to fail?

A yield or process team may want to know:

* Which production examples are at higher risk?
* Which process measurements are associated with failure?
* Are failures concentrated in certain process regimes?
* Can we detect abnormal behavior earlier?
* Can we reduce scrap, rework, or yield loss?
* Can analytics help engineers prioritize investigation?

This project does **not** prove root cause. It identifies patterns that may support engineering investigation.

---

## 4. Main Machine Learning Problem

This is a **binary classification problem**.

The model will use many process/sensor features to predict whether each example belongs to one of two classes:

* pass,
* fail.

The failure class is the most important class because failures are usually less common but more important from a manufacturing-risk perspective.

The machine learning question is:

> Can a model use process measurements to predict pass/fail outcomes better than a simple baseline?

The semiconductor question is:

> Can process data reveal signatures associated with yield risk?

---

## 5. Dataset

The project uses the **SECOM dataset**.

The dataset contains semiconductor manufacturing process data with many anonymized numerical features and a pass/fail target label.

Because the feature names are anonymized, the project cannot say exactly which physical sensor or process variable caused the failure. Instead, the project will focus on the correct analytics workflow:

* data cleaning,
* missing-value handling,
* class-imbalance analysis,
* exploratory data analysis,
* dimensionality reduction,
* machine learning,
* model evaluation,
* feature importance,
* process-regime interpretation,
* professional communication.

---

## 6. Career Relevance

This project is directly relevant to your goal of moving from production back toward a more technical semiconductor role.

It can support future conversations for roles such as:

* Yield Analyst,
* Yield Engineering Technician,
* Process Engineering Technician,
* Manufacturing Data Analyst,
* Quality Analyst,
* Process Control Analyst,
* Failure Analysis Support,
* Manufacturing AI/ML Analyst,
* Entry-level Yield Engineer path,
* Entry-level Process Engineer path.

The professional story behind the project is:

> I understand production, process/yield context, and data analytics. I can take messy semiconductor manufacturing data, clean it, model it, interpret it, and communicate useful insights for yield or process improvement.

---

## 7. Project Goals

The main goals are:

1. Understand semiconductor manufacturing data from an analytics perspective.
2. Clean a high-dimensional process dataset.
3. Handle missing values carefully.
4. Analyze class imbalance between pass and fail outcomes.
5. Build baseline machine learning models.
6. Evaluate models using manufacturing-relevant metrics.
7. Identify features associated with failure risk.
8. Explore whether the data contains hidden process regimes.
9. Communicate findings in a way that would make sense to yield or process teams.
10. Prepare the project for later TDA extension.

---

## 8. Final Deliverables

By the end of the project, you should have:

### 1. Project README

A professional GitHub README explaining:

* the problem,
* the dataset,
* the methods,
* the results,
* the limitations,
* the business relevance,
* the next steps.

### 2. Cleaned Dataset Summary

A section explaining:

* original dataset shape,
* number of rows,
* number of features,
* target distribution,
* missing-value issues,
* variables removed,
* variables kept,
* cleaning decisions.

### 3. Exploratory Data Analysis Report

A report showing:

* pass/fail distribution,
* missing-value patterns,
* feature distributions,
* outliers,
* correlations,
* PCA visualizations,
* possible process regimes.

### 4. Baseline Model Comparison

A comparison of models such as:

* majority-class baseline,
* logistic regression,
* random forest,
* gradient boosting,
* optional SGD classifier,
* optional support vector machine.

### 5. Imbalanced Classification Evaluation

A section comparing models using:

* recall,
* precision,
* F1-score,
* balanced accuracy,
* confusion matrix,
* false-negative rate,
* precision-recall curve.

### 6. Feature Importance and Process Insight Summary

A section explaining:

* which anonymized features are most associated with failure,
* how those features differ between pass and fail groups,
* what an engineer might investigate next,
* why the results should not be interpreted as proof of causation.

### 7. Optional Dashboard

A simple visual dashboard showing:

* failure rate,
* key feature distributions,
* model results,
* confusion matrix,
* feature importance,
* PCA/process-regime view.

---

## 9. Recommended Project Duration

A realistic timeline is **3 to 5 weeks**.

Recommended schedule:

* **Week 1:** Dataset understanding, cleaning, missing values.
* **Week 2:** Exploratory analysis, PCA, initial modeling.
* **Week 3:** Model evaluation, class imbalance, feature importance.
* **Week 4:** Process interpretation, error analysis, final report.
* **Week 5:** Optional dashboard and optional TDA preparation.

A strong first version can be completed in about **20 to 30 focused hours**.

---

## 10. Final Portfolio Message

The final message of this project should be:

> I can apply data analytics and machine learning to semiconductor manufacturing data. I understand messy process data, class imbalance, yield risk, process-regime analysis, and the importance of communicating results carefully to engineering teams.

This project should become the first piece of a larger semiconductor analytics portfolio.
