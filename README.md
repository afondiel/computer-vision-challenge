# Computer Vision 'Hello World' Challenges 🏆 

## Overview

This is a collection of computer vision foundational projects for anyone diving into the field. By the way, if that's the case, welcome.

The **goal** of this project is to help you learn and practice computer vision skills and concepts in a fun and engaging way.

The project has 3 levels: 
- **Level 0 - Zero (beginner): Getting Started with Basics** 
- **Level 1 - Apprentice (intermediate): Hands-on Computer Vision with Deep Learning**
- **Level 2 - Hero (advanced): Vision LLMs: Image Generation(GANs, VAEs...), Synthesis & Captioning** 

## Recall of a Basic Computer Vision Pipeline

1. Image Acquisition
2. Image Processing
3. Feature Extraction
4. Output, Interpretation & Analysis

## Requirements

You can install the depencies packages using `pip` or `conda`. For example:

create a new conda environment using

```
conda create --name cv-hell-world
```
then,

```bash
pip install -r requirements.txt
```
or 

```bash
conda install --channel conda-forge --file requirements.txt
```

## Hands-on Computer Vision Challenges!

### Level 0 - Zero: Getting Started with Basics 

||Project|Description|Notebooks|
|--|--|--|--|
|[[1]](./01_Zero_Getting_Started_With_Images)| Getting Stated with Images| Load an image, display it, and apply basic transformations.|[![Open notebook in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/afondiel/computer-vision-hello-world-challenges/blob/main/01_Zero_Getting_Started_With_Images/Getting_Started_with_Images.ipynb)|
|[2](#)| Image Manipulation| Modify pixels, resizing, Flipping, Cropping, image annotations|[![Open notebook in Colab](https://colab.research.google.com/assets/colab-badge.svg)](#)|
|[3](#)| Image Filtering & Restoration|	Enhance or manipulate image features using filtering techniques.|[![Open notebook in Colab](https://colab.research.google.com/assets/colab-badge.svg)](#)|
|[4](#)| Image Enhancement|	Enhance using arithmetic & bitwise operations|[![Open notebook in Colab](https://colab.research.google.com/assets/colab-badge.svg)](#)|
|[5](#)| Image Segmentation| segment images into regions or pixels that belong to different classes or categories|[![Open notebook in Colab](https://colab.research.google.com/assets/colab-badge.svg)](#)|
|[6](#)| Feature Extraction & Alignement| Learn how to extract features from images using descriptors based on the nature of the features|[![Open notebook in Colab](https://colab.research.google.com/assets/colab-badge.svg)](#)|
|[7](#)| Optical Character Recognition (OCR)| Learn how to recognize text in images or documents using libraries such as Tesseract, Pytesseract, or EasyOCR|[![Open notebook in Colab](https://colab.research.google.com/assets/colab-badge.svg)](#)|
||||

### Level 1 - Apprentice: Hands-on Computer Vision with Deep Learning

||Project|Description|Notebooks|
|--|--|--|--|
|[1](#)|MNIST Handwritten Digit Recognition	|Train a simple neural network to classify handwritten digits from the MNIST dataset.|[![Open notebook in Colab](https://colab.research.google.com/assets/colab-badge.svg)](#)|
|[2](#)|CIFAR-10 Image Classification	|Utilize convolutional neural networks (CNNs) to classify images of different types of objects from the CIFAR-10 dataset.|[![Open notebook in Colab](https://colab.research.google.com/assets/colab-badge.svg)](#)|
|[3](#)|Object Detection with YOLOv5	|Implement YOLOv5, a real-time object detection algorithm, to detect objects in images and videos.|[![Open notebook in Colab](https://colab.research.google.com/assets/colab-badge.svg)](#)|
|[4](#)|Semantic Segmentation with DeepLabv3+	|Utilize DeepLabv3+, a semantic segmentation model, to segment images into different semantic categories.|[![Open notebook in Colab](https://colab.research.google.com/assets/colab-badge.svg)](#)|
|[5](#)|Facial Recognition with OpenFace	|Explore facial recognition using OpenFace, a facial recognition library, to identify individuals in images.|[![Open notebook in Colab](https://colab.research.google.com/assets/colab-badge.svg)](#)|
|[6](#)| Object Tracking|	Follow the movement of objects in a video sequence.|[![Open notebook in Colab](https://colab.research.google.com/assets/colab-badge.svg)](#)|
|[7](#) | Human Pose Estimation | Estimate the pose of a person in an image or a video using OpenCV and a pre-trained model. |[![Open notebook in Colab](https://colab.research.google.com/assets/colab-badge.svg)](#)|
||||


### Level 2 - Hero: Vision LLMs: Image Generation(GANs, VAEs...), Synthesis & Captioning

||Project|Description|Notebooks|
|--|--|--|--|
|[1](#)|Creative Image Generation with GANs	|Generate novel images of different styles using GANs.|[![Open notebook in Colab](https://colab.research.google.com/assets/colab-badge.svg)](#)|
|[2](#)|Text-to-Image Synthesis with LLMs and Diffusion Models	|Create realistic and creative images from text descriptions using LLMs and diffusion models.|[![Open notebook in Colab](https://colab.research.google.com/assets/colab-badge.svg)](#)|
|[3](#)|AI-Powered Image Restoration and Enhancement	|Restore and enhance images using AI methods.|[![Open notebook in Colab](https://colab.research.google.com/assets/colab-badge.svg)](#)|
|[4](#)|Style Transfer with GANs and Image Processing	|Transfer the artistic style of one image to another.|[![Open notebook in Colab](https://colab.research.google.com/assets/colab-badge.svg)](#)|
|[5](#)|AI-Driven Image Captioning and Storytelling	|Generate comprehensive and creative captions and stories from images using LLMs.|[![Open notebook in Colab](https://colab.research.google.com/assets/colab-badge.svg)](#)|
|[6](#)|AI-Assisted Image Editing and Manipulation	|Automate image editing and manipulation tasks using AI.|[![Open notebook in Colab](https://colab.research.google.com/assets/colab-badge.svg)](#)|
|[7](#)|AI-Powered Image Analysis and Classification	|Analyze and classify images using AI models|[![Open notebook in Colab](https://colab.research.google.com/assets/colab-badge.svg)](#)|
||||

## Usage

Some projects are implemented in Jupyter notebooks, while others have a `main.py` file.

For projects implemented in Jupyter notebooks, run the notebook using:

- jupyter notebook/lab
- Google Colab

For projects with a main.py file, run the following command:
  
```
python main.py
```

## Contributing

If you want to contribute to this project, you are welcome to do so. You can either add new projects, improve existing ones, or fix bugs and errors. 

Please follow these steps to contribute:

- Fork this repository and clone it to your local machine.
- Create a new branch with a descriptive name for your contribution.
- Add your code and files to the branch and commit your changes.
- Push your branch to your forked repository and create a pull request to the main repository.
- Wait for your pull request to be reviewed and merged.


## LICENSE

This project is licensed under the MIT [LICENSE](./LICENSE).

## Reference

Some of the projects in this repository are inspired by or based on the following sources:

- [Computer Vision OpenCV Python Free Course Udemy](https://github.com/afondiel/Computer-Vision-OpenCV-Python-Free-Course-Udemy)
- [Computer Vision Free Course - Kaggle](https://github.com/afondiel/Computer-Vision-Kaggle-Free-Course)
- [Visual Perception for Self-Driving Cars - University of Toronto](https://github.com/afondiel/Self-Driving-Cars-Specialization/tree/main/Course3-Visual-Perception-for-Self-Driving-Cars)
- [The Complete Self-Driving Car Course - Udemy](https://github.com/afondiel/The-Complete-Self-Driving-Car-Course-Udemy)
- [Top Computer Vision Projects (2023) - GeeksforGeeks](https://www.geeksforgeeks.org/computer-vision-projects/)
- [15 Computer Visions Projects You Can Do Right Now - neptune.ai](https://neptune.ai/blog/15-computer-visions-projects)
- [30+ Unique Computer Vision Projects with Source Code – 2023](https://machinelearningprojects.net/opencv-projects/)
- [7+ Computer Vision Projects on GitHub with Source Code 2024 - Omdena](https://omdena.com/blog/computer-vision-projects-github/)
- [20+ Computer Vision Projects Ideas for Beginners in 2023](https://www.projectpro.io/article/computer-vision-projects/437).
-  [A Dive into Vision-Language Models](https://huggingface.co/blog/vision_language_pretraining)
-  [Advances in Visual Pretraining for LLMS | Neil Houlsby](https://www.youtube.com/watch?v=ZwtMEF0u5cM)
-  [VisionLLM: Large Language Model is also an Open-Ended Decoder for Vision-Centric Tasks](https://arxiv.org/pdf/2305.11175.pdf)
-  [LLMs as Visual Explainers: Advancing Image Classification with Evolving Visual Descriptions](https://arxiv.org/pdf/2311.11904.pdf)
-  [Transforming Computer Vision with LLMs - Data Science Dojo](https://datasciencedojo.com/tutorial/transforming-computer-vision-with-llms/)

> ### "Vision is a picture of the future that produces passion." - Bill Hybels


