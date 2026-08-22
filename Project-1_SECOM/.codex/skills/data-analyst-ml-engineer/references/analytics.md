# Analytics Workflow

Use this reference for data audits, exploratory analysis, KPIs, SQL, statistical analysis, experiments, and decision support.

## Establish the analytical contract

Translate the request into a measurable question with a population, observation grain, time window, comparison or benchmark, and success criterion. Confirm the denominator and unit of analysis before calculating rates or aggregations. Treat metric definitions as part of the result, not incidental implementation detail.

## Audit before analysis

- Inventory sources, tables or files, shapes, schemas, keys, units, and time coverage.
- Check duplicates at the intended grain, missingness patterns, impossible values, inconsistent categories, and suspicious defaults or sentinels.
- For joins, state the expected cardinality and compare pre/post row counts and unmatched keys.
- For filters and cohorts, report how many observations are excluded and why.
- Prefer compact summaries and representative samples over dumping entire datasets.

## Analyze in layers

1. Compute a trustworthy baseline: counts, distributions, central tendency, dispersion, and relevant rates.
2. Segment by variables that can reveal mix shifts or hidden heterogeneity, while avoiding tiny groups that invite overinterpretation.
3. Examine trends with appropriate calendar, seasonality, and exposure denominators.
4. Investigate relationships with effect sizes and uncertainty, not p-values or correlation coefficients alone.
5. Stress-test conclusions against plausible alternative definitions, outliers, missing-data treatments, and influential segments.

For controlled experiments, verify assignment, sample-ratio balance, exposure, metric windows, exclusions, and unit-of-analysis alignment. Report effect size and interval estimates. Do not interpret an observational comparison as causal without a defensible identification strategy and assumptions.

## Visual and tabular output

Choose the simplest form that exposes the relevant comparison. Label units, denominators, time windows, and sample sizes. Avoid truncated scales or dual axes when they could distort interpretation. Use accessible colors and distinguish missing or suppressed values from zero.

## Completion checks

- Reconcile headline values against an independent calculation or source total when feasible.
- Confirm that grouping, sorting, null behavior, date boundaries, and SQL integer division behave as intended.
- Keep reusable transformations in code rather than manual notebook state.
- Deliver the decision-relevant finding first, followed by evidence, method, caveats, and recommended next action.
