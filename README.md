# Sinhala Handwritten Character Recognition Project

## Project Overview
This project aims to recognize Sinhala handwritten characters and convert them to digital Unicode text.

## Members
- IT24102111 Thiqa Zibrij A.G
- IT24102160 Gangamini A.H.A
- IT24102051 Madhushan P.S.A.D.Y.
- IT24102031 Disanayaka K.G.G.S
- IT24102090 Bandara D M R M
- IT24102032 Thilina N.A.D.I.D

## Dataset
- Sourced from Kaggle: Sinhala Letter and Modifications
- Link to dataset: [Kaggle Dataset](https://www.kaggle.com/datasets/sathiralamal/sinhala-letter-454)
- >81,000+ images
- Image size: 80x80 JPG
- Stored locally in `data/raw/` (not pushed to GitHub)

## Preprocessing Techniques
Our dataset is already preprocessed and standardized (80x80 JPG images), so further image improvements are limited. However, we explored several preprocessing techniques to optimize model performance:
- **Resizing**: Ensured all images are 80x80 pixels.
- **Data Augmentation**: Applied transformations to increase dataset diversity (rotation, flipping, etc.).
- **Image Normalization**: Scaled pixel values for consistent input.
- **Noise Reduction**: Reduced image noise to improve clarity.
- **Grayscale Conversion**: Converted images to grayscale for simpler feature extraction.
- **Histogram Equalization**: Enhanced image contrast where applicable.

These steps were implemented in the `notebooks/preprocessing/` directory. Due to the dataset's quality, these techniques provide only marginal improvements.

## Next Steps: Group Pipeline
We plan to create a group pipeline that combines the best preprocessing techniques to fit our model and maximize recognition accuracy.
