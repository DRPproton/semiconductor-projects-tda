**Project 2 Execution Guide**

*WM-811K Wafer Map Pattern Analytics and Topological Data Analysis through a Yield/Process Engineer Lens*

Companion project to SECOM - Version 1.0

**Main constraint: use public data only; do not include Microchip confidential data.**

# Purpose of This Document

This document creates the second project in the same style as the Project 1 SECOM plan. Project 2 is different because it is spatial. Instead of hundreds of anonymized sensor columns, you analyze wafer maps: die-level pass/fail patterns across the wafer. This makes it a better project for topology, connected components, loops/rings, local clusters, scratches, and defect-pattern interpretation.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Project identity</strong></p>
<p>A wafer-map spatial defect-pattern investigation. The main goal is to connect wafer spatial signatures to process/yield questions, then use TDA features as interpretable shape descriptors.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# How Project 2 Complements Project 1

| **Dimension**             | **Project 1: SECOM**                                            | **Project 2: WM-811K**                                                                              |
|---------------------------|-----------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| Data type                 | High-dimensional tabular process/sensor data.                   | Spatial wafer maps with die-level pass/fail patterns.                                               |
| Main engineering question | Which process/sensor signals are associated with yield failure? | What spatial defect patterns appear on wafers, and what process/tool signatures might they suggest? |
| Best TDA use              | Mapper for process-regime discovery in selected feature space.  | Persistent homology, connected components, Betti curves, persistence images, and shape features.    |
| Main risk                 | Overclaiming root cause from anonymized features.               | Treating pattern classification as image ML only and ignoring process meaning.                      |
| Portfolio value           | Process-signal investigation and feature selection.             | Wafer-space defect-pattern reasoning and topology-based interpretation.                             |

# Project Summary

| **Item**                 | **Project decision**                                                                                                                                                                    |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Project title            | Wafer Map Pattern Analytics and TDA with WM-811K                                                                                                                                        |
| Dataset                  | WM-811K wafer map dataset, commonly distributed through MIR/Kaggle and used in wafer defect classification examples.                                                                    |
| Dataset structure        | Wafer maps contain pixel/die values where background, good dies, and defective dies are encoded. Labeled maps have pattern classes.                                                     |
| Known scale              | MathWorks describes the dataset as 811,457 wafer map images, including 172,950 labeled images.                                                                                          |
| Common labels            | Center, Donut, Edge-Loc, Edge-Ring, Loc, Near-full, Random, Scratch, and none.                                                                                                          |
| Main problem             | Can spatial and topological features describe wafer defect modes in a way that supports process/yield investigation?                                                                    |
| Main portfolio story     | I analyzed wafer-level spatial defect patterns, extracted interpretable geometry/topology features, compared pattern classes, and connected patterns to process-engineering hypotheses. |
| Confidentiality boundary | Use only public WM-811K data. Do not include Microchip wafers, lot names, tool information, internal maps, or production anecdotes.                                                     |

# Important Mindset Shift

A wafer map is not just an image. It is a spatial record of die-level test behavior across a wafer. Defect patterns can reflect process/tool behavior, but public labels alone do not prove root cause. The correct goal is to produce process hypotheses and engineering questions.

| **Pattern family** | **Shape intuition**                                  | **Possible engineering question**                                                                                     |
|--------------------|------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| Center             | Defects concentrated near the wafer center.          | Is there a radial uniformity issue, thermal center effect, spin/coating effect, or center-specific process condition? |
| Donut              | Ring-like failure with a cleaner center.             | Is there a radial process nonuniformity, edge exclusion interaction, or deposition/etch/CMP radial effect?            |
| Edge-Loc           | Localized defects near one edge area.                | Is a handling, chucking, edge-bead, gas-flow, or chamber asymmetry issue plausible?                                   |
| Edge-Ring          | Ring of failures near the wafer edge.                | Is the edge exclusion, etch/deposition uniformity, CMP edge effect, or temperature profile involved?                  |
| Loc                | Localized cluster anywhere on wafer.                 | Could this be particle contamination, localized scratch, reticle/field issue, or local tool instability?              |
| Near-full          | Most dies fail.                                      | Is this a severe excursion, recipe/tool issue, or upstream catastrophic process failure?                              |
| Random             | Scattered defects without obvious spatial structure. | Is this background defectivity, random particles, or test noise?                                                      |
| Scratch            | Elongated line-like structure.                       | Could this indicate mechanical handling, wafer transport, CMP scratch, or contact damage?                             |
| None               | No labeled failure pattern.                          | What is the expected normal pass/fail background and how should normal maps be represented?                           |

