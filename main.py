from datetime import datetime
import requests
import os

import streamlit as st

import prompts
import gpt3
import stable_diffusion


st.set_page_config(page_title="Once Upon AI Time -- by AskEdith", page_icon="story-book.png")

# Don't show certain things
hide_menu_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_menu_style, unsafe_allow_html=True)

# For uploading to Airtable
airtable_prompt = ""
airtable_story = ""
airtable_date = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
airtable_type = ""

st.title("Once Upon AI Time")
st.write("Presented by [AskEdith.ai](https://www.askedith.ai)")

# Generate plot or allow user to prompt
option = st.selectbox("Random or Prompted?", ("Prompted", "Random"))
airtable_type = option

# Read plot from text field if Prompted
plot = ""
if option == "Prompted":
    plot = st.text_area('Prompt')
    if len(plot) == 0:
        st.stop()

# Prevent auto generate
if not st.button("Generate"):
    st.stop()

with st.spinner("Writing..."):

    # Generate plot if empty
    if len(plot) == 0:
        try:
            plot_prompt = prompts.plot()
            plot = gpt3.generate_with_prompt(plot_prompt, 1.0)
        except Exception as e:
            print(e)
            st.warning("Failed to generate story.")
            st.stop()

    airtable_prompt = plot

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

    for i, part in enumerate(parts):

        st.write(part)
        airtable_story += part + "\n\n"

        try:
            image_prompt = prompts.illustration(f"{plot}\n\n{'' if i == 0 else parts[i - 1]}\n\n{part}")
            image_url = stable_diffusion.generate_image(image_prompt)
            airtable_story += image_url + "\n\n"
            st.image(image_url, use_column_width=True)
        except Exception as e:
            print(e)

    # Write to Airtable
    requests.post(
        url="https://api.airtable.com/v0/appZJEELvJrHMxCHq/Table%201",
        headers={
            "Authorization": f"Bearer {os.environ.get('AIRTABLE_API_KEY')}",
            "Content-Type": "application/json",
        },
        json={
            "records": [
                {
                    "fields": {
                        "Prompt": airtable_prompt,
                        "Story": airtable_story,
                        "Date": airtable_date,
                        "Type": airtable_type,
                    }
                }
            ]
        }
    )

st.write("This story is brought to you by [AskEdith.ai](https://www.askedith.ai)")
