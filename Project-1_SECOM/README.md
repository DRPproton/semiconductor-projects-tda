# Project Summary

### SECOM Semiconductor 
#### Yield Prediction and Feature Selection through a Process/Yield Engineer Lens


<br>

| **Item**                 | **Project decision**                                                                                                                                                                                            |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Project title            | Semiconductor Yield Prediction and Feature Selection with SECOM                                                                                                                                                 |
| Dataset                  | SECOM public semiconductor manufacturing dataset from UCI Machine Learning Repository.                                                                                                                          |
| Dataset shape            | 1,567 examples and 591 real-valued features.                                                                                                                                                                    |
| Label meaning            | -1 = pass; 1 = fail. Positive class is fail.                                                                                                                                                                    |
| Failure count            | 104 failures, about 6.6% of examples.                                                                                                                                                                           |
| Main problem             | Can a smaller group of process/sensor features predict yield failure and support process-engineering investigation?                                                                                             |
| What could be done       | Analyzed high-dimensional semiconductor process data, selecte relevant signals, evaluate rare-failure prediction using balanced metrics, and communicate findings as engineering investigation candidates. |

<br>

[Project Summary](documents/Project_Summary.md)

[Learning Outcomes](documents/Learning_Outcomes.md)   

[Terminology & Definitions](documents/Terminology_Definitions.md)   

## This project is about:

- semiconductor manufacturing analytics,

- yield-risk detection,

- process/sensor signal understanding,

- missing-value interpretation,

- feature selection,

- imbalanced classification,

- balanced error rate,

- process-regime exploration,

- engineering communication.

### This project is not about:

- generic machine learning tutorials,

- deep learning leaderboard optimization,

- claiming root cause from anonymized features,

- deployment,

- dashboards first,

- AutoML,

- perfect hyperparameter tuning.


## Business Problem

>Semiconductor manufacturing produces a large amount of process and sensor data during production. Engineers monitor many signals from tools, measurements, and process steps, but not every signal is useful for understanding yield problems. Some signals may contain important information about process variation, while others may be noisy, redundant, missing, or unrelated to the final pass/fail outcome.

>The business problem is to identify which process signals are most useful for detecting possible yield failures. If engineers can recognize abnormal process behavior earlier, they may be able to investigate the right tools, steps, or measurements faster. This can help reduce time spent searching through hundreds of signals, support yield-excursion investigation, and improve manufacturing decision-making.

>In plain English: this project asks whether a smaller group of useful process measurements can help identify production units that are more likely to fail, so process and yield engineers can focus their investigation on the most relevant signals.
