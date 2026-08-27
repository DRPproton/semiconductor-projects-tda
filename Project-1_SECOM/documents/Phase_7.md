# Phase 7: Leakage-Safe Baseline Modeling and Representation Selection

**Goal:** Determine whether a smaller representation can match or improve the failure-screening performance of all 460 retained measurements, then identify the strongest representation and model candidates without using the untouched test set.

**Tasks:**

- [ ] Finalize and verify the reusable modeling pipeline with optional correlation pruning, imputation, feature selection, scaling, dimensionality reduction, and classification steps.

- [ ] Confirm that every learned preprocessing step is fitted inside each cross-validation training fold to prevent data leakage.

- [ ] Create the six planned feature representations:

  1. All 460 retained features.
  2. Correlation-pruned features using an absolute Spearman threshold of 0.90.
  3. Correlation-pruned features with Random Forest RFE top 40.
  4. Correlation-pruned features with Random Forest RFE top 30.
  5. Correlation-pruned features with Random Forest RFE top 20.
  6. PCA components retaining 95% of the variance from the full retained feature set.

- [ ] Use the same balanced Logistic Regression baseline and identical repeated stratified cross-validation splits to compare all six representations.

- [ ] Record balanced accuracy, balanced error rate, failure recall, false-negative rate, failure precision, failure F1, average precision, and variation across folds.

- [ ] Record the number and names of features retained by correlation pruning and RFE when the final candidate pipelines are fitted on the complete training set.

- [ ] Examine feature-selection stability across validation folds, with particular attention to the small failure-class sample.

- [ ] Select the smallest representation that provides competitive failure detection and stable cross-validation performance relative to all 460 features.

- [ ] Compare balanced Logistic Regression, Random Forest, and HistGradientBoosting only on the strongest one or two representations.

- [ ] Select the final model and representation candidate using cross-validation results, model simplicity, interpretability, and manufacturing-screening risk.

- [ ] Keep the test set untouched for the final manufacturing-focused evaluation.

**Expected output:** A reproducible comparison table for all planned representations, a concise comparison of the three finalist models, the retained feature lists, and a justified final model/representation candidate.

**Key question:** What is the smallest stable feature representation that detects failures competitively without adding unnecessary model complexity or redundant process measurements?

**Stop condition:** One final model and representation are selected using training-only cross-validation, the selection rationale is documented, and the untouched test set has not been used for model or feature-set selection.

## Modeling Design

### Stage 1: Representation screening

Balanced Logistic Regression will act as the controlled baseline for comparing feature representations. Keeping the classifier and validation splits fixed isolates the effect of correlation pruning, RFE, and PCA. The representation decision will not be based on ordinary accuracy because the failure class represents only about 6.6% of the observations.

### Stage 2: Focused model comparison

After the representation screen, only the strongest one or two representations will move forward. Logistic Regression provides an interpretable linear baseline, Random Forest provides a nonlinear tree-based comparison, and HistGradientBoosting provides a second nonlinear alternative. This restricted comparison prevents the project from expanding into an unnecessary search across many models and feature combinations.

### Stage 3: Final-candidate handoff

The final candidate will be chosen from cross-validation evidence only. The untouched test set will be reserved for the next phase, where failure recall, false negatives, false-positive burden, threshold behavior, and final generalization will be evaluated once.

## Decision Rules

- Failure recall and false-negative rate receive priority because missed failures represent the main manufacturing-screening risk.
- Balanced error rate and balanced accuracy measure performance across both classes.
- Average precision summarizes ranking quality under severe class imbalance.
- Failure precision measures the operational burden created by false alarms.
- Fold-to-fold variation is considered alongside mean performance; a small apparent gain is not persuasive if it is unstable.
- If two representations perform similarly, prefer the smaller and more interpretable original-feature representation.
- PCA remains a benchmark rather than the preferred interpretation because its components mix many anonymous process measurements.
- The final test set must not influence feature selection, representation selection, model selection, or threshold selection.

## Planned Phase Report

At the end of the phase, document the completed pipeline design, cross-validation setup, representation comparison, selected features, stability findings, finalist-model comparison, decisions, limitations, and the rationale for the candidate carried into final evaluation.