# Learning Outcomes

- Explain what a wafer map represents and how it differs from tabular process data.

- Identify major wafer-map defect pattern classes and describe their spatial signatures.

- Explain why wafer-map labels are imbalanced and why macro/per-class metrics matter.

- Create a defect-pattern atlas that a process or yield engineer could scan quickly.

- Extract interpretable spatial features: fail density, radial distribution, edge concentration, connected components, compactness, elongation, and nearest-neighbor structure.

- Translate TDA concepts into wafer-map language: H0 as connected regions, H1 as loops/rings, persistence as feature scale stability.

- Use persistent homology or related topology features to compare Center, Donut, Edge-Ring, Scratch, Random, and Local patterns.

- Avoid claiming root cause from public wafer-map labels alone.

- Write a portfolio report that connects topology to process/yield reasoning.

# Project Roadmap

The minimum pre-certificate version starts during Weeks 7-8 of the eight-week plan. The portfolio-complete version can continue for four more weeks after the certificate begins or during lighter study periods.

| **Stage**       | **Time**       | **Main work**                                                             | **Output**                                   |
|-----------------|----------------|---------------------------------------------------------------------------|----------------------------------------------|
| Minimum Week 7  | 4-5 hour block | Download/inspect WM-811K, understand labels, visualize examples by class. | Wafer-map orientation notebook.              |
| Minimum Week 8  | 4-5 hour block | Build defect-pattern atlas and define topology questions.                 | README draft and TDA experiment plan.        |
| Extended Week 1 | Optional       | Preprocess wafer maps and compute spatial features.                       | Spatial feature table.                       |
| Extended Week 2 | Optional       | Build connected-component and radial/angular descriptors.                 | Geometry feature report.                     |
| Extended Week 3 | Optional       | Run persistent homology/TDA experiments on selected classes.              | Persistence diagrams and feature comparison. |
| Extended Week 4 | Optional       | Write final process/yield interpretation report and README.               | Portfolio-ready Project 2.                   |

# Recommended Project Folder

project-2-wm811k-wafer-map-tda/

data/raw/ \# original dataset files only

data/interim/ \# sampled/labeled subsets, resized maps if needed

data/processed/ \# feature tables and topology features

notebooks/ \# 01_orientation.ipynb, 02_spatial_features.ipynb, etc.

reports/ \# final report, atlas, README assets

figures/ \# wafer class examples, diagrams, TDA plots

src/ \# loaders, feature extraction, TDA utilities

references/ \# source notes and citation metadata

README.md

# Phase-by-Phase Execution Plan

## Phase 0: Wafer-Map and Process Context Setup

**Goal:** Understand the semiconductor meaning of wafer maps before treating them as images.

**Tasks:**

- Define wafer, die, wafer map, pass die, fail die, defect pattern, lot, wafer index, edge exclusion, and spatial signature.

- Explain why wafer-level spatial patterns may help engineers diagnose manufacturing issues.

- Write why this project is not a generic CNN image-classification project.

- Create a vocabulary page for the nine common WM-811K labels.

**Expected output:** Business and Process Context section.

**Key question:** What manufacturing question does a wafer map help answer?

**Stop condition:** You can explain each label in plain process/yield language.

## Phase 1: Dataset Acquisition and Project Setup

**Goal:** Download and organize the public wafer-map dataset.

**Tasks:**

- Use a public WM-811K source such as MIR/Kaggle or the MathWorks helper workflow.

- Keep raw files unchanged.

- Document dataset size, file format, fields, labels, and source.

- Create raw, interim, processed, notebooks, figures, reports, and src folders.

- Confirm that no company-confidential wafer maps or internal lot names are included.

**Expected output:** Project folder and dataset source note.

**Key question:** Can another person reproduce the dataset acquisition?

**Stop condition:** Source and license/usage notes are in the README.

## Phase 2: Problem Framing

**Goal:** Define the spatial analytics and TDA problem clearly.

**Tasks:**

- Write the business problem: classify and describe wafer spatial defect patterns for yield investigation.

- Write the analytics problem: extract image/spatial/topological features from wafer maps.

- Write the TDA problem: use topology to capture connected regions, loops/rings, and persistent shape patterns.

- Define whether the first version is descriptive, supervised, or both.

- Define success as interpretability plus reasonable pattern separation, not only high accuracy.

