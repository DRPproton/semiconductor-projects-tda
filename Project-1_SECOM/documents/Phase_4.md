# Phase 4: Target Imbalance and Manufacturing Risk

**Goal:** Evaluate the rare-failure problem correctly.

**Tasks:**

- Calculate pass and fail percentages.
    - Pass example count 1463 that is 93.36% of the total
    - Fail example count 104 that is the 6.64% of the total

    > The SECOM dataset is highly imbalanced. Out of 1,567 production examples, 1,463 passed and only 104 failed. This means failures represent approximately 6.64% of the dataset. Because failure examples are rare, standard accuracy can be misleading, and the evaluation should focus on metrics that measure failure detection performance.

- ~~Create class-distribution chart.~~

- Calculate majority-class baseline accuracy and explain why it is misleading.

    #### Manufacturing interpretation
    In a fab or production environment, this is common. Most units should pass. But the minority failure class is often the most valuable class because it may represent:

    - yield loss,
    - process drift,
    - tool issues,
    - abnormal process conditions,
    - possible yield excursion signals,
    - downstream cost.
    - What you should write in your project

    ```The class-distribution chart shows a strong imbalance between pass and fail examples. Pass examples account for more than 93% of the dataset, while failures account for less than 7%. This imbalance means that a naive model can appear highly accurate while failing to identify actual yield failures.```

- Define false negative and false positive from a manufacturing viewpoint.

    > A false negative occurs when the model predicts that a production entity will pass, but the actual label is failure. From a manufacturing viewpoint, this is a missed yield-risk case. False negatives are especially important because they may represent failures that the model failed to detect early.

- Choose recall, precision, F1, balanced accuracy, BER, confusion matrix, and PR curve.

    > The SECOM dataset is highly imbalanced, with 1,463 pass examples and 104 failure examples. This corresponds to approximately 93.36% pass and 6.64% fail. A majority-class baseline that predicts every example as pass would achieve approximately 93.36% accuracy, but it would detect zero failures. This makes ordinary accuracy misleading. Because the goal is to identify yield-risk examples, the evaluation focuses on failure-class recall, precision, F1-score, balanced accuracy, Balanced Error Rate, confusion matrices, and precision-recall curves. These metrics provide a better view of how well the model detects rare failures while controlling false alarms.

    ### Confusion matrix
    |             | Predicted fail | Predicted pass |
    | ----------- | -------------: | -------------: |
    | Actual fail |  True positive | False negative |
    | Actual pass | False positive |  True negative |


    ### Recall
    > Out of all actual failures, how many did the model catch?

    - Recall = TP / (TP + FN) <br>
    - Failure recall = correctly predicted failures / all actual failures

    ### Precision
    > Out of all examples predicted as failures, how many were actually failures?

    - Precision = TP / (TP + FP)

    ### F1-score
    > F1-score combines precision and recall.

    - F1 = 2 × precision × recall / (precision + recall)

    ### Balanced accuracy
    > Balanced accuracy is useful when classes are imbalanced.

    - Balanced accuracy = (true positive rate + true negative rate) / 2

    ### Balanced Error Rate (BER)
    > Balanced Error Rate, or BER, is directly connected to the original SECOM benchmark

    - BER = 1 - balanced accuracy
    - **Lower BER is better.**

    ### Precision-recall curve
    > The precision-recall curve shows how precision and recall change when you adjust the model threshold.

    #### 0.50 is not always the best threshold.

    For imbalanced manufacturing problems, you may lower the threshold to catch more failures.

    ```Example:

    Threshold = 0.50
    Catches fewer failures
    Creates fewer false alarms

    Threshold = 0.30
    Catches more failures
    Creates more false alarms
    ```

    - **Why PR curve is better than ROC curve here**

        - ROC curves can sometimes look too optimistic on imbalanced datasets.

``**Expected output:** Class Imbalance section.``

**Key question:** Can the analysis detect failures, or does it hide behind the majority class?

``**Stop condition:** Accuracy is not used as the main success metric.``