# Phase 5: Process-Oriented Exploratory Data Analysis

**Goal:** Explore the remaining anonymous measurements as process/sensor signals and identify behavior patterns that merit later validation.

## Technical Summary

Phase 5 produced a process-signal taxonomy for all 460 measurements retained after the earlier cleaning decisions. The dataset does not contain a single feature that cleanly separates passing and failing observations. Instead, it contains moderate pass/fail shifts, heavier failure tails, extensive skew, and substantial redundancy across feature families.

Thirty-eight measurements were identified as exploratory process-signal candidates. Thirty-seven have a standardized pass/fail mean difference of at least 0.30, two place at least 25% of observed failures outside the central 90% of the passing distribution, and feature `64` satisfies both rules. These are investigation candidates rather than final selected features or evidence of process causation.

## Process-Signal Taxonomy

The taxonomy labels are intentionally non-exclusive. A feature may be skewed, outlier-heavy, target-associated, and redundant at the same time.

| Behavior group | Definition | Features | Percentage |
|---|---|---:|---:|
| Missing-heavy | At least 50% missing | 20 | 4.35% |
| Low-information / rare-state | One value represents at least 98% of observed values | 4 | 0.87% |
| Highly skewed | Absolute skew of at least 2 | 259 | 56.30% |
| Outlier-heavy | At least 10% of observed values outside the Tukey IQR bounds | 28 | 6.09% |
| Pass/fail-shifted | Absolute standardized mean difference of at least 0.30 | 37 | 8.04% |
| Failure-extreme | At least 25% of failures outside the pass 5th–95th percentile range | 2 | 0.43% |
| Highly redundant | Absolute Spearman correlation of at least 0.95 | 263 | 57.17% |

The largest categories are highly skewed and highly redundant signals. This means that standard mean-based summaries and independent-feature interpretations are insufficient for much of the dataset. Robust statistics, distribution plots, and redundancy-aware feature selection are needed in later phases.

## Pass/Fail Distribution Findings

The largest absolute standardized mean differences were observed for:

| Feature | Standardized mean difference | Failure coverage | Interpretation |
|---:|---:|---:|---|
| `59` | 0.632 | 104 of 104 | Strongest observed shift; failures tend toward higher values and a wider right tail. |
| `103` | 0.614 | 104 of 104 | Comparatively clear location shift with substantial class overlap. |
| `510` | 0.533 | 104 of 104 | Higher failure values, but the distribution is strongly right-skewed. |
| `348` | 0.523 | 104 of 104 | Combines a mean shift with a 23.08% failure-extreme rate. |
| `111` | -0.504 | 30 of 104 | Potentially interesting but low-support because the feature is 64.96% missing. |

The twelve inspected pass/fail plots confirm that the distributions overlap substantially. Therefore, these measurements may contribute to a multivariable failure-screening model, but none should be described as a standalone failure detector.

Features `59`, `210`, `294`, `299`, and `348` appeared in both the top pass/fail-shift and top failure-extreme ranking lists. This agreement makes them useful investigation candidates, although the intersection is based on top-30 rankings rather than formal statistical validation.

## Failure-Extreme Behavior

Features `64` and `65` had the largest failure-extreme rate: 28.85% of observed failures fell outside the passing population's 5th–95th percentile interval. Both features had complete failure-class coverage.

Feature `64` also met the pass/fail-shift threshold, while feature `65` had a smaller standardized mean difference of approximately 0.22. This shows why mean separation and tail behavior answer different questions: a feature may have similar central values across classes while failures occur more often in unusual ranges.

## Availability and Reliability

Twenty-seven of the 30 heuristic-shortlist features were observed for at least 103 of the 104 failures, so most shortlist comparisons have strong class coverage. Three require additional caution:

