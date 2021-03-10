"""face_rec_config.py: Configuration file. All 'global' variables are captured here."""

__author__ = "Simon Aytes"
__version__ = "1.0.0"
__maintainer__ = "Simon Aytes"
__email__ = "saytes@umich.edu"
__status__ = "Release"

### DIRECTORY INFO ###
KNOWN_FACES_DIR = "known_faces" # Training face images
UNKNOWN_FACES_DIR = "unknown_faces" # Unknown face images
FACE_ENCODINGS_DIR = "face_encodings" # Existing face encodings
SOURCE_IMAGE_DIR = "SourceImages" # Container for all processed images

### FACIAL RECOGNITION ###
TOLERANCE = 0.6 # Tolerance value for the facial match
    # For a small sample set:
    # The higher you go, more false positives
    # The lower you go, the more false negatives
MODEL = "hog" # Model used for the facial recognition
    # Options: "cnn", "hog"
known_faces = [] # Known face encodings
known_names = [] # Names associated with faces

### IMAGE PROCESSING ###
FRAME_THICKNESS = 3 # Square thickness
FRAME_COLOR = [255, 0, 0] # Fill color of the square
FONT_THICKNESS = 2 # Font thickness
FONT_COLOR = [255, 255, 255] # Fill color of the font