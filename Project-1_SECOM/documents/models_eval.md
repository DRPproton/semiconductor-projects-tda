# Model Evaluation Log

**Purpose:** Maintain a consistent, evidence-based analysis of every feature-representation and model pipeline evaluated in Phase 7.

## Evaluation Protocol

- Modeling data: training partition only, containing 1,253 observations and 83 failures (6.62%).
- Validation: repeated stratified 5-fold cross-validation with five repeats and `random_state=42`.
- Total validation results per pipeline: 25 folds.
- All learned preprocessing is fitted again inside each training fold.
- Primary manufacturing-risk metrics: failure recall and false-negative rate.
- Supporting metrics: balanced accuracy, balanced error rate (BER), failure precision, failure F1, and average precision.
- The same validation design and random seed must be used for every pipeline comparison.
- The test partition must not be used to select a feature representation, model, hyperparameter, or decision threshold.

## Model Comparison

| Pipeline | Representation | Balanced accuracy | BER | Failure recall | False-negative rate | Failure precision | Failure F1 | Average precision | Status |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| Balanced Logistic Regression baseline | All 460 retained features | 0.5787 ± 0.0585 | 0.4213 ± 0.0585 | 0.2650 ± 0.1167 | 0.7350 | 0.1475 ± 0.0591 | 0.1885 ± 0.0770 | 0.1539 ± 0.0536 | Baseline only |
| Random Forest diagnostic | Correlation-pruned + RF-RFE top 40 | 0.4998 ± 0.0006 | 0.5002 ± 0.0006 | 0.0000 ± 0.0000 | 1.0000 | 0.0000 ± 0.0000 | 0.0000 ± 0.0000 | 0.1853 ± 0.0521 | Reject at default threshold |
| Balanced regularized Random Forest | Correlation-pruned + RF-RFE top 40 | 0.5042 ± 0.0123 | 0.4958 ± 0.0123 | 0.0143 ± 0.0254 | 0.9857 | 0.0933 ± 0.1753 | 0.0244 ± 0.0435 | 0.1827 ± 0.0482 | Reject at default threshold |
| Balanced regularized Random Forest | 50%-missingness filter + correlation pruning + missing indicators; no RFE | 0.5000 ± 0.0000 | 0.5000 ± 0.0000 | 0.0000 ± 0.0000 | 1.0000 | 0.0000 ± 0.0000 | 0.0000 ± 0.0000 | 0.2086 ± 0.0610 | Ranking candidate only |
| Balanced regularized Random Forest | 50%-missingness filter + correlation pruning; no RFE or imputation | 0.5000 ± 0.0000 | 0.5000 ± 0.0000 | 0.0000 ± 0.0000 | 1.0000 | 0.0000 ± 0.0000 | 0.0000 ± 0.0000 | 0.1988 ± 0.0524 | Reject at default threshold |
| Balanced regularized Random Forest | ANOVA SelectKBest top 100 | 0.5068 ± 0.0159 | 0.4932 ± 0.0159 | 0.0147 ± 0.0316 | 0.9853 | 0.1800 ± 0.3709 | 0.0269 ± 0.0573 | 0.1911 ± 0.0652 | Reject at default threshold |

## Model 1: Balanced Logistic Regression with All 460 Features

### Pipeline configuration

1. Remove features exceeding 80% missingness within the fitted training data.
2. Do not apply correlation pruning.
3. Apply median imputation.
4. Do not apply RFE or another feature selector.
5. Standardize the measurements.
6. Do not apply PCA.
7. Fit Logistic Regression with balanced class weights, a maximum of 5,000 iterations, and `random_state=42`.

### Cross-validation results

| Metric | Mean | Standard deviation | Interpretation |
|---|---:|---:|---|
| Balanced accuracy | 0.5787 | 0.0585 | Better than the approximately 0.50 chance reference, but only modestly. |
| Balanced error rate | 0.4213 | 0.0585 | The average class-balanced error remains high; lower is better. |
| Failure recall | 0.2650 | 0.1167 | The model detects approximately 26.5% of failures at the default threshold. |
| False-negative rate | 0.7350 | — | The model misses approximately 73.5% of failures. |
| Failure precision | 0.1475 | 0.0591 | Approximately 15% of failure alerts correspond to actual failures. |
| Failure F1 | 0.1885 | 0.0770 | The combined failure recall and precision performance is weak. |
| Average precision | 0.1539 | 0.0536 | Above the 6.62% failure prevalence, indicating some useful ranking signal. |

