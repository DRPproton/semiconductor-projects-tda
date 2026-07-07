# Project 1 — Purpose and Project Summary  
## Semiconductor Yield Prediction and Feature Selection with SECOM

**Project type:** Semiconductor process/yield analytics portfolio project  
**Dataset:** SECOM — UCI Machine Learning Repository  
**Primary audience:** Process engineers, yield engineers, manufacturing analytics teams, hiring managers, and technical interviewers  
**Main goal:** Analyze high-dimensional semiconductor manufacturing process data through the lens of process/yield engineering, not as a generic machine learning classification exercise.

---

## 1. Why This Project Exists

This project exists because semiconductor manufacturing produces many process, sensor, and metrology signals, but not every signal is equally valuable. In real fabs, engineers monitor many variables because the process is complex, expensive, sensitive, and highly sequential. However, some variables contain useful process information, some are redundant, some are noisy, and some may be irrelevant for a specific yield problem.

The SECOM dataset is valuable because it represents exactly this type of problem:

> A complex semiconductor manufacturing process is monitored with many signals, and feature selection is used to identify the most relevant signals for yield prediction and yield-excursion investigation.

That means this project should **not** be framed as:

> “I trained a classifier.”

It should be framed as:

> “I analyzed high-dimensional semiconductor process data, identified candidate process signals associated with yield failure, evaluated rare-failure detection with balanced metrics, and translated the results into engineering questions that could support yield or process investigation.”

---

## 2. Why This Project Fits Your Current Goal

You are preparing for a Semiconductor Processing Graduate Certificate and want to move toward a process/yield engineering direction. This project supports that goal because it forces you to connect your existing data analytics and machine learning background to semiconductor manufacturing decisions.

The certificate will teach semiconductor processing topics such as silicon preparation, wafering, epitaxial growth, photolithography, doping, ion implantation, etching, oxidation, metallization, and device processing. The lab is expected to cover five important unit operations: thermal oxidation, lithography, deposition, plasma etching, and surface preparation through cleaning and wet etching.

This project should prepare you to think like someone who can work with those topics using data:

- What process signals are being measured?
- Which signals are stable?
- Which signals drift?
- Which signals are noisy?
- Which signals are missing often?
- Which signals are associated with failure?
- Which signals would be worth engineering review?
- Which signals may reflect process route, tool condition, metrology behavior, or sensor availability?
- Which results can be trusted, and which require domain validation?

---

## 3. The Main Project Statement

**Project title:**

> Semiconductor Yield Prediction and Feature Selection with SECOM

**Short description:**

This project analyzes the SECOM semiconductor manufacturing dataset to identify process/sensor signals associated with rare yield failures. The project emphasizes data-quality assessment, missing-value interpretation, class imbalance, feature selection, balanced error rate, process-regime exploration, and engineering communication.

**Main project question:**

> Can we identify a smaller group of process or sensor features that help predict yield failure and support process/yield engineering investigation?

**Secondary questions:**

1. How severe is the pass/fail imbalance?
2. Which features have missingness patterns that may be process-relevant?
3. Which features show different behavior between pass and fail examples?
4. Can selected feature groups perform similarly to or better than all features?
5. Which selected features appear consistently relevant across multiple ranking methods?
6. Are failures concentrated in abnormal regions of the high-dimensional process space?
7. What would a yield or process engineer investigate next?
8. What are the limitations caused by anonymized features?

---

## 4. Dataset Summary

The SECOM dataset comes from a semiconductor manufacturing process. It contains:

| Item | Value |
|---|---:|
| Examples / production entities | 1,567 |
| Process/sensor features | 591 |
| Failure examples | 104 |
| Pass label | -1 |
| Fail label | 1 |
| Feature type | Real-valued |
| Missing values | Yes |
| Task type | Classification / causal-discovery context |
| Dataset files | `secom.data`, `secom_labels.data`, `secom.names` |

The dataset is anonymized, so the features do not reveal their real process names. That is a limitation, but it also makes the project useful for learning how to reason with incomplete manufacturing context.

The correct way to treat the target is:

- **Positive class:** fail = `1`
- **Negative class:** pass = `-1`

The failure rate is approximately:

```text
104 / 1567 ≈ 6.6%
```

That means a model could predict every example as pass and achieve about 93.4% accuracy while detecting zero failures. Therefore, ordinary accuracy is not an acceptable primary metric.

---

## 5. What This Project Is

This project is a **process/yield analytics investigation**.

It includes:

1. Semiconductor manufacturing context.
2. Dataset documentation.
3. Data-quality analysis.
4. Missing-value analysis.
5. Class-imbalance analysis.
6. Exploratory data analysis.
7. Feature-selection benchmarking.
8. Baseline failure-prediction models.
9. Balanced error rate and manufacturing-focused metrics.
10. Dimensionality reduction for process-regime thinking.
11. Error analysis.
12. Feature-importance interpretation.
13. Careful communication of engineering implications.
14. Final GitHub-ready portfolio report.

