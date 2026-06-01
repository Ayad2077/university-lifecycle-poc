import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="University Student Lifecycle POC",
    layout="wide"
)

# --------------------------------------------------
# Demo Data
# --------------------------------------------------

universities = pd.DataFrame([
    {
        "University": "University of Washington",
        "City": "Seattle, USA",
        "Region": "North America",
        "Program": "Business Analytics",
        "Tuition": 35000,
        "Academic Fit": 95,
        "Career Fit": 91,
        "Financial Fit": 85,
        "Location Fit": 97,
        "Admission Likelihood": 78,
        "ROI Score": 8.9,
        "Satisfaction": 4.7
    },
    {
        "University": "University of Toronto",
        "City": "Toronto, Canada",
        "Region": "North America",
        "Program": "Data Science",
        "Tuition": 45000,
        "Academic Fit": 92,
        "Career Fit": 89,
        "Financial Fit": 72,
        "Location Fit": 90,
        "Admission Likelihood": 71,
        "ROI Score": 9.1,
        "Satisfaction": 4.8
    },
    {
        "University": "University of Manchester",
        "City": "Manchester, UK",
        "Region": "Europe",
        "Program": "Finance",
        "Tuition": 32000,
        "Academic Fit": 88,
        "Career Fit": 85,
        "Financial Fit": 82,
        "Location Fit": 87,
        "Admission Likelihood": 68,
        "ROI Score": 8.5,
        "Satisfaction": 4.6
    },
    {
        "University": "National University of Singapore",
        "City": "Singapore",
        "Region": "Asia-Pacific",
        "Program": "Business Analytics",
        "Tuition": 28000,
        "Academic Fit": 88,
        "Career Fit": 93,
        "Financial Fit": 90,
        "Location Fit": 92,
        "Admission Likelihood": 65,
        "ROI Score": 9.3,
        "Satisfaction": 4.9
    },
    {
        "University": "University of Melbourne",
        "City": "Melbourne, Australia",
        "Region": "Asia-Pacific",
        "Program": "Information Systems",
        "Tuition": 38000,
        "Academic Fit": 85,
        "Career Fit": 86,
        "Financial Fit": 75,
        "Location Fit": 83,
        "Admission Likelihood": 62,
        "ROI Score": 8.7,
        "Satisfaction": 4.7
    },
    {
        "University": "Boston University",
        "City": "Boston, USA",
        "Region": "North America",
        "Program": "Business Analytics",
        "Tuition": 50000,
        "Academic Fit": 84,
        "Career Fit": 82,
        "Financial Fit": 70,
        "Location Fit": 88,
        "Admission Likelihood": 70,
        "ROI Score": 8.2,
        "Satisfaction": 4.5
    },
    {
        "University": "Imperial College London",
        "City": "London, UK",
        "Region": "Europe",
        "Program": "Data Science",
        "Tuition": 48000,
        "Academic Fit": 91,
        "Career Fit": 92,
        "Financial Fit": 68,
        "Location Fit": 86,
        "Admission Likelihood": 60,
        "ROI Score": 9.0,
        "Satisfaction": 4.7
    }
])

courses = pd.DataFrame([
    ["Business Analytics Fundamentals", "University of Washington", "Business Analytics", "Undergraduate", 4.8, "12h/week", "Medium", 9.2, 95],
    ["Advanced Data Science", "University of Toronto", "Data Science", "Undergraduate", 4.9, "15h/week", "High", 9.5, 92],
    ["Financial Management & Strategy", "University of Manchester", "Finance", "Undergraduate", 4.6, "10h/week", "Medium", 8.7, 88],
    ["Information Systems Design", "National University of Singapore", "Information Systems", "Undergraduate", 4.7, "11h/week", "Medium", 8.9, 90],
    ["Machine Learning for Business", "University of Melbourne", "Data Science", "Undergraduate", 4.8, "14h/week", "High", 9.3, 91],
], columns=[
    "Course",
    "University",
    "Field",
    "Level",
    "Professor Rating",
    "Workload",
    "Difficulty",
    "ROI Score",
    "Match Score"
])

