
import streamlit as st

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
    st.subheader("📅 Your 7-Day Placement Study Plan")

    study_plan = {
        1: "Revise the fundamentals of your weakest skill.",
        2: "Learn important concepts and take notes.",
        3: "Solve 5 beginner-level practice questions.",
        4: "Practice interview questions for your weakest skill.",
        5: "Work on your second-weakest skill.",
        6: "Solve a timed coding or technical quiz.",
        7: "Revise everything and take a mock interview."
    }

    for day, task in study_plan.items():
        st.markdown(f"**Day {day}:** {task}")