**Expected output:** Problem Definition section.

**Key question:** Are we classifying images, describing process signatures, or both?

**Stop condition:** The project statement includes spatial interpretation and TDA.

## Phase 3: Initial Dataset Inspection

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

## Phase 4: Wafer Map Representation and Preprocessing

**Goal:** Represent maps consistently without destroying shape information.

**Tasks:**

- Confirm pixel/die values: background, good die, defective die.

- Convert each map into a binary failed-die mask and coordinate list.

- Preserve original aspect ratio when possible.

- Normalize coordinates to a common wafer coordinate system such as \[-1, 1\] x \[-1, 1\].

- Decide whether to resize images for CNN baselines separately from TDA features.

- Document every transformation.

**Expected output:** Preprocessing Strategy section.

**Key question:** Does preprocessing preserve the spatial signature?

**Stop condition:** Every map can be represented as failed-die coordinates plus metadata.

## Phase 5: Class Imbalance and Sampling Strategy

**Goal:** Handle label imbalance without hiding rare patterns.

**Tasks:**

- Create class-distribution chart.

- Separate none maps from defect maps for some analyses.

- Create a balanced exploratory subset for visualization.

- Keep a realistic imbalanced subset for evaluation.

- Use macro F1, balanced accuracy, per-class recall, and confusion matrix for any classifier.

- Do not let the none class dominate the story.

**Expected output:** Class Imbalance section.

**Key question:** Which classes are rare, and how will you avoid ignoring them?

**Stop condition:** You have both balanced and realistic subsets documented.

## Phase 6: Visual Defect-Pattern Atlas

**Goal:** Create a visual catalog before extracting features.

**Tasks:**

- Plot 16-25 examples per class.

- Create a single-class page for each label.

- Write human descriptions of the spatial pattern.

- Note ambiguous examples or mixed patterns.

- Write possible process/yield questions for each pattern family.

**Expected output:** Defect Pattern Atlas.

**Key question:** Can a reader visually understand the classes before seeing code?

**Stop condition:** Atlas is clear enough to include in the README/report.

## Phase 7: Spatial Feature Engineering

**Goal:** Extract interpretable wafer-shape features.

**Tasks:**

- Compute total dies, failed dies, fail density, and good/fail ratio.

- Compute center of mass of failed dies.

- Compute radial distribution: center, middle, edge fail concentration.

- Compute angular distribution and quadrant imbalance.

- Compute edge concentration and distance-to-center statistics.

- Compute bounding box, aspect ratio, elongation, compactness, and orientation when possible.

- Compute nearest-neighbor distances among failed dies.

**Expected output:** Spatial Feature Table.

**Key question:** Which features describe what a process engineer sees visually?

**Stop condition:** Each feature has a plain-English interpretation.

## Phase 8: Connected Components and Geometry Features

**Goal:** Bridge image analysis and topology.

**Tasks:**

- Find connected components in the failed-die mask.

- Compute number of components, largest component size, component-size distribution, and isolated-fail count.

- Compute skeleton/line-like features for Scratch when useful.

- Compute ring/annulus heuristics for Donut and Edge-Ring.

- Compare distributions by class.

**Expected output:** Connected-Component Feature Report.

**Key question:** Are failures one connected region, many isolated regions, a line, or a ring?

**Stop condition:** Component features separate at least some pattern families.

## Phase 9: TDA Feature Design

**Goal:** Translate topology into wafer-map language.

**Tasks:**

- Represent failed dies as a point cloud in normalized wafer coordinates.

- Use H0 to describe connected regions and cluster merging across scale.

- Use H1 to describe loop or ring-like structure where applicable.

- Generate persistence diagrams for selected examples from each class.

- Avoid applying TDA blindly to all maps before testing small examples.

- Decide which TDA summaries to use: persistence images, landscapes, Betti curves, persistence entropy, or selected diagram statistics.

**Expected output:** TDA Design Memo.

**Key question:** What shape information should topology capture that simple features may miss?

**Stop condition:** You have small, verified TDA examples for at least Center, Donut, Edge-Ring, Scratch, Random, and Loc.

## Phase 10: TDA Experiments

**Goal:** Test whether topology features separate defect classes.

**Tasks:**

- Choose a manageable subset for computation.

- Compute persistence diagrams for failed-die point clouds.

- Compare class-level diagram summaries.

- Create persistence images or landscapes for classification/visualization.

- Compare topology features against spatial features.

- Identify which classes topology helps most.

