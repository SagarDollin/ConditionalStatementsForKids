import streamlit as st
import random
import time
from streamlit.components.v1 import html
# Define the activities and corresponding graphics
activities = {
    'Sit': '🐕‍🦺',
    'Stand': '🐕',
    'Fetch': '🏃‍♂️🐕',
    'Roll Over': '🔄🐕'
}

# Display title and instructions
st.title("Dog Activities")
st.subheader("Conditional Statements", anchor='h3')
st.write("Today we will learn about conditional statements **If** and **Else** by teaching some activities to your virtual dog.")

# st.markdown(f'<h6></h6>', unsafe_allow_html=True)
dog_name = st.text_input(label="**Choose a name for your dog!**",placeholder="Your virtual dog's name")
if dog_name:
    st.success(f'Great! You have named your dog **{dog_name}**.')



    st.write(f"Select an activity that you want to teach **{dog_name}**")
    # Display the activity options
    selected_activity = st.selectbox("Select an activity", list(activities.keys()))

    # Display the dog's graphic based on the selected activity
    cols = st.columns(3)
    with cols[1]:
        st.markdown(f'<p style="font-size:500%">{activities[selected_activity]}</p>', unsafe_allow_html=True)
    if selected_activity:
        cols = st.columns(2)
        with cols[0]:
            reward_options = [f'Give {dog_name} a cookie 🍪', f"Give {dog_name} a biscuit 🍞", f'Give {dog_name} a bone 🦴']
            st.write(f'<p style="font-size:110%"> <b>If</b> {dog_name} can {selected_activity.lower()} select a reward to give.</p>', unsafe_allow_html=True)
            selected_reward = st.radio(label=f"", options=reward_options)
        with cols[1]:
            console_options = [f'Take {dog_name} for a walk 🚶‍♂️🐕', f"Pet {dog_name} 🐾🐶", f'Train {dog_name} again! 🐾🎾🐕‍🦺']
            st.write(f'<p style="font-size:110%"> <b>Else if</b> {dog_name} <b>cannot</b> {selected_activity.lower()} select an option to console</p>', unsafe_allow_html=True)
            selected_console = st.radio(label=f"", options=console_options, label_visibility='collapsed')

        cols = st.columns(3)
        # with cols[1]:
        if st.button(f"Ask {dog_name} to {selected_activity.lower()}"):
            with st.spinner(f"IF {dog_name} does {selected_activity}, It gets reward. Else {dog_name} gets the console"):
                time.sleep(3)
            activity = random.choice([0,1])
            if activity:
                st.markdown(f'<p style="font-size:500%">{activities[selected_activity]}</p>', unsafe_allow_html=True)
                st.success(f"Congratulations, {dog_name} understood your command to {selected_activity.lower()}")
                st.success(f"Now you have to {selected_reward} ")
            else:
                other_activities = list(activities.keys())
                other_activities.remove(selected_activity)
                other_activity = random.choice(other_activities)

                st.markdown(f'<p style="font-size:500%">{activities[other_activity]}</p>', unsafe_allow_html=True)
                st.error(f"Sorry {dog_name} did not understandd your command to {selected_activity.lower()} but instead {other_activity.lower()}")
                st.warning(f"Now you have to {selected_console} ")
            html_file = open("output.html", 'r', encoding='utf-8').read()
            rendered_html = html_file.replace('\n', ' ')
            html(rendered_html, height=500)





    


# Check if the selected activity is 'Sitting' to give the dog a cookie

