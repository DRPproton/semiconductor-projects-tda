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