applications = pd.DataFrame([
    ["University of Melbourne", "MS Business Analytics", "Planning", "2026-06-30", 25, "Research program, Gather documents, Draft SOP"],
    ["INSEAD", "MBA", "Planning", "2026-07-15", 15, "Review requirements, Schedule GMAT"],
    ["University of Washington", "MS Business Analytics", "In Progress", "2026-05-24", 75, "Upload transcripts, Finalize SOP, Submit"],
    ["University of Toronto", "MS Applied Economics", "In Progress", "2026-06-01", 60, "Letter of recommendation, Video essay, Submit"],
    ["University of Manchester", "MSc Data Science", "In Progress", "2026-06-15", 50, "References, Personal statement review, Submit"],
    ["National University of Singapore", "MS Business Analytics", "Submitted", "2026-04-28", 100, "Under review"],
    ["Imperial College London", "MS Business Analytics", "Submitted", "2026-04-15", 100, "Interview scheduled"],
    ["Boston University", "MS Business Analytics", "Admitted", "2026-06-01", 100, "Accept offer"],
], columns=[
    "University",
    "Program",
    "Status",
    "Deadline",
    "Progress",
    "Tasks"
])

academic_courses = pd.DataFrame([
    ["Business Analytics Fundamentals", "Dr. Johnson", 4, "A", "94%", "98%", "12h/week", 75],
    ["Advanced Data Science", "Prof. Martinez", 4, "A-", "91%", "95%", "15h/week", 70],
    ["Financial Management", "Dr. Lee", 4, "A", "95%", "100%", "10h/week", 80],
    ["Statistical Methods", "Prof. Chen", 4, "B+", "88%", "92%", "13h/week", 68],
], columns=[
    "Course",
    "Professor",
    "Credits",
    "Current Grade",
    "Grade %",
    "Attendance",
    "Workload",
    "Progress"
])

# --------------------------------------------------
# Core POC Logic
# --------------------------------------------------

universities["Match Score"] = (
    universities["Academic Fit"] * 0.35
    + universities["Career Fit"] * 0.30
    + universities["Financial Fit"] * 0.20
    + universities["Location Fit"] * 0.15
)

today = datetime(2026, 5, 10)

applications["Days Left"] = applications["Deadline"].apply(
    lambda x: (datetime.strptime(x, "%Y-%m-%d") - today).days
)

applications["Urgency"] = applications["Days Left"].apply(
    lambda x: "Urgent" if 0 <= x <= 14 else "Normal"
)

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.title("University Student Lifecycle")
st.sidebar.caption("EdTech SaaS Platform")
st.sidebar.divider()

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Profile Setup",
        "University Search",
        "Course Finder",
        "AI Match",
        "Applications",
        "Academic Progress"
    ]
)

st.sidebar.divider()
st.sidebar.write("Maya Chen")
st.sidebar.caption("Prospective Student")

# --------------------------------------------------
# Dashboard
# --------------------------------------------------

if page == "Dashboard":
    st.title("Welcome back, Maya Chen")
    st.caption("Your personalized student dashboard")
    st.info("User Type: Prospective Student")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Universities Saved", "12", "+3 this week")

    with col2:
        st.metric("Avg Match Score", "87%", "Excellent fit")

    with col3:
        st.metric("Applications", "5", "In progress")

    with col4:
        st.metric("Next Deadline", "14d", "UW - May 24")

    left, right = st.columns([2, 1])

    with left:
        st.subheader("Top University Matches")

        top_matches = universities.sort_values("Match Score", ascending=False).head(4)

        for _, row in top_matches.iterrows():
            with st.container(border=True):
                st.write(f"**{row['University']}**")
                st.caption(
                    f"Match: {row['Match Score']:.0f}% | "
                    f"Admission Likelihood: {row['Admission Likelihood']}% | "
                    f"Tuition: ${row['Tuition']:,.0f}/yr"
                )

        st.subheader("Recommended Courses")

        st.dataframe(
            courses[[
                "Course",
                "University",
                "Professor Rating",
                "Workload",
                "Difficulty",
                "ROI Score",
                "Match Score"
            ]],
            use_container_width=True,
            hide_index=True
        )

    with right:
        st.subheader("Upcoming Deadlines")

        upcoming = applications.sort_values("Days Left").head(4)

        for _, row in upcoming.iterrows():
            with st.container(border=True):
                st.write(f"**{row['University']}**")
                st.caption(f"{row['Deadline']} | {row['Days Left']} days left")

        st.subheader("Quick Actions")
        st.button("Start New Application", use_container_width=True)
        st.button("Search Universities", use_container_width=True)
        st.button("Compare Programs", use_container_width=True)
        st.button("View AI Matches", use_container_width=True)

