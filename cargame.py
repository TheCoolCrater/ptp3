command = ""
started= False
while True:
    command = input("Car Commands >>>  ").lower()
    if command == "start":
        
        if started:
            print("Car Already Started Bro")
        else:
            started= True
            print("we on tHE roADDDDDDDDD")
    elif command == "stop":
        
        if started :
            print("Bro Are U Stopid We Are Already Stoped")
        else:
            started = False
            print("pIT StoOOOOOOoOoOOOppppppppppppPPppPp")
        
    elif command == "help":
        print("Commands Are Start, Stop, Exit, and Help")
    elif command == "exit":
        break
    else:
        print("U SPAK ENGLESh, Type Help For Commands")