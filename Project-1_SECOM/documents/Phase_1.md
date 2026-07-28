
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

- [x] Define the business problem in plain English. 
    >This project asks whether a smaller group of useful process measurements can help identify production units that are more likely >to fail, so process and yield engineers can focus their investigation on the most relevant signals.

- [x] Define the modeling problem in technical language.
    >This project is a supervised classification problem using high-dimensional semiconductor manufacturing data. Each observation represents one production entity with a set of anonymized process or sensor measurements. 

    >Because the dataset is highly imbalanced, with failures representing a small minority of observations, standard accuracy is not an appropriate primary evaluation metric. The model should be evaluated using manufacturing-relevant and imbalance-aware metrics such as failure-class recall, failure-class precision, F1-score, balanced accuracy, balanced error rate, confusion matrix, false-negative rate, and precision-recall analysis.

    >In addition to prediction, this project treats feature selection as a core modeling objective. The goal is not only to classify pass/fail outcomes, but also to identify a smaller subset of process or sensor variables that retain predictive value and may serve as candidates for yield or process-engineering investigation.

- [x] Define the process/yield interpretation: relevant signal discovery and rare-failure screening.
    >This project is not only about predicting whether a production entity will pass or fail. The main objective is to discover which process or sensor signals may be most relevant to yield risk and to evaluate whether those signals can support rare-failure screening.

- [x] Select evaluation metrics before building models.
    > 1. Failure-Class Recall
    > 2. Balanced Error Rate (BER)
    > 3. Balanced Accuracy
    > 4. False-Negative Rate

~~**Expected output:** Problem Definition section.~~

~~**Key question:** Are we only predicting failure, or are we identifying useful process signals?~~

**Stop condition:** The problem statement includes both prediction and feature relevance.
