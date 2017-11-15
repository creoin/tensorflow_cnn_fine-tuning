# Fine-Tuning a CNN Model in TensorFlow

## Introduction

The objective of this project is to build a model that can take in images of dogs and classify their breed. This is an example of how to build a state-of-the-art image recognition model for images in any domain.

### Dataset and Image Recognition

The
[Stanford Dogs Dataset](http://vision.stanford.edu/aditya86/ImageNetDogs)
has 20,580 images of 120 breeds of dogs. In recent years, the best models for image recognition have been Convolutional Neural Network (CNN) based models, so a CNN model would be recommended for this task. Since images are a complicated visual field of pixels, it is common to train on a large image dataset for weeks in order to learn the image statistics (real-world images are not random "pixels," otherwise our brains would not be able to learn to see). These are common characteristics and patterns that occur in any image.

### Fine-Tuning

We do not have to train a model for weeks, however, as transfer learning allows us to take a pre-trained model and fine-tune it for another similar task. We can just cut the final layer of a model, which translates image features into recognised classes, and train that final layer to recognise new classes.

### Image Recognition Model

There have been many successful CNN models. In 2012, AlexNet (CNN model) won the ImageNet competition which has over 1 million images with 1000 classes. ResNet dropped the top-5 error rate to below the human error rate, around 5.1%. A more powerful, and fairly light-weight model,
[Inception-v3](https://arxiv.org/abs/1512.00567)
had a top-5 error rate of 3.6%. There are multiple other potential models with their advantages and disadvantages. ResNet, VGG, Inception v3/v4, and ensembles are good options for a server based model, while MobileNet or SqueezeNet may be good options for embedded models in devices or smartphones.

### A Proposed Solution

As an initial step, a recommended solution is to take an
[Inception v3](https://arxiv.org/abs/1512.00567)
model pre-trained on ImageNet, and fine-tune it for recognising the dog classes. If further accuracy is required, this model could be compared with other potential models as well as taking measures to improve the model training. For example, the image data can be augmented by training on variations of the images such as randomly scaled, rotated, brightened/darkened, or cropped versions. This increases the generality of the model.

## How to Run

### Download the Data

Firstly the
[Stanford Dogs Dataset](http://vision.stanford.edu/aditya86/ImageNetDogs)
should be downloaded.
In the data directory, run:

```
$ python3 download_data.py
```

This will download the archive of dog images, uncompress them, and simplify the names of the folders to basic class names.

For this implementation, we need a directory of images, which includes a folder for each class we want to recognise. The class name will be taken from the folder names, and inside each folder there should be many example images of that class. For example, the directory of images will be `data/ImageNetDogs/Images`, and a class folder may be `Collie` that contains may images of Collies.

### Training

From the root directory, run:

```
$ python3 fine-tune.py
```

This script is adapted from a script provided by TensorFlow, and contains many options. The default options have already been set to use the `inception v3` model. A pre-trained version of this model will be downloaded by the script into the `pretrained` directory. The data/image directory has been set to `data/ImageNetDogs/Images` and most of the intermediate and output files will go into the `working` directory.

The output fine-tuned graph will be saved in `working/finetuned_graph.pb`, with the labels stored in `working/finetuned_labels.txt`.

### Predictions

To try out the fine-tuned model, pass in an image like so:
```
$ python3 predict.py --image try_image/rough_collie.jpg
```

This will give you an output of something like this:
```
collie 0.565662
shetland sheepdog 0.36928
border collie 0.00504679
borzoi 0.00179517
papillon 0.00172817
```

So the model correctly predicted the breed of our "Rough Collie" image as a "collie."


# References

- ["TensorFlow for poets 2" codelab](https://codelabs.developers.google.com/codelabs/tensorflow-for-poets-2).
- [Inception-v3](https://arxiv.org/abs/1512.00567)
- [Stanford Dogs Dataset](http://vision.stanford.edu/aditya86/ImageNetDogs)
