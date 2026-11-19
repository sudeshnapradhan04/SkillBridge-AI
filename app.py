
import streamlit as st
from pypdf import PdfReader
import re


st.set_page_config(
    page_title="SkillBridge AI",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 SkillBridge AI")
st.subheader("Your Personal Placement Preparation Assistant")

st.write(
    "Identify skill gaps, assess your preparation, "
    "and prepare smarter for campus placements."
)

st.divider()

st.header("📌 Choose Your Target Role")

role = st.selectbox(
    "Select your placement role",
    [
        "Software Developer",
        "Data Analyst",
        "Machine Learning Engineer"
    ]
)

role_skills = {
    "Software Developer": ["Java", "DSA", "DBMS", "Operating Systems", "SQL"],
    "Data Analyst": ["Python", "SQL", "Statistics", "Data Visualization", "DBMS"],
    "Machine Learning Engineer": ["Python", "Machine Learning", "Statistics", "SQL", "Data Structures"]
}

required_skills = role_skills[role]

st.info(f"Recommended skills for {role}: {', '.join(required_skills)}")

st.header("📊 Self-Assess Your Skills")

skill_scores = {}

for skill in required_skills:
    key = f"{role}_{skill}"
    skill_scores[skill] = st.slider(
        skill,
        min_value=0,
        max_value=100,
        value=50,
        key=key
    )

if st.button("Analyze My Preparation"):
    average = sum(skill_scores.values()) / len(skill_scores)

    st.subheader(f"Preparation Analysis: {role}")
    st.metric("Average Self-Assessment", f"{average:.1f}/100")

    if average < 40:
        st.info("Start with fundamentals and practice basic questions daily.")
    elif average < 60:
        st.info("Focus on core concepts and solve beginner-level problems.")
    elif average < 80:
        st.info("Practice interview questions and timed coding problems.")
    else:
        st.success("Great progress! Focus on mock interviews and revision.")

    weak_skills = {
        skill: score
        for skill, score in skill_scores.items()
        if score < 60
    }

    if weak_skills:
        st.warning("Skills to improve:")
        for skill, score in weak_skills.items():
            st.write(f"- {skill}: {score}/100")
    else:
        st.success("Great! All assessed skills are at least 60/100.")

    st.subheader("Your Skill Scores")
    st.bar_chart(skill_scores)
    
    st.subheader("🎯 Skill Improvement Priorities")

    priority_skills = sorted(
        skill_scores.items(),
        key=lambda item: item[1]
    )

    for skill, score in priority_skills:
        if score < 60:
            st.write(f"🔴 High priority: {skill} — {score}/100")
        elif score < 80:
            st.write(f"🟡 Medium priority: {skill} — {score}/100")
        else:
            st.write(f"🟢 Maintain: {skill} — {score}/100")
            
    st.divider()
    st.subheader("📚 Your Personalized Study Roadmap")

    study_tasks = {
        "Java": [
            "Revise variables, loops, arrays, and OOP.",
            "Solve 3 beginner Java coding problems."
        ],
        "DSA": [
            "Study arrays, strings, and searching.",
            "Practice 3 easy DSA problems."
        ],
        "Data Structures": [
            "Learn arrays, linked lists, stacks, and queues.",
            "Solve 3 beginner problems."
        ],
        "DBMS": [
            "Revise keys, normalization, and joins.",
            "Practice SQL queries and DBMS interview questions."
        ],
        "Operating Systems": [
            "Study processes, threads, and CPU scheduling.",
            "Revise deadlocks and memory management."
        ],
        "SQL": [
            "Practice SELECT, JOIN, GROUP BY, and subqueries.",
            "Solve 5 beginner SQL questions."
        ],
        "Python": [
            "Revise functions, lists, dictionaries, and loops.",
            "Solve 3 Python coding problems."
        ],
        "Statistics": [
            "Study mean, median, standard deviation, and probability.",
            "Practice basic statistics questions."
        ],
        "Data Visualization": [
            "Learn charts using Matplotlib and Plotly.",
            "Create charts from a small dataset."
        ],
        "Machine Learning": [
            "Revise regression, classification, and model evaluation.",
            "Build a small model using scikit-learn."
        ]
    }

    for skill, score in priority_skills:
        if score < 60:
            st.markdown(f"**🎯 {skill} — Start here ({score}/100)**")
            for task in study_tasks.get(
                skill,
                ["Revise the fundamentals.", "Practice beginner-level questions."]
            ):
                st.write(f"- {task}")
                
        
st.divider()
st.header("✅ Track Your Study Progress")

daily_tasks = [
    "Day 1: Revise fundamentals",
    "Day 2: Learn important concepts",
    "Day 3: Solve 5 practice questions",
    "Day 4: Practice interview questions",
    "Day 5: Study your second-weakest skill",
    "Day 6: Take a timed technical quiz",
    "Day 7: Complete a mock interview"
]

completed = 0

for i, task in enumerate(daily_tasks):
    if st.checkbox(task, key=f"progress_day_{i+1}"):
        completed += 1

st.progress(completed / len(daily_tasks))
st.write(f"**Progress: {completed}/7 days completed**")
st.divider()

st.header("📄 Resume Analysis & Job Matching")

uploaded_resume = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste the Job Description here",
    height=200,
    placeholder="Paste the job description..."
)
if st.button("Analyze Resume"):
    if uploaded_resume is None:
        st.warning("Please upload your resume PDF.")

    elif not job_description.strip():
        st.warning("Please paste the job description.")

    else:
        pdf_reader = PdfReader(uploaded_resume)

        resume_text = ""
        for page in pdf_reader.pages:
            resume_text += page.extract_text() or ""

        if not resume_text.strip():
            st.error("Could not extract text from this PDF. Please upload a text-based PDF.")
        else:

            st.success("Resume uploaded and text extracted successfully!")

            # Define technical skills
            all_skills = [
                "Java", "Python", "SQL", "DSA", "DBMS",
                "Operating Systems", "Machine Learning",
                "Statistics", "HTML", "CSS", "JavaScript",
                "Communication", "Problem Solving"
            ]

            # Find skills in job description
            jd_lower = job_description.lower()
            resume_lower = resume_text.lower()

            required_skills = [
                skill for skill in all_skills
                if skill.lower() in jd_lower
            ]

            # Find matching and missing skills
            matched_skills = [
                skill for skill in required_skills
                if skill.lower() in resume_lower
            ]

            missing_skills = [
                skill for skill in required_skills
                if skill.lower() not in resume_lower
            ]

            # Calculate match percentage
            if required_skills:
                match_score = (len(matched_skills) / len(required_skills)) * 100
            else:
                match_score = 0

            st.subheader("📊 Resume Match Results")
            st.metric("Resume Match Score", f"{match_score:.1f}%")
            st.progress(match_score / 100)

            st.subheader("✅ Matching Skills")
            st.write(matched_skills if matched_skills else "No matching skills found.")

            st.subheader("❌ Missing Skills")
            st.write(missing_skills if missing_skills else "No missing skills!")

           
            st.subheader("💡 Smart Skill Recommendations")

            for skill in missing_skills:
                if skill in ["Java", "Python", "DSA", "SQL"]:
                    priority = "High"
                    suggestion = f"Learn {skill} fundamentals and solve beginner-level problems."

                elif skill in ["DBMS", "Operating Systems", "Machine Learning", "Statistics"]:
                    priority = "Medium"
                    suggestion = f"Study core concepts of {skill} and practice examples."

                else:
                    priority = "Low"
                    suggestion = f"Build practical knowledge of {skill} through small projects."

                st.write(f"**{skill} — {priority} Priority**")
                st.info(suggestion)

                                