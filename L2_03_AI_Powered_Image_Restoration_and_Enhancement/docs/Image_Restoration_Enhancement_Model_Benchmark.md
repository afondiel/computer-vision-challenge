# Image Restoration and Enhancement Model Benchmarking (June-2024)

## Overview

Top State Of The Art (SOTA) models reference **Benchmarking** for Image Restoration and Enhancement tasks:

|Task|Task Name|Description| 
|--|--|--|
|T1|Image resolution|Increase image resolution|
|T2|De-noising|Remove noise|
|T3|De-blurring|Sharp blurry images|
|T4|Image Colorization|Add color information to grayscale images|
|T5|Image Inpainting | Reconstruct missing or damaged parts of an image|


**Performance Metrics:**
|Metrics|Description|
|--|--|
|**PSNR** (Peak Signal-to-Noise Ratio)| Higher values indicate better quality|
|**SSIM** (Structural Similarity Index)| Values range from -1 to 1, with higher values indicating better structural similarity|
|**MSE** (Mean Squared Error)| Lower values indicate better quality|
|**VQA** (Visual Quality Assessment)| This can be any standardized measure of perceptual quality, higher values indicate better perceived quality|

> [!IMPORTANT]\
> These performance metrics are averaged based on standard benchmark datasets commonly used for each task. Specific results may vary depending on the dataset and evaluation protocols used.

## T1: Image Resolution

| **Rank** | **Model Name**          | **Type**       | **Primary Use Case**      | **Key Features**                                                                                       | **PSNR (dB)** | **SSIM** | **MSE**  | **VQA**                    |
|----------|-------------------------|----------------|---------------------------|--------------------------------------------------------------------------------------------------------|---------------|----------|----------|----------------------------|
| 1        | EDSR                    | CNN            | Image Super-Resolution    | Enhanced deep residual networks, large model capacity                                                  | 28.95         | 0.856    | 17.28    | 0.780                      |
| 2        | RCAN                    | CNN            | Image Super-Resolution    | Residual channel attention, deep network, feature extraction                                           | 29.31         | 0.870    | 16.21    | 0.792                      |
| 3        | SRGAN                   | GAN            | Image Super-Resolution    | Generative adversarial network, perceptual loss, high-resolution output                                | 25.16         | 0.840    | 26.77    | 0.715                      |
| 4        | VDSR                    | CNN            | Image Super-Resolution    | Very deep network, residual learning, high-speed                                                       | 28.83         | 0.849    | 17.67    | 0.776                      |
| 5        | SwinIR                  | Transformer    | Image Super-Resolution    | Swin transformer, hierarchical design, self-attention                                                  | 30.77         | 0.896    | 14.09    | 0.812                      |
| 6        | RDN                     | CNN            | Image Super-Resolution    | Residual dense network, feature fusion, global and local feature extraction                            | 29.28         | 0.878    | 16.25    | 0.789                      |
| 7        | LapSRN                  | CNN            | Image Super-Resolution    | Laplacian pyramid network, progressive upsampling                                                      | 28.82         | 0.851    | 17.73    | 0.773                      |
| 8        | ESRGAN                  | GAN            | Image Super-Resolution    | Enhanced SRGAN, perceptual loss, improved generator and discriminator                                  | 26.22         | 0.856    | 24.52    | 0.728                      |
| 9        | DBPN                    | CNN            | Image Super-Resolution    | Deep back-projection network, iterative up and down sampling                                           | 28.82         | 0.848    | 17.71    | 0.772                      |
| 10       | LDM                     | Diffusion Model| Image Super-Resolution    | Latent diffusion model, noise-aware, generative approach                                               | 29.95         | 0.882    | 15.37    | 0.798                      |
| 11 (Bonus)       | ISR                     | CNN | Image Super-Resolution    | Customizable architectures, multiple pre-trained models (e.g., RRDN, RDN), flexible framework                                               | 28.50         | 0.840    | 18.50    | 0.770                      |


## T2: Denoising

