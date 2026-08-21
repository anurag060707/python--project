print("welcome to treasure island")
print("your mission to  find the treasure")
choice1=input('you\'re at a crossroad , where do you want to go ?.'
             'type "left" or "right".').lower()
if choice1=="left":
    choice2=input('you\'ve come to a lake,'
    ' there is an island in the middle of the lake.'
    'type "wait" to wait for a boat.type "swim" to swim across:').lower()
    if choice2=="wait":
        choice3=input('you arrives at the island unharmed.'
                      'there is house with 3 doors.one red,'
                        'one yellow  and one blue.'
                          'which colour do you choose?:').lower()
        if choice3 =="red":
            print("it's a room full of fire.game over")
        elif choice3=="blue":
            print("you found the treasure.you win")
        elif choice3=="yellow":
            print("you enter a room of beasts.game over.")
        else:
            print("you chose a door that doesn't exist.game over.")                  
    else:
        print("you got attacked by an angry trout .game over.")    
else:
    print("you fell in to a hole. game over.")

    