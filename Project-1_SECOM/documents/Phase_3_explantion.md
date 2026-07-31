# Missingness by Target Report

## Overall conclusion 

There is **no obvious missingness leakage** in the data. None of the leading features has missingness that perfectly matches the failure label, and the flags `all_fails_missing`, `missing_only_when_fail`, `perfect_failure_missing_signal`, and `exact_match_fail_flag` are `False` in the reported rows. That is good: missingness does not appear to be simply reproducing the target. 

However, there are several **groups of features with coordinated missingness**, and some groups differ between pass and fail examples. Those groups may reflect shared measurement steps, process routes, tools, or data-collection systems.

## 1. Features 109–111, 244–246, 382–384, and 516–518

These features all show the same summary:

* Pass missing rate: **64.52%**
* Fail missing rate: **71.15%**
* Difference: **+6.63 percentage points**
* Failures among missing rows: **7.27%**

The overall dataset failure rate is approximately:

[
\frac{104}{1567} \approx 6.64%
]

Therefore, the failure rate among rows where these features are missing—7.27%—is only slightly higher than the overall 6.64% failure rate.

### Interpretation

These columns are missing a lot, but the missingness is only weakly associated with failure. They may represent a block of measurements collected together, perhaps from the same process stage or route.

Because approximately 65% of their values are missing, they are difficult to use reliably as numerical features. I would not automatically remove them yet, but they are candidates for:

* high-missingness review,
* one shared missingness indicator,
* or removal if their observed values provide little additional information.

A simple Fisher exact test using these counts gives a raw (p)-value of approximately **0.20**, so this missingness difference is not strong evidence by itself.

## 2. Features 562–569

These are more interesting:

* Pass missing rate: **17.02%**
* Fail missing rate: **23.08%**
* Difference: **+6.06 percentage points**
* Failures among missing rows: **8.79%**

Unlike the previous group, these features still contain values for most observations.

### Interpretation

This is probably the most reasonable positive missingness candidate in the visible results. When these measurements are missing, the failure share increases from the baseline of approximately 6.64% to 8.79%.

That is not a dramatic separation, but it may indicate:

* a measurement block skipped more often for failed entities,
* a process route associated with somewhat higher failure risk,
* a shared sensor or metrology availability condition,
* or a production state associated with both missing measurements and failure.

I would:

1. Retain these features initially.
2. Impute their numerical values inside the modeling pipeline.
3. Add a missingness indicator.
4. Test whether the indicator improves cross-validated failure detection.

The raw Fisher exact (p)-value is approximately **0.14**, so the association should still be treated as exploratory.

## 3. Features 85, 220, 358, and 492

These features have:

* Pass missing rate: **85.30%**
* Fail missing rate: **89.42%**
* Difference: **+4.12 percentage points**
* Failures among missing rows: **6.94%**

### Interpretation

The failure share among missing rows is almost identical to the overall failure rate. At the same time, approximately 86% of the values are missing.

These are strong candidates for removal because:

* they contain very little observed data,
* their missingness barely separates pass from fail,
* and the missing rows do not show meaningful failure enrichment.

Before removing them, inspect whether the small number of observed values is unusually informative. Otherwise, these features likely add more instability than useful information.

## 4. Features 157, 158, 292, and 293

These are missing in more than 91% of the observations:

* Pass missing rate: **91.11%**
* Fail missing rate: **92.31%**
* Difference: **+1.19 percentage points**
* Failures among missing rows: **6.72%**

### Interpretation

These appear largely uninformative from a missingness perspective.

Their failure share among missing rows is nearly identical to the overall failure rate, and the difference between pass and fail missingness is negligible.

These are your strongest removal candidates, subject to checking whether their few observed values contain exceptional signal.

## 5. Features with only two missing values

Several groups, including features 21–31 and related blocks, have:

* One missing pass row
* One missing fail row
* Two missing rows total
* `fail_share_among_missing = 50%`

At first glance, 50% appears important. It is not reliable here.

The denominator is only two rows:

[
\frac{1\text{ failure}}{2\text{ missing rows}} = 50%
]

### Interpretation

This is a small-sample artifact. One failure among two missing observations does not provide enough evidence to treat missingness as predictive.

The same issue applies to:

* features with four total missing values and one failure: 25%,
* features with seven total missing values and one failure: 14.29%,
* features with ten total missing values and one failure: 10%.

These percentages look elevated only because the denominators are tiny. Do not create missing indicators solely because of these percentages.

Require a minimum missing count before interpreting `fail_share_among_missing`, such as:

* at least 20 total missing rows, and
* at least 5 missing failure rows.

## 6. Features 546–557

These features have:

* Pass missing rate: **16.54%**
* Fail missing rate: **17.31%**
* Difference: **+0.77 percentage points**
* Failure share among missing rows: **6.92%**

### Interpretation

This looks like general missingness, not failure-specific missingness.

The missing rate is almost the same in both classes. You can retain and impute these features, but a missingness indicator is unlikely to add much value unless later cross-validation proves otherwise.

## 7. Important negative differences

Your report also contains features that are missing **less often among failures**.

Examples include:

### Features 112, 247, 385, and 519

* Pass missing rate: **46.62%**
* Fail missing rate: **31.73%**
* Difference: **−14.89 percentage points**

### Features 72, 73, 345, and 346

* Pass missing rate: **51.81%**
* Fail missing rate: **34.62%**
* Difference: **−17.20 percentage points**

These are actually more interesting statistically than the positive differences shown at the top of the table. 

### Interpretation

For these features, the measurement is more likely to be present in failed entities.

That could indicate:

* a route where these measurements are collected more frequently,
* additional metrology applied to higher-risk production,
* a process stage associated with increased failure risk,
* or a data-collection pattern correlated with failure.

Using the counts shown, simple raw Fisher exact tests give approximately:

* Features 112/247/385/519: (p \approx 0.0031)
* Features 72/73/345/346: (p \approx 0.0008)

These are stronger exploratory findings. However, because you are examining hundreds of features, you must apply a multiple-testing correction such as Benjamini–Hochberg before treating them as statistically significant.

Also remember: a negative missingness difference can be informative. Do not examine only features missing more often in failures. Sort by the **absolute missing-rate difference**.

## 8. Repeated feature groups

Many features have exactly the same missing counts and rates.

Examples include:

* 109–111, 244–246, 382–384, 516–518
* 562–569
* 85, 220, 358, 492
* 157, 158, 292, 293
* 546–557

This strongly suggests that features may have been collected in measurement blocks.

However, identical counts do not necessarily prove that the exact same rows are missing. Verify the row-level missingness masks.

From a process perspective, coordinated missingness may indicate:

* measurements from the same tool,
* variables recorded during the same operation,
* repeated measurement modules,
* a shared process route,
* a metrology step that was skipped or applied as a group.

This is valuable process-structure information even though the features are anonymized.

## Recommended treatment

| Feature group                     | Recommended action                                                        |
| --------------------------------- | ------------------------------------------------------------------------- |
| 157, 158, 292, 293                | Strong removal candidates                                                 |
| 85, 220, 358, 492                 | Likely remove after checking observed-value signal                        |
| 109–111 and related blocks        | Review as a coordinated high-missingness block; test one shared indicator |
| 562–569                           | Retain, impute, and test missingness indicators                           |
| 546–557                           | Retain/impute; missing indicators probably unnecessary                    |
| Tiny-count missingness groups     | Do not interpret as meaningful                                            |
| 72/73/345/346 and 112/247/385/519 | Investigate carefully; missingness differs substantially by class         |
| Zero-missing features             | No missingness action required                                            |

## Final process/yield interpretation

The missingness analysis does not reveal a feature whose missing values perfectly identify failures. That reduces immediate concern about direct target leakage.

The more important result is that missingness occurs in coordinated feature blocks. Some blocks have similar missingness in pass and fail entities and likely represent general data availability. Other blocks—especially features 72/73/345/346 and 112/247/385/519—show materially different missingness between the classes and may reflect process-route, measurement-availability, or metrology-selection differences associated with yield outcome.

These patterns should be treated as candidates for engineering investigation, not as evidence of root cause.