**Expected output:** TDA Results section.

**Key question:** Does topology add information beyond density, radial, and component features?

**Stop condition:** TDA results are compared to non-TDA features.

## Phase 11: Baseline Classification or Similarity Search

**Goal:** Use simple models only to test feature usefulness.

**Tasks:**

- Train a simple classifier on spatial features.

- Train a classifier on topology features.

- Train a combined feature model.

- Optional: train a small CNN or use an existing image baseline only as a benchmark.

- Evaluate with macro F1, balanced accuracy, per-class recall, and confusion matrix.

- Alternatively, build nearest-neighbor similarity retrieval for engineering review.

**Expected output:** Baseline/Similarity Results section.

**Key question:** Which feature family best supports defect-pattern separation?

**Stop condition:** Classification is used to validate features, not to replace interpretation.

## Phase 12: Process Interpretation Matrix

**Goal:** Connect spatial signatures to process hypotheses carefully.

**Tasks:**

- For each class, write what the pattern looks like, what features detect it, and what process questions it raises.

- Map patterns to possible categories such as radial nonuniformity, edge effects, local contamination, mechanical damage, catastrophic excursion, or random defectivity.

- State that public labels do not prove process root cause.

- List the missing metadata needed for real engineering validation: tool, chamber, route, recipe, layer, step, lot history, maintenance, metrology, time order.

**Expected output:** Process Interpretation Matrix.

**Key question:** What would a yield/process engineer ask next?

**Stop condition:** Each pattern has hypotheses and required validation data.

## Phase 13: Error and Ambiguity Analysis

**Goal:** Study confusing patterns and model mistakes.

**Tasks:**

- Identify classes that are visually or topologically similar.

- Inspect confusion between Edge-Loc and Scratch, Donut and Edge-Ring, Loc and Random, none and low-fail maps.

- Review examples where topology features disagree with labels.

- Write why ambiguous maps are expected in real manufacturing.

**Expected output:** Error and Ambiguity Analysis section.

**Key question:** Which maps are hard to classify, and why?

**Stop condition:** The report includes examples of ambiguity rather than hiding them.

## Phase 14: Final Report

**Goal:** Create a professional process/yield and TDA report.

**Tasks:**

- Write executive summary, dataset description, wafer-map vocabulary, pattern atlas, preprocessing, spatial features, topology features, results, process interpretation, limitations, and next steps.

- Include diagrams and examples, not just metrics.

- Use caution around process hypotheses.

**Expected output:** Final Project 2 report.

**Key question:** Can someone understand why topology is relevant to wafer maps in five minutes?

**Stop condition:** Report includes process interpretation and limitations.

## Phase 15: Portfolio README

**Goal:** Make the project GitHub-ready.

**Tasks:**

- Add title, summary, dataset source, examples, defect classes, methods, TDA explanation, results, limitations, and how to run.

- Include small images of wafer-map examples and topology outputs.

- Cross-link back to Project 1.

**Expected output:** GitHub README.

**Key question:** Would this README help explain your process/yield engineering direction?

**Stop condition:** README is useful to a semiconductor reader, not only an ML reader.

# TDA Concepts to Spend the Most Time Understanding

| **TDA concept**             | **Wafer-map interpretation**                                         | **Best use in this project**                                           |
|-----------------------------|----------------------------------------------------------------------|------------------------------------------------------------------------|
| Point cloud                 | Failed die coordinates on a wafer.                                   | Represent each wafer as positions of failed dies.                      |
| H0 / connected components   | How many defect regions exist and how they merge as scale increases. | Separate random scattered fails from compact local defects.            |
| H1 / loops                  | Ring or donut-like spatial structure.                                | Detect Donut and Edge-Ring patterns.                                   |
| Persistence                 | How stable a shape feature is across distance scales.                | Distinguish real pattern structure from noise.                         |
| Persistence diagram         | Birth/death summary of connected regions and loops.                  | Visual explanation for selected wafer maps.                            |
| Persistence image/landscape | Vectorized summary for modeling or comparison.                       | Compare topology features with standard spatial features.              |
| Betti curve                 | Number of components/loops across scale.                             | Readable topology summary for report figures.                          |
| Mapper                      | Graph summary of high-dimensional feature space.                     | Optional later extension for grouping wafer maps or combined features. |

# Minimal Feature Set to Build First

Build the simple interpretable features before TDA. If these features already explain a class well, TDA should be used to complement, not replace, them.

- Fail density: failed dies divided by total active dies.

