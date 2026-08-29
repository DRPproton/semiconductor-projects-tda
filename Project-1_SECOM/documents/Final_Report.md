# SECOM Semiconductor Feature-Screening Final Report

**Analysis completed:** August 2026  
**Dataset:** Public UCI SECOM manufacturing dataset  
**Primary objective:** Reduce a high-dimensional anonymous process dataset to a defensible shortlist of variables for further engineering investigation.  
**Secondary objective:** Determine whether the available signals support useful failure ranking or classification.

## Technical summary

The project reduced the original 590 numeric process variables to 460 usable features, evaluated their data quality and relationships with failure, compared several feature-selection and modeling approaches, and measured the stability of the final ANOVA shortlists across 25 repeated cross-validation resamples.

The main deliverable is a ranked investigation shortlist rather than a deployable yield classifier. Features **103, 59, and 510** were selected in the top 20 in all 25 resamples. Features **129** and **348** were also highly reproducible, with top-20 selection frequencies of 92% and 80%. These five variables form the strongest first investigation tier under the methods tested.

The tuned Random Forest with 100 ANOVA-selected features produced the strongest tested Random Forest ranking result: repeated-cross-validation average precision of **0.2000 ± 0.0627**, compared with a failure prevalence of **0.0662**. This indicates useful ranking signal, but the model is not suitable for failure screening at the default 0.50 threshold: failure recall was only **0.0196**, corresponding to a false-negative rate of **0.9804**. Reducing the representation to 70, 40, 30, or 20 variables did not improve average precision.

The anonymous feature names and missing process context prevent physical interpretation or root-cause conclusions. The final variables should be treated as sensor or process-step candidates to be mapped to real equipment metadata and validated on independent, temporally separated manufacturing data.

## Key findings

### 1. A small core is reproducible, but the broader top-20 list is less stable

![Feature-selection frequency across 25 resamples](../figures/final_feature_stability.png)

The stability analysis repeated five-fold stratified cross-validation five times. Within each training resample, the greater-than-80% missingness filter, median imputation, and ANOVA selection were relearned. Selection frequency therefore measures how consistently a variable survives changes in the training sample.

- **Core tier:** 103, 59, and 510 were selected in every top-20 list; 129 appeared in 92% and 348 in 80%.
- **Supporting tier:** 64, 431, 21, 100, 125, and 430 appeared in 60%–72% of top-20 lists.
- **Exploratory tier:** the remaining nine variables appeared in 40%–56% of top-20 lists and require more cautious interpretation.

These frequencies are reproducibility indicators, not probabilities that a feature is causal. The repeated splits overlap, so the 25 results are not independent experiments.

### 2. The signal is distributed; 100 features ranked failures better than smaller representations

![Repeated-CV average precision by retained feature count](../figures/final_model_comparison.png)

The plotted points are repeated-cross-validation means and the error bars show plus or minus one standard deviation. The 100-feature Random Forest had the highest numerical average precision among the controlled Random Forest feature-count experiments. Performance declined when the representation was reduced, although the differences are small relative to the cross-validation standard deviations. The evidence therefore supports 100 variables as the strongest tested **predictive representation**, while 40-, 30-, and 20-feature sets are **interpretability-constrained investigation lists**.

The all-feature Logistic Regression line is included only as a reference. Because it is a different classifier, it does not isolate the effect of feature count.

### 3. Ranking information did not translate into usable default-threshold alerts

All Random Forest variants predicted very few failures at the default 0.50 threshold. The top-100 model ranked failures above the prevalence baseline but detected only about 2% of failures as positive classifications. Even the top-20 model, which had the highest Random Forest default-threshold recall, missed approximately 91% of failures.

The balanced Logistic Regression detected more failures at the default threshold, but its ranking performance was lower. This reinforces the distinction between:

- **Ranking:** whether failures tend to receive higher predicted probabilities, measured by average precision.
- **Classification:** whether a chosen threshold converts those probabilities into acceptable alerts, measured by recall, false-negative rate, precision, and balanced accuracy.

No operating threshold was selected, so none of the models should be described as a production failure detector.

## Scope, data, and metric definitions

The merged dataset contains **1,567 observations**, **590 anonymous numeric process features**, one timestamp, and a binary outcome where `-1` means pass and `1` means fail. There are **104 failures**, or approximately **6.6%** of all observations, creating a strongly imbalanced classification problem.

The stratified development split contained:

| Partition | Observations | Failures | Failure rate |
|---|---:|---:|---:|
| Training | 1,253 | 83 | 6.62% |
| Test | 314 | 21 | 6.69% |

The following metrics were emphasized:

| Metric | Meaning in this project |
|---|---|
| Average precision (AP) | Quality of the complete failure-probability ranking; appropriate for rare positive outcomes. |
| Failure recall | Proportion of actual failures detected at a chosen threshold. |
| False-negative rate (FNR) | Proportion of actual failures missed; `1 - recall`. |
| Failure precision | Proportion of failure alerts that are actual failures. |
| Balanced accuracy (BA) | Mean of pass recall and failure recall, giving both classes equal weight. |
| Balanced error rate (BER) | `1 - balanced accuracy`. |

Ordinary accuracy was not used to select the final models because an always-pass prediction would already be approximately 93.4% accurate.

## Data preparation and exploratory findings

### Feature removal decisions

| Step | Decision | Result |
|---|---|---:|
| Constant screening | Removed variables with no variation. | 116 removed |
| Near-constant screening | Removed variables with three observed states including missingness, dominated by zero. | 6 removed |
| Missingness screening | Removed variables with more than 80% missing values. | 8 removed |
| Final modeling space | Retained numeric variables after these filters. | 460 features |

The 80% threshold was chosen because the affected variables had too little observed information to support stable estimation in this small, imbalanced dataset. Median imputation was learned within each cross-validation training fold to avoid leakage.

### Exploratory signal and redundancy

The dataset contains substantial skew, outliers, missingness, and correlation:

- 259 features were classified as highly skewed.
- 28 were outlier-heavy.
- 37 showed a notable pass/fail distribution shift.
- 263 participated in strong redundancy relationships, covering 224 highly correlated pairs.
- Features 59, 103, 510, and 348 showed some of the strongest univariate standardized pass/fail differences.
- Features 64 and 65 were associated with elevated observed failure rates in their extreme regions.

These findings motivated robust preprocessing, fold-local feature selection, and stability analysis. Correlated signals may represent duplicate measurements, linked process stages, or a shared latent process condition; correlation alone cannot determine which interpretation is correct.

### PCA result

Principal component analysis showed that the variance is distributed across many dimensions:

| Explained variance | Components required |
|---|---:|
| 80% | 87 |
| 90% | 129 |
| 95% | 164 |

The first two components explained only 9.34% of total variance and did not visibly separate pass from fail. PCA therefore supported the conclusion that the dataset has no simple low-dimensional failure boundary. It was retained as an exploratory result rather than used in the final feature-identification pipeline because transformed components would make sensor-level investigation harder.

## Modeling and validation methodology

### Leakage controls

Preprocessing and feature selection were placed inside the modeling pipeline so that each validation fold learned its own missingness filter, imputation values, and ANOVA rankings. Model selection used training data only. Stratification preserved the rare-failure proportion across folds.

### Model search

The project evaluated balanced Logistic Regression, Random Forest, and HistGradientBoosting representations, along with ANOVA, mutual information, Random Forest importance, recursive feature elimination, correlation pruning, and PCA. These methods did not produce identical rankings, which is expected because they measure different kinds of signal:

- ANOVA measures one-variable-at-a-time linear class separation.
- Mutual information can detect more general univariate dependence.
- Random Forest importance reflects nonlinear and multivariate tree splits but can divide importance among correlated variables.
- RFE depends on the fitted estimator and the candidate variables available at each step.

Optuna compared classifier and feature-count choices using average precision. Its best fixed-split result was 0.23085 with a 100-feature Random Forest. Repeated cross-validation reduced the estimate to 0.2000 ± 0.0627, which is the more realistic summary. The fixed-split optimum is selection-biased because it was chosen as the best of 50 trials on one cross-validation partition.

### Final feature-count comparison

| Representation and classifier | BA | Failure recall | FNR | Precision | F1 | AP |
|---|---:|---:|---:|---:|---:|---:|
| All 460, balanced Logistic Regression | 0.5787 ± 0.0585 | 0.2650 ± 0.1167 | 0.7350 | 0.1475 | 0.1885 | 0.1539 ± 0.0536 |
| ANOVA 100, tuned Random Forest | 0.5084 ± 0.0212 | 0.0196 ± 0.0414 | 0.9804 | 0.1867 | 0.0349 | **0.2000 ± 0.0627** |
| ANOVA 70, tuned Random Forest | 0.5085 ± 0.0211 | 0.0243 ± 0.0423 | 0.9757 | 0.1727 | 0.0402 | 0.1785 ± 0.0548 |
| ANOVA 40, tuned Random Forest | 0.5186 ± 0.0324 | 0.0506 ± 0.0629 | 0.9494 | 0.2293 | 0.0789 | 0.1780 ± 0.0642 |
| ANOVA 30, tuned Random Forest | 0.5228 ± 0.0339 | 0.0674 ± 0.0663 | 0.9326 | 0.2067 | 0.0953 | 0.1723 ± 0.0567 |
| ANOVA 20, tuned Random Forest | 0.5296 ± 0.0376 | 0.0887 ± 0.0720 | 0.9113 | 0.1809 | 0.1166 | 0.1717 ± 0.0648 |

The observed differences among the Random Forest AP values are smaller than their fold-to-fold standard deviations. The table supports a numerical preference for 100 features, but not a claim that its true performance is definitively superior to every smaller set.

## Final investigation shortlist

The final list was sorted first by top-20 selection frequency, then by Random Forest importance rank, and then by full-training ANOVA rank.

| Feature | ANOVA rank | RF rank | Top-20 frequency | Investigation tier |
|---:|---:|---:|---:|---|
| 103 | 1 | 1 | 100% | Core |
| 59 | 3 | 2 | 100% | Core |
| 510 | 2 | 8 | 100% | Core |
| 129 | 5 | 25 | 92% | Core |
| 348 | 4 | 50 | 80% | Core |
| 64 | 7 | 6 | 72% | Supporting |
| 431 | 6 | 56 | 72% | Supporting |
| 21 | 8 | 17 | 68% | Supporting |
| 100 | 12 | 72 | 64% | Supporting |
| 125 | 9 | 13 | 60% | Supporting |
| 430 | 10 | 67 | 60% | Supporting |
| 316 | 13 | 24 | 56% | Exploratory |
| 434 | 11 | 79 | 56% | Exploratory |
| 436 | 15 | 87 | 52% | Exploratory |
| 435 | 14 | 89 | 52% | Exploratory |
| 351 | 19 | 12 | 48% | Exploratory |
| 213 | 21 | 10 | 44% | Exploratory |
| 95 | 18 | 96 | 44% | Exploratory |
| 28 | 16 | 32 | 40% | Exploratory |
| 114 | 26 | 98 | 40% | Exploratory / rare-state |

Feature 114 deserves a special warning. It was frequently selected by univariate ANOVA in broader lists, but it had zero Random Forest importance in the fitted top-100 model and was previously identified as a rare-state, low-information feature. It may describe an unusual event, but it is not part of the cross-method core and should not be prioritized without examining its measurement definition and support among failures.

Some variables ranked highly by Random Forest but not by ANOVA, including 477, 247, 205, and 31. These are reasonable secondary candidates for investigating nonlinear effects or interactions, but the current evidence does not justify replacing the stability-based shortlist with them.

## Limitations, uncertainty, and robustness

