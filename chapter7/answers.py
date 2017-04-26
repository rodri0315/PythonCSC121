
# Create text file of user answers

outputfile = open("answers.txt", "w")

for question in range(20):
    answer = input(f"What is the answer to question {str(question+1)}: ")
    outputfile.write(answer + "\n")

outputfile.close()
