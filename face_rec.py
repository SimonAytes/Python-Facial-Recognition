"""face_rec.py: Function definition file for the appliation. All function calls are directed here."""

__author__ = "Simon Aytes"
__version__ = "1.0.0"
__maintainer__ = "Simon Aytes"
__email__ = "simon.aytes@lc.cuny.edu"
__status__ = "Release"

#Import necessary libraries
import face_recognition #Face detection
import cv2 #Image processing
import os #File I/O and management
import face_rec_config as uc #User settings
import pickle #Saving encodings
import shutil #Moving folders

def load_known_faces():
    # Load in known faces
    print("Initializing...")
    for name in os.listdir(uc.FACE_ENCODINGS_DIR):
        #Get the number of imported facial profiles
        num_imported_encodings = 0
        #Check if the folder is an Apple folder (they start with a '.')
        if name[0] == '.' or name == "SourceImages":
            continue
        data = pickle.loads(open(f"{uc.FACE_ENCODINGS_DIR}/{name}", "rb").read())
        uc.known_faces.append(data)
        uc.known_names.append(name[0:-7])

def import_new_faces():
    print(f"Importing new faces from /{uc.KNOWN_FACES_DIR}")
    num_new_faces = 0
    #Iterate through all known face folders
    for name in os.listdir(uc.KNOWN_FACES_DIR):
        #Get the number of usable images in the folder
        numUsableImanges = 0
        #Check if the folder is an Apple folder (they start with a '.')
        if name[0] == '.':
            continue
        print(f"Loading {name}")
        #Iterate over all images in the directory
        for filename in os.listdir(f"{uc.KNOWN_FACES_DIR}/{name}"):
            #Check if the file is an Apple file (they start with a '.')
            if filename[0] == '.':
                continue
            #Load the image with the Facial_Recognition library
            image = face_recognition.load_image_file(f"{uc.KNOWN_FACES_DIR}/{name}/{filename}")
            #Check that there were faces detected in the image
            if len(face_recognition.face_encodings(image)) > 0:
                #Create the encoding (at the first face it finds)
                encoding = face_recognition.face_encodings(image)[0]
                #Add the encoding to the known_faces list
                uc.known_faces.append(encoding)
                #Add the name to the names list
                uc.known_names.append(name)
                numUsableImanges = numUsableImanges + 1
            #If there are none, print a debug message
            else:
                print(f"No faces detected in {uc.KNOWN_FACES_DIR}/{name}/{filename}")
            #Save the encoding to disk
            f = open(f"{uc.FACE_ENCODINGS_DIR}/{name}.pickle", "wb")
            f.write(pickle.dumps(encoding))
            f.close()
        #Print the number of usable images for the specified person
        print(f"Usable Images for {name}: {numUsableImanges}")
        #Move the folder with pictures into the source_images directory
        shutil.move(f"{uc.KNOWN_FACES_DIR}/{name}", f"{uc.FACE_ENCODINGS_DIR}/{uc.SOURCE_IMAGE_DIR}/{name}")


def process_unkown_images():
    print(f"Processing Unknown Faces from /{uc.UNKNOWN_FACES_DIR}")
    #Iterate through each of the unkown faces
    for filename in os.listdir(uc.UNKNOWN_FACES_DIR):
        faces_in_image = []
        #Check if the file is an Apple file (they start with a '.')
        if filename[0] == '.':
            continue
        print(f"Processing {filename}")
        image = face_recognition.load_image_file(f"{uc.UNKNOWN_FACES_DIR}/{filename}")
        #Find all the faces in the image
        locations = face_recognition.face_locations(image, model=uc.MODEL)
        #Identify the faces at each location
        encodings = face_recognition.face_encodings(image, locations)
        #Make the image grayscale
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        for face_encoding, face_location in zip(encodings, locations):
            results = face_recognition.compare_faces(uc.known_faces, face_encoding, uc.TOLERANCE)
            match = None
            if True in results:
                #Identify which image is in a match
                match = uc.known_names[results.index(True)]
            else:
                #Identify that a face was found, but it is Unknown
                match = "Unknown"
            #Get the coordinates for the box
            top_left = (face_location[3], face_location[0])
            bottom_right = (face_location[1], face_location[2])
            #Draw the rectangle
            cv2.rectangle(image, top_left, bottom_right, uc.FRAME_COLOR, uc.FRAME_THICKNESS)
            #Get label box location
            top_left = (face_location[3], face_location[2])
            bottom_right = (face_location[1], face_location[2]+22)
            #Draw the label rectangle
            cv2.rectangle(image, top_left, bottom_right, uc.FRAME_COLOR, cv2.FILLED)
            #Place the text over the image
            cv2.putText(image, match, (face_location[3]+10, face_location[2]+15), cv2.FONT_HERSHEY_COMPLEX, 0.5, uc.FONT_COLOR, uc.FONT_THICKNESS)    
            #Add the identified name to the list of faces in the image
            faces_in_image.append(match)
        #Print the names found in the image
        print(f"Face(s) in Image: {faces_in_image}")

        #Show the image
        cv2.imshow(filename, image)
        #Wait until '0' is pressed and then, ...
        cv2.waitKey(0)
        #... destroy the window
        cv2.destroyWindow(filename)

def list_facial_profiles():
    # Load in known faces
    print("Saved Profiles:\n")
    out_string = ""
    for name in os.listdir(uc.FACE_ENCODINGS_DIR):
        #Check if the folder is an Apple folder (they start with a '.')
        if name[0] == '.' or name == "SourceImages":
            continue
        #Add the name to the output string
        out_string = out_string + "\t>> " + name[0:-7] + "\n"
    #Print the list of names
    print(out_string)

def remove_facial_profile():
    # Load in known faces
    print("Current Profiles:\n")
    out_string = ""
    index = 1
    for name in os.listdir(uc.FACE_ENCODINGS_DIR):
        #Check if the folder is an Apple folder (they start with a '.')
        if name[0] == '.' or name == "SourceImages":
            continue
        #Add the name to the output string
        out_string = out_string + f"\t<{index}> " + name[0:-7] + "\n"
        index = index + 1
    #Print the list of names
    print(out_string)

    #Get the index to delete
    index_to_delete = int(input(f"Profile to delete (1 to {index-1}): "))
    #Confirm deletion
    y_n_input = input(f"\nNOTE: This will delete all source images as well as the facial profile.\nAre you sure you would like to delete the profile for {uc.known_names[index_to_delete-1]}? (y/n): ")
    
    #Check to see if the user wants to cancel the deletion
    if y_n_input == "y":
        print("\nDeleting profile...")
        #Delete the pickle file
        os.remove(f"{uc.FACE_ENCODINGS_DIR}/{uc.known_names[index_to_delete-1]}.pickle")
        #Delete the SourceImage folder
        shutil.rmtree(f"{uc.FACE_ENCODINGS_DIR}/{uc.SOURCE_IMAGE_DIR}/{uc.known_names[index_to_delete-1]}")
        #Remove selection from 'known_*' lists
        del uc.known_names[index_to_delete-1]
        del uc.known_faces[index_to_delete-1]
        print("Profile deleted!")
    else:
        print("Aborting...")
        return