---

## 6. What This Project Is Not

This project is **not**:

- a generic machine learning tutorial,
- a competition-style leaderboard project,
- a deep learning project,
- a hyperparameter-tuning exercise,
- a dashboard-first project,
- a causal root-cause analysis project,
- a claim that anonymized features prove physical failure mechanisms,
- a replacement for real process-engineer domain review.

This project should avoid spending too much time on:

- advanced neural networks,
- AutoML,
- perfect model optimization,
- deployment,
- streaming data infrastructure,
- complex dashboards,
- advanced causal inference,
- unsupported root-cause claims.

---

## 7. Project Pillars

The project has four major pillars.

### Pillar 1 — Manufacturing Context

You must explain the semiconductor meaning of the project before modeling.

Important terms:

- yield,
- pass/fail testing,
- process variation,
- process drift,
- process window,
- process excursion,
- yield excursion,
- sensor signal,
- metrology measurement,
- tool state,
- route difference,
- false positive,
- false negative,
- failure recall,
- balanced error rate.

### Pillar 2 — Process Signal Understanding

The core data question is:

> Which signals appear useful, noisy, redundant, missing, unstable, or associated with failure?

You are not just cleaning data. You are trying to understand the behavior of manufacturing signals.

### Pillar 3 — Feature Selection

Feature selection is central because the dataset description says engineers may collect more signals than necessary and that feature selection can help identify the most relevant signals.

The project should compare:

- all cleaned features,
- top 40 selected features,
- top 20 selected features,
- top 10 selected features.

The top 40 comparison is especially important because the original SECOM benchmark used feature selection methods that selected the 40 highest-ranked features.

### Pillar 4 — Manufacturing-Focused Evaluation

The model should be evaluated as a possible engineering screening tool.

Key metrics:

- failure-class recall,
- failure-class precision,
- F1-score,
- balanced accuracy,
- balanced error rate,
- false-negative rate,
- confusion matrix,
- precision-recall curve.

Accuracy should be reported only as a secondary metric, and only with a warning.

---

## 8. The Business and Engineering Decision

This project should answer:

> If a yield or process engineer used this workflow, what decision would it support?

Possible decisions:

1. Which process signals should be monitored more closely?
2. Which sensors or measurements appear most related to failure risk?
3. Which variables should be included in a reduced monitoring model?
4. Which production entities should be flagged for review?
5. Which process regions appear abnormal?
6. Which false negatives require extra engineering concern?
7. Which features should be investigated with domain experts?
8. Which additional data should be requested: tool ID, chamber ID, recipe, lot route, metrology step, maintenance history, wafer position, product type, or time sequence?

The final report should present model results as **engineering evidence**, not as automatic truth.

---

## 9. Correct Final Message

At the end of this project, you should be able to say:

> I built a semiconductor yield analytics workflow using SECOM. I analyzed high-dimensional process/sensor data, handled missing values and rare failures, compared feature-selection strategies, evaluated failure detection using balanced metrics, and translated selected features into engineering questions for process/yield investigation.

A stronger interview version:

> This was not just a classifier. The goal was to identify a smaller set of process signals that may help engineers investigate downstream yield failures. Because the features are anonymized, I avoided unsupported root-cause claims and focused on association, signal behavior, model stability, and engineering follow-up questions.

---

## 10. Final Deliverables

The final project should produce the following deliverables.

### Required deliverables

1. `README.md`
2. `notebooks/01_business_context.ipynb`
3. `notebooks/02_data_overview_missingness.ipynb`
4. `notebooks/03_class_imbalance_eda.ipynb`
5. `notebooks/04_feature_selection.ipynb`
6. `notebooks/05_baseline_models_cv_ber.ipynb`
7. `notebooks/06_error_analysis_process_interpretation.ipynb`
8. `reports/secom_process_yield_report.md`
9. `reports/secom_process_yield_report.pdf` if desired
10. `figures/`
11. `tables/`
12. `docs/`
13. `requirements.txt` or `environment.yml`

### Strong optional deliverables

1. `src/` package for reusable cleaning, scoring, and feature-selection code.
2. Model comparison table in CSV.
3. Feature-ranking table in CSV.
4. Error-analysis table.
5. Small presentation deck.
6. One-page executive summary.
7. `docs/process_engineering_questions.md`

---

## 11. Recommended Repository Structure

