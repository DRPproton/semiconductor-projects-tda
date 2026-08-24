# Phase 4: Target Imbalance and Manufacturing Risk

**Goal:** Evaluate the rare-failure problem using metrics that reflect manufacturing screening risk.

## Class Distribution

The SECOM dataset contains 1,567 production observations:

| Class | Label | Count | Percentage |
|---|---:|---:|---:|
| Pass | -1 | 1,463 | 93.36% |
| Fail | 1 | 104 | 6.64% |

The class-distribution chart confirms a strong imbalance. Passing observations account for more than 93% of the dataset, while failures account for less than 7%. Therefore, ordinary accuracy can appear strong even when a model fails to identify the minority failure class.

## Majority-Class Baseline

A majority-class classifier that predicts every observation as pass would produce the following results:

| Metric | Baseline result |
|---|---:|
| Accuracy | 93.36% |
| Failure recall | 0% |
| Pass recall (specificity) | 100% |
| Balanced accuracy | 50% |
| Balanced Error Rate | 50% |
| Failure F1-score | 0 |

Failure precision is undefined because this classifier never predicts the failure class; evaluation software may report it as zero when zero-division handling is enabled.

This baseline demonstrates why accuracy is misleading for SECOM. A model can classify more than 93% of observations correctly while detecting none of the actual failures. A useful model must improve failure detection and balanced performance—not merely exceed the baseline's accuracy.

## Manufacturing Interpretation of Prediction Errors

### False negative

A false negative occurs when the model predicts pass for an observation whose actual label is fail. From a manufacturing viewpoint, this represents a missed yield-risk case. False negatives matter because a potentially abnormal observation is not flagged for investigation.

### False positive

A false positive occurs when the model predicts fail for an observation whose actual label is pass. In a manufacturing screening workflow, false positives may create unnecessary inspection, additional metrology, engineering-review workload, production holds, or avoidable rework. Excessive false alarms may also reduce confidence in the screening system.

The two error types have different operational costs. Failure recall is important, but maximizing recall without considering false positives could create an impractical engineering workload.

## Evaluation Metrics

### Confusion matrix

| | Predicted fail | Predicted pass |
|---|---:|---:|
| Actual fail | True positive | False negative |
| Actual pass | False positive | True negative |

### Failure recall

Failure recall answers: **Of all actual failures, how many did the model identify?**

- Recall = TP / (TP + FN)
- False-negative rate = 1 - failure recall

### Failure precision

Failure precision answers: **Of all observations flagged as failures, how many were actually failures?**

- Precision = TP / (TP + FP)

Precision represents the usefulness of the model's alerts. Low precision means that engineering teams must investigate many passing observations to find a true failure.

### F1-score

The F1-score is the harmonic mean of precision and recall:

- F1 = 2 × precision × recall / (precision + recall)

F1 is useful as a combined summary, but it does not express that false negatives and false positives may have different manufacturing costs. It should not be the only model-selection metric.

### Specificity and false-positive rate

Specificity, also called true-negative rate, measures the percentage of actual passing observations correctly classified as pass.

- Specificity = TN / (TN + FP)
- False-positive rate = 1 - specificity

### Balanced accuracy

Balanced accuracy gives equal importance to failure recall and pass recall:

- Balanced accuracy = (failure recall + specificity) / 2

This prevents the large passing class from dominating the evaluation.

### Balanced Error Rate

Balanced Error Rate (BER) is directly related to balanced accuracy and aligns with the original SECOM benchmark:

- BER = 1 - balanced accuracy
- BER = (false-negative rate + false-positive rate) / 2
- **Lower BER is better.**

### Precision-recall curve and average precision

The precision-recall curve shows how failure precision and recall change as the classification threshold changes. It is especially informative for SECOM because failures are rare and the analysis is focused on the minority class.

The no-skill precision baseline is the failure prevalence, approximately 6.64%. Average precision can summarize performance across thresholds and should be interpreted relative to this baseline.

An ROC curve is not incorrect, but it can appear optimistic in a highly imbalanced dataset because the large number of passing observations can keep the false-positive rate numerically small. The precision-recall curve more directly shows the quality and coverage of failure alerts.

## Threshold Decision

A probability threshold of 0.50 is only a default and is not automatically the best operating threshold. Lowering the threshold will generally flag more observations, potentially increasing failure recall while also increasing false positives.

The final threshold should be selected after model evaluation using:

- the cost of missed failures,
- the cost of false alarms,
- available engineering-review capacity,
- failure recall and false-negative rate,
- alert precision and false-positive burden,
- and the intended screening use case.

Threshold selection will be performed using cross-validated or held-out predictions rather than the training data.

## Phase 4 Decisions and Rationale

- Failure (`1`) remains the positive class, and pass (`-1`) remains the negative class.
- Ordinary accuracy will be reported only as supporting context, not as the main success metric.
- The majority-class baseline establishes 50% balanced accuracy and 50% BER as the minimum balanced-performance reference.
- Primary evaluation will include failure recall, failure precision, false-negative rate, F1-score, specificity, false-positive rate, balanced accuracy, BER, average precision, a confusion matrix, and a precision-recall curve.
- Model selection will balance missed-failure risk against false-alarm workload rather than automatically favoring the model with the highest recall.
- The final decision threshold will be justified using manufacturing risk and operational capacity rather than accepted at 0.50 by default.

**Expected output:** Class Imbalance and Manufacturing Risk section.

**Key question:** Can the analysis detect failures, or does it hide behind the majority class?

**Stop condition:** Accuracy is not used as the main success metric, and both failure detection and false-alarm burden are included in the evaluation plan.
