# L0 - 07: Optical Character Recognition (OCR)

## Overview

This is an Optical Character Recognition (OCR) projet, a sort of Image-To-Text technique using traditional computer vision and deep learning approaches, to recognize and extract text from images.

## Requirements

```
- keras-ocr
- tesseract
- EasyOCR 
```

## Applications

- Image-To-Text
- Convert scanned documents to text
- Handwritten text to machine digital text
- Text extraction and Recognition from images


## Pipeline

![](https://i0.wp.com/theailearner.com/wp-content/uploads/2020/12/OCR_pipeline.png?resize=768%2C265&ssl=1)
(Src: [TheAILearner](https://theailearner.com/2019/05/28/optical-character-recognition-pipeline/))

## Usage

Run the notebook using notebook tools such as Jupyter notebook/lab, Google Colab, Kaggle or any other.

>[!TIP]
> Create a new cell and add the following command to download image resources from github to your Colab or Kaggle environment:

```sh
!wget https://github.com/afondiel/computer-vision-hello-world-challenges/tree/main/06_Zero_Feature_Extraction_Alignment/image_missing_files.png
```

|Notebook|Colab|Kaggle|
|--|--|--|
|[Go to notebook](./L0_07_Optical_Character_Recognition_OCR/Zero_Optical_Character_Recognition_OCR.ipynb)| [![Open notebook in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/afondiel/computer-vision-hello-world-challenges/blob/main/L0_07_Optical_Character_Recognition_OCR/Zero_Optical_Character_Recognition_OCR.ipynb)|[![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](#)|

## Contributing

If you want to contribute to this project, you are welcome to do so. You can either add new projects, improve existing ones, or fix bugs and errors. 

Please follow these steps to contribute:

- Fork this repository and clone it to your local machine.
- Create a new branch with a descriptive name for your contribution.
- Add your code and files to the branch and commit your changes.
- Push your branch to your forked repository and create a pull request to the main repository.
- Wait for your pull request to be reviewed and merged.

## References

HuggingFace

- https://huggingface.co/tasks/image-to-text

Keras: 

- https://github.com/faustomorales/keras-ocr
- https://keras.io/examples/vision/captcha_ocr/
- https://www.analyticsvidhya.com/blog/2022/09/extract-text-from-images-quickly-using-keras-ocr-pipeline/

Google - tesseract
- https://github.com/tesseract-ocr/tesseract
- https://dev.to/ethand91/simple-text-extraction-using-python-and-tesseract-ocr-3b2b
