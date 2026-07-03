# Document 4: SECOM Dataset Notes and Project Design Changes

# Dataset-Specific Notes for Project 1

## 1. Why This Document Exists

This document captures the important information from the SECOM dataset description and explains how that information changes the project design.

The dataset description shows that SECOM is not just a generic classification dataset. It is specifically about semiconductor process monitoring, feature selection, and yield improvement.

Therefore, Project 1 should be framed around:

> Semiconductor yield prediction and feature selection.

---

## 2. Important Dataset Information

The SECOM dataset description says that a complex modern semiconductor manufacturing process is monitored through many signals and variables collected from sensors or process measurement points.

This means the dataset represents a realistic manufacturing situation where many signals are collected, but not all signals are equally useful.

The measured signals may contain:

* useful process information,
* irrelevant information,
* noise.

Useful information may be buried inside noisy or irrelevant signals.

This is exactly why feature selection matters.

---

## 3. Why Feature Selection Matters

The dataset description says engineers usually have a much larger number of signals than are actually required.

If each signal is considered a feature, then feature selection can be used to identify the most relevant signals.

The purpose of feature selection is to rank features according to their impact on yield or their usefulness for predicting failure.

In a real engineering environment, process engineers could use selected signals to investigate possible factors contributing to downstream yield excursions.

This can help:

* increase process throughput,
* reduce time to learning,
* reduce per-unit production cost,
* focus engineering attention on the most relevant measurements,
* reduce monitoring complexity.

---

## 4. Updated Project Interpretation

Before reading the dataset description, the project could be interpreted as:

> Build a model to predict pass or fail.

After reading the dataset description, the better interpretation is:

> Identify the most relevant process/sensor signals for predicting yield failure and use them to build an interpretable failure-prediction workflow.

This changes the project emphasis.

Prediction is still important, but feature relevance is equally important.

---

## 5. Dataset Structure

The dataset contains:

* **1,567 examples**
* **591 features**
* **104 failures**

Each example represents:

* one production entity,
* many associated process or sensor measurements,
* a pass/fail yield label,
* an associated timestamp.

The label definition is:

* **-1 = pass**
* **1 = fail**

This means:

* positive class should be fail,
* negative class should be pass.

---

## 6. Class Imbalance

The dataset contains 104 failures out of 1,567 examples.

That means the failure rate is approximately 6.6%.

The pass rate is approximately 93.4%.

This creates a major class-imbalance problem.

A model that predicts every example as pass would get about 93.4% accuracy, but it would detect zero failures.

Therefore, ordinary accuracy should not be the main metric.

---

## 7. Correct Evaluation Metrics

The original dataset description uses **Balanced Error Rate**, also called BER.

This project should include BER because it matches the original benchmark and is useful for imbalanced datasets.

Important metrics for this project:

* balanced error rate,
* balanced accuracy,
* failure-class recall,
* failure-class precision,
* F1-score,
* confusion matrix,
* false-negative rate,
* precision-recall curve.

Balanced accuracy is the average of true positive rate and true negative rate.

Balanced Error Rate is:

> 1 - balanced accuracy

Lower BER is better.

---

## 8. Original Baseline Results

The dataset description includes baseline results using feature selection methods.

The original benchmark:

* standardized the data,
* removed constant features,
* selected the 40 highest-ranked features,
* used a simple kernel ridge classifier,
* used 10-fold cross-validation,
* reported Balanced Error Rate.

The listed feature selection methods included:

* signal-to-noise,
* t-test,
* Relief,
* Pearson,
* F-test,
* Gram-Schmidt.

The strongest baseline listed was around the low-to-mid 30% BER range, depending on the feature selection method.

This means the project should not focus only on a single model score. It should compare feature-selection strategies and evaluate performance using balanced metrics.

---

## 9. Project Design Changes

Based on the dataset information, the project should change in the following ways.

### Change 1: Update the Title

Old title:

> Semiconductor Yield Prediction with SECOM

New title:

> Semiconductor Yield Prediction and Feature Selection with SECOM

---

### Change 2: Add Feature Selection as a Main Pillar

The project should have three main pillars:

1. Predict pass/fail yield outcome.
2. Rank features by relevance.
3. Interpret selected features as candidates for process/yield investigation.

---

### Change 3: Use Failure as the Positive Class

The correct class setup is:

* positive class = fail = 1,
* negative class = pass = -1.

This matters for recall, precision, confusion matrix, and false-negative analysis.

---

### Change 4: Use Balanced Metrics

Accuracy should not be the main metric.

The project should report:

* balanced error rate,
* balanced accuracy,
* failure recall,
* failure precision,
* F1-score,
* confusion matrix.

---

### Change 5: Compare Feature Sets

The project should compare models using:

* all cleaned features,
* top 40 selected features,
* top 20 selected features,
* top 10 selected features.

This connects directly to the original benchmark, which used top 40 selected features.

---

### Change 6: Use Cross-Validation

The original benchmark used 10-fold cross-validation.

The project should include:

* stratified cross-validation,
* preferably 10-fold cross-validation if practical,
* mean and variation of results across folds.

This is important because the failure class is small.

---

### Change 7: Be Careful with Causality

The dataset description mentions that causal relationships may be considered, but this project should be careful.

Because the data is anonymized and observational, the project should not claim root cause.

Use cautious language:

* “associated with failure,”
* “predictive of yield risk,”
* “candidate for process review,”
* “requires engineering validation.”

Avoid:

* “causes failure,”
* “root cause identified,”
* “proves yield excursion factor.”

---

### Change 8: Treat TDA as a Later Extension

This dataset is tabular and high-dimensional. Each row is one production entity.

That makes it less natural for basic persistent homology on individual examples.

The better TDA extension is:

* Mapper for process-regime discovery,
* topology of high-dimensional process clouds,
* comparison of pass and fail regions,
* nonlinear process-structure exploration.

TDA should come after:

1. cleaning,
2. EDA,
3. baseline modeling,
4. feature selection,
5. balanced evaluation.

---

## 10. Updated Project Question

The updated main project question is:

> Can we identify a small group of process or sensor features that help predict yield failure and may support process-engineering investigation?

Secondary questions:

* Can selected features perform as well as all features?
* Which features appear most associated with failure?
* Does feature selection improve interpretability?
* Are failures concentrated in specific process regions?
* How well does the model detect rare failure examples?
* What would process engineers investigate next?

---

## 11. Updated Final Project Message

The final message should be:

> This project demonstrates an applied semiconductor analytics workflow for identifying relevant process signals, predicting yield failure, evaluating imbalanced classification performance, and communicating feature relevance in a way that can support process or yield engineering investigation.

---

## 12. Why This Is Better for Your Portfolio

This updated framing is stronger because it sounds closer to real semiconductor work.

Instead of saying:

> I built a classifier.

You can say:

> I analyzed high-dimensional semiconductor process data, selected the most relevant signals, evaluated failure prediction using balanced metrics, and explained how selected features could support yield-excursion investigation.

That is much more valuable for internal mobility toward yield, process, or manufacturing analytics roles.
