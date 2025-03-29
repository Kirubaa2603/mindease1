import streamlit as st
import random
import time

# Set page title and icon
st.set_page_config(page_title="MindEase", page_icon="🧠", layout="wide")

# Sidebar Menu
st.sidebar.title("🌟 MindEase Navigation")
menu = st.sidebar.selectbox("Choose a Feature", ["💬 Chat", "📅 Study Plan", "⏳ Study Timer", "💧 Hydration & Breaks", "🌿 Stress Management"])

# Dictionary of chatbot responses
responses = {
    "exam stress": [
        "Take a deep breath! You’re doing great, just focus on one step at a time. 💙",
        "Exams are tough, but so are you! Stay confident and trust your preparation. 📚✨",
        "Remember, your worth is not defined by a single exam. Just do your best! 🌟"
    ],
    "academic stress": [
        "Learning is a journey, not a race. You’re improving every day! Keep going. 🚀",
        "It’s okay to struggle. Take breaks, hydrate, and come back stronger! 💧",
        "You are more capable than you think. Believe in yourself! 💙"
    ],
    "study plan": [
        "Divide your subjects into small goals and tackle them one by one! ✅",
        "Use the Pomodoro technique: Study for 25 mins, then take a short break. ⏳",
        "Plan your study time wisely—consistency is the key to success! 📅"
    ],
    "hydration": [
        "Have you had water in the last hour? Hydrate and refresh your mind! 💧",
        "Water helps your brain function better. Take a sip now! 🥤",
        "A hydrated brain is a happy brain. Drink up! 🚰"
    ],
    "breaks": [
        "Your mind needs rest too! Take a 5-minute break and stretch a little. 🧘",
        "Overworking can lead to burnout. Pause, breathe, and refresh! 🌿",
        "Breaks improve focus! Step away for a moment and come back stronger. 💪"
    ],
    "positive affirmations": [
        "You are smart, capable, and strong. Keep believing in yourself! 💙",
        "Every challenge is a stepping stone to success. You got this! 🌟",
        "Mistakes are proof that you are trying. Keep pushing forward! 🚀"
    ],
}

# Main Content
if menu == "💬 Chat":
    st.title("🧠 MindEase - Your Student Mental Health Companion 💙")

    # Emotion-based dropdown
    emotion = st.selectbox("How are you feeling today?", ["Select an emotion", "Exam Stress", "Academic Pressure", "Lack of Motivation", "Overwhelmed", "Need Encouragement"])
    
    # Chatbot Response Logic
    user_input = st.text_input("Type your concern or ask for advice:")
    
    if st.button("Send"):
        if emotion != "Select an emotion":
            emotion_key = emotion.lower().replace(" ", "_")
            if emotion_key in responses:
                st.write(random.choice(responses[emotion_key]))
            else:
                st.write("I'm here for you! Stay strong, you've got this! 💙")
        elif user_input:
            found = False
            for key in responses:
                if key in user_input.lower():
                    st.write(random.choice(responses[key]))
                    found = True
                    break
            if not found:
                st.write("I'm here to listen! Let's tackle it together. 💙")

# Study Plan Generator
elif menu == "📅 Study Plan":
    st.title("📚 Study Plan Generator")
    
    subjects = st.text_area("Enter your subjects/topics (comma-separated):")
    study_days = st.slider("Select study duration (days):", 1, 30, 7)
    
    if st.button("Generate Plan"):
        if subjects:
            topics = subjects.split(",")
            plan = {}
            for i, topic in enumerate(topics):
                day = (i % study_days) + 1
                if day not in plan:
                    plan[day] = []
                plan[day].append(topic.strip())

            for day, topic_list in plan.items():
                st.subheader(f"📅 Day {day}")
                for topic in topic_list:
                    st.write(f"📖 Study: {topic}")

# Study Timer
elif menu == "⏳ Study Timer":
    st.title("⏳ Custom Study Timer")
    
    study_minutes = st.number_input("Set your study duration (minutes):", min_value=1, max_value=120, step=1)
    if st.button("Start Timer"):
        st.write(f"Timer started for {study_minutes} minutes. Stay focused! 🚀")
        with st.empty():
            for i in range(study_minutes, 0, -1):
                st.write(f"⏳ {i} minutes remaining...")
                time.sleep(60)
            st.write("⏰ Time's up! Take a short break! 🧘‍♂️")

# Hydration & Break Reminders
elif menu == "💧 Hydration & Breaks":
    st.title("💧 Stay Hydrated & Take Breaks")

    st.subheader("💙 Hydration Reminder")
    if st.button("Hydration Check"):
        st.write(random.choice(responses["hydration"]))

    st.subheader("🌿 Take a Break")
    if st.button("Break Reminder"):
        st.write(random.choice(responses["breaks"]))

# Stress Management
elif menu == "🌿 Stress Management":
    st.title("🌿 Stress Management & Relaxation")

    stress_reduction = [
        "Try deep breathing: Inhale for 4 seconds, hold for 4 seconds, exhale for 4 seconds. 🌬️",
        "Listen to calming music. 🎵",
        "Take a short walk outside to refresh your mind. 🚶‍♂️",
        "Practice mindfulness or guided meditation for 5 minutes. 🧘‍♀️",
        "Write down three things you are grateful for today. ✨",
    ]

    st.subheader("✨ Stress Relief Tips")
    if st.button("Give Me a Tip!"):
        st.write(random.choice(stress_reduction))

# Sidebar Extra Encouragement
st.sidebar.subheader("💙 Need extra motivation?")
if st.sidebar.button("Inspire Me!"):
    st.sidebar.write(random.choice(responses["positive affirmations"]))

