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

st.header("📊 Self-Assess Your Skills")

java = st.slider("Java", 0, 100, 50)
dsa = st.slider("Data Structures & Algorithms", 0, 100, 40)
dbms = st.slider("DBMS", 0, 100, 50)
os = st.slider("Operating Systems", 0, 100, 50)
sql = st.slider("SQL", 0, 100, 50)

if st.button("Analyze My Preparation"):
    scores = {
        "Java": java,
        "DSA": dsa,
        "DBMS": dbms,
        "Operating Systems": os,
        "SQL": sql
    }

    st.subheader(f"Preparation Analysis: {role}")

    average = sum(scores.values()) / len(scores)
    st.metric("Average Self-Assessment", f"{average:.1f}/100")

    weak_topics = [
        topic for topic, score in scores.items()
        if score < 50
    ]

    if weak_topics:
        st.warning("Focus on these topics first:")
        for topic in weak_topics:
            st.write(f"- {topic}")
    else:
        st.success("All assessed topics scored 50 or above!")

    st.subheader("Your Skill Scores")
    st.bar_chart(scores)