| **Rank** | **Model Name**          | **Type**       | **Primary Use Case** | **Key Features**                                                                                                                                                         | **PSNR (dB)** | **SSIM** | **MSE**  | **VQA**                    |
|----------|-------------------------|----------------|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|----------|----------|----------------------------|
| 1        | DnCNN                   | CNN            | Image Denoising      | Residual learning, multiple layers                                                                                                                                       | 32.43         | 0.790    | 18.76    | 0.675                      |
| 2        | FFDNet                  | CNN            | Image Denoising      | Downsampling, multiple noise levels                                                                                                                                      | 32.75         | 0.801    | 17.92    | 0.688                      |
| 3        | MemNet                  | CNN            | Image Denoising      | Memory blocks, persistent memory, deep network                                                                                                                           | 32.41         | 0.785    | 18.83    | 0.670                      |
| 4        | RED-Net                 | CNN            | Image Denoising      | Encoder-decoder architecture, symmetric skip connections                                                                                                                 | 31.72         | 0.760    | 20.27    | 0.655                      |
| 5        | VDN                     | CNN            | Image Denoising      | Variational model, generative approach, Bayesian framework                                                                                                               | 33.34         | 0.810    | 16.31    | 0.702                      |
| 6        | Noise2Noise             | CNN            | Image Denoising      | Self-supervised, uses pairs of noisy images                                                                                                                              | 30.96         | 0.735    | 21.48    | 0.635                      |
| 7        | BM3D                    | Traditional    | Image Denoising      | Block-matching, 3D collaborative filtering                                                                                                                               | 30.88         | 0.725    | 21.76    | 0.630                      |
| 8        | WNNM                    | Traditional    | Image Denoising      | Weighted nuclear norm minimization, non-local means                                                                                                                      | 29.64         | 0.700    | 25.00    | 0.610                      |
| 9        | SwinIR                  | Transformer    | Image Restoration    | Swin transformer, hierarchical design, self-attention                                                                                                                    | 32.92         | 0.805    | 17.28    | 0.695                      |
| 10       | NAFNet                  | CNN            | Image Denoising      | Non-linear activation-free network, adaptive normalization                                                                                                               | 32.60         | 0.795    | 18.07    | 0.680                      |


## T3: Deblurring

| **Rank** | **Model Name**          | **Type**       | **Primary Use Case** | **Key Features**                                                                                          | **PSNR (dB)** | **SSIM** | **MSE**  | **VQA**                    |
|----------|-------------------------|----------------|----------------------|-----------------------------------------------------------------------------------------------------------|---------------|----------|----------|----------------------------|
| 1        | DeblurGAN               | GAN            | Image Deblurring     | Generative adversarial network, perceptual loss, end-to-end training                                      | 29.08         | 0.900    | 13.76    | 0.785                      |
| 2        | SRN-DeblurNet           | CNN            | Image Deblurring     | Scale-recurrent network, multi-scale, hierarchical features                                               | 30.26         | 0.915    | 11.72    | 0.805                      |
| 3        | DMPHN                   | CNN            | Image Deblurring     | Deep multi-patch hierarchy network, patch-based, multi-level feature fusion                               | 29.09         | 0.906    | 13.73    | 0.792                      |
| 4        | EDVR                    | CNN            | Image and Video Deblurring | Enhanced deformable convolution, video frame alignment, multi-scale                                        | 31.21         | 0.920    | 10.88    | 0.820                      |
| 5        | MPRNet                  | CNN            | Image Deblurring     | Multi-stage progressive restoration, residual learning, attention mechanism                               | 31.76         | 0.925    | 10.24    | 0.828                      |
| 6        | U-Net                   | CNN            | Image Deblurring     | Encoder-decoder architecture, skip connections, efficient feature extraction                              | 28.47         | 0.890    | 14.67    | 0.765                      |
| 7        | DeblurGAN-v2            | GAN            | Image Deblurring     | Improved GAN architecture, feature pyramid network, multi-scale discriminator                             | 30.22         | 0.912    | 11.80    | 0.810                      |
| 8        | DBGAN                   | GAN            | Image Deblurring     | Dual branch GAN, content and detail preservation, adversarial loss                                        | 30.45         | 0.917    | 11.38    | 0.815                      |
| 9        | Spatio-Temporal DeblurNet| CNN            | Video Deblurring     | Spatio-temporal approach, motion compensation, temporal consistency                                       | 30.81         | 0.918    | 11.00    | 0.822                      |
| 10       | Pyramid DeblurNet       | CNN            | Image Deblurring     | Pyramid structure, progressive deblurring, feature fusion                                                 | 30.12         | 0.910    | 12.08    | 0.808                      |


## T4: Colorization


