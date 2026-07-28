
## Phase 1: Dataset Acquisition and Project Setup

**Goal:** Download and organize the public data professionally.

**Tasks:**

- [x] Download SECOM from UCI using either the browser or ucimlrepo.

- [x] Save raw data without modification.

- [x] Create raw_data, processed, notebooks, graphs, and reports folders.

- [x] Document the source, license, files, row/column counts, and label meaning.


~~**Expected output:** Clean project folder and README draft.~~

**Key question:** Could another person open the repo and understand the dataset?

~~**Stop condition:** Raw data is stored separately and never overwritten.~~


## Phase 1.2: Problem Framing

**Goal:** Define the business, ML, and semiconductor versions of the problem.

**Tasks:**

- [x] Target variable: The target variable is the first variable in the ***secom_labels.data*** file. 

- [x] Positive class: fail = 1. Negative class: pass = -1.

- [X] Define the business problem in plain English. 
    >This project asks whether a smaller group of useful process measurements can help identify production units that are more likely >to fail, so process and yield engineers can focus their investigation on the most relevant signals.

- [ ] Define the modeling problem in technical language.

- [ ] Define the process/yield interpretation: relevant signal discovery and rare-failure screening.

- [ ] Select evaluation metrics before building models.

~~**Expected output:** Problem Definition section.~~

**Key question:** Are we only predicting failure, or are we identifying useful process signals?

**Stop condition:** The problem statement includes both prediction and feature relevance.
