
#Ethics statement: This file is part of a project that aims to provide educational resources on software security. The code examples included here are intended for learning purposes only and should not be used in production environments without proper security assessments. The authors do not take responsibility for any misuse of the code provided.
l = []
for n in range(10):
    print(n)
    l.append(n)
    l.sort(reverse=True) # Sorting the list in descending order after each append

print(l)