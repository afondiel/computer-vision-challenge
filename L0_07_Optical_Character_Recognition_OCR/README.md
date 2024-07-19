# L0 - 07: Optical Character Recognition (OCR)

## Overview

This is an Optical Character Recognition (OCR) projet, a specific type of `Image-To-Text technique` using traditional computer vision and deep learning approaches, to recognize and extract text from images.

**Popular OCR Tools**

| Name | Description | Pros | Cons |
|---|---|---|---|
| Tesseract-OCR (Tesseract) | Core OCR engine (C++) | Powerful, open-source | Not directly usable in Python |
| Tesserocr | Python wrapper for Tesseract-OCR C++ API | Less common, allows Python use | Might be less user-friendly than PyTesseract |
| PyTesseract | Python library for Tesseract-OCR | Simple to use, powerful | Requires separate Tesseract-OCR installation |
| EasyOCR | Separate Python library for OCR | Lightweight, good for receipts/PDFs, multi-language | Might not be as powerful as Tesseract-OCR for all tasks |
| Keras-OCR | Python library built on Keras/TensorFlow | User-friendly, deep learning approach | Might require more computing resources |
| Ocrad/GOCR | Open-source OCR engines | Established, free options | May have lower accuracy compared to newer libraries |
| ocropus/Calamari | Free, open-source OCR with LSTMs | Potentially high accuracy | May be more complex to set up |
| Amazon Textract | Cloud-based OCR service (AWS) | High accuracy, scalable, pre-built functionalities | Requires paid AWS account |
| Microsoft Azure Cognitive Services - Computer Vision | Cloud-based OCR solution (Microsoft) | Various features, text extraction, document processing | Requires paid Azure account |
| Google Cloud Vision API | Cloud-based OCR with image intelligence functionalities | Offered by Google Cloud Platform | Requires paid GCP account |

## Requirements

```
- tesseract-ocr
- libtesseract-dev
- pytesseract
- pillow
- io
- matplotlib.pyplot
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

Open the notebook using Google Colab (link below), Kaggle, Jupyter notebook/lab or a similar tool.

>[!TIP]
> Create a new cell and add the following command to download project resources from github to your Colab or Kaggle environment if needed:

```sh
!wget https://github.com/afondiel/computer-vision-hello-world-challenges/tree/main/06_Zero_Feature_Extraction_Alignment/image_missing_files.png
```

|Notebook|Colab|Kaggle|
|--|--|--|
|[Go to notebook](./L0_07_Optical_Character_Recognition_OCR/Zero_Optical_Character_Recognition_OCR.ipynb)| [![Open notebook in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/afondiel/computer-vision-challenge/blob/main/L0_07_Optical_Character_Recognition_OCR/notebooks/OCR_Pytesseract.ipynb)|[![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](#)|

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

OCR in age of LMM:
- [Tradition OCR vs Text Extraction from Image using Google Gemini ](https://medium.com/google-cloud/text-extraction-from-image-using-google-gemini-6b9d9989fa84)
