#Import necessary libraries
import face_recognition
import cv2
import os

### GLOBAL VARIABLES ###
# Face directory
KNOWN_FACES_DIR = "known_faces"
UNKNOWN_FACES_DIR = "unknown_faces"

# Tolerance for facial match
TOLERANCE = 0.6
# For a small sample set:
# The higher you go, more false positives
# The lower you go, the more false negatives

# Square thickness
FRAME_THICKNESS = 3

# Font thickness
FONT_THICKNESS = 2

# Model used for the facial recognition
MODEL = "hog"
# Alternative, "cnn"

# Load in known faces
print("Loading known faces")

known_faces = [] # Face encodings
known_names = [] # Names associated with faces

#Iterate through all known face folders
for name in os.listdir(KNOWN_FACES_DIR):
    #Check if the folder is an Apple folder (they start with a '.')
    if name[0] == '.':
        continue
    print(f"Loading {name}")
    #Iterate over all images in the directory
    for filename in os.listdir(f"{KNOWN_FACES_DIR}/{name}"):
        #Check if the file is an Apple file (they start with a '.')
        if filename[0] == '.':
            continue
        #Load the image with the Facial_Recognition library
        image = face_recognition.load_image_file(f"{KNOWN_FACES_DIR}/{name}/{filename}")
        #Create the encoding (at the first face it finds)
        encoding = face_recognition.face_encodings(image)[0]
        #Add the encoding to the known_faces list
        known_faces.append(encoding)
        #Add the name to the names list
        known_names.append(name)

print("Processing Unknown Faces")
#Iterate through each of the unkown faces
for filename in os.listdir(UNKNOWN_FACES_DIR):
    #Check if the file is an Apple file (they start with a '.')
    if filename[0] == '.':
        continue
    print(filename)
    image = face_recognition.load_image_file(f"{UNKNOWN_FACES_DIR}/{filename}")
    #Find all the faces in the image
    locations = face_recognition.face_locations(image, model=MODEL)
    #Identify the faces at each location
    encodings = face_recognition.face_encodings(image, locations)
    #Make the image grayscale
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    for face_encoding, face_location in zip(encodings, locations):
        results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)
        match = None
        if True in results:
            match = known_names[results.index(True)]
            print(f"Match found: {match}")
            #Get the coordinates for the box
            top_left = (face_location[3], face_location[0])
            bottom_right = (face_location[1], face_location[2])
            #Set the color of the box
            color = [0, 255, 0]
            #Draw the rectangle
            cv2.rectangle(image, top_left, bottom_right, color, FRAME_THICKNESS)
            #Get label box location
            top_left = (face_location[3], face_location[2])
            bottom_right = (face_location[1], face_location[2]+22)
            #Draw the label rectangle
            cv2.rectangle(image, top_left, bottom_right, color, cv2.FILLED)
            #Place the text over the image
            cv2.putText(image, match, (face_location[3]+10, face_location[2]+15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), FONT_THICKNESS)
    #Show the image
    cv2.imshow(filename, image)
    #Wait until '0' is pressed and then, ...
    cv2.waitKey(0)
    #... destroy the window
    cv2.destroyWindow(filename)
