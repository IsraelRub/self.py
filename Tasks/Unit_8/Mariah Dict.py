mariah_dict = {
    'first_name': "Mariah",
    'last_name' : 'Carey',         
    'birth_date' : '27.03.1970',        
    'hobbies' : ['Sing', 'Compose', 'Act']
      }

while True:
    action_number = input(
        "1. Display last name\n"
        "2. Display birth month\n"
        "3. Display number of hobbies\n"
        "4. Display last hobby\n"
        "5. Add 'Cooking' to hobbies\n"
        "6. Display birth date numbers\n"
        "7. Add and display age\n"
        "8. Exit\n"
        "Choose an action number: "
    )

    if action_number == "1":
        print(mariah_dict["last_name"])
    
    elif action_number == "2":
        print(mariah_dict["birth_date"][3:5])
    
    elif action_number == "3":
        print((len(mariah_dict["hobbies"])))
    
    elif action_number == "4":
        print((mariah_dict["hobbies"][-1]))
    
    elif action_number == "5":
        mariah_dict["hobbies"].append("Cooking")
    
    elif action_number == "6":
        print(int(mariah_dict["birth_date"][:2]), int(mariah_dict["birth_date"][3:5]), int(mariah_dict["birth_date"][6:]))
    
    elif action_number == "7":
        mariah_dict["age"] = 37
        print(mariah_dict["age"])
    
    elif action_number == "8":
        break
    
    else:
        print("Please enter a valid action number.")