```text
secom-yield-feature-selection/
│
├── README.md
├── requirements.txt
├── environment.yml
│
├── data/
│   ├── raw/
│   │   ├── secom.data
│   │   ├── secom_labels.data
│   │   └── secom.names
│   ├── interim/
│   └── processed/
│
├── notebooks/
│   ├── 01_business_context.ipynb
│   ├── 02_data_overview_missingness.ipynb
│   ├── 03_class_imbalance_eda.ipynb
│   ├── 04_feature_selection.ipynb
│   ├── 05_baseline_models_cv_ber.ipynb
│   └── 06_error_analysis_process_interpretation.ipynb
│
├── src/
│   ├── data.py
│   ├── cleaning.py
│   ├── features.py
│   ├── evaluation.py
│   └── visualization.py
│
├── figures/
├── tables/
├── reports/
│   ├── secom_process_yield_report.md
│   └── executive_summary.md
│
└── docs/
    ├── dataset_notes.md
    ├── feature_selection_notes.md
    ├── metric_definitions.md
    └── process_engineering_questions.md
```

---

## 12. Tools and Libraries

Use tools you already know. The important part is not the Python syntax; it is the engineering interpretation.

Recommended tools:

- Python
- pandas
- NumPy
- scikit-learn
- matplotlib
- seaborn or plotly if desired
- scipy
- imbalanced-learn only if needed
- shap only if used carefully
- JupyterLab / VS Code
- Git / GitHub

Possible models:

- majority-class baseline,
- logistic regression,
- random forest,
- gradient boosting,
- support vector machine if useful,
- XGBoost or LightGBM if you want a stronger model, but not required.

Possible feature-selection methods:

- missingness ranking,
- variance filtering,
- signal-to-noise ratio,
- t-test,
- F-test,
- Pearson correlation,
- mutual information,
- tree-based importance,
- permutation importance,
- stability selection across folds.

---

## 13. Eight-Week Project Summary

| Week | Project focus | Main output |
|---|---|---|
| Week 1 | Business context, dataset setup, semiconductor vocabulary | Business Context + repo setup |
| Week 2 | Dataset overview, missingness, class imbalance | Data Overview + Cleaning Strategy |
| Week 3 | EDA from process/yield perspective | EDA + candidate signal behavior |
| Week 4 | Feature-selection benchmark | Top 40 / 20 / 10 feature tables |
| Week 5 | Baseline models and balanced evaluation | Model comparison table |
| Week 6 | Cross-validation, BER, threshold analysis | Manufacturing-focused evaluation |
| Week 7 | Error analysis and process interpretation | Feature insight + error analysis |
| Week 8 | Final report, README, portfolio story | GitHub-ready project package |

---

## 14. Success Criteria

This project is successful if someone can open your GitHub repository and understand:

1. What the SECOM dataset represents.
2. Why this is a semiconductor process/yield problem.
3. Why feature selection is central.
4. Why accuracy is misleading.
5. How missing values were handled and interpreted.
6. Which features appeared most associated with failure.
7. Which model and feature set performed best.
8. How balanced error rate was calculated.
9. What the main limitations are.
10. What engineering questions should be asked next.

---

## 15. Portfolio Positioning

Use this project to position yourself as someone who can bridge:

- semiconductor manufacturing,
- process/yield engineering,
- data analytics,
- machine learning,
- feature selection,
- engineering communication.

Suggested portfolio sentence:

> This project demonstrates my ability to translate high-dimensional semiconductor manufacturing data into engineering-oriented insight, using feature selection, balanced rare-failure evaluation, and careful process/yield interpretation.

Suggested resume bullet:

> Built a semiconductor yield analytics workflow using the SECOM manufacturing dataset, comparing feature-selection strategies and balanced classification metrics to identify candidate process signals associated with rare yield failures.

Suggested interview explanation:

> I already knew the ML side, so I focused on reframing the dataset as a process/yield engineering problem. The most important part was not training a model; it was understanding missingness, rare failures, feature relevance, false negatives, and how to communicate selected features as candidates for engineering review rather than unsupported root causes.

---

## 16. Sources to Record in the Project

Use these as your starting references in the README and final report:

1. UCI Machine Learning Repository — SECOM dataset  
   <https://archive.ics.uci.edu/dataset/179/secom>

2. University of Arizona Online — Semiconductor Processing Graduate Certificate  
   <https://online.arizona.edu/programs/graduate-certificate/online-graduate-certificate-semiconductor-processing-gcert>

3. scikit-learn documentation — model evaluation and cross-validation  
   <https://scikit-learn.org/stable/modules/model_evaluation.html>  
   <https://scikit-learn.org/stable/modules/cross_validation.html>

4. scikit-learn documentation — feature selection  
   <https://scikit-learn.org/stable/modules/feature_selection.html>

---

## 17. One-Sentence Final Summary

> Project 1 uses SECOM to practice semiconductor process/yield analytics by identifying relevant process signals, evaluating rare failure prediction with balanced metrics, and translating model evidence into engineering investigation priorities.