# --------------------------------------------------
# Profile Setup
# --------------------------------------------------

elif page == "Profile Setup":
    st.title("Student Profile Setup")
    st.caption("Complete your profile to get personalized recommendations")
    st.info("User Type: Prospective Student")

    st.write("Profile Completion: 60%")
    st.progress(60)

    st.subheader("Personal Information")

    col1, col2 = st.columns(2)

    with col1:
        st.text_input("Full Name", "Maya Chen")
        st.text_input("Phone", "+1 (555) 000-0000")

    with col2:
        st.text_input("Email", "maya.chen@email.com")
        st.text_input("Date of Birth", "mm/dd/yyyy")

    st.subheader("Academic Background")

    col3, col4 = st.columns(2)

    with col3:
        st.number_input("Current GPA", min_value=0.0, max_value=4.0, value=3.8)
        st.number_input("Test Score", min_value=0, max_value=1600, value=1450)

    with col4:
        st.selectbox("Highest Education Level", ["High School", "Associate", "Bachelor"])
        st.selectbox("Preferred Study Level", ["Undergraduate", "Graduate", "MBA"])

    st.subheader("Interests & Preferences")

    st.multiselect(
        "Areas of Interest",
        ["Business Analytics", "Data Science", "Finance", "Computer Science", "Information Systems"],
        ["Business Analytics", "Data Science", "Finance", "Computer Science", "Information Systems"]
    )

    st.multiselect(
        "Preferred Locations",
        ["North America", "Europe", "Asia-Pacific"],
        ["North America", "Europe", "Asia-Pacific"]
    )

    st.slider("Budget Range", 10000, 70000, (20000, 50000), step=5000)

    col5, col6 = st.columns([1, 2])

    with col5:
        st.button("Save Draft")

    with col6:
        st.button("Continue to Dashboard", type="primary")

    st.success("Profile data saved for the POC demo.")

# --------------------------------------------------
# University Search
# --------------------------------------------------

elif page == "University Search":
    st.title("University Search & Rankings")
    st.caption("Discover and compare universities worldwide")
    st.info("User Type: Prospective Student")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        region_filter = st.selectbox("Region", ["All"] + sorted(universities["Region"].unique()))

    with col2:
        program_filter = st.selectbox("Program", ["All"] + sorted(universities["Program"].unique()))

    with col3:
        max_tuition = st.slider("Max Tuition", 10000, 70000, 50000, step=5000)

    with col4:
        sort_by = st.selectbox("Sort by", ["Best Match", "Lowest Tuition", "Highest ROI"])

    filtered = universities.copy()

    if region_filter != "All":
        filtered = filtered[filtered["Region"] == region_filter]

    if program_filter != "All":
        filtered = filtered[filtered["Program"] == program_filter]

    filtered = filtered[filtered["Tuition"] <= max_tuition]

    if sort_by == "Best Match":
        filtered = filtered.sort_values("Match Score", ascending=False)
    elif sort_by == "Lowest Tuition":
        filtered = filtered.sort_values("Tuition", ascending=True)
    else:
        filtered = filtered.sort_values("ROI Score", ascending=False)

    st.write(f"Showing {len(filtered)} universities")

    st.dataframe(
        filtered[[
            "University",
            "City",
            "Program",
            "Match Score",
            "Admission Likelihood",
            "Tuition",
            "ROI Score",
            "Satisfaction"
        ]],
        use_container_width=True,
        hide_index=True
    )

    st.subheader("Match Score Chart")

    if len(filtered) > 0:
        st.bar_chart(filtered.set_index("University")["Match Score"])
    else:
        st.warning("No universities match the selected filters.")

    st.caption(
        "System Response: Filter selection updates the results. "
        "Schools are ranked using Maya's profile and weighted match logic."
    )

