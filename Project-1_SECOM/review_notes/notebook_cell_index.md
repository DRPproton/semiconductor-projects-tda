# Notebook Cell Index

This file tracks the current cell locations used during the collaborative notebook review. Cell numbers are zero-based and may change if cells are inserted or removed.

## Project Phase 2: Initial Data Inspection

- Cell 14: Phase heading
- Cells 16-19: dataset dimensions and class distribution
- Cells 21-23: missing-value inspection
- Cells 24-35: constant and near-constant feature report
- Cell 37: rule selecting near-constant features for removal
- Cells 38-41: selected feature counts and threshold comparison
- Cell 42: removal of selected constant and near-constant features
- Cell 43: preview of the reduced dataframe

### Near-constant decision verified from raw data

The six selected near-constant features are `74`, `206`, `209`, `342`, `347`, and `478`.

For every one of these features:

- There are two non-missing values: zero and one rare nonzero value.
- Including `NaN`, there are three unique values.
- Six rows are missing.
- Zero occurs in 1,560 rows.
- The only nonzero observation occurs in row 1,458.
- Row 1,458 has label `-1` (pass).

This supports removing these six features: their only observed variation is a single passing observation shared across all six signals, so it provides no repeatable failure-discrimination evidence and poses an overfitting risk.

### Current saved-output status

At the time of this review, Phase 2 code cells 16-43 had `execution_count = null` and no saved outputs in `notebooks/notebook.ipynb`. Save the notebook after execution when output review is requested.

## Project Phase 3: Missingness as Process Information

- Cells 44-52: duplicate check, feature types, and timestamp conversion
- Cells 54-56: features above 50% missingness
- Cells 58-66: missingness comparison by pass/fail target
- Cells 68-71: highest-missingness features and overall sparsity summary

### Saved results reviewed

- No duplicate rows were found.
- The reduced dataset contains 468 float features, one integer label, and one timestamp.
- The timestamp was converted to datetime.
- Twenty-eight process features are more than 50% missing.
- Four features (`157`, `158`, `292`, and `293`) are 91.19% missing.
- Four features (`85`, `220`, `358`, and `492`) are 85.58% missing.
- No feature has a missingness pattern that perfectly matches or exclusively identifies the failure class.

### Important validation notes

- Cell 58 includes the timestamp in `missingness_target_report`, producing 469 reported fields even though there are 468 process features. The complete timestamp does not change the major findings, but future process-feature reports should exclude it.
- Cell 65 compares the numeric `missing_rate_diff_fail_minus_pass` column with Boolean `True`. Its output of zero does not mean that no pass/fail missingness differences exist.
- Independent verification found 101 features with positive differences, 315 with negative differences, and 52 with exactly equal pass/fail missingness rates. Eighty-six features differ by at least one percentage point, and 28 differ by at least five percentage points in absolute value.
- Features `72`, `73`, `345`, and `346` have the largest absolute difference: missingness is 17.20 percentage points lower in failures than passes.
- Features `112`, `247`, `385`, and `519` are 14.89 percentage points lower in failures than passes.
- The repeated groups documented in `Phase_3_explantion.md` have identical row-level missingness masks, supporting the interpretation that they were collected as coordinated measurement blocks.

## Project Phase 4: Target Imbalance and Manufacturing Risk

- Cells 72-74: final Phase 3 high-missingness removal
- Cell 75: Phase 4 heading
- Cells 76-79: class counts, class-distribution chart, and summary table
- Cell 80: Phase 5 heading

### Saved Phase 4 results reviewed

- Pass: 1,463 observations (93.36%)
- Fail: 104 observations (6.64%)
- A classifier predicting every observation as pass would have 93.36% accuracy, 0% failure recall, 50% balanced accuracy, and 50% balanced error rate.
- The class-distribution chart and the written metric rationale agree with the saved counts.

### Important notebook-state note before Phase 5

- Cell 72 selects features using pass-class missingness greater than 65%, although the documented decision is overall missingness greater than 80%. The two rules happen to identify the same eight features in this dataset, but they are not the same reproducible rule.
- Cell 74 has been corrected to drop the eight features from `df_no_constant_cols`, preserving the Phase 2 removals.
- The intended Phase 5 input therefore contains 460 numerical process features, plus the label and timestamp.

## Project Phase 5: Process-Oriented EDA

- Cells 81-84: descriptive profile, feature EDA report, report shape, and median outlier count
- Cells 85-88: top pass/fail standardized-mean-difference candidates
- Cells 89-91: features with failures in pass-defined extreme ranges
- Cells 92-96: strongly skewed and outlier-heavy features
- Cells 97-101: behavior flags, candidate count, and heuristic EDA shortlist
- Cells 102-103: selected pass/fail distribution plots
- Cells 104-110: intersections among the candidate lists

