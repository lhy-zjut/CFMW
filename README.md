<div align="center">

<h1 align="center"><strong>CFMW: Cross-modality Fusion Mamba for Robust Object Detection under Adverse Weather</strong></h1>
<b>Haoyuan Li, Qi Hu, Binjia Zhou, You Yao, Jiacheng Lin, Kailun Yang<sup>*</sup>, Peng Chen<sup>*</sup></b>

<b><sup>*</sup>Corresponding Authors</b>
<p align="center">
  <a href="https://arxiv.org/pdf/2404.16302" target='_**blank**'>
    <img src="https://img.shields.io/badge/CFMW-ArXiv-red?">
  </a> 
  <a href="https://huggingface.co/datasets/lhy-zju/SWVI/tree/main" target='_blank'>
    <img src="https://img.shields.io/badge/SWVI-Dataset-blue">
  </a>
  <a href="https://github.com/lhy-zjut/CFMW/" target='_blank'>
    <img src="https://img.shields.io/github/stars/lhy-zjut/CFMW?style=social">
  </a>
</p>
</div>

## 🔍 Overview

### Model
<h1 align="center"><img src="pictures/main_pipeline_00.png" align="center" width="100%"></h1>
</p>

### Dataset
<h1 align="center"><img src="pictures/picture3_00.png" align="center" width="70%"></h1>


### Data Preparation
1. Download the four compressed files [here](https://huggingface.co/datasets/lhy-zju/SWVI/tree/main). They require about 20GB of storage space.
2. Run the following command to merge the two files into one and uncompress it. This will produce a folder named `SWVI` containing 60K visible images, infrared images and visible images with weather-influence. 
```bash
cat SWVI.* > SWVI.zip
unzip SWVI.zip
```
</p>

### Demo
<h1 align="center"><img src="pictures/picture4_00.png" align="center" width="100%"></h1>
</p>


## 🏠 About

In this work, we propose the Cross-modality Fusion Mamba with Weather-removal (CFMW) to augment stability and cost-effectiveness under adverse weather conditions. Leveraging the proposed Perturbation-Adaptive Diffusion Model (PADM) and Cross-modality Fusion Mamba (CFM) modules, CFMW is able to reconstruct visual features affected by adverse weather, enriching the representation of image details. To bridge the gap in relevant datasets, we construct a new Severe Weather Visible-Infrared (SWVI) dataset, encompassing diverse adverse weather scenarios such as rain, haze, and snow.

## 🔗 Citation

If you find our work and this codebase helpful, please consider starring this repo 🌟 and cite:

```bibtex
@ARTICLE{11077409,
  author={Li, Haoyuan and Hu, Qi and Zhou, Binjia and Yao, You and Lin, Jiacheng and Yang, Kailun and Chen1, Peng},
  journal={IEEE Transactions on Circuits and Systems for Video Technology}, 
  title={CFMW: Cross-modality Fusion Mamba for Robust Object Detection under Adverse Weather}, 
  year={2025},
  doi={10.1109/TCSVT.2025.3587918}}
```

## 👏 Acknowledgements
- [YOLOv5](https://github.com/ultralytics/yolov5)
- [CFT](https://github.com/DocF/multispectral-object-detection)
- [Vison Mamba](https://github.com/hustvl/Vim)
- [WeatherDiffusion](https://github.com/IGITUGraz/WeatherDiffusion)
