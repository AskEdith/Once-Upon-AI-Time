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

st.title("Once Upon AI Time")
st.write("Presented by [AskEdith.ai](https://www.askedith.ai)")

# Generate plot or allow user to prompt
option = st.selectbox("Random or Prompted?", ("Random", "Prompted"))

with st.spinner("Writing..."):

    plot = None
    if option == "Random":
        plot_prompt = prompts.plot()
        try:
            plot = gpt3.generate_with_prompt(plot_prompt, 1.0)
        except Exception as e:
            print(e)
            st.warning("Failed to generate story.")
            st.stop()

    elif option == "Prompted":
        plot = st.text_area('Prompt')

        if len(plot) == 0:
            st.stop()

    # Generate story from plot
    story = plot
    print(f"Writing story using plot: {plot}")
    for _ in range(10):
        if len(story.split(". ")) < 20:
            try:
                story_prompt = prompts.story_expansion(story)
                story = gpt3.generate_with_prompt(story_prompt, 0.6)
            except Exception as e:
                print(e)

        break

    parts = story.split("\n\n")
    parts = [part for part in parts if len(part) > 0]

    for i, part in enumerate(parts):

        st.write(part)

        try:
            image_prompt = prompts.illustration(f"{parts[max(i - 1, 0)]}\n\n{parts[max(i, 0)]}")
            image_url = stable_diffusion.generate_image(image_prompt)
            st.image(image_url, use_column_width=True)
        except Exception as e:
            print(e)

st.write("This story brought to you by [AskEdith.ai](https://www.askedith.ai)")
rerun = st.button("Rerun")
