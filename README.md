# Traffic Signs Classification and Detection
The objective of the project is to detect traffic signs using image dataset. Convolutional Neural Network is used to classify the images. The output class consists of 43 different traffic signs.

I update this project to include a traffic signs and lights detection using YOLOv7. The used model is YOLOv7-tiny. The dataset of this task is much smaller, it consist of 24 different traffic signs and lights.

# Dataset Information
## The dataset of classification task
The training archive contains 43 different type of traffic signs.<br />
Some images of the dataset:<br />
<img align='center' src="https://github.com/gnurt2041/Traffic_Signs_Classification/blob/main/image/dataset.jpg" width="700">

**Paperwithcode dataset link:** https://paperswithcode.com/dataset/gtsrb

## The dataset of object detection task( sefl-collected dataset):
**Gooogle Drive:** https://drive.google.com/file/d/1SSqYsNNb6eghhFjuwKTGEG4UlujuWT8Z/view?usp=sharing

# Environment: Google Colab

# The directory structure:
### Classification task:
```
Traffic_Signs_Classification/
	├── signsdata/
		├── train.p
		├── test.p
		└──  valid.p
  └──main/
        └── traffic_signs_classification.ipynb
```
### Object Detection task:
```
Traffic_Signs_Classification/
	├── dataset/
		├── train/
		      ├── images/
		      └── labels/
		└──  valid/
		      ├── images/
		      └── labels/
  └──main/
        └── road_sign_detection.ipynb
```
# Libraries

<li>pickle
<li>os
<li>wget
<li>numpy
<li>seaborn
<li>tensorflow
<li>torch
<li>scikit-learn
<li>livelossplot

# Setup of YOLO model:
I will update the way of data collection in the future. Currently, you need to do some configuration so that the model knows some information of the dataset. Use data_config.py to do that if you have the directory of the dataset the same as mine.

# Neural Network

<li>CNN Architecture of Classification task:

<h2><img align='center' src="https://github.com/gnurt2041/Traffic_Signs_Classification/blob/main/image/plot_cnn.png" width="700"><h2>

# Result
## Classification task:
<h3><img align='center' src="https://github.com/gnurt2041/Traffic_Signs_Classification/blob/main/image/result.png" width="700"><h3>

**Accuracy of classification task:** ~96.65%( with class_weight ), look the above code to more detail
## Object detection task:
<h3><img align='center' src="https://github.com/gnurt2041/Traffic_Signs_Classification/blob/main/image/001683.jpg" width="700"><h3>
Metrics:
<h3><img align='center' src="https://github.com/gnurt2041/Traffic_Signs_Classification/blob/main/image/results.png" width="700"><h3>

You can download and use the weights of model (best.pt).