1. **Anonymous features:** There are no sensor names, units, process stages, control limits, tools, chambers, recipes, or maintenance records. Statistical associations cannot be translated into mechanisms or root causes.
2. **Rare outcome:** Only 104 failures are available overall and 83 are in the training partition. Estimates involving failure recall and feature effects therefore have substantial uncertainty.
3. **Observational evidence:** Association with failure does not establish that changing a variable would improve yield.
4. **Cross-validation dependence:** Repeated folds overlap. Selection frequencies and metric distributions describe resampling stability, not independent replications.
5. **Selection optimism:** Optuna's best fixed-split score was optimized over 50 trials. Repeated validation is more cautious but is not a fully nested, unbiased estimate because the same training dataset informed tuning decisions.
6. **Impurity importance:** Random Forest importance can favor some variables and divide credit unpredictably among correlated features. It is supporting evidence, not a definitive ranking.
7. **Test-set status:** The test partition was consulted once earlier for a preliminary baseline accuracy result. It was not used for the later feature selection, Optuna search, or stability analysis, but it is no longer a perfectly untouched final holdout.
8. **No final operating threshold:** A threshold was not selected from out-of-fold training predictions, so a final confusion matrix would be arbitrary. No confusion matrix is included in this report for that reason.

## Conclusions and decisions

The analysis achieved its realistic objective: it reduced 590 anonymous process measurements to a reproducible, tiered list for future investigation. The strongest candidates are **103, 59, 510, 129, and 348**, with the first three showing perfect top-20 stability across the 25 resamples.

The project also showed why this dataset is difficult. Failure information appears to be distributed across many variables, class imbalance is severe, and a model with useful ranking signal can still fail as a default-threshold classifier. The 100-feature Random Forest should be retained as the leading ranking representation, while the 20-feature list should be retained as the most interpretable engineering shortlist.

No model from this study is production-ready, and no root-cause statement is supported. The correct handoff is a set of prioritized questions for engineers with access to the real process context.

## Recommended next steps

1. **Map the core five feature IDs to physical metadata.** Identify sensor name, unit, process step, tool, chamber, recipe, sampling time, and control limits for 103, 59, 510, 129, and 348.
2. **Inspect the core variables by manufacturing context.** Compare distributions and failure rates by tool, chamber, recipe, product, lot, wafer position, maintenance state, and time period.
3. **Investigate redundancy as process structure.** Determine whether correlated shortlisted variables are duplicate sensors, consecutive process steps, or responses to a shared condition.
4. **Review missingness operationally.** Establish whether missing values indicate sensor failure, an optional recipe step, tool configuration, or data-collection behavior.
5. **Validate on new temporal data.** Freeze the preprocessing, feature selection, and model configuration before applying them to a later production period or another manufacturing cohort.
6. **Only if failure screening remains a goal, choose an operating threshold.** Use out-of-fold training probabilities and an explicit cost or recall requirement, then produce the confusion matrix and alert-volume tradeoff. Because the present test set was previously viewed, independent data would provide the cleanest final evaluation.
7. **Preserve the three feature products.** Keep the 100-feature predictive representation, the 20-feature engineering shortlist, and the five-feature core. They answer different questions and should not be treated as interchangeable.

## Further questions for process engineers

- What physical measurements correspond to features 103, 59, 510, 129, and 348?
- Are these measurements taken before the failure outcome is known, and would they be available at decision time?
- Do features 64 and 65 measure the same process stage, given their similar extreme-region behavior?
- Are the missingness blocks tied to particular tools, recipes, or optional process paths?
- Are failures concentrated by lot, tool, chamber, product, or time period?
- What false-alarm rate is acceptable for a required failure-recall target?
- Can a temporally later, fully independent dataset be obtained for confirmation?

## Reproducibility artifacts

- Main analysis notebook: `notebooks/notebook.ipynb`
- Phase documentation: `documents/Phase_1.md` through `documents/Phase_7.md`
- Detailed model log: `documents/models_eval.md`
- Figure-generation script: `figures/build_final_report_figures.py`
- Final figures: `figures/final_feature_stability.png` and `figures/final_model_comparison.png`