### Interpretation

The all-feature Logistic Regression is a valid reference model, but it is not an adequate manufacturing-screening model in its current form. Its mean failure recall is only 26.5%, which corresponds to a 73.5% false-negative rate. Missing nearly three quarters of failures conflicts with the project's primary screening objective.

Failure precision is also low. Approximately one in seven observations predicted as failures is an actual failure, implying a substantial false-alarm burden. Nevertheless, average precision is more than twice the training failure prevalence, so the measurements contain some predictive ranking information even though the default classification threshold does not convert that information into strong failure detection.

The standard deviations are material relative to the mean scores, especially for failure recall and F1. Each validation fold contains only approximately 16 or 17 failures, so a small number of changed predictions can produce large metric changes. Model stability must therefore be considered alongside average performance.

### Overfitting assessment

The pipeline achieved 97.85% ordinary accuracy when scored on the same training observations used for fitting. This fitted score is substantially more optimistic than its out-of-fold performance and is consistent with overfitting in a dataset containing 460 measurements but only 83 training failures.

An earlier preliminary test check produced 83.76% ordinary accuracy. That value is not used for model selection and is less informative than failure-sensitive metrics. For comparison, predicting every test observation as passing would produce 93.31% ordinary accuracy because the dataset is severely imbalanced.

### Decision

- Retain this pipeline as the all-feature baseline.
- Do not select it as the final screening model based on the current evidence.
- Do not use ordinary training or test accuracy as the primary comparison measure.
- Compare the next representation against this baseline using the identical training-only cross-validation procedure.
- Evaluate whether correlation pruning improves generalization, failure recall, BER, average precision, or fold-to-fold stability.

## Model 2: Random Forest with Correlation Pruning and RF-RFE Top 40

### Pipeline configuration

1. Remove features exceeding 80% missingness within the fitted training data.
2. Apply absolute Spearman correlation pruning at 0.90 with at least 100 paired observations.
3. Apply median imputation.
4. Apply balanced Random Forest RFE to retain 40 features.
5. Standardize the selected features.
6. Do not apply PCA.
7. Fit a 500-tree Random Forest without class weighting.

On the complete training set, correlation pruning reduced the input from 460 to 261 features before RFE retained 40. This confirms that both learned selection stages were active.

### Cross-validation results

| Metric | Mean | Standard deviation | Interpretation |
|---|---:|---:|---|
| Balanced accuracy | 0.4998 | 0.0006 | Approximately chance-level balanced classification. |
| Balanced error rate | 0.5002 | 0.0006 | Approximately the chance reference; lower is better. |
| Failure recall | 0.0000 | 0.0000 | No validation failures were detected at the default threshold. |
| False-negative rate | 1.0000 | — | Every validation failure was missed. |
| Failure precision | 0.0000 | 0.0000 | No useful positive predictions were produced. |
| Failure F1 | 0.0000 | 0.0000 | Failure classification failed completely at the default threshold. |
| Average precision | 0.1853 | 0.0521 | Probability ranking contains signal despite the failed default-threshold classifications. |

### Interpretation

The fitted training accuracy of 97.77% is nearly identical to the all-feature baseline's 97.85%, but that similarity is not evidence of equal generalization. In cross-validation, this pipeline behaves approximately like an always-pass classifier and misses every failure.

The final Random Forest does not use class weights, even though the Random Forest inside RFE is balanced. The selector's class weighting does not transfer to the final classifier. This likely contributes to all predicted failure probabilities remaining below the default classification threshold. The average-precision score of 18.53%—higher than the all-feature Logistic Regression baseline's 15.39%—shows that its probability ranking contains some failure information, but the current classifier does not convert that ranking into usable failure decisions.

This result cannot isolate the effect of correlation pruning or top-40 RFE because both the representation and the final classifier changed relative to Model 1. A controlled representation comparison must keep balanced Logistic Regression as the classifier. Scaling is also unnecessary for Random Forest, although it does not explain the failed recall.

### Decision

- Reject this configuration as a failure-screening classifier at the default threshold.
- Retain the result as evidence that ordinary training accuracy is misleading.
- Do not treat it as the controlled correlation-pruned/top-40 comparison.
- Repeat the representation with the same balanced Logistic Regression used in Model 1.
- If Random Forest is reconsidered during the finalist-model stage, use explicit imbalance handling and evaluate threshold behavior using training-only validation.

