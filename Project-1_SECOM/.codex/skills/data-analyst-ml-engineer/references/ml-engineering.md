# Machine-Learning Engineering Workflow

Use this reference for predictive modeling, segmentation or anomaly detection, feature pipelines, evaluation, packaging, and inference.

## Define the learning problem

Specify the prediction target or unsupervised objective, unit of prediction, eligible population, observation cutoff, prediction horizon, action enabled by the output, and error costs. Confirm that labels and candidate features would actually be available at inference time.

## Design validation before modeling

- Choose random, stratified, grouped, temporal, or nested validation based on how future predictions will be made.
- Hold out a final test set when model selection is substantial. Do not repeatedly tune against it.
- Keep related entities, near-duplicates, batches, sessions, or future records from crossing boundaries.
- Put all learned preprocessing inside the fitted pipeline. Apply resampling only within training folds.
- Compare split distributions and investigate suspiciously large validation gains as possible leakage.

## Build from a baseline

Start with a naive policy and a simple interpretable model. Add complexity only when validation shows a meaningful gain relative to operational costs. For imbalance, report class prevalence and use suitable metrics such as precision-recall measures, class-specific recall, cost-weighted utility, or calibrated decision curves rather than accuracy alone.

Feature engineering should follow domain and availability constraints. Track feature lineage, handle missingness explicitly, and avoid identifiers or post-outcome fields that act as proxies for the label. Use dimensionality reduction or selection within cross-validation when it is learned from data.

## Tune and evaluate

- Select hyperparameters using training/validation data with a bounded search appropriate to dataset size and compute budget.
- Report variability across folds, seeds, time windows, or relevant subgroups when instability would affect use.
- Evaluate calibration and threshold behavior when probabilities drive actions. Choose the threshold from costs or capacity constraints, not the default value by habit.
- Review confusion patterns, residuals, slices, drift-sensitive features, and failure cases.
- Use explanation methods as diagnostic evidence, not proof of causality. Check whether explanations are stable and plausible.

If comparing models, use identical splits and preprocessing assumptions. Prefer the simplest model whose performance, latency, interpretability, robustness, and maintenance profile satisfy the use case.

## Make the system reproducible

Package preprocessing and prediction together when possible. Persist the model with schema, feature order, training-data snapshot or version, code version, dependencies, seeds, metrics, and threshold. Validate serialization by loading the artifact and reproducing predictions on a small fixture.

For inference, define behavior for missing columns, new categories, type changes, out-of-range values, and unavailable dependencies. Add checks for schema, output shape, finite values, probability bounds, and deterministic behavior where expected.

## Production readiness

Only add deployment or monitoring work when it is requested or needed by the deliverable. When relevant, specify latency and throughput needs, batch versus online semantics, retraining triggers, rollback strategy, ownership, and monitoring for input quality, drift, calibration, performance, and decision outcomes. A model is not production-ready merely because it has been serialized.

## Completion checks

Report the baseline, selected model, validation scheme, final metrics with uncertainty, threshold, important failure modes, and leakage checks. Provide a rerunnable training/evaluation entrypoint and verify that a fresh process can load the artifact and perform inference.