### Saved Phase 5 results reviewed

As of August 26, 2026, Phase 5 cells 81-110 are saved with sequential execution counts 54-79 and no stored errors.

- The EDA report contains 460 process features and 35 initial statistics per feature.
- The median Tukey outlier count is 39.5 observations per feature; because feature availability differs, outlier rate is the more comparable measure.
- The largest absolute standardized mean differences are feature `59` (0.632), `103` (0.614), `510` (0.533), `348` (0.523), and `111` (0.504, negative direction).
- Features `64` and `65` have the highest failure-extreme rate at 28.85%. Feature `348` follows at 23.08%.
- The behavior rule flags 38 of 460 features (8.26%) as candidate process signals.
- Five features occur in both the top-30 pass/fail-shift and top-30 failure-extreme lists: `59`, `210`, `294`, `299`, and `348`.
- Features `59` and `129` occur in both the top-30 pass/fail-shift and top-30 overall-outlier lists.
- The twelve saved density plots confirm substantial class overlap despite several visible distribution shifts and heavier failure tails.
- The shortlist support check shows that 27 of 30 features are observed for 103 or all 104 failures.
- Feature `111` is the weakest-supported shortlist candidate: 30 observed failures (28.85%) and 519 observed passes (35.48%).
- Feature `247` has moderate and class-dependent availability: 71 observed failures (68.27%) and 781 observed passes (53.38%).
- Feature `562` is observed for 80 failures (76.92%) and 1,214 passes (82.98%).
- Features `59`, `103`, `210`, `348`, and `510` combine strong or moderate effect sizes with complete failure-class coverage.
- The low-information check identifies four retained rare-state features: `114`, `249`, `387`, and `521`.
- Zero is the dominant value for about 98.6% of observations in each of these four features. They are classified as low-information/rare-state signals rather than removed automatically.
- Spearman redundancy screening at absolute correlation >= 0.95 with at least 100 paired observations identifies 224 highly correlated feature pairs involving 263 of the 460 remaining process features (57.2%).
- Several relationships are exact or nearly exact, including `578`/`586`, `581`/`589`, `580`/`588`, `579`/`587`, `249`/`387`, and the inverse pair `34`/`36`.
- Correlation is treated as evidence of shared behavior or redundancy, not proof that anonymous variables originate from the same physical sensor or process step.
- The final process-signal taxonomy contains 460 rows. Its category counts are: 20 missing-heavy, 4 low-information/rare-state, 259 highly skewed, 28 outlier-heavy, 37 pass/fail-shifted, 2 failure-extreme, and 263 highly redundant features.
- The taxonomy categories overlap. The pass/fail-shift and failure-extreme rules jointly identify 38 candidate process signals because feature `64` satisfies both rules.
- Phase 5 meets its stop condition: a complete process-signal taxonomy and written technical synthesis are available.

### Review points for the next saved run

- Interpret pass/fail effect size and failure-extreme behavior as exploratory association, not causation.
- Check `pass_count` and `fail_count` before trusting high-ranked sparse features.
- Treat skew and overall outlier rate as distribution behavior, not evidence of failure relevance by themselves.
- The additive `eda_priority_score` is a heuristic that combines an unbounded effect size with bounded rates and should not be treated as a validated ranking metric.
- The set intersections compare top-30 rank lists, not all features satisfying the behavior-flag thresholds.
- The strongest-skew table is calculated but not displayed in the notebook.
- Phase 5 is not complete until the notebook contains a process-signal taxonomy, low-variance assessment, redundancy/correlation analysis, and a written synthesis.

## Project Phase 6: Feature Selection and PCA

- Cells 119-124: Phase 6 heading, stratified train/test split, and split verification
- Cells 125-128: training-only median imputation and mutual-information ranking
- Cells 129-135: Random Forest importance and `SelectFromModel`
- Cells 136-138: balanced Random Forest RFE and selected 40-feature set
- Cells 139-146: training-only PCA pipeline, variance summary, cumulative-variance curve, and PC1-PC2 projection

### Saved PCA results reviewed

- PCA was fitted on the 1,253-row training set after training-only median imputation and standardization.
- The diagnostic fit retained all 460 components; 87 components explain 80% of variance, 129 explain 90%, and 164 explain 95%.
- PC1 explains 5.62% and PC2 explains 3.72%, for 9.34% combined.
- The first 20 components explain 39.15% of total training variance.
- The PC1-PC2 plot shows strong pass/fail overlap in the dense central region. Some failures occur in extreme PCA regions, but passing examples also occupy those regions.
- PCA supports substantial redundancy but not a very low-dimensional structure, and the first two components do not provide a clean failure boundary.
- The saved pipeline currently uses `PCA()` and therefore does not yet reduce the matrix. A later `n_components=0.95` modeling branch would retain 164 training-derived components.

