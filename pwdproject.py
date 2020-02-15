import re

                            #This code was made in Python 3.7 
                            #and was maked by HamzaOPLEX 
                            #Facebook : facebook.com/Hamza0plex
                            #Website : www.freetechways.xyz
                            #Youtube : https://www.youtube.com/channel/UCbeSJJWGNppv5decBIjsfuw
                            #github : github.com/HamzaOPLEX

# for use just import the python file in your script ( import pwdproject )
# then use it : pwdproject.password(#here the password variable or string)

def password(pass_enter) :
    a = "try again because a Strong Password is  : \n\t1-contain 8 characters \n\t2-First character must be Uppercase\n\t3-other character must be even upper or lowercase\n\t4-at least one digit"
    compile01 = re.compile(r"^[A-Z][a-zA-Z0-9]{8,20}")
    search01 = compile01.findall(pass_enter)
    if search01 :
        for i in search01 :
            compile02 = re.compile(r".*\d{1,8}.*") #Check if There is Numbers
            search02 = compile02.findall(i)
            if search02 :
                return "Your Password is Strong :)"
            if not search02:
                return a
    if not search01 :
        return a
