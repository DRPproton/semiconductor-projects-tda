# Phase 3: Initial Dataset Inspection

**Goal:** Understand fields, labels, sizes, and usable subsets.

**Tasks:**

- Load metadata and inspect the first records.

- Identify waferMap/image array, dieSize, lotName, waferIndex, train/test label, and failureType if present.

- Count labeled and unlabeled maps.

- Count maps per defect class.

- Inspect map dimensions and identify whether dimensions vary.

- Sample visual examples from each class.

**Expected output:** Dataset Overview section.

**Key question:** What exactly is one row/map in this dataset?

**Stop condition:** You have a labeled-class count table and example plots.

---

## Response: Dataset Overview

### Dataset structure

The loaded WM-811K dataset contains **811,457 rows and six original columns**. One row represents one inspected wafer and combines its spatial die map with wafer-level metadata.

| Field | Interpretation in this project |
|---|---|
| `waferMap` | Two-dimensional array describing the state of each position on one wafer |
| `dieSize` | Wafer-level die-count/size metadata supplied by the dataset |
| `lotName` | Manufacturing lot identifier |
| `waferIndex` | Wafer identifier within its lot |
| `trianTestLabel` | Training/test designation supplied by the source; the column name is misspelled in the original data |
| `failureType` | Original nested failure-pattern label |
| `Label` | Cleaned label created during inspection |

The inspected map contains the categorical values `0`, `1`, and `2`, visualized as background, good die, and failed die. These values should be treated as categories rather than continuous image intensity.

### Label availability and class distribution

The cleaned `Label` column contains two values that pandas prints as `None`, but they have different meanings:

- The string `"None"` is a valid labeled class meaning that no named defect pattern was assigned.
- Python `None` is a missing label and therefore represents an unlabeled wafer.

This distinction must be preserved in later processing. Clear internal names such as `No pattern` and `Unlabeled` would prevent accidental mixing.

| Label status | Maps | Share of all maps |
|---|---:|---:|
| Labeled, no named pattern (`"None"`) | 638,507 | 78.69% |
| Labeled, one of eight defect classes | 25,519 | 3.14% |
| Unlabeled (`None`) | 147,431 | 18.17% |
| **Total** | **811,457** | **100.00%** |

The total labeled population is **664,026 maps (81.83%)**. Within that labeled population, the no-pattern class accounts for **96.16%**, confirming that a direct nine-class experiment would be dominated by this class.

For the initial supervised experiment defined in Phase 2, the usable eight-class defect subset contains **25,519 maps**:

| Defect class | Maps | Share of defect subset |
|---|---:|---:|
| Edge-Ring | 9,680 | 37.93% |
| Edge-Loc | 5,189 | 20.33% |
| Center | 4,294 | 16.83% |
| Loc | 3,593 | 14.08% |
| Scratch | 1,193 | 4.67% |
| Random | 866 | 3.39% |
| Donut | 555 | 2.17% |
| Near-full | 149 | 0.58% |
| **Total** | **25,519** | **100.00%** |

The defect subset is strongly imbalanced. `Edge-Ring` contains almost 65 times as many samples as `Near-full`. Later evaluation must therefore use stratified or group-aware splitting and class-sensitive metrics such as macro F1, balanced accuracy, and per-class recall rather than accuracy alone.

### Map dimensions

The complete dimension scan found **632 distinct wafer-map shapes**, so map dimensions and aspect ratios vary substantially across the dataset. The maps cannot be stacked directly into one fixed-size image tensor without an explicit transformation.

This result supports two separate representations in the next phase:

- Preserve the original grid and convert failed dies to normalized coordinates for spatial, geometric, and topological analysis.
- If a CNN baseline is used later, create a separate resizing or padding workflow and verify that it does not distort the spatial signature.

### Visual inspection of the classes

Four reproducible examples were sampled for each labeled class. The gallery confirms that the labels generally correspond to recognizable spatial structures:

- `None`: mostly dispersed failures without one dominant named geometry, although failure density varies.
- `Loc`: compact local failure regions whose position varies across wafers; some maps also contain scattered noise.
- `Edge-Loc`: localized clusters concentrated near part of the wafer boundary.
- `Center`: failures concentrated around the central region, often with additional isolated failures.
- `Edge-Ring`: failures concentrated around the outer rim; rings may be incomplete or noisy.
- `Scratch`: narrow, elongated paths with varying orientation and curvature.
- `Random`: broadly dispersed failures without a single compact location or stable direction.
- `Near-full`: failed dies occupy almost the entire valid wafer area.
- `Donut`: an annular interior pattern surrounding a comparatively clear center; examples vary in completeness and thickness.

The examples also show meaningful within-class variation in map resolution, failure density, noise, position, and pattern completeness. This makes the project more than a simple template-matching problem. Geometry should help describe position, radial concentration, edge proximity, elongation, and density, while TDA may add information about connectivity and persistent loops. Neither representation should be assumed sufficient on its own before the comparative experiments.

### Phase decisions

1. Use one wafer map as the unit of analysis and prediction.
2. Use the **25,519 labeled defect maps** for the initial eight-class supervised workflow established in Phase 2.
3. Keep `"None"` (no named pattern) separate from missing `None` (unlabeled); do not silently combine them.
4. Exclude unlabeled maps from supervised training, while retaining them as a possible future dataset for unsupervised or semi-supervised work.
5. Preserve `lotName` for group-aware splitting and leakage checks, not as a predictor.
6. Preserve original map geometry for the spatial/TDA branch because the 632 observed shapes rule out direct stacking without preprocessing.
7. Treat the sampled maps as descriptive evidence only; spatial appearance can support a defect-signature label but cannot establish a physical manufacturing root cause.

### Answer to the key question

One row is one wafer inspection: a categorical two-dimensional die map plus its die-size, lot, wafer index, source split, and failure-label metadata. The `waferMap` is therefore both the primary analytical object and the source from which spatial, geometric, topological, and image-based features will be derived.

### Phase status

Phase 3 is complete. The notebook contains the required dataset inspection, class counts, full map-dimension inventory, and example galleries for every labeled class. Phase 4 can now define representations that preserve these observed spatial structures while handling variable map sizes.
