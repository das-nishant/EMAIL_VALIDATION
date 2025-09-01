email = input("Enter Your Email: ")
k, j, d = 0, 0, 0

if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4] == ".") ^ (email[-3] == "."):
                for i in email:
                    if i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i.isupper():
                            j = 1    
                    elif i.isdigit():  
                        continue  
                    elif i in "_@.":
                        continue
                    else:
                        d = 1
                if k == 1 or j == 1 or d == 1:
                    print("Wrong Email 5")   
                else:
                    print("Valid Email ✅")
            else:
                print("Wrong Email 4 (dot position issue)")
        else:
            print("Wrong Email 3 (invalid @)")
    else:
        print("Wrong Email 2 (must start with alphabet)")
else:
    print("Wrong Email 1 (too short)")



 
