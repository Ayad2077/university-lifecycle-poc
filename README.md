# University Student Lifecycle POC

A Python Streamlit proof of concept for a university student lifecycle platform. This prototype demonstrates how student profile data can be used to generate personalized university recommendations, compare courses, track applications, monitor deadlines, and display academic progress.

## Project Overview

The University Student Lifecycle platform is an EdTech SaaS concept designed to support students from university discovery through academic progress tracking. The Figma wireframe shows the full product vision, while this Python proof of concept validates the core system logic behind the platform.

The prototype focuses on the prospective student experience. It uses demo data to show how a student profile can drive university matching, course recommendations, application tracking, and academic progress insights.

## Purpose of the POC

This proof of concept was built to test whether the platform’s main logic could work before building a full production application.

The POC validates:

* Profile-based university recommendations
* Weighted university match scoring
* Course comparison by ROI, workload, difficulty, and professor rating
* Application progress tracking
* Deadline urgency detection
* Academic progress dashboarding

## Core Features

### Student Dashboard

The dashboard gives students a high-level view of their university search progress, including saved universities, average match score, active applications, upcoming deadlines, top matches, and recommended courses.

### Profile Setup

The profile setup page collects key student information such as GPA, test score, interests, preferred locations, and budget range. This data represents the type of profile information that would drive personalized recommendations in the full product.

### University Search and Rankings

The university search page allows users to filter schools by region, program, and tuition. Universities are ranked using a weighted match score based on academic fit, career fit, financial fit, and location fit.

### Course Finder and Comparison

The course finder allows students to compare courses across programs. The comparison includes professor rating, workload, difficulty level, ROI score, and course match score.

### AI Match Dashboard

The AI Match page demonstrates the recommendation logic behind the platform. It breaks fit into academic, career, and financial categories and shows the top recommended universities based on the student’s profile.

### Application Tracker

The application tracker organizes applications by status: Planning, In Progress, Submitted, and Admitted. It also calculates days left until each deadline and flags urgent applications.

### Academic Progress Dashboard

The academic progress page shows GPA, credits earned, attendance, workload, course performance, milestones, and projected career outcomes.

## Match Score Logic

The university match score is calculated using a weighted scoring model:

```text
Match Score =
Academic Fit × 35%
+ Career Fit × 30%
+ Financial Fit × 20%
+ Location Fit × 15%
```

This scoring model reflects the platform’s goal of recommending universities based on a balanced view of academic compatibility, career outcomes, affordability, and location preference.

## Technology Used

* Python
* Streamlit
* Pandas
* GitHub Codespaces

## How to Run the Project

Install the required packages:

```bash
pip install streamlit pandas
```

Run the Streamlit app:

```bash
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
```

If using GitHub Codespaces, open the app through:

```text
Ports > 8501 > Open in Browser
```

## Demo Data Notice

This project uses sample demo data for proof-of-concept purposes. The numbers shown for universities, courses, applications, and academic progress are used to demonstrate functionality and system logic. In a production version, this data would come from verified university databases, admissions data, labor market sources, course catalogs, and student records.

## Product Vision

The full platform would connect multiple parts of the student lifecycle into one system:

1. University discovery
2. Program comparison
3. AI-powered fit recommendations
4. Course planning
5. Application tracking
6. Academic progress monitoring
7. Alumni and career outcome insights

The goal is to reduce fragmented decision-making and give students a single connected system for evaluating universities, managing applications, and tracking academic progress.

## Future Improvements

Future versions could include:

* Real university datasets
* User authentication
* Persistent database storage
* Interactive application updates
* Live deadline reminders
* Personalized AI explanations
* Admin dashboard for universities
* Employer and alumni outcome tracking
* Deployment to Streamlit Community Cloud or another hosting platform

## Project Status

This is a working Python proof of concept. It is not a full production application. The goal is to validate the core platform logic and show how the Figma product design can be translated into a functional prototype.
