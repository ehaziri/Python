print ("Scores and Grades")

for i in range(0,10):
    piket = input("Shkruaj piket: ")

    if(piket>=60 and piket<70):
        print("Score: ", piket,"; Your grade is D.")
    elif(piket>=70 and piket<80):
        print("Score: " ,piket ,"; Your grade is C.")
    elif(piket>=80 and piket<90):
        print("Score: ", piket ,"; Your grade is B.")
    elif(piket>=90 and piket<=100):
        print("Score: ", piket ,"; Your grade is A.")
    else:
        print("Piket e shenuara duhet te jene ne intervalin [60,100]")
