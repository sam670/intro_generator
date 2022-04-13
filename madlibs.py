'''
##frist we have to take an string to achive madlibs in python
string = ""     #this is the string
#there are few ways to create madlibs
#1st way to create
print("Hi this is the first string that is "+string)
#2nd way to create
print("Hi this is the second string that is {}".format(string))
#3rd way to create
print(f"Hi this is the third string that is {string}")
'''

#creating a introduction using the values that is give by the user
name = input("Enter your name: ")
address = input("Enter your address: ")
education = input("Enter your heighest and completed education: ")
year = input("Enter the year of passing this education: ")
current_edu = input("Enter your current education that you are doing: ")
skills = input("Enter your skills with comma seprated: ")
project_name = input("Enter your project name: ")
project_topic = input("Enter the topic of the project: ")
strengths = input("Enter your strengths in comma seprated: ")
hobbies = input("Enter your hobbies in comma seprated: ")
string = f"Hi My name is {name} and i am from {address} I have done\n my {education} in {year} " \
         f"and now i am doing {current_edu}\n. My skills are {skills} \nand i have worked a project " \
         f"that is {project_name} that is based on {project_topic}.\n My strengths are {strengths}."\
        f"and my Hobbies are {hobbies}.\n"\
        f"Thank you sir/mam"
print(string)
