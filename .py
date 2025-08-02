import streamlit as st
import openai

openai.api_key = st.secrets["openai_key"]

st.title("Phonics Story Studio")
sound_input = st.text_input("Enter 1–3 phonics sounds (e.g. ai, ee, igh):")

if st.button("Generate Story"):
    if sound_input:
        with st.spinner("Writing your story..."):
            prompt = f"Write a decodable children's story using the phonics sounds: {sound_input}. Make it fun, simple, and no more than 150 words."
            story_response = openai.Completion.create(
                engine="gpt-4",
                prompt=prompt,
                max_tokens=250
            )
            story = story_response.choices[0].text.strip()

            q_prompt = f"Write 3 simple comprehension questions based on this story:\n{story}"
            questions_response = openai.Completion.create(
                engine="gpt-4",
                prompt=q_prompt,
                max_tokens=100
            )
            questions = questions_response.choices[0].text.strip()

            st.subheader("📖 Story")
            st.write(story)
            st.subheader("❓ Questions")
            st.write(questions)
    else:
        st.warning("Please enter at least one sound.")
