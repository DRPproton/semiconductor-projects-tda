# Phase 5 Code Review (Guide Phase 6)

## Phase mapping

The project combines the guide's Phase 1 (dataset setup) and Phase 2 (problem framing). Therefore:

- Project Phase 5 = Guide Phase 6: Process-Oriented EDA.
- Project Phase 6 = Guide Phase 7: Feature Selection Benchmark.

## Review scope

Reviewed:

- `guide.md`
- `documents/Phase_5.md`
- `notebooks/notebook.ipynb`
- `notebooks/helpers.py`
- `notebooks/missing_features_helper.py`
- Earlier phase documents and the project README for upstream decisions

## What the current EDA code does well

- Loads and merges 1,567 rows, 590 anonymous numeric measurements, the label, and timestamp.
- Confirms 1,463 pass examples and 104 fail examples.
- Removes 116 constant and 6 selected near-constant measurements before the current EDA report.
- Builds a 468-feature EDA report with availability, distribution, spread, skew, Tukey outlier, pass/fail, standardized mean difference, and failure extreme-range statistics.
- Defines the normal extreme range from the pass population's 5th and 95th percentiles.
- Produces candidate lists for pass/fail shifts, failure extremes, skew, and outlier rate.
- Flags 43 candidate process signals using pass/fail shift or failure-extreme criteria.
- Plots 12 selected pass/fail distributions.
- Uses association/screening language instead of making causal root-cause claims.

## Phase completion decision

The calculation layer is substantially complete, but the phase stop condition is not complete yet. The guide requires a process-signal taxonomy table and an Exploratory Data Analysis section. The notebook currently has partial flags and rankings, but not a complete taxonomy or written synthesis.

## Required gaps before closing this phase

1. Create one reproducible process-signal inventory table covering all 590 numeric measurements. Constant and near-constant measurements should remain visible in this inventory even if they are excluded from later modeling.
2. Add the missing behavior groups: constant, near-constant/low-information, missing-heavy, skewed, outlier-heavy, pass/fail-shifted, failure-extreme, and correlated/redundant.
3. Do not label a signal as "noisy" from this dataset alone. Without repeated measurements, specifications, or sensor precision, use observable descriptions such as high-variability, outlier-heavy, or weakly associated.
4. Add correlation/redundancy analysis. Prefer Spearman correlation for the heavily skewed features, create highly correlated groups, and select a documented threshold such as absolute correlation >= 0.95 for screening.
5. Add sample-support columns and reliability rules. Several highly ranked features are 65% to 91% missing, so large effects may be based on very few observed failures. At minimum include observed pass/fail counts and flag low-support estimates.
6. Replace the current additive `eda_priority_score` or clearly label it as a heuristic. It adds effect size, failure-extreme rate, and overall outlier rate with equal weight; outlier prevalence is not necessarily failure relevance and can promote unstable signals.
7. Improve plots for skewed and extreme-valued features. Raw histograms with KDE can hide class behavior; use robust axis limits or log transforms where valid, and pair them with ECDF, box/violin, or quantile summaries.
8. Write a concise EDA conclusion answering which variables differ, which findings are reliable, which are sparse, and which should proceed only as Phase 6 feature-selection candidates.
9. Save the inventory and shortlist to `reports/` or `clean_data/`, and save a small curated figure set for the report.

## Upstream technical debt that affects the next phase

- Notebook cell 65 compares the numeric missing-rate difference to Boolean `True`, so its reported count of zero is not a valid missingness comparison. Use an explicit magnitude threshold and/or a statistical association test.
- The missingness phase states that no decision was made, while the reusable dropper defaults to a 50% threshold. This must become a documented experimental choice rather than an implicit final decision.
- The notebook execution counts are out of order and the final cell is blank. Restart-and-run-all verification is needed before using its outputs as reproducible evidence.
- There is no environment specification (`requirements.txt`, `pyproject.toml`, or environment file). The current review runtime did not contain scikit-learn, so a clean rerun cannot yet be reproduced from the repository alone.
- The README and summary say "591 real-valued features." The raw measurement matrix has 590 numeric columns; timestamp can be described separately as an additional predictor/context field.
- The repository does not yet contain the guide's suggested `figures/`, `src/`, and `references/` structure, and `reports/` and `clean_data/` do not contain the Phase 5 outputs.

## Recommended decisions

### Missingness

Do not permanently discard every feature above 50% missing before benchmarking. Treat missingness threshold as a feature-selection/modeling experiment (for example, 50%, 70%, and 90%) performed inside cross-validation. Always compare against a conservative baseline and preserve missingness indicators only where they add validated value.

### EDA versus feature selection

The 43 EDA candidates are a hypothesis shortlist, not the final top feature set. Phase 6 should independently benchmark statistical and model-based selectors, then compare method overlap and stability.

### Correlation

Use correlated groups to describe redundancy, but do not automatically remove all correlated signals before the benchmark. For compact feature sets, retain one representative per stable group using a documented rule.

### Sparse high-ranked signals

Keep sparse signals visible, but separate them into a "sparse candidate" group. Require sufficient observed failures and cross-validation stability before promoting them to the engineering-review shortlist.

## Recommended next-phase sequence

1. Close this phase by generating the complete taxonomy, correlation groups, curated plots, saved outputs, and written EDA conclusion.
2. Fix the missingness comparison and document threshold experiments.
3. Add an environment file and verify the notebook with a clean restart/run-all.
4. Begin project Phase 6 / guide Phase 7 with leakage-safe feature-selection benchmarks.
5. Compare signal-to-noise, t-test, F-test, Pearson correlation, mutual information (optional), model importance, and permutation importance.
6. Produce reproducible top 40, top 20, and top 10 sets, method-overlap tables, and selection-stability summaries.
7. Keep all learned preprocessing and selection inside each cross-validation training fold when model performance is evaluated.

## Validation performed in this review

- Notebook JSON loaded successfully: 109 cells and no stored error outputs.
- Both Python helper files passed syntax parsing.
- Stored notebook outputs were checked against the code and phase requirements.
- A full clean notebook execution was not possible because the repository has no declared environment and the available review runtime does not include scikit-learn.
