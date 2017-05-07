# Video-Scene-Classification-Based-on-Python-and-Tensorflow
Copyright 2017 Ameer Hamza Khan

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

The aim of this project was to classify a single scene in a video and then attach/mix an appropriate sound to the video.


The project contains,
1- subprocess_learn_mod.py --> The main Python file that should be executed to see the results.
2- classify_image_mod.py --> Modified file from Tensorflow's models repository that gives a single string as an output that is read by the main program.
3- Test files such as the 458_video, Pistol.mp4.
4- Sounds to be attached.

Pre-Requisites for this program,
1- Python 3.5.2
2- OpenCV 3.0+.(https://pypi.python.org/pypi/opencv-python#downloads)
3- TensorFlow (pip3 install --upgrade tensorflow)
4- TensorFlow Models Repo. (Download/clone TensorFlow models repository (https://github.com/tensorflow/models)
5- ffmpeg

Running the program:
###################
Install every component required and put all program files in the same directory.
Run classify_image.py in the TensorFlow models to install necessary files and data.

After everything is installed, run the program "subprocess_learn_mod.py"
A video will start playing based on your selection.

Hit the 'Q' button to capture a frame for analysis. Be careful to choose a scene that clearly shows the main focus of the video.
Hit 'X' to stop the video and start the analysis.

Sit back and enjoy the results.
