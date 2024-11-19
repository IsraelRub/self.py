the_player_character = input("Enter letters:")

if  the_player_character.isalpha() and len(the_player_character)>1:
    print('E1')
elif not the_player_character.isalpha() and len(the_player_character)<2:
    print('E2')
elif not the_player_character.isalpha() and len(the_player_character)>=2: 
    print('E3')
else:
    print(the_player_character).lower()