## Model 3: Balanced Regularized Random Forest with Correlation Pruning and RF-RFE Top 40

### Pipeline configuration

This run retains the same correlation-pruned, RF-RFE top-40 representation as Model 2. The final classifier was revised to use 500 trees, balanced subsampling, maximum depth 8, minimum split size 5, minimum leaf size 4, square-root feature sampling, and bootstrap sampling. Scaling was correctly disabled because tree models do not require standardized inputs.

The saved code uses `n_jobs=-1` in both the final Random Forest and the outer cross-validation. This does not explain the predictive result, but it can create inefficient nested parallelism. The estimator should use one worker when the outer cross-validation already parallelizes folds.

### Cross-validation results

| Metric | Mean | Standard deviation | Interpretation |
|---|---:|---:|---|
| Balanced accuracy | 0.5042 | 0.0123 | Only slightly above the chance reference. |
| Balanced error rate | 0.4958 | 0.0123 | Approximately chance-level class-balanced error. |
| Failure recall | 0.0143 | 0.0254 | The model detects approximately 1.4% of validation failures. |
| False-negative rate | 0.9857 | — | Approximately 98.6% of validation failures are missed. |
| Failure precision | 0.0933 | 0.1753 | Failure alerts are extremely rare and unstable across folds. |
| Failure F1 | 0.0244 | 0.0435 | Default-threshold failure classification remains ineffective. |
| Average precision | 0.1827 | 0.0482 | Probability rankings retain some failure signal despite the failed classifications. |

### Interpretation

Adding balanced class weights produces only a minimal improvement in default-threshold failure detection: mean recall rises from 0% to approximately 1.4%. The model still behaves almost like an always-pass classifier during validation. Balanced class weights influence the fitted loss but do not guarantee that predicted failure probabilities will exceed the default 0.50 threshold.

The fitted training accuracy rises to 99.92%, while balanced cross-validation performance remains near chance. This is stronger evidence of overfitting than the previous run. The high training accuracy should not be interpreted as improvement.

Average precision remains above the 6.62% failure prevalence and above the all-feature Logistic Regression baseline, indicating that the model ranks some failures above passing observations. This may justify threshold analysis if Random Forest later becomes a finalist, but threshold adjustment cannot repair a representation or classifier that has not first demonstrated competitive cross-validated ranking and stability.

### Decision

- Reject this configuration as a default-threshold failure-screening model.
- Do not continue tuning the Random Forest during the controlled representation screen.
- Return to balanced Logistic Regression to isolate the effect of correlation pruning and RFE top 40.
- Reconsider Random Forest only after the strongest feature representation has been selected.
- If reconsidered, tune its threshold and complexity using training-only validation, never the test set.

## Model 4: Balanced Regularized Random Forest without RFE

### Pipeline configuration

This run uses a 50% missingness threshold, absolute Spearman correlation pruning at 0.90, median imputation with automatic missing-value indicators, no RFE, no scaling, no PCA, and the balanced regularized 500-tree Random Forest.

Although it was introduced as a no-RFE comparison, it also changes the missingness threshold from 80% to 50% and enables missing indicators. Its result therefore cannot isolate the effect of removing RFE. The saved output does not report the number of features retained after missingness and correlation pruning or the number of indicators added.

### Cross-validation results

| Metric | Mean | Standard deviation | Interpretation |
|---|---:|---:|---|
| Balanced accuracy | 0.5000 | 0.0000 | Exactly the always-one-class balanced reference. |
| Balanced error rate | 0.5000 | 0.0000 | No useful default-threshold class separation. |
| Failure recall | 0.0000 | 0.0000 | No validation failures were detected. |
| False-negative rate | 1.0000 | — | Every validation failure was missed. |
| Failure precision | 0.0000 | 0.0000 | No positive failure predictions were produced. |
| Failure F1 | 0.0000 | 0.0000 | Failure classification failed completely at the default threshold. |
| Average precision | 0.2086 | 0.0610 | Best ranking result so far, but still variable and not converted into failure predictions. |

### Interpretation

At the default 0.50 decision threshold, this pipeline predicts every validation observation as passing. It is therefore unusable as a failure-screening classifier in its current form.

