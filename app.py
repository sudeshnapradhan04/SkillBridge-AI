
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
