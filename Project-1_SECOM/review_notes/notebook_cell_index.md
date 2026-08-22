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