Average precision improves to 20.86%, compared with 18.27% for the balanced RF-RFE top-40 run and 15.39% for the all-feature Logistic Regression baseline. This indicates that the model's probabilities contain meaningful ranking information. However, the experiment does not show whether the improvement comes from removing RFE, dropping features above 50% missingness, adding missing indicators, or their interaction.

### Decision

- Reject the pipeline as a classifier at the default threshold.
- Retain it only as a probability-ranking candidate for possible later threshold analysis.
- Do not interpret it as evidence that removing RFE improved performance.
- For a controlled no-RFE comparison, restore the 80% missingness threshold and disable missing indicators while keeping the remaining pipeline settings unchanged.
- Complete the planned representation screen with balanced Logistic Regression before further Random Forest tuning.

## Model 5: Balanced Regularized Random Forest without RFE or Imputation

### Pipeline configuration

This run applies the 50% missingness filter and absolute Spearman correlation pruning at 0.90, then passes the remaining missing values directly to the balanced regularized Random Forest. It uses no RFE, imputation, missing indicators, scaling, or PCA. The successful fit confirms that the installed Random Forest implementation accepts the remaining missing values.

### Cross-validation results

| Metric | Mean | Standard deviation | Interpretation |
|---|---:|---:|---|
| Balanced accuracy | 0.5000 | 0.0000 | Exactly the always-one-class balanced reference. |
| Balanced error rate | 0.5000 | 0.0000 | No useful default-threshold class separation. |
| Failure recall | 0.0000 | 0.0000 | No validation failures were detected. |
| False-negative rate | 1.0000 | — | Every validation failure was missed. |
| Failure precision | 0.0000 | 0.0000 | No positive failure predictions were produced. |
| Failure F1 | 0.0000 | 0.0000 | Failure classification failed completely at the default threshold. |
| Average precision | 0.1988 | 0.0524 | The probability ranking contains signal, but classifications remain unusable. |

### Interpretation and decision

Removing imputation does not solve the Random Forest's failure-detection problem. Average precision is 19.88%, compared with 20.86% in the prior imputation-and-indicator run. That difference is small relative to fold variability and does not establish a meaningful advantage for either missing-value strategy.

Reject this configuration at the default threshold. Retain it only as evidence that native missing-value handling is technically feasible in the installed environment. Do not continue varying Random Forest preprocessing until the controlled Logistic Regression representation screen is complete.

## Model 6: Balanced Regularized Random Forest with ANOVA Top 100

### Pipeline configuration

This run applies the 80% missingness filter, median imputation, ANOVA `SelectKBest` with `f_classif` and `k=100`, standardization, no PCA, and the balanced regularized Random Forest. The selector is inside the pipeline and is therefore relearned within every cross-validation fold.

Standardization is unnecessary for Random Forest and can be removed in future tree-only runs, although it does not explain the predictive result. This experiment uses Random Forest rather than the balanced Logistic Regression specified for the controlled representation screen.

### Cross-validation results

| Metric | Mean | Standard deviation | Interpretation |
|---|---:|---:|---|
| Balanced accuracy | 0.5068 | 0.0159 | Only slightly above the chance reference. |
| Balanced error rate | 0.4932 | 0.0159 | Default-threshold balanced error remains near chance. |
| Failure recall | 0.0147 | 0.0316 | Approximately 1.5% of validation failures are detected. |
| False-negative rate | 0.9853 | — | Approximately 98.5% of validation failures are missed. |
| Failure precision | 0.1800 | 0.3709 | Failure alerts are extremely rare and unstable across folds. |
| Failure F1 | 0.0269 | 0.0573 | Failure classification remains ineffective. |
| Average precision | 0.1911 | 0.0652 | Probability ranking contains signal but is variable and below the best prior RF ranking result. |

### Interpretation and decision

ANOVA top-100 selection does not make the standard 0.50 Random Forest threshold useful. Recall remains approximately 1.5%, and the very large precision standard deviation indicates that a few rare positive predictions dominate the mean.

Average precision of 19.11% is above the 6.62% failure prevalence, but it does not improve on the 20.86% observed in the earlier Random Forest missingness-aware experiment. Because the classifier differs from the all-feature Logistic Regression baseline, this run does not establish whether ANOVA top 100 is better than all 460 features.

Reject this configuration as a default-threshold classifier. Retain the ANOVA selector for the planned controlled Logistic Regression comparison, using the same pipeline structure with the baseline classifier.

