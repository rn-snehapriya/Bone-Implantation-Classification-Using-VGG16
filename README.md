# Bone-Implantation-Classification-Using-VGG16



### Steps followed in the project:

- Initially, the dataset with four classes is taken and the images in each classes are augumented until the number of images in each class is atleast 2000+ images.
- Then in seperate folder named "data", three different sub folders are created. I.e., Train, Test, Val. Each sub folders have 4 other subfolders each for one class of the dataset. That is, train has four subfolders called, Cofield, Depuy, Tornier, Zimmer.
- Then the images in each of the classes are divided into 90:8:2 and put into train, test and val folders respectively in their respected subfolders as well.
- Bone implantation classification is then done using VGG16 model and training of the model is done using five epochs. 
- Finally, the model is saved by the name "model_vgg16.h5". 
- This model can be checked with any image in val folder or with any bone implantation image belonging to these four classes.


**Dataset Used:** https://www.kaggle.com/datasets/yasserhessein/shoulder-implant-xray

This total model training was done in **Google Cloud**. And the model validation was done on **local system** equipped with 8GB RAM and Intel Core i5 processor.
