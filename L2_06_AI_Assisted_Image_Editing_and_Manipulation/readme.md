# L2-06: AI Assisted Image Editing and Manipulation	

## Overview

Automate image editing and manipulation tasks using AI.

## Pipeline

```mermaid
flowchart LR
  subgraph Pipeline
    direction LR
    B(Owl-ViT)--Bounding Boxes-->C(SAM)
    C--Seg Masks-->D(Diffusion Model)
  end 
  
  A>Text Prompt]-->B
  D-->E>Final image]

  style B stroke:#f11,stroke-width:4px
  style C stroke:#1f1,stroke-width:4px
  style D stroke:#11f,stroke-width:4px
```

## Contributing

If you want to contribute to this project, you are welcome to do so. You can either add new projects, improve existing ones, or fix bugs and errors. 

Please follow these steps to contribute:

- Fork this repository and clone it to your local machine.
- Create a new branch with a descriptive name for your contribution.
- Add your code and files to the branch and commit your changes.
- Push your branch to your forked repository and create a pull request to the main repository.
- Wait for your pull request to be reviewed and merged.

## References
- [Rethinking Image Editing Detection in the Era of Generative AI Revolution - 2023](https://arxiv.org/pdf/2311.17953.pdf)
- [LEDITS: Real Image Editing with DDPM Inversion and Semantic Guidance](https://huggingface.co/spaces/editing-images/project)
- [Image-Editing Basics and a Tutorial for Automation With AI - Cloudinary](https://cloudinary.com/blog/image_editing_basics_and_a_tutorial_for_automation_with_ai)
- [Revolutionizing Image Editing: How AI is Transforming Photo Retouching](https://topdigital.agency/revolutionizing-image-editing-how-ai-is-transforming-photo-retouching/)



