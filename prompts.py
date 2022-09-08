"""
Generate prompts for different tasks.
"""


def plot() -> str:
    """
    Generate the prompt for creating the plot of a story.
    
    Returns:
        prompt
    """
    return "Create a detailed prompt and plot for a new happy children's short story. The story can be about animals, people, children, adventure, morals, or anything you want.\n\n"


def story_expansion(existing_story: str) -> str:
    """
    Expand a given story.

    Returns:
        prompt
    """
    return f"Rewrite this as a 2 page story with much more detail and a happy ending. Give the characters names and describe the environment and plot in greater detail:\n\n{existing_story}\n\n"


def illustration(story: str) -> str:
    """
    Illustrate a part of the story.

    Returns:
        prompt
    """
    return f"Landscape watercolor in the style of John DuVal for the scene:\n\n{story}"