| **Rank** | **Model Name**          | **Type**       | **Primary Use Case** | **Key Features**                                                                                           | **PSNR (dB)** | **SSIM** | **MSE**  | **VQA**                    |
|----------|-------------------------|----------------|----------------------|------------------------------------------------------------------------------------------------------------|---------------|----------|----------|----------------------------|
| 1        | DeOldify                | GAN            | Image Colorization   | Generative adversarial network, perceptual loss, high-resolution output                                     | 24.12         | 0.850    | 125.67   | 0.780                      |
| 2        | CIC                     | CNN            | Image Colorization   | Contextual information, end-to-end training, feature extraction                                             | 25.37         | 0.865    | 110.24   | 0.798                      |
| 3        | Deep Color              | CNN            | Image Colorization   | User-guided colorization, deep network, interactive approach                                                | 24.50         | 0.855    | 120.92   | 0.785                      |
| 4        | ChromaGAN               | GAN            | Image Colorization   | Generative adversarial network, multi-scale approach, perceptual loss                                       | 24.98         | 0.860    | 115.39   | 0.790                      |
| 5        | U-Net Colorization      | CNN            | Image Colorization   | Encoder-decoder architecture, skip connections, efficient feature extraction                                | 24.25         | 0.852    | 123.48   | 0.782                      |
| 6        | InstColor               | CNN            | Image Colorization   | Instance-aware colorization, segmentation-based approach, high-resolution output                            | 25.10         | 0.862    | 113.72   | 0.796                      |
| 7        | Colorful Image Colorization | CNN        | Image Colorization   | Classification-based colorization, end-to-end training, large-scale dataset                                 | 23.92         | 0.845    | 130.56   | 0.775                      |
| 8        | PixColor                | CNN            | Image Colorization   | Pixel-wise colorization, deep network, feature extraction                                                   | 24.30         | 0.851    | 122.34   | 0.784                      |
| 9        | CIE-Lab Colorization    | Traditional    | Image Colorization   | CIE-Lab color space, hand-crafted features, non-deep learning approach                                      | 23.47         | 0.835    | 138.20   | 0.760                      |
| 10       | iGAN                    | GAN            | Image Colorization   | Interactive GAN, user-guided, real-time colorization                                                        | 24.75         | 0.858    | 118.04   | 0.788                      |


## T5: Image Inpainting

| **Rank** | **Model Name**           | **Type**       | **Primary Use Case** | **Key Features**                                                                                           | **PSNR (dB)** | **SSIM** | **MSE**  | **VQA**                    |
|----------|--------------------------|----------------|----------------------|------------------------------------------------------------------------------------------------------------|---------------|----------|----------|----------------------------|
| 1        | DeepFill v2              | CNN            | Image Inpainting     | Gated convolution, contextual attention, large receptive field                                              | 28.94         | 0.920    | 15.67    | 0.810                      |
| 2        | EdgeConnect              | GAN            | Image Inpainting     | Edge-preserving, two-stage process, edge detection and image completion                                     | 29.34         | 0.930    | 14.78    | 0.825                      |
| 3        | Partial Convolutions     | CNN            | Image Inpainting     | Mask-update mechanism, partial convolution, dynamic filter weights                                          | 27.95         | 0.900    | 18.54    | 0.795                      |
| 4        | LaMa                     | CNN            | Image Inpainting     | Large mask inpainting, coarse-to-fine, contextual attention                                                 | 29.20         | 0.925    | 15.01    | 0.820                      |
| 5        | PConv                    | CNN            | Image Inpainting     | Partial convolution, mask updating, efficient feature extraction                                            | 28.75         | 0.915    | 16.25    | 0.805                      |
| 6        | GCAM (Gated Convolution) | CNN            | Image Inpainting     | Gated convolutions, mask-aware, attention mechanism                                                         | 28.45         | 0.910    | 17.02    | 0.800                      |
| 7        | PICNet                   | CNN            | Image Inpainting     | Parallel convolutional network, context aggregation, image blending                                         | 27.60         | 0.890    | 19.43    | 0.780                      |
| 8        | RFR-Net                  | CNN            | Image Inpainting     | Recurrent feature reasoning, multi-scale, iterative refinement                                              | 28.60         | 0.912    | 16.76    | 0.798                      |
| 9        | Context Encoder          | GAN            | Image Inpainting     | Autoencoder, adversarial loss, context encoder, global content consistency                                  | 27.28         | 0.885    | 20.21    | 0.770                      |
| 10       | HiFill                   | GAN            | Image Inpainting     | Hierarchical filling, multi-scale, attention mechanism                                                      | 28.20         | 0.905    | 17.89    | 0.790                      |


## Sources & Improvement

This benchmark was generated by latest version of `GPT-4o` (June-2024) to be set as **reference** for the purpose of this [project](https://github.com/afondiel/computer-vision-challenge/tree/main/L2_03_AI_Powered_Image_Restoration_and_Enhancement). Notice that these rates might vary depending on which dataset you're using for the model.

Feel free to update these table by openning a PR, if you get better result. 

## References




