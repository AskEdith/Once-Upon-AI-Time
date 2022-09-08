import streamlit as st
import openai
import replicate


model = replicate.models.get("stability-ai/stable-diffusion")

# Don't show certain things
hide_menu_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_menu_style, unsafe_allow_html=True)

st.title("AI Short Story")
st.write("Presented by [AskEdith.ai](https://www.askedith.ai)")

story_prompt = st.text_area("Prompt")

# Generate story
response = openai.Completion.create(
    model="text-davinci-002",
    prompt=f"Write a happy short story about: {story_prompt}\n\nStory:\n",
    temperature=0.85,
    max_tokens=500,
    top_p=1,
    frequency_penalty=0.5,
    presence_penalty=0
)
story = response["choices"][0].text

# Content filtered story
response = openai.Completion.create(
    engine="content-filter-alpha",
    prompt="<|endoftext|>" + story + "\n--\nLabel:",
    temperature=0,
    max_tokens=1,
    top_p=0,
    logprobs=10,
)
output_label = response["choices"][0].text
if int(output_label) >= 2:
    st.warning("Could not generate story.")
    st.stop()

parts = story.split("\n\n")
parts = [part for part in parts if len(part) > 0]

for part in parts:

    st.write(part)
    image_url = model.predict(
        prompt=f"Beautiful hand drawn water color image for the prompt: {part}",
        width=768,
        height=512,
        num_inference_steps=50
    )[0]
    st.image(image_url)
