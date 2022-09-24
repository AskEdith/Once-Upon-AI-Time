import urllib.parse
import codecs

import streamlit as st

from utils import prompts, gpt3, stable_diffusion


st.set_page_config(page_title="Once Upon AI Time -- by AskEdith", page_icon="story-book.png")

# Don't show certain things
hide_menu_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_menu_style, unsafe_allow_html=True)

# Load params if relevant
params = st.experimental_get_query_params()
st.experimental_set_query_params()

st.title("OnceUponAITime.com")
st.write("Presented by [AskEdith.ai](https://www.askedith.ai) -- Follow [@jrdzha](https://twitter.com/its_jared_zhao) for updates")

# Generate plot or allow user to prompt
type_ = st.selectbox(
    "Random or Prompted?",
    ("Prompted", "Random"),
    index=(1 if "type" in params and params["type"][0] == "Random" else 0),
)

# Read plot from text field if Prompted
plot = codecs.decode(params["prompt"][0], "rot13") if ("prompt" in params and "type" in params and params["type"][0] == "Prompted") else ""
if type_ == "Prompted":
    plot = st.text_area("Prompt", value=plot)

# Prevent auto generate
if not st.button("Generate") and "story" not in params:
    st.stop()

with st.spinner("Writing..."):

    # Only generate if story is not in URL params
    story = codecs.decode(params["story"][0], "rot13") if "story" in params else ""
    if story == "":

        # Generate plot if empty
        if len(plot) == 0:
            try:
                plot_prompt = prompts.plot()
                plot = gpt3.generate_with_prompt(plot_prompt, 0.8)
            except Exception as e:
                print(e)
                st.warning("Failed to generate story.")
                st.stop()

        # Generate story from plot
        story = plot
        for _ in range(10):
            if len(story.split(". ")) < 20:
                try:
                    story_prompt = prompts.story_expansion(story)
                    story = gpt3.generate_with_prompt(story_prompt, 0.6)
                except Exception as e:
                    print(e)

            break

    # Render story
    parts = story.split("\n\n")
    parts = [part for part in parts if len(part) > 0]

    story_with_images = ""

    for i, part in enumerate(parts):

        # Need to account for when the story is embedded in URL
        if "replicate.com" not in part:
            st.write(part)
            story_with_images += part + "\n\n"
        else:
            image_url = part
            story_with_images += image_url + "\n\n"
            st.image(image_url, use_column_width=True)

        if "replicate.com" not in story:
            try:
                image_prompt = prompts.illustration(f"{plot}\n\n{'' if i == 0 else parts[i - 1]}\n\n{part}")
                image_url = stable_diffusion.generate_image(image_prompt)
                story_with_images += image_url + "\n\n"
                st.image(image_url, use_column_width=True)
            except Exception as e:
                print(e)

story_url = f"https://onceuponaitime.com?type={type_}&prompt={urllib.parse.quote_plus(codecs.encode(plot, 'rot13'))}&story={urllib.parse.quote_plus(codecs.encode(story_with_images, 'rot13'))}"

st.write("Brought to you by [AskEdith.ai](https://www.askedith.ai)")
