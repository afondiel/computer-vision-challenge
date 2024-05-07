# Zero - 06: Basic Image Features and Alignment

## Overview

Basic Image Features and Alignment in computer vision pipelines.

**Read template and scanned Image:**

`Image => Operation => Final Image`

**Visual Feature Extraction pipeline:**

Features: points of interest in an img, defined by its pixel coord[u,v]

- Feature types
    - Edges
    - Corners/interest points
    - Blobs/region of interest points
    - Ridges 

`Detection => Description => Matching`

We use `descriptor` to extract feature keypoints from the image
- Keypoints: feature types described by pixels coord(u,v)
- Descriptor: image summary: [f1...fN], where f: img feature [u,v]

Descriptor types based on the type of features: 
- SIFT, SURF, GLOH, BRIEF, ORB (Oriented Fast and Rotated Brief) ...

- We later use the descriptor to match up the keypoints of two image
- Finally apply the homagraphy

## Requirements

- Jupyter Notebook
- JupyterLab
- Colab
- Kaggle
  
## Usage

To run the notebook, use Jupyter notebook, Google Colab, Kaggle or any other notebook tool.

>[!TIP]
> Use the following command to download image resources from github to your Colab or Kaggle environment:

```sh
!wget https://github.com/afondiel/computer-vision-hello-world-challenges/tree/main/06_Zero_Feature_Extraction_Alignment/image_files.png
```

|Notebook|Colab|Kaggle|
|--|--|--|
|[Go to notebook](06_Zero_Feature_Extraction_Alignment\Image_Features_and_Image_Alignment.ipynb)| [![Open notebook in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/afondiel/computer-vision-hello-world-challenges/blob/main/06_Zero_Feature_Extraction_Alignment/Image_Features_and_Image_Alignment.ipynb)|[![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://www.kaggle.com/code/thepostitguy/object-tracking-deep-sort/edit)|

## Contributing

If you want to contribute to this project, you are welcome to do so. You can either add new projects, improve existing ones, or fix bugs and errors. 

Please follow these steps to contribute:

- Fork this repository and clone it to your local machine.
- Create a new branch with a descriptive name for your contribution.
- Add your code and files to the branch and commit your changes.
- Push your branch to your forked repository and create a pull request to the main repository.
- Wait for your pull request to be reviewed and merged.

