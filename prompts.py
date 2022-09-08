

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
    return f"""Write a story using the following plot: 
    
A young boy wakes up on Christmas morning to find that his presents have all been taken by a group of mischievous monkeys. The boy sets off into the jungle to find the monkeys and get his presents back. Along the way he makes some new friends who help him on his quest. In the end, the boy gets his presents back and learns the true meaning of Christmas.

Story:

A young boy named Timmy woke up on Christmas morning to find that all of his presents were gone. He looked out the window and saw a group of mischievous monkeys running around with his presents. Timmy was determined to get his presents back, so he set off into the jungle to find the monkeys.

Along the way, Timmy made some new friends who helped him on his quest. He met a friendly lion who showed him the way, a helpful elephant who gave him a ride, and a wise monkey who helped him figure out how to get his presents back.

In the end, Timmy got his presents back and learned the true meaning of Christmas. He learned that Christmas is about giving, not receiving.


Write a story using the following plot:

{plot}

Story:
"""
