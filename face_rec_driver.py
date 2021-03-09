import face_rec as fr
import face_rec_config as uc

#Initial load of faces
fr.load_known_faces()

#Loop the program until isQuit == True
isQuit = False
while isQuit == False:
    #Present Menu
    print("*"*50, "\n\tPYTHON FACIAL RECOGNITION\n", "*"*50)
    print(f"\n(Faces Available: {len(uc.known_faces)})")
    print("\n(1) Create Facial Profile\n(2) Process Images\n(3) Remove Facial Profile\n(4) List All Profiles\n(5) Quit\n")

    #Wait for valid input
    is_valid = False
    user_input = ""
    while is_valid == False:
        user_input = input("Please enter a choice: ")
        if(user_input == "1" or user_input == "2" or user_input == "3" or user_input == "4" or user_input == "5"):
            is_valid = True
        else:
            print("Unknown choice, please try again.\n")

    #Process input
    if user_input == "1": #Import Faces
        print("*"*50, "\n\tCREATE FACIAL PROFILE\n", "*"*50)
        fr.import_new_faces()
    elif user_input == "2": #Process Images
        print("*"*50, "\n\tPROCESS UNKNOWN IMAGES\n", "*"*50)
        uc.TOLERANCE = float(input("Tolerance (0.6 Reccomended): "))
        uc.MODEL = input("Model ('hog' Reccomended): ")
        fr.process_unkown_images()
    elif user_input == "3": #Remove Facial Profile
        print("*"*50, "\n\tREMOVE FACIAL PROFILE\n", "*"*50)
        fr.remove_facial_profile()
    elif user_input == "4": #List All Profiles
        print("*"*50, "\n\tLIST FACIAL PROFILES\n", "*"*50)
        fr.list_facial_profiles()
    elif user_input == "5": #Quit
        print("\nTerminating Program...")
        isQuit = True
