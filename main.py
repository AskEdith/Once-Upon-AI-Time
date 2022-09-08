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

st.title("Once Upon AI Time")
st.write("Presented by [AskEdith.ai](https://www.askedith.ai)")

option = st.selectbox("Random or Prompted?", ("Random", "Prompted"))

story_prompt = "Write a short story.\n\n"
if option == "Prompted":
    input = st.text_area('Prompt')
    story_prompt = f"Write a short story for the prompt:\n\n{input}\n\n"

    if len(input) == 0:
        st.stop()

with st.spinner("Writing..."):

    for _ in range(5):

        # Generate story
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=story_prompt,
            temperature=0.9,
            max_tokens=500,
            top_p=1,
            frequency_penalty=0,
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

        # Regenerate story if failed content filter or story too short
        if int(output_label) < 2 and len(story.split("\n\n")) > 3:
            break

parts = story.split("\n\n")
parts = [part for part in parts if len(part) > 0]

for part in parts:

    st.write(part)

    with st.spinner("Drawing..."):

        image_url = None

        while image_url is None:

            try:
                image_url = model.predict(
                    prompt=f"Landscape watercolor in the style of John DuVal for the prompt:\n\n{part}",
                    width=768,
                    height=512,
                    num_inference_steps=50
                )[0]
            except:
                pass

        st.image(image_url, use_column_width=True)

st.write("This story brought to you by [AskEdith.ai](https://www.askedith.ai)")
rerun = st.button("Rerun")
