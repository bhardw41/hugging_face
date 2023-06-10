def logits_to_image(logits):
    # Convert logits to probabilities using softmax
    probabilities = F.softmax(logits, dim=1)

    # Select the probabilities for the desired class (e.g., class 0)
    class_probabilities = probabilities[:, 0, :, :]

    # Convert probabilities to an image
    class_probabilities_np = class_probabilities.detach().numpy()
    class_probabilities_np = class_probabilities_np.squeeze()
    image_array = np.uint8(class_probabilities_np * 255)

    image = Image.fromarray(image_array, mode="L")  # Create grayscale image
    return image
#     # Display or save the image
#     image.show()