import openai


def generate_with_prompt(prompt: str, temperature: float) -> str:
    """
    Generate text given input prompt.
    
    Args:
        prompt: Input prompt
        temperature: Temperature of generation

    Returns:
        output

    Raises:
        RuntimeError: Failed to generate
    """
    # Generate story
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=temperature,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    output = response["choices"][0].text

    # Content filtered story
    response = openai.Completion.create(
        engine="content-filter-alpha",
        prompt="<|endoftext|>" + output + "\n--\nLabel:",
        temperature=0,
        max_tokens=1,
        top_p=0,
        logprobs=10,
    )
    output_label = response["choices"][0].text

    # Regenerate story if failed content filter or story too short
    if int(output_label) < 2:
        return output

    raise RuntimeError("Failed to generate")
