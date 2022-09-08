

def plot() -> str:
    """
    Generate the prompt for creating the plot of a story.
    
    Returns:
        prompt
    """
    return """Write a story plot that's suitable for a short story for children.

Plot:

A girl gets lost in the forest and is helped by a friendly fox. The fox leads her back to safety but the girl's parents are very angry with her.

Write a story plot that's suitable for a short story for children.

Plot:

A young boy wakes up on Christmas morning to find that his presents have all been taken by a group of mischievous monkeys. The boy sets off into the jungle to find the monkeys and get his presents back. Along the way he makes some new friends who help him on his quest. In the end, the boy gets his presents back and learns the true meaning of Christmas.

Write a story plot that's suitable for a short story for children.

Plot:
"""


def story(plot: str) -> str:
    """
    Generate the prompt for creating a story
    
    Returns:
        prompt
    """
    return f"""Write a story using the following plot: A great oak stands near a brook in which some slender reeds grow. The winds blow, and the oak stands upright while the reeds bow low and sing a sad song. The oak complains that the winds don't harm it, but the reeds say that the end is coming. A hurricane rushes out of the north and blows the oak over, and it lies among the reeds.

Story:

A Giant Oak stood near a brook in which grew some slender Reeds. When the wind blew, the great Oak stood proudly upright with its hundred arms uplifted to the sky. But the Reeds bowed low in the wind and sang a sad and mournful song.

"You have reason to complain," said the Oak. "The slightest breeze that ruffles the surface of the water makes you bow your heads, while I, the mighty Oak, stand upright and firm before the howling tempest."

"Do not worry about us," replied the Reeds. "The winds do not harm us. We bow before them and so we do not break. You, in all your pride and strength, have so far resisted their blows. But the end is coming."

As the Reeds spoke a great hurricane rushed out of the north. The Oak stood proudly and fought against the storm, while the yielding Reeds bowed low. The wind redoubled in fury, and all at once the great tree fell, torn up by the roots, and lay among the pitying Reeds.


Write a story using the following plot: {plot}

Story:
"""
