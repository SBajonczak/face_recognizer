# About
This is a small example for using the face_recognition libary to identify faces in a picutre.
For aboiding to intall a complete environment I creating a docker container and use it as a environment. 


# Build the container 

First Generate Container
```shell
docker build -t train_image
```
# Run the Image

```shell
docker run -v ${PWD}/images:/app/input -v ${PWD}/test:/app/test -v ${PWD}/result:/app/output train_image  
```

# Folderstructure

# input
Here are the images that will be idenfitied. You can cluster it into separate subfolders. The filenames will be used as label that are identified.

# test
This folder will contains all images that must run throught the identify process. So this will be used to identify the faces

# output
When the engine identify a face, it will result the modified image (marked with a bounding box) into this folder. It will use the same filename like the input filename