- Radial concentration: fraction of failed dies in center, middle, and edge zones.

- Edge ratio: fraction of failed dies near wafer boundary.

- Center of mass: mean x/y location of failed dies.

- Spread: standard deviation of failed-die coordinates.

- Connected component count and largest component fraction.

- Elongation/orientation of the main failed region.

- Ring score: high failure in annular zone with lower center failure.

- Scratch score: elongated, line-like connected region.

- Randomness score: many isolated small components and weak spatial concentration.

# Correct Language for the Final Report

| **Use this language**                                                             | **Avoid this language**                            |
|-----------------------------------------------------------------------------------|----------------------------------------------------|
| This wafer pattern is consistent with an edge-related signature.                  | This was caused by edge bead removal.              |
| The topology features capture a loop-like defect structure.                       | TDA proves the process mechanism.                  |
| Scratch-like maps may suggest mechanical handling or CMP-related questions.       | This scratch came from CMP.                        |
| The pattern class raises a process hypothesis requiring tool/layer/time metadata. | The public label is enough to identify root cause. |
| Topology adds shape descriptors beyond simple density features.                   | TDA is better than all image methods.              |

# Final Report Template

1.  Executive Summary

2.  Manufacturing and Wafer-Map Context

3.  Dataset Source and Structure

4.  Defect Class Vocabulary

5.  Visual Defect-Pattern Atlas

6.  Preprocessing Strategy

7.  Class Imbalance and Sampling Plan

8.  Spatial Feature Engineering

9.  Connected Components and Geometry Features

10. TDA Feature Design

11. TDA Results

12. Baseline/Similarity Results

13. Process Interpretation Matrix

14. Error and Ambiguity Analysis

15. Limitations

16. Recommendations

17. Next Steps

# GitHub README Checklist

- Project title and one-paragraph summary.

- Dataset source and field explanation.

- Sample wafer maps by class.

- Explanation of why wafer maps are process/yield artifacts, not just images.

- Spatial features table and what each feature means.

- TDA explanation using H0/H1/persistence in wafer-map language.

- Key results: atlas, feature comparisons, topology diagrams, confusion/similarity analysis.

- Limitations and missing metadata needed for real root-cause analysis.

- How to run notebooks and reproduce figures.

- Connection to Project 1: SECOM signal-space project plus Project 2 wafer-space project.

# Sources and Reference Directory

Use these sources as the official public reference points for the project. The hyperlinks are intentionally placed in one section so the notebooks and README can cite them cleanly.

| **Source**                                                   | **Use in this project**                                                                                | **Link**                                                                                                                                            |
|--------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| MathWorks WM-811K example                                    | Dataset facts, label names, pixel meanings, and a public example workflow.                             | [<u>Open MathWorks example</u>](https://www.mathworks.com/help/vision/ug/classify-defects-on-wafer-maps-using-deep-learning.html)                   |
| Kaggle WM-811K dataset page                                  | Common public dataset mirror used in many examples.                                                    | [<u>Open Kaggle dataset</u>](https://www.kaggle.com/datasets/qingyi/wm811k-wafer-map)                                                               |
| MIR Lab public dataset page                                  | Original public dataset reference page for WM-811K/LSWMD distribution context.                         | [<u>Open MIR dataset page</u>](https://mirlab.org/dataset/public/)                                                                                  |
| Wu, Jang, and Chen wafer-map paper                           | Original wafer-map failure pattern recognition reference for large-scale wafer maps.                   | [<u>Open IEEE page</u>](https://ieeexplore.ieee.org/document/6932449/)                                                                              |
| University of Arizona - Semiconductor Processing Certificate | Boundary for process topics: oxidation, lithography, deposition, plasma etching, cleaning/wet etching. | [<u>Open certificate page</u>](https://online.arizona.edu/programs/graduate-certificate/online-graduate-certificate-semiconductor-processing-gcert) |
| Khan Academy - AP/College Physics 2 Geometric Optics         | Optional optics refresher for lithography intuition.                                                   | [<u>Open Khan optics</u>](https://www.khanacademy.org/science/ap-physics-2/x0e2f5a2c%3Ageometric-optics)                                            |
| Khan Academy - Chemistry Gases and Kinetic Molecular Theory  | Gas/pressure intuition before plasma/deposition/etch coursework.                                       | [<u>Open Khan gases</u>](https://www.khanacademy.org/science/chemistry/gases-and-kinetic-molecular-theory)                                          |

End of Project 2 guide.
