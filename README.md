# Object Detection by using CHOOCH AI API
This repository focuses developing a sample project for object detection and counting using CHOOCH AI API and OpenCV. CHOOCH AI is used for object detection, OpenCV is used for drawing bounding boxes and saving the output images.

<p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/105612702-a8b4cf00-5dce-11eb-9ecf-3c39a9a1d301.gif" | width = 720>
</p>

CHOOCH AI provides object detection in milliseconds and it is reachable from any edge devices since it uses HTTP methods (as like a RESTful web service).

---
Some of the cool features of this project:

- Detecting the objects in milliseconds.
- Counting the objects in milliseconds.
- Detecting the texts in milliseconds.
- Cropping the detected objects and saving them as new images.
- Cropping the detected texts and saving them as new images.
- Storing the detected objects titles and pixel coordinates in a csv file.
- Storing the detected texts and pixel coordinates in a csv file.
---

## Software Architecture

<p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/105613442-9721f600-5dd3-11eb-84f0-9c1b5c27d082.png" | width = 600>
</p>

Here are the explanation of software work-flow:

- Input image is sent (http post) to CHOOCH AI and then detected objects information fetch in json format.
- Json string is parsed and detected objects are stored in a dictionary (key='object_title', value='coordinates').
- Drawing bounding boxes around the etected object using OpenCV.
- Cropping the detected objects and saving as new images using OpenCV.
- Storing the detected object informatin in csv files.

### Folders and files explanations

Here are the explanation of folders and files:

- [main.py](https://github.com/ahmetozlu/object_detection_chooch/blob/main/main.py): main python program that contains all of the logic.
- [detected_objects](https://github.com/ahmetozlu/object_detection_chooch/tree/main/detected_objects): Detected objects are cropped and saved as new images under this folder.
- [detected_texts](https://github.com/ahmetozlu/object_detection_chooch/tree/main/detected_texts): Detected texts are cropped and saved as new images under this folder.
- [input](https://github.com/ahmetozlu/object_detection_chooch/tree/main/input): Input images are located under this folder.
- [output](https://github.com/ahmetozlu/object_detection_chooch/tree/main/output): Input images are stored in folder.
- [object_detection.csv](https://github.com/ahmetozlu/object_detection_chooch/blob/main/object_detection.csv): Detected object information are stored in this csv file.
- [text_detection.csv](https://github.com/ahmetozlu/object_detection_chooch/blob/main/text_detection.csv): Detected text information are stored in this csv file.

## Installation

You don't need to instal any fancy library or package to run this program. CHOOCH AI provides its object detection services with HTTP methods so it can be reacheable by any edge devices. You just need to install OpenCV for basic image procesing operations (like cropping the images, saving the images and etc.).

OpenCV can be installed by pip:

    pip install opencv-python
    
Moreover, please update the API key with your own key on [line#7 in main.py](https://github.com/ahmetozlu/object_detection_chooch/blob/main/main.py#L7).
   

## Citation
If you use this code for your publications, please cite it as:

    @ONLINE{
        author = "Ahmet Özlü",
        title  = "Object Detection and Counting with CHOOCH AI API",
        year   = "2021",
        url    = "https://github.com/ahmetozlu/object_detection_chooch"
    }

## Author
Ahmet Özlü

## License
This system is available under the MIT license. See the LICENSE file for more info.