## Model 7: Optuna-Tuned ANOVA and Classifier Search

### Search design

Optuna completed 50 trials using a fixed, shuffled five-fold stratified cross-validation split and mean average precision as the objective. Each trial learned the 80% missingness filter, median imputation, and ANOVA feature selection entirely within its training folds. The search compared 40, 70, and 100 selected features across balanced Logistic Regression, balanced Random Forest, and balanced HistGradientBoosting. The test set was not used.

The best tuning result was a mean average precision of 0.23085. Its configuration was:

- ANOVA `SelectKBest(f_classif, k=100)`.
- Random Forest with 500 trees, maximum depth 10, minimum split size 12, minimum leaf size 8, logarithmic feature sampling, balanced subsampling, and bootstrap sampling.

All ten highest-ranked trials used Random Forest and 100 features. Five trials tied at 0.23085. These ties are not independent confirmations: with a minimum leaf size of 8, the tested minimum split sizes of 6, 8, and 12 are below the effective sample requirement for producing two valid leaves and therefore do not change the fitted trees. Duplicate trials also used identical parameters.

### Repeated cross-validation confirmation

The winning pipeline was then evaluated with five-fold repeated stratified cross-validation, repeated five times.

| Metric | Mean | Standard deviation | Interpretation |
|---|---:|---:|---|
| Balanced accuracy | 0.5084 | 0.0212 | Only slightly above the chance reference. |
| Balanced error rate | 0.4916 | 0.0212 | Default-threshold balanced error remains near chance. |
| Failure recall | 0.0196 | 0.0414 | Approximately 2.0% of validation failures are detected. |
| False-negative rate | 0.9804 | — | Approximately 98.0% of validation failures are missed. |
| Failure precision | 0.1867 | 0.3781 | Positive predictions are extremely rare and unstable. |
| Failure F1 | 0.0349 | 0.0732 | Default-threshold failure classification remains ineffective. |
| Average precision | 0.2000 | 0.0627 | Ranking signal is about three times the 6.62% failure prevalence, but remains unstable. |

### Interpretation

The repeated-validation average precision of 0.2000 is substantially lower than Optuna's best fixed-split value of 0.23085. This is expected after selecting the best of 50 trials against one cross-validation partition: the winning objective is optimistically biased toward that partition. Repeated validation provides the more cautious estimate, although it is still not a fully unbiased nested-cross-validation estimate because the same training dataset informed hyperparameter selection.

The confirmed ranking result is not clearly better than the earlier no-RFE Random Forest results of 0.2086 and 0.1988; all differences are small relative to their fold-to-fold standard deviations. It is, however, above the all-feature Logistic Regression baseline of 0.1539. The model therefore contains useful failure-ranking information, but it still predicts almost every observation as passing at the default 0.50 threshold.

The search consistently favors 100 ANOVA-selected features rather than 40 or 70 among its strongest trials. This suggests that aggressively reducing this dataset to 40 features sacrifices useful distributed signal under the tested approach. It does not prove that these exact 100 variables are stable across resamples, nor does it establish a final top-40, top-30, or top-20 set.

### Decision

- Retain this pipeline as the leading tuned ranking candidate, not as a deployable default-threshold classifier.
- Use the repeated-CV result, not 0.23085, as the realistic performance estimate.
- Do not evaluate additional alternatives on the test set.
- Before selecting the final process variables, measure how frequently each ANOVA feature is selected across resamples; a single full-training top-100 list may be unstable.
- If a predictive failure-screening model remains in scope, select an operating threshold from out-of-fold training predictions and report the recall/false-positive tradeoff. Threshold tuning will not change average precision, but it can convert the ranking signal into actionable alerts.
- Treat 100 features as the strongest tested size. Any final 40-, 30-, or 20-feature deliverable should be presented as an interpretability-constrained shortlist rather than the empirically best predictive representation.

## Future Model Entries

For each new pipeline, add:

1. Feature representation and retained feature count.
2. Preprocessing, selector, reducer, and classifier configuration.
3. Cross-validation means and standard deviations.
4. Comparison with the all-feature baseline and current leading pipeline.
5. Failure-screening interpretation and operational tradeoffs.
6. Evidence of stability or overfitting.
7. A clear decision: reject, retain for comparison, or advance as a finalist.
