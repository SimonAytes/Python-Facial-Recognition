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
    print("\n(1) Import Faces\n(2) Process Images\n(3) Remove Faces\n(4) Quit\n")

    #Wait for valid input
    is_valid = False
    user_input = ""
    while is_valid == False:
        user_input = input("Please enter a choice: ")
        if(user_input == "1" or user_input == "2" or user_input == "3" or user_input == "4"):
            is_valid = True
        else:
            print("Unknown choice, please try again.\n")


    #Process input
    if user_input == "1": #Import Faces
        print("*"*50, "\n\tIMPORT NEW FACES\n", "*"*50)
        fr.import_new_faces()
    elif user_input == "2": #Process Images
        print("*"*50, "\n\tPROCESS UNKNOWN IMAGES\n", "*"*50)
        uc.TOLERANCE = float(input("Tolerance (0.6 Reccomended): "))
        uc.MODEL = input("Model ('hog' Reccomended): ")
        fr.process_unkown_images()
    elif user_input == "3": #Add/Remove Face
        print("*"*50, "\n\REMOVE FACE\n", "*"*50)
    elif user_input == "4": #Quit
        fr.save_and_quit()
        print("\nTerminating Program...")
        isQuit = True
