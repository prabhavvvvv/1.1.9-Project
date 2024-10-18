def main():
    faces_upper = ["Spiderman", "Batman"] 
    faces_lower = ["spiderman", "batman"]
    print("The available faces that I can draw are", faces_upper, "or", faces_lower)
    print("Please type your input exactly how it is in the list")
    while True:
        face_input = input("What do you want to draw?: ")
        face_input = face_input.lower()
         
        if face_input in faces_upper or face_input in faces_lower:
            if "spiderman" in face_input:
                print("Now drawing Spiderman...")
                draw_spiderman()
                break
            elif "batman" in face_input
            else:
                print("Please enter a valid input")

if __name__ == "__main__":
    main()
