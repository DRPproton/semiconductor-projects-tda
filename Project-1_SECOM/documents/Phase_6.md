# Phase 6: Feature Selection and Dimensionality Reduction

**Goal:** Identify smaller, reproducible representations of the 460 retained process measurements while preserving an untouched test set for final model evaluation.

**Tasks:**

- [x] Create and verify a stratified training/test split.

- [x] Compare complementary feature-relevance methods using training data: mutual information, Random Forest importance, `SelectFromModel`, and Random Forest recursive feature elimination (RFE).

- [x] Select an initial 40-feature RFE candidate set.

- [x] Apply principal component analysis (PCA) after training-only median imputation and standardization.

- [x] Examine cumulative explained variance and the first two principal components for possible process regimes or abnormal regions.

- [ ] Order the 40 RFE candidates and create nested top-40, top-30, and top-20 feature sets.

- [ ] Create a correlation-pruned alternative using an absolute Spearman-correlation threshold of 0.90, with the removal rule learned from training data.

- [ ] Create a consensus table combining Phase 5 evidence, mutual-information rank, Random Forest rank, RFE selection, missingness, and redundancy status.

- [ ] Compare the reduced representations against all 460 features during cross-validated baseline modeling.

**Expected output:** A feature-selection benchmark, nested 40/30/20 feature sets, a correlation-pruned alternative, and a PCA process-structure assessment.

**Key question:** Can a smaller and more interpretable representation retain useful failure-screening information without relying on redundant process measurements?

**Stop condition:** The candidate feature sets and PCA representation are reproducible, compared using leakage-safe validation, and ready for baseline modeling.

## Phase 6 Results and Interpretation

### Validation design

The 1,567 observations were divided using a stratified 80/20 split. The training set contains 1,253 observations, including 83 failures (6.62%), and the test set contains 314 observations, including 21 failures (6.69%). The closely matched failure rates confirm that stratification worked as intended. Supervised feature selection and PCA preprocessing were fitted using the training data, while the test set remains reserved for final evaluation.

### Feature-selection findings

The feature-selection methods produced different candidate rankings because they answer different questions. Mutual information evaluates each feature independently and can detect nonlinear dependence, while Random Forest importance and RFE evaluate features as part of a multivariable nonlinear model.

The mutual-information top five were features `128`, `541`, `411`, `274`, and `443`. The initial Random Forest importance ranking was led by features `64`, `562`, `65`, `574`, and `103`. RFE selected 40 candidates, including features `59`, `64`, `65`, `103`, and `510`, which also appeared prominently in the Phase 5 exploratory analysis. Eleven RFE-selected measurements overlapped the 38 Phase 5 process-signal candidates, while only features `91` and `125` overlapped the mutual-information top 20. This limited agreement is evidence that the methods capture different types of structure; it is not sufficient by itself to declare one method superior.

RFE did not eliminate all redundancy. For example, features `247` and `519` were both selected even though Phase 5 found an approximately 0.9998 Spearman correlation between them. This confirms the need for a separate, deterministic correlation-pruning comparison before the final feature set is selected.

### PCA results

PCA was fitted to the 1,253-row training matrix after median imputation and standardization. The diagnostic fit retained all 460 components so that the full cumulative-variance curve could be inspected. The results were:

| Variance retained | Components required |
|---:|---:|
| 80% | 87 |
| 90% | 129 |
| 95% | 164 |

PC1 explains 5.62% of the training variance and PC2 explains 3.72%, for 9.34% combined. The first 20 components explain approximately 39.15%. The cumulative-variance curve rises smoothly rather than showing a sharp low-dimensional cutoff. Therefore, the dataset contains substantial redundancy, but its overall variation is still distributed across many process directions. A future `n_components=0.95` modeling branch would reduce the matrix from 460 measurements to 164 components.

The PC1-PC2 projection shows strong overlap between passing and failing observations in the dense central region. Some failures occur in extreme PCA regions, but passing observations also occupy those regions. The first two components therefore do not reveal a clean failure boundary or a single isolated failure regime. Because they contain only 9.34% of total variance, this plot cannot determine whether later components contain predictive failure information.

### Phase interpretation and decision

The PCA result supports the Phase 5 conclusion that the SECOM measurements contain extensive shared structure. However, PCA should remain a dimensionality-reduction benchmark and process-structure diagnostic rather than the main engineering interpretation, because each component combines many anonymous measurements and is harder to discuss as an individual process signal.

The primary project story will remain focused on original-feature sets containing 40, 30, and 20 measurements. PCA at 95% variance will be retained as an optional comparison during baseline modeling. Performance has not yet been demonstrated for any reduced representation; that conclusion must come from leakage-safe cross-validation and one final evaluation on the untouched test set.

**Current status:** PCA and the initial 40-feature RFE selection are complete. Phase 6 will be finalized after the nested 40/30/20 sets, the 0.90 correlation-pruned alternative, the consensus table, and the baseline comparison are completed.
