# CAPTCHA Generation Module

This module provides functionality for generating CAPTCHA images with random text and various visual effects. The CAPTCHAs are designed to be challenging for bots while remaining user-friendly for human users.

## Features

- **Random Text Generation**: Generates random strings using English or Russian characters, including digits.
- **3D Text Effects**: Renders text with a 3D effect for enhanced visual appeal.
- **Background Noise**: Creates a random background filled with noise and geometric shapes.
- **Text Distortion**: Applies distortion effects to individual letters, making them harder to recognize by bots.
- **Connecting Lines**: Draws straight lines connecting the centers of letters for added complexity.
- **Customizable Options**: Allows users to choose between English and Russian character sets.

## Requirements

- Python 3.x
- Pillow (for image processing)
- NumPy (for numerical operations)

## Installation

To install the required libraries, run:

```bash
pip install pillow numpy
```

## Usage

To use the CAPTCHA generation module, follow these steps:

1. Import the necessary functions from the `captcha_generator.py` file.
2. Call the `generate_3d_captcha` function to create a CAPTCHA image.

### Example

Here’s a simple example of how to generate and display a CAPTCHA:

```python
from captcha_generator import generate_3d_captcha
import matplotlib.pyplot as plt

# Generate a CAPTCHA image
captcha_image = generate_3d_captcha(use_russian=False)  # Set to True for Russian text

# Display the generated CAPTCHA image
plt.imshow(captcha_image)
plt.axis('off')  # Hide axes
plt.show()

## License

This project is licensed under the MIT License - see the [Unlicense](unlicense.org) file for details.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## Acknowledgements

This module was inspired by the need for effective CAPTCHA solutions in web applications. Thank you for using this library!