# --------------------------------------------------
# Course Finder
# --------------------------------------------------

elif page == "Course Finder":
    st.title("Course Finder & Comparison")
    st.caption("Explore and compare courses across programs")
    st.info("User Type: Prospective Student")

    col1, col2 = st.columns(2)

    with col1:
        field_filter = st.selectbox("Field", ["All"] + sorted(courses["Field"].unique()))

    with col2:
        difficulty_filter = st.selectbox("Difficulty", ["All"] + sorted(courses["Difficulty"].unique()))

    filtered_courses = courses.copy()

    if field_filter != "All":
        filtered_courses = filtered_courses[filtered_courses["Field"] == field_filter]

    if difficulty_filter != "All":
        filtered_courses = filtered_courses[filtered_courses["Difficulty"] == difficulty_filter]

    st.subheader("Course Comparison")

    st.dataframe(
        filtered_courses,
        use_container_width=True,
        hide_index=True
    )

    st.subheader("Selected Courses Comparison")

    default_courses = filtered_courses["Course"].head(2).tolist()

    selected_courses = st.multiselect(
        "Choose courses to compare",
        filtered_courses["Course"].tolist(),
        default_courses
    )

    comparison = filtered_courses[filtered_courses["Course"].isin(selected_courses)]

    columns = st.columns(max(1, len(comparison)))

    for i, (_, row) in enumerate(comparison.iterrows()):
        with columns[i]:
            with st.container(border=True):
                st.write(f"**{row['Course']}**")
                st.caption(row["University"])
                st.write(f"Professor Rating: {row['Professor Rating']}")
                st.write(f"Workload: {row['Workload']}")
                st.write(f"Difficulty: {row['Difficulty']}")
                st.write(f"ROI Score: {row['ROI Score']}/10")
                st.button("Add to Application", key=f"course_{i}")

    st.caption(
        "System Response: Course filters update the table, and selected courses can be compared side by side."
    )

# --------------------------------------------------
# AI Match
# --------------------------------------------------

elif page == "AI Match":
    st.title("AI Personalized Match Dashboard")
    st.caption("Machine learning-powered university recommendations")
    st.info("User Type: Prospective Student")

    st.success(
        "AI Analysis Summary for Maya Chen: Based on GPA, test score, career goals, budget, "
        "and location preferences, the system identified strong university matches."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True):
            st.subheader("Academic Fit")
            st.write("GPA Match: 95%")
            st.progress(95)
            st.write("Test Score Match: 92%")
            st.progress(92)
            st.write("Program Alignment: 88%")
            st.progress(88)

    with col2:
        with st.container(border=True):
            st.subheader("Career Outcomes")
            st.write("Employment Rate: 91%")
            st.progress(91)
            st.write("Salary Potential: 87%")
            st.progress(87)
            st.write("ROI Score: 89%")
            st.progress(89)

    with col3:
        with st.container(border=True):
            st.subheader("Financial Fit")
            st.write("Budget Alignment: 78%")
            st.progress(78)
            st.write("Scholarship Availability: 72%")
            st.progress(72)
            st.write("Cost of Living: 75%")
            st.progress(75)

    st.subheader("Top AI-Recommended Universities")

    top_ai = universities.sort_values("Match Score", ascending=False).head(3)

    for _, row in top_ai.iterrows():
        with st.container(border=True):
            col_a, col_b, col_c = st.columns([3, 1, 1])

            with col_a:
                st.write(f"**{row['University']}**")
                st.caption(
                    f"Academic Fit: {row['Academic Fit']}% | "
                    f"Career Fit: {row['Career Fit']}% | "
                    f"Financial Fit: {row['Financial Fit']}% | "
                    f"Admission Likelihood: {row['Admission Likelihood']}%"
                )

            with col_b:
                st.metric("Match", f"{row['Match Score']:.0f}%")

            with col_c:
                st.button("Apply Now", key=f"apply_{row['University']}")

    col4, col5 = st.columns(2)

    with col4:
        st.success(
            "Strengths: GPA exceeds requirements, test score is competitive, "
            "and business analytics interests align with high-demand programs."
        )

    with col5:
        st.warning(
            "Recommendations: Apply to 2 to 3 reach schools, secure recommendation letters, "
            "and highlight analytics experience."
        )

    st.caption(
        "System Response: Match scores are calculated using Academic 35%, Career 30%, "
        "Financial 20%, and Location 15%."
    )

# --------------------------------------------------
# Applications
# --------------------------------------------------

elif page == "Applications":
    st.title("Application Tracker")
    st.caption("Manage your university applications with Kanban board view")
    st.info("User Type: Prospective Student")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric("Total Applications", len(applications))

    with col2:
        st.metric("In Progress", len(applications[applications["Status"] == "In Progress"]))

    with col3:
        st.metric("Submitted", len(applications[applications["Status"] == "Submitted"]))

    with col4:
        st.metric("Admitted", len(applications[applications["Status"] == "Admitted"]))

    with col5:
        st.metric("Urgent", len(applications[applications["Urgency"] == "Urgent"]))

    statuses = ["Planning", "In Progress", "Submitted", "Admitted"]
    columns = st.columns(4)

    for i, status in enumerate(statuses):
        with columns[i]:
            st.subheader(status)

            status_apps = applications[applications["Status"] == status]

            for _, row in status_apps.iterrows():
                with st.container(border=True):
                    st.write(f"**{row['University']}**")
                    st.caption(row["Program"])
                    st.write(f"Deadline: {row['Deadline']}")
                    st.write(f"Days left: {row['Days Left']}")
                    st.write(f"Progress: {row['Progress']}%")
                    st.progress(row["Progress"])
                    st.caption(f"Tasks: {row['Tasks']}")

                    if row["Urgency"] == "Urgent":
                        st.error("Urgent deadline")

    st.button("Export Application Report", type="primary")
    st.button("Set Reminder")
    st.button("Share Progress")

    st.caption(
        "System Response: Application progress and deadline urgency are calculated automatically."
    )

# --------------------------------------------------
# Academic Progress
# --------------------------------------------------

elif page == "Academic Progress":
    st.title("Academic Progress Dashboard")
    st.caption("Track your academic performance and milestones")
    st.info("User Type: Current Student")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric("Current GPA", "3.85", "+0.15 from last term")

    with col2:
        st.metric("Credits Earned", "43/120", "36% complete")

    with col3:
        st.metric("Cohort Percentile", "92nd", "Top 10%")

    with col4:
        st.metric("Attendance", "96%", "Excellent")

    with col5:
        st.metric("Avg Workload", "14h", "per week")

    col6, col7 = st.columns(2)

    with col6:
        st.subheader("GPA Trend by Semester")

        gpa_data = pd.DataFrame({
            "Semester": ["Fall 2025", "Spring 2026", "Summer 2026"],
            "GPA": [3.70, 3.85, 3.90]
        })

        st.line_chart(gpa_data.set_index("Semester"))

    with col7:
        st.subheader("Current Semester Performance")

        performance_data = pd.DataFrame({
            "Course": ["Bus Analytics", "Data Science", "Finance", "Statistics"],
            "Grade": [4.0, 3.7, 4.0, 3.3]
        })

        st.bar_chart(performance_data.set_index("Course"))

    st.subheader("Current Semester Courses")

    st.dataframe(
        academic_courses,
        use_container_width=True,
        hide_index=True
    )

    st.subheader("Your Profile vs. Alumni Outcomes")

    col8, col9, col10, col11 = st.columns(4)

    with col8:
        st.metric("Employment Rate", "94%", "within 6 months")

    with col9:
        st.metric("Avg Starting Salary", "$78,000", "Business Analytics majors")

    with col10:
        st.metric("Your GPA Rank", "Top 8%", "Among 2026 cohort")

    with col11:
        st.metric("Projected Salary", "$85K+", "Based on profile")

    st.caption(
        "System Response: Academic progress aggregates GPA, course performance, attendance, and career outcome data."
    )

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.divider()

st.caption(
    "Python POC Summary: This prototype validates the core platform logic behind the Figma design, "
    "including student profile setup, university matching, course comparison, application tracking, "
    "deadline urgency, and academic progress reporting."
)