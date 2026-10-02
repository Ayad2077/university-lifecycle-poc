# University Student Lifecycle Prototype

A **Python + Streamlit proof of concept** exploring university discovery, course comparison, application planning, and academic progress in one interface.

**Stack:** Python, Streamlit, Pandas  
**Data:** synthetic and illustrative  
**Status:** portfolio prototype

## The Problem

Student planning often spans ranking sites, spreadsheets, course catalogs, and application portals. This prototype explores a connected workflow and demonstrates interactive filtering, weighted scoring, and dashboard presentation.

## What Works in the Demo

| View | Implemented behavior |
| --- | --- |
| University Search | Filter by region, program, and maximum tuition; sort by match score, tuition, or ROI; display a score chart |
| Course Finder | Filter by field and difficulty; select courses for side-by-side comparison |
| Match Dashboard | Rank universities using predefined fit scores and show the weighted scoring breakdown |
| Applications | Group sample applications by status and calculate days remaining and urgency |
| Academic Progress | Display sample GPA trends, course performance, and outcome metrics |
| Profile Setup | Demonstrate the profile form and intended information flow |

## Run Locally

From a terminal:

```bash
git clone https://github.com/Ayad2077/university-lifecycle-poc.git
cd university-lifecycle-poc
python -m venv .venv
```

Activate the environment:

**Windows PowerShell**
```powershell
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux**
```bash
source .venv/bin/activate
```

Install dependencies and launch:

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Open the local URL printed by Streamlit.

## Suggested Walkthrough

1. In **University Search**, change the region or tuition limit and observe the table and chart.
2. In **Course Finder**, filter a field and select courses to compare.
3. In **Match Breakdown**, inspect the four weighted fit dimensions. This implementation uses a deterministic formula.
4. In **Applications**, inspect status groups and deadline urgency.
5. In **Academic Progress**, review the sample charts and metrics.

## Scoring Logic

```text
Match Score =
  Academic Fit × 35%
+ Career Fit × 30%
+ Financial Fit × 20%
+ Location Fit × 15%
```

The app calculates this score from predefined university fit values. Changes to the profile form do not currently recalculate these values. No trained machine-learning model or admissions prediction service is included.

Deadline calculations use a fixed demo date of **May 10, 2026**. An application is marked urgent when its deadline is 0–14 days after that date.

## Repository Contents

```text
university-lifecycle-poc/
├── app.py                                # Streamlit app with embedded demo data
├── requirements.txt                      # Streamlit and Pandas
├── university_lifecycle_analysis.ipynb   # Earlier notebook prototype
├── nexus_courses_synthetic.csv           # Synthetic course dataset
├── nexus_students_synthetic.csv          # Synthetic student dataset
├── nexus_universities_synthetic.csv      # Synthetic university dataset
├── nexus_match_results_sample.csv        # Sample matching output
└── nexus_predictive_dashboard_sample.csv # Sample dashboard output
```

The current Streamlit app uses data defined in `app.py`; it does not load the CSV files. The notebook and CSVs provide additional prototype artifacts.

## Scope & Limitations

- Profile inputs and action buttons illustrate intended workflows. Saving profiles, submitting applications, exporting reports, and scheduling reminders are not implemented.
- Application status, academic results, and headline metrics use fixed sample data.
- There is no authentication, database, or persistent user storage.
- Fit scores, admission likelihoods, tuition, rankings, salaries, and outcomes are demonstration values, not validated predictions or institutional data.
- Dependencies are listed without pinned versions.

All data is demo or synthetic, including values shown alongside real university names. It should not be used for admissions or financial decisions.

## Possible Next Steps

Connect profile inputs to scoring, add persistent application tracking, replace demonstration values with verified datasets, and validate the model with user research.
