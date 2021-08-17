TextInput = input()

Characters = list(TextInput)
for x in Characters:
    if x == "l":
        Change_l = Characters.index("l")
        Characters[Change_l] = "w"

    if x == "L":
        Change_L = Characters.index("L")
        Characters[Change_L] = "W"

    if x == "r":
        Change_r = Characters.index("r")
        Characters[Change_r] = "w"

    if x == "R":
        Change_R = Characters.index("R")
        Characters[Change_R] = "W"

WordTest = ''.join(Characters)
WordTest = WordTest.split()
for x in WordTest:
    if x == "hi":
        Change_hi = WordTest.index("hi")
        WordTest[Change_hi] = "hewwo"
    if x == "Hi":
        Change_Hi = WordTest.index("Hi")
        WordTest[Change_Hi] = "Hewwo"
    if x == "no":
        Change_no = WordTest.index("no")
        WordTest[Change_no] = "nyo"    
    if x == "No":
        Change_No = WordTest.index("No")
        WordTest[Change_No] = "Nyo"

Output = ' '.join(WordTest)
Characters = list(Output)

FirstLetter = Characters[0]
Characters.insert(0,FirstLetter)
Characters.insert(1,"-")
Characters.append("~~")

Output = ''.join(Characters)
print(Output)
