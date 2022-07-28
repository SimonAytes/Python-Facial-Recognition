# Python-Facial-Recognition

A personal project to explore the [face_recognition](https://face-recognition.readthedocs.io/en/latest/index.html) package.

## System Requirements

_The following versions reflect the environment wherein this program was created._

**Python Version:** Python 3.8.5

**Face-Recognition Version:** 1.3.0

**OpenCV-Python Version:** 4.5.1.48

## How to Use (Mac)

### Starting the Application
1. Clone the repository to your machine (or download the code).
2. Open **Terminal** and cd into the repository.
3. Execute the following command: `python face_rec_driver.py`
4. You should be presented with the following in your terminal:
<img width="766" alt="image" src="https://user-images.githubusercontent.com/44680601/110698751-0dc85680-81bc-11eb-8ecd-9c8b8dc8f7cd.png">

5. You are now ready to use the application!

### Creating a Facial Profile
1. Gather images of the person whose profile you are creating. It is reccomended that you have at least 20 in varying light-levels/environments.
2. Create a new folder and name it after the person.
3. Copy all photos into the folder.
4. Navigate to the project folder and find the folder named `known_faces`. 
5. Place your folder in that directory and run the program.
6. Select option one to import a new face.

### Processing Images
1. Gather the photos you wish to process.
2. Navigate to the project folder and find the folder named `unknown_faces`.
3. Place all of your images in this directory.
4. Run the program and select option two.
5. When prompted, enter a value of `0.6` for `Tolerance`.
6. Next, enter `hog` for `Model`.
7. The program will now detect and match any faces present in the images and present them one-by-one. If there is a match, then a box will be drawn around the face and a label with the person's name will be placed underneath. 

_NOTE: If the program does not detect any faces in an image, it is most likely because the training data did not have enough pictures. To fix this, remove the facial profile (option three), add more pictures to their directory. Finally, re-create their profile following the steps above and try again._

## Self Check

Please ensure that you install the packages outlined in the `requirements.txt` file.