- Feature `111` was observed for only 30 failures (28.85%) and is classified as low-support.
- Feature `247` was observed for 71 failures (68.27%) and 53.38% of passes; its availability differs by class and may itself contain information.
- Feature `562` was observed for 80 failures (76.92%) and 82.98% of passes; it appears more consistent with a complex or regime-like signal than a strong mean shift.

Sparse features remain visible in the taxonomy, but they are not promoted to the primary engineering shortlist without later stability testing.

## Low-Information and Rare-State Signals

Features `114`, `249`, `387`, and `521` are complete but dominated by zero in approximately 98.6% of observations. Their nonzero variation occurs in only about 21–22 production observations.

These measurements are classified as low-information or rare-state signals rather than automatically removed. Their rare nonzero states could represent unusual measurement or process conditions, but the available data does not establish that interpretation.

## Redundancy and Signal Families

Spearman screening identified 224 highly correlated pairs involving 263 features. Several relationships were exact or nearly exact, including `578`/`586`, `581`/`589`, `580`/`588`, `579`/`587`, and `249`/`387`. Features `34` and `36` had a perfect inverse monotonic relationship.

These relationships suggest duplicated transformations, coordinated measurements, or shared process behavior. Because the variables are anonymous, correlation cannot establish that two features originate from the same physical sensor, tool, or process step. Correlated features will be grouped during feature selection, but they will not be removed arbitrarily during EDA.

## Methods and Definitions

- Standardized mean difference compares failure and passing means using their pooled standard deviation. Its sign gives direction; its absolute value gives separation magnitude.
- Failure-extreme rate uses the passing distribution's 5th and 95th percentiles as reference limits and measures the percentage of observed failures outside those limits.
- Tukey outliers are observations below Q1 − 1.5 × IQR or above Q3 + 1.5 × IQR.
- Spearman correlation was selected because it is less dependent on linearity and is more appropriate than Pearson correlation for strongly skewed measurements. Correlations required at least 100 paired observations.
- Failure support is classified as low below 50%, moderate from 50% to below 90%, and high at 90% or above.

The additive EDA priority score is retained only as a heuristic for plot selection. It combines quantities with different scales and meanings and will not be used as a validated feature-selection score.

## Limitations and Uncertainty

- Feature names, units, specifications, tool context, and process stages are unavailable, so the analysis cannot identify physical root causes.
- Only 104 failure observations are available. Effects based on sparse features may be unstable.
- Examining 460 features creates multiple-comparison risk; some observed differences may occur by chance.
- High skew and extreme observations can influence mean-based effect sizes.
- Correlation describes shared behavior, not causal or physical equivalence.
- This EDA uses the full dataset for descriptive investigation. Any learned feature-selection or preprocessing decision used to estimate model performance must be repeated within the training folds during cross-validation.

## Phase 5 Decisions and Rationale

- The 38 candidate process signals are treated as hypotheses for Phase 6, not final selected features.
- Features `59`, `103`, `210`, `348`, and `510` receive priority because they combine meaningful effects with complete failure coverage.
- Feature `111` remains visible but is labeled low-support.
- Features `247` and `562` remain availability-sensitive candidates.
- Features `114`, `249`, `387`, and `521` are retained as low-information/rare-state signals rather than automatically removed.
- Highly correlated features are grouped as redundant signal families; no automatic correlation-based deletion is made in this phase.
- Skew and overall outlier rate describe distribution behavior and are not treated as failure relevance by themselves.
- Phase 6 will independently benchmark feature relevance and selection stability, with all learned decisions performed inside cross-validation when model performance is evaluated.

## Next Step

Proceed to the feature-selection benchmark. Compare reproducible top-40, top-20, and top-10 feature sets across statistical and model-based ranking methods, then examine method overlap, correlated groups, missingness, and selection stability.

**Key question answered:** Several measurements behave differently between passing and failing observations, but the evidence supports a multivariable, redundancy-aware investigation rather than a single-feature failure explanation.

**Stop condition:** Completed. The notebook contains a 460-row process-signal taxonomy with behavior, support, association, and redundancy labels.
