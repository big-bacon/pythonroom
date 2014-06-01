# author: big-bacon
you = input("talk")
you = you.lower()

if you[0] == "a" or you[0] == "e" or you[0] == "i" or you[0] == "o" or you[0] == "u" or you[0] == "y":
	you = you + "yay"

else:
    you = you + you[1:]+ you[:1]+ "ay"
print you