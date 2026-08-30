# Semiconductor Manufacturing Analytics Portfolio

Applied data-science projects focused on semiconductor process, yield, and defect-pattern investigation.

This repository documents a four-project portfolio built with public manufacturing datasets. The work combines exploratory analysis, statistical reasoning, machine learning, reproducible validation, and engineering interpretation. The objective is not simply to produce model scores, but to convert difficult manufacturing data into defensible priorities and questions for process or yield engineers.

**Portfolio website:** [drpproton.github.io/semiconductor-projects-tda](https://drpproton.github.io/semiconductor-projects-tda/)  
**GitHub profile:** [github.com/DRPproton](https://github.com/DRPproton)

> The website becomes available after GitHub Pages is enabled for this repository. Deployment instructions are included below.

## Portfolio roadmap

| No. | Project | Primary focus | Status |
|---:|---|---|---|
| 01 | [SECOM Semiconductor Feature Screening](Project-1_SECOM/) | High-dimensional process data, feature stability, and rare-failure modeling | **Completed** |
| 02 | [Wafer Map Pattern Analytics with WM-811K](Project-2WM811k_wafer/) | Spatial defect patterns and interpretable topological analysis | **In development** |
| 03 | Forthcoming semiconductor study | Scope and public dataset to be defined | Planned |
| 04 | Forthcoming semiconductor study | Scope and public dataset to be defined | Planned |

## Project 1 — SECOM Semiconductor Feature Screening

### Engineering question

Which anonymous SECOM process measurements remain relevant when the training sample changes, and which should be investigated first by an engineer with access to the missing process context?

### Data challenge

The public UCI SECOM dataset contains 1,567 manufacturing observations, 590 anonymous numeric process measurements, extensive missing data, and only 104 recorded failures. The 6.64% failure rate makes ordinary accuracy misleading and requires rare-event metrics and careful validation.

### Main result

The project reduced the original measurement space to a reproducible investigation hierarchy:

- **100-feature predictive representation:** retained the strongest tested Random Forest failure-ranking result.
- **20-feature engineering shortlist:** a smaller boundary for interpretable process review.
- **Five-feature core:** features **103, 59, 510, 129, and 348** were the strongest first investigation tier.
- Features **103, 59, and 510** appeared in every top-20 selection across 25 repeated validation resamples.

The tuned 100-feature Random Forest achieved repeated-cross-validation average precision of **0.2000 ± 0.0627**, compared with a failure prevalence of **0.0662**. However, failure recall at the default 0.50 threshold was only **0.0196**. The model contains useful ranking information, but it is not a production-ready failure detector.

Because the variables are anonymous, the result does not establish physical root cause. The correct engineering handoff is to map the shortlisted feature IDs to sensor names, units, process stages, tools, chambers, recipes, and later manufacturing data.

### Project 1 materials

- [Web case study](https://drpproton.github.io/semiconductor-projects-tda/Project-1_SECOM/website/)
- [Employer-facing paper](Project-1_SECOM/paper/SECOM_Feature_Screening_Case_Study.md)
- [Complete technical report](Project-1_SECOM/documents/Final_Report.md)
- [Analysis notebook](Project-1_SECOM/notebooks/notebook.ipynb)
- [Detailed model evaluation log](Project-1_SECOM/documents/models_eval.md)
- [Phase-by-phase project documentation](Project-1_SECOM/documents/)

## Analytical principles

The projects follow a consistent set of working principles:

1. **Start with the engineering question.** Methods are selected for the decision or investigation they support.
2. **Keep preprocessing inside validation.** Imputation and feature selection are learned from training folds to reduce leakage.
3. **Use metrics appropriate for rare events.** Average precision, recall, false-negative rate, precision, and balanced accuracy are emphasized over ordinary accuracy.
4. **Measure stability, not only fitted importance.** Repeated resampling is used to identify conclusions that survive changes in the training sample.
5. **Separate association from mechanism.** Statistical relationships generate process questions; they do not prove root cause.
6. **Document uncertainty and limitations.** Every result is accompanied by the conditions under which it should and should not be used.
7. **Use public data only.** This portfolio contains no confidential company, product, tool, wafer, lot, or manufacturing information.

## Repository structure

```text
semiconductor-projects-tda/
├── index.html                         # Portfolio homepage
├── portfolio.css                      # Homepage styling
├── portfolio.js                       # Homepage interactions
├── Project-1_SECOM/
│   ├── notebooks/                     # Main analysis and helper modules
│   ├── documents/                     # Phase records and technical reports
│   ├── figures/                       # Final analytical figures
│   ├── paper/                         # Employer-facing case-study paper
│   ├── raw_data/                      # Public SECOM source data
│   └── website/                       # Completed Project 1 case-study site
├── Project-2WM811k_wafer/
│   ├── notebooks/                     # Project 2 analysis in development
│   ├── documents/                     # Project 2 documentation
│   └── project2_wm811k_wafer_map_tda_guide.md
├── ENVIRONMENT_SETUP.md
└── requirements.txt
```

## Reproducing the analysis

The shared Python dependencies are listed in [`requirements.txt`](requirements.txt). See [`ENVIRONMENT_SETUP.md`](ENVIRONMENT_SETUP.md) for the complete environment and Jupyter-kernel instructions.

A minimal setup begins by creating the environment:

```bash
python -m venv .venv
```

Activate the virtual environment before installing packages. On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

Then install the dependencies and start Jupyter:

```bash
python -m pip install -r requirements.txt
jupyter lab
```

## Previewing the website locally

Run a static server from the repository root:

```bash
python -m http.server 8000
```

Then open [http://127.0.0.1:8000/](http://127.0.0.1:8000/). Serving from the repository root is important because the portfolio homepage uses relative links to each project website.

Future pushes to the selected publishing branch automatically update the website. Deployment status and errors can be inspected from the repository’s **Actions** tab.

See GitHub’s official guide: [Configuring a publishing source for your GitHub Pages site](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

## Data source

McCann, M., & Johnston, A. (2008). *SECOM* [Dataset]. UCI Machine Learning Repository. [https://doi.org/10.24432/C54305](https://doi.org/10.24432/C54305)

## Current project status

Project 1 is complete as an analytical case study. Its feature shortlist is ready for process-context mapping and independent temporal validation, but its classifier should not be deployed as a manufacturing failure detector.

Project 2 is under development and extends the portfolio from anonymous tabular process measurements to spatial wafer-map defect patterns.
