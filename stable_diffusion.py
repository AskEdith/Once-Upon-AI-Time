import replicate


# Load image model
model = replicate.models.get("stability-ai/stable-diffusion")

def generate_image(prompt: str) -> str:
    """
    Generate an image and get image link.

    Args:
        prompt for image

    Returns:
        image link

    Raises:
        Failed to generate image
    """
    image_url = None

    for _ in range(5):

        try:
            image_url = model.predict(
                prompt=f"Landscape watercolor in the style of John DuVal for the prompt:\n\n{prompt}",
                width=768,
                height=512,
                num_inference_steps=50
            )[0]

            if image_url is not None:
                return image_url
        except:
            pass

    raise RuntimeError("Failed to generate image")