## Project Phase 7: Baseline Modeling

- Cell 147: Phase 7 heading
- Cell 148: all-feature balanced Logistic Regression pipeline definition
- Cell 149: pipeline fitted on `X_train` and `y_train`
- Cell 150: preliminary `.score(X_test, y_test)` result

### Saved baseline result reviewed

- The pipeline uses the 0.80 missingness threshold, no correlation pruning, median imputation, no selector, standardization, no reducer, and balanced Logistic Regression.
- Cell 150 now reports ordinary training accuracy of 0.97845.
- Cells 151-152 evaluate the complete pipeline with 5-fold repeated stratified cross-validation, repeated five times, using training data only.
- Mean balanced accuracy is 0.57874 (SD 0.05854), corresponding to mean BER of 0.42126.
- Mean failure recall is 0.265 (SD 0.11674), so the mean false-negative rate is 0.735.
- Mean failure precision is 0.14753 (SD 0.05912), failure F1 is 0.18847 (SD 0.07697), and average precision is 0.15386 (SD 0.05363).
- Average precision is above the training failure prevalence of 0.0662, indicating some ranking signal, but the default classifier misses nearly three quarters of failures and is unstable across folds.
- The large difference between fitted training accuracy and out-of-fold performance is consistent with substantial overfitting in the 460-feature Logistic Regression baseline.
- Representation and model comparisons should continue using training-only cross-validation; the test set should not be consulted again until the final selected pipeline is evaluated.

### Correlation-pruned RF-RFE top-40 diagnostic

- Cells 154-160 define, fit, and cross-validate a correlation-pruned, RF-RFE top-40 pipeline with a 500-tree Random Forest classifier.
- The full-training fit confirms correlation pruning from 460 to 261 features before RFE retains 40.
- Fitted training accuracy is 0.97765, but cross-validated balanced accuracy is 0.49983 and failure recall is 0.0; mean FNR is 1.0.
- Mean average precision is 0.18528, indicating ranking signal even though the default threshold detects no failures.
- The final Random Forest lacks class weighting; the balanced class weights used inside the RFE estimator do not apply to the final classifier.
- Because both the representation and classifier changed relative to the baseline, this is not a controlled test of correlation pruning/RFE. Repeat with the same balanced Logistic Regression classifier for the representation screen.
- Cells 155-160 were rerun with a revised final Random Forest using balanced subsampling, maximum depth 8, minimum leaf size 4, and no scaler.
- The revised model reaches 0.99920 fitted training accuracy but only 0.50423 mean balanced accuracy in cross-validation.
- Mean failure recall is 0.01427, mean FNR is 0.98574, and mean average precision is 0.18272.
- The revised class weighting does not solve default-threshold failure detection; the training/CV gap provides stronger evidence of overfitting.
- The final Random Forest and outer cross-validation both use `n_jobs=-1`, creating potential nested parallelism. This affects efficiency rather than the reported predictive metrics.
- Cells 161-165 add a second correlation-pruned Random Forest run without RFE.
- This run also changes the missingness threshold from 0.80 to 0.50 and enables `SimpleImputer(add_indicator=True)`, so it does not isolate the effect of removing RFE.
- Mean balanced accuracy is exactly 0.50, failure recall is 0.0, and FNR is 1.0; the classifier predicts no validation failures at the default threshold.
- Mean average precision rises to 0.20856 (SD 0.06105), the strongest ranking result so far, but the responsible pipeline change cannot be identified from this multi-change experiment.
- The second run correctly uses the revised Random Forest with `min_samples_split=10` and `n_jobs=1`.
- Cell 162 was later changed to standard median imputation without missing indicators, and cell 163 refitted that pipeline in execution 140.
- Cells 164-165 were not rerun after that change; their visible cross-validation output is stale from execution 138 and must not be attributed to the no-indicator pipeline.
- Cells 162-165 were subsequently rerun in executions 143-146 with `imputer=None`, no RFE, a 50% missingness threshold, correlation pruning, and the balanced regularized Random Forest.
- The no-imputation pipeline fits successfully, confirming native missing-value support in the installed Random Forest implementation.
- Mean balanced accuracy remains 0.50, failure recall remains 0.0, FNR remains 1.0, and mean average precision is 0.19878 (SD 0.05241).
- Cells 166-170 add an ANOVA `SelectKBest(f_classif, k=100)` pipeline using the balanced regularized Random Forest.
- The selector is correctly placed inside the pipeline after median imputation and before the classifier; correlation pruning is disabled.
- Mean balanced accuracy is 0.50684, failure recall is 0.01471, FNR is 0.98529, and average precision is 0.19106 (SD 0.06520).
- The pipeline uses Random Forest rather than the balanced Logistic Regression required for the controlled representation screen, so it cannot isolate the value of the ANOVA top-100 representation relative to the baseline.
