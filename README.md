# University Student Lifecycle POC

A **Python + Streamlit proof of concept** for a student decision-support platform. The prototype uses student profile data to rank universities, compare courses, track applications and deadlines, and summarize academic progress in one interface.

## Why I Built It

University planning is often fragmented across ranking sites, spreadsheets, application portals, course catalogs, and career resources. This project explores how those decisions could be brought into one connected workflow.

The goal of the POC is not to simulate a production admissions system. It is to validate the core product logic behind a broader EdTech platform concept.

## What the Prototype Does

- Builds a student profile using GPA, test score, interests, preferred location, and budget
- Ranks universities with a weighted fit model
- Compares courses using ROI, workload, difficulty, and professor ratings
- Tracks application status and upcoming deadlines
- Flags urgent deadlines
- Displays academic progress and performance metrics
- Uses synthetic data so the product logic can be demonstrated without relying on real student records

## Match Scoring Model

The university recommendation score uses four weighted dimensions:

```text
Match Score =
Academic Fit × 35%
+ Career Fit × 30%
+ Financial Fit × 20%
+ Location Fit × 15%
```

The weighting is intentionally simple and transparent for a proof of concept. A production model would require validated data, user research, and more rigorous testing.

## Technology

- Python
- Streamlit
- Pandas

## Run Locally

Clone the repository and install dependencies:

```bash
git clone https://github.com/Ayad2077/university-lifecycle-poc.git
cd university-lifecycle-poc
pip install -r requirements.txt
```

Start the application:

```bash
streamlit run app.py
```

## Repository Contents

```text
university-lifecycle-poc/
├── app.py                                  # Main Streamlit prototype
├── requirements.txt                        # Python dependencies
├── University_Lifecycle_Python_POC_FIXED.ipynb
│                                           # Earlier notebook-based prototype
├── nexus_courses_synthetic.csv             # Synthetic course data
├── nexus_students_synthetic.csv            # Synthetic student data
├── nexus_universities_synthetic.csv         # Synthetic university data
├── nexus_match_results_sample.csv          # Sample recommendation output
└── nexus_predictive_dashboard_sample.csv   # Sample dashboard output
```

## Data Notice

All student, university, course, application, and outcome information in this repository is **demo or synthetic data** created to demonstrate product behavior. It should not be interpreted as verified admissions, tuition, ranking, career, or academic-performance data.

## Product Direction

A fuller version could add:

- Verified university and program datasets
- Authentication and persistent user profiles
- Database-backed application tracking
- Live deadline reminders
- Explainable personalized recommendations
- University administration tools
- Alumni and career outcome data

## Status

This is a working proof of concept intended to demonstrate product thinking, data-driven decision logic, and rapid application prototyping rather than a production-ready platform.
