# Core Terminology and Definitions

- **Yield**: The percentage of the total number of manufacturing units produced that meet all the quality and functional specifications.
$$
\text{Yield} = \frac{\text{Good Units}}{\text{Total Units Produced}} \times 100\%
$$
- **Pass/Fail Yield Testing**: Units are either accepted (Pass) or rejected (Fail) at a screening step during or after production, where they are evaluated against target specifications. 
- **Process Variation**: The expected fluctuations in the manufacturing process and conditions that cause slight physical or operational variations between units.
- **Drift**: A gradual, systematic shift in process parameters over time due to small changes. Examples: a drill bit slowly dulling or a chemical bath degrading across shifts
- **Excursion**: A sudden, significant jump or drop in process parameters outside of acceptable limits or specs. Can be caused by human error, material defects, or equipment failure.
- **Process Monitoring**: The continuous collection and analysis of sensor data, telemetry, and metrology (measurement) data during manufacturing to ensure equipment and processes stay within target specs.
- **False positive**: Flagging a good unit as defective.
- **False negative**: Flagging a defective unit as good.

## Why False Negatives Are Dangerous in Yield Screening

In a manufacturing or test context, a false positive costs money immediately in lost scrap value or unnecessary rework. A false negative, however, can be disastrous for several reasons:

1. **Escaped Defects Reach Customers**: Bad units leave the factory floor. In industries like automotive, medical devices, or aerospace, a defective part that passes testing can lead to field failure, product recalls, or loss of life.
2. **Exponentially Higher Failure Costs**: Catching a defect at the silicon wafer or raw component stage costs pennies. Catching it after it has been assembled into a finished car or server board—or after it fails in a customer's hands—can cost thousands or millions of dollars.
3. **Reputational Damage**: Consistently shipping "escaped" defective products damages brand trust and can cause customers to cancel supply contracts or impose heavy financial penalties (e.g., warranty claims).

## Why Engineers Collect Many Signals (and Why Few Are Useful)

Modern fabrication plants and automated assembly lines use thousands of sensors measuring temperature, pressure, vibration, voltage, flow rates, and timing every millisecond.

### Why Collect So Many Signals?

* **Completeness**: Manufacturing processes are non-linear and interconnected. You rarely know in advance which specific tool metric will trigger a future defect.
* **Traceability**: If a batch fails weeks down the line, high-density sensor history lets process engineers perform root-cause analysis (RCA).

### Why Are Only a Few Signals Useful?

* **Multicollinearity & Redundancy**: Many sensors track the same physical system; if temperature spikes, five adjacent sensors will all register the same event, offering redundant information.
* Background Noise: Most signals reflect normal, harmless process variation rather than meaningful indicators of failure.
* **The "Curse of Dimensionality"**: Having thousands of telemetry channels makes statistical models prone to finding coincidental correlations. Feature selection (identifying the few critical process parameters that directly correlate with ultimate device yield) is one of the primary tasks in modern yield engineering.