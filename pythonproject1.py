import random

x = 'y'
while x == 'y':

    randNumber = random.randint(1,6)
    if randNumber==1 :
        print("\n[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("\n[-----]")

    if randNumber==2 :
        print("\n[-----]")
        print("[0    ]")
        print("[     ]")
        print("[    0]")
        print("\n[-----]")

    if randNumber==3 :
        print("\n[-----]")
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
        print("\n[-----]")

    if randNumber==4 :
        print("\n[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("\n[-----]")

    if randNumber==5 :
        print("\n[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("\n[-----]")

    if randNumber==6 :
        print("\n[-----]")
        print("[0 0 0]")
        print("[     ]")
        print("[0 0 0]")
        print("\n[-----]")

    x = input("\npress y to roll again and n to exit:")
    print("\n")
