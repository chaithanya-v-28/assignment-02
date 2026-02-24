Name = "John Doe"      #student name
Age = "20 "            #student age
Course = "Python Programming"       #student course
College = "ABC University"          #student college
Email = "john@example.com"          # student email id
print("╔══════════════════════════════════════════╗")    #print top border of the card
print("║           STUDENT BIO CARD               ║")    # print title section
print("╠══════════════════════════════════════════╣")    #print separator line
print(f"║ Name: {Name:<34} ║" )                           #print each field inside fixed width of 34
print(f"║ Age : {str(Age) + 'years' :<34} ║")             #print each field inside fixed width of 34
print(f"║ Course : {Course:<31} ║")                       #print each field inside fixed width of 31
print(f"║ College : {College:<30} ║")                     #print each field inside fixed width of 30
print(f"║ Email : {Email:<32} ║")                         #print each field inside fixed width of 32
print("╚══════════════════════════════════════════╝")     #print the bottom border