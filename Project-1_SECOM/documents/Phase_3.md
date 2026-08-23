# Phase 3: Missingness as Process Information

**Goal:** Handle missing values without destroying possible engineering signal.

**Tasks:**

- [x] Calculate missing percentage per feature.

- [x] Flag very high missingness features.

- [x] Compare missingness rates between pass and fail groups.

- [x] Think about which features to drop and which to impute.

- [x] Add missing-value indicators only when missingness appears informative.

- [x] Document every cleaning decision.

**Expected output:** Data Cleaning Strategy and Missingness Report.

**Key question:** Is missingness random noise, process route information, or data-collection behavior?

**Stop condition:** Cleaning decisions are documented and reproducible.

## Phase 3 Decisions and Rationale

- **Data-quality assessment:** No duplicate observations were found. After Phase 2 feature removal, the working dataset contained 468 numerical process features, one pass/fail label, and one timestamp. The timestamp was converted to a datetime value for possible time-aware analysis later in the project.

- **Missingness structure:** Twenty-eight process features were more than 50% missing. Missingness often occurred in coordinated feature blocks, and row-level verification confirmed that several groups were missing in exactly the same observations. This suggests shared measurement availability, process routing, or data-collection behavior, although the anonymized data cannot identify the physical cause.

- **Leakage assessment:** No feature was missing exclusively for failures, missing for every failure, or an exact match for the failure label. Missingness therefore does not provide an obvious direct target-leakage signal. However, several retained blocks have materially different missingness rates between passing and failing observations and remain candidates for later evaluation.

- **High-missingness removal:** We selected a strict removal threshold of more than 80% missingness. This removes features `157`, `158`, `292`, and `293`, which are 91.19% missing, and features `85`, `220`, `358`, and `492`, which are 85.58% missing. These features contain too few observed failures for stable distribution estimates, and the features within each group share identical missingness patterns. Removing them reduces sparsity, redundancy, and overfitting risk without discarding a strong unique missingness signal.

- **Retained sparse features:** Features below the 80% threshold were retained for now. In particular, the approximately 65%-missing block still contains 549 observed examples, while the approximately 46%-51%-missing groups show some of the largest pass/fail missingness differences. Removing these groups solely because they are sparse could discard useful process-availability information.

- **Imputation and indicators:** Remaining numerical missing values will be median-imputed inside the modeling pipeline so that imputation statistics are learned only from each training fold. Missingness indicators will be treated as model features only when the pattern is plausibly informative. For groups with identical missingness masks, one shared block indicator should be evaluated instead of adding redundant indicators for every feature.

- **Resulting feature set:** The eight-feature removal decision leaves 460 numerical process features for subsequent analysis. The label and timestamp remain separate, producing a 462-column working dataset. The 80% removal rule must be applied inside the preprocessing pipeline during model evaluation to prevent information from validation folds influencing feature removal.

These findings describe associations in measurement availability. They do not establish that missing measurements, process routes, or metrology decisions caused yield failure.
