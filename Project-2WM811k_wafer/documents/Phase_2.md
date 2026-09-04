# Phase 2: Problem Framing

**Goal:** Define the spatial analytics and TDA problem clearly.

**Tasks:**

- Write the business problem: classify and describe wafer spatial defect patterns for yield investigation.

- Write the analytics problem: extract image/spatial/topological features from wafer maps.

- Write the TDA problem: use topology to capture connected regions, loops/rings, and persistent shape patterns.

- Define whether the first version is descriptive, supervised, or both.

- Define success as interpretability plus reasonable pattern separation, not only high accuracy.

**Expected output:** Problem Definition section.

**Key question:** Are we classifying images, describing process signatures, or both?

---

## Response: Problem Definition

### Project decision

This project will do **both classification and process-signature description**. The primary modeling task is supervised multiclass classification of wafer-map defect signatures. Descriptive spatial, geometric, and topological analysis will explain what distinguishes the classes and why a model may have assigned a label. The output is intended to support engineering triage and yield investigation; it is not intended to establish the physical root cause of a defect.

The first complete version will use the **eight labeled defect classes**:

- Center
- Donut
- Edge-Loc
- Edge-Ring
- Loc
- Random
- Scratch
- Near-full

Wafers labeled `None` will be excluded from the initial eight-class experiment so that the dominant non-pattern class does not obscure performance on rare defect signatures. After the eight-class pipeline is stable, the project may add either a nine-class experiment including `None` or a two-stage system that first detects defect versus no defect and then classifies the defect signature.

### Business and engineering problem

Semiconductor test data records which die locations pass or fail across each wafer. The spatial arrangement of failing dies can form recognizable signatures associated with different families of process, equipment, or handling problems. Manually reviewing large numbers of wafer maps is slow and can be inconsistent, while class imbalance makes rare but important signatures easy to miss.

The business problem is therefore:

> Use the spatial distribution of failing dies to consistently classify and describe wafer failure-pattern signatures so that engineers can prioritize wafers for investigation, compare recurring patterns, and accelerate yield-triage workflows.

The system will provide a diagnostic clue rather than a causal conclusion. A predicted ring, center, or scratch pattern may guide an engineer toward relevant process hypotheses, but wafer-map geometry alone cannot prove which tool, recipe, material, or process step caused the pattern.

### Analytics and machine-learning problem

The unit of analysis and prediction is **one wafer map**. Each map is a two-dimensional die grid containing background, passing-die, and failing-die states. Because these are categorical spatial states rather than natural-image colors, preprocessing must preserve the wafer boundary and die categories.

For each eligible labeled wafer, the analytics workflow will:

1. Describe map dimensions, valid-die count, failing-die ratio, lot membership, and class frequency.
2. Characterize within-class and between-class spatial variation using representative galleries and class-level distributions.
3. Extract interpretable spatial and geometric features such as failure density, centroid location, radial and angular distributions, edge concentration, connected-component statistics, elongation, and spatial entropy.
4. Extract topological features that summarize connectivity and loop structure across multiple thresholds or spatial scales.
5. Compare classical models using engineered features, classical models using TDA features, and an end-to-end CNN using a common, leakage-aware evaluation design.

The supervised target is the canonical eight-class defect label. Candidate features must be computed from information available in the wafer map at inference time. Lot identifiers may be used to construct group-aware splits and audit leakage, but they must not be used as predictive shortcuts.

### TDA problem

The TDA objective is to represent spatial structure that simple counts or fixed-threshold geometric measurements may miss. Persistent homology will track topological features as a filtration changes:

- **H0 features** describe the appearance and merging of connected failure regions.
- **H1 features** describe loops or holes, which may be informative for annular and ring-like signatures.
- **Persistence** distinguishes stable shape structure from small, short-lived variations that may reflect noise or isolated failing dies.

Persistence diagrams will be converted into fixed-length model inputs, such as compact persistence statistics or persistence images. These features will be evaluated alone and, if time permits, in combination with geometric or CNN-derived features. TDA is a complementary representation, not an assumption that every class is uniquely defined by topology.

### Scope and intended use

| Item | Definition |
|---|---|
| Primary user | Yield, process, quality, or reliability engineer performing wafer triage |
| Input | One wafer map with categorical die-level states |
| Initial population | Labeled wafers belonging to one of the eight named defect classes |
| Primary output | Predicted defect-signature class and confidence score |
| Supporting output | Spatial/geometric summary, topological summary, and visual explanation when appropriate |
| Primary action | Prioritize and route wafers for engineering review |
| Out of scope for Version 1 | Physical root-cause identification, causal claims, mixed-label recognition, and deployment without human review |

### Error costs and evaluation

The dataset is severely imbalanced, so overall accuracy is not sufficient. A model can appear accurate while failing on rare classes. The primary metric will be **macro F1**, supported by balanced accuracy, per-class precision, per-class recall, class support, and confusion matrices. All model families will be compared on the same reproducible split, with a lot-aware split preferred for the main generalization estimate so related wafers do not cross data partitions.

The main error costs are:

- A **false negative or wrong defect class** can delay investigation or send an engineer toward the wrong family of hypotheses. Recall on rare classes is therefore important.
- A **false positive or low-confidence assignment** can consume engineering review time. Precision, probability calibration, and an eventual reject-for-review option are therefore relevant.

### Success criteria

Version 1 will be considered successful when it demonstrates all of the following:

1. **Descriptive value:** class profiles reveal understandable differences in failure density, location, connectivity, elongation, edge concentration, or loop structure.
2. **Pattern separation:** the trained models outperform naive and simple interpretable baselines under the same split, while macro F1, balanced accuracy, and per-class results show that performance is not driven only by common classes.
3. **Interpretability:** representative predictions can be connected to plausible spatial, geometric, or topological evidence, with limitations stated explicitly.
4. **Robust evaluation:** preprocessing is fit only on training data, lot-related leakage is controlled, class imbalance is addressed within training folds, and the final test set is reserved for final evaluation.
5. **Engineering usefulness:** the result can support triage by returning a predicted signature, confidence, and enough evidence for a human reviewer to decide whether further investigation is warranted.

No single accuracy threshold will define success before the data audit and baseline experiments establish a realistic benchmark. The project will emphasize transparent comparison, rare-class behavior, and reproducible evidence rather than selecting a favorable headline score.

### Final answer to the key question

The project is **both** an image/spatial classification problem and a process-signature description problem. Classification supplies a consistent defect-pattern label; descriptive geometry and TDA explain the global spatial structure behind that label. Together they form an engineering decision-support system for wafer triage, not an automated root-cause diagnosis system.
