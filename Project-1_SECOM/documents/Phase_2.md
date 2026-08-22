## Phase 2: Initial Data Inspection

**Goal:** Understand structure and data-quality problems.

**Tasks:**

- [x] Count rows, columns, pass examples, fail examples, and failure percentage.

- [x] Confirm 1,567 examples, 591 features, and 104 failures.

- [x] Count missing values per feature and per row.

- [x] Identify constant and near-constant features.

- [x] Check duplicate rows and feature types.

- [x] Inspect the timestamp field and decide how to use it later.

~~**Expected output:** Data Overview section.~~

**Key question:** What are the biggest data-quality problems before modeling?

- The number of null values (41951) and the high dimensionality of the dataset

**Stop condition:** You can describe the dataset without reading code.

## Phase 2 Decisions and Rationale

- **Dataset structure:** The merged dataset contains 1,567 observations, 590 anonymized numerical process features, one pass/fail label, and one timestamp. The target contains 1,463 passing observations (93.36%) and 104 failing observations (6.64%), confirming a strongly imbalanced problem.

- **Missing data:** The initial inspection found 41,951 missing values across the process features. Missing values were documented as a major data-quality issue, but their treatment was deferred to the next phase so that possible process or data-collection information would not be removed prematurely.

- **Constant features:** We removed 116 features with only one unique non-missing value. Missing values do not create meaningful signal variation, so these features cannot distinguish passing from failing observations.

- **Near-constant features:** Using a 98% dominance threshold, 10 features were flagged as near-constant. We removed only features `74`, `206`, `209`, `342`, `347`, and `478`. Each contained zero in 1,560 rows, six missing values, and a single nonzero observation. The nonzero value occurred in the same passing observation for all six features, providing no repeatable failure-discrimination evidence and creating an unnecessary overfitting risk. The other four flagged features were retained because they contained more distinct observed values and may still provide useful information in later analysis.

- **Resulting dataset:** Removing 116 constant and six selected near-constant features reduced the analysis matrix to 468 numerical process features. The label and timestamp were retained, resulting in 470 columns for the next phase.
