print("Hello, World")

#operators

#add, concat operator

print(2 + 3)
print("hi" + "gh")
print("Messi " + str(100) + " goals")

#subtract
print(2 - 3)


#multiply
print(2 * 33)
print("A" * 10)
print(2 ** 4)

#division - normal and floor
print(10 / 3)
print(10 // 3) #Quotient

#modulus
print(20 % 3) #remainder

#increment and decrement
i = 3
i += 4
print(i)
i -= 2
print(i)
i *= 2
print(i)

#loops - for and while

#while (condition) - loop will continue till this is true

goals = 10
while (goals < 20):
    print(goals)
    goals += 1

#for (start, stop, step) or (range)
#python the stop is non-inclusive (10) - 0 to 9
for i in range(10):
    print(i)

print("for loop with step")
for i in range(10, 1, -1):
    print(i)

print(" ")

#slicing - will return from start to stop(non-inclusive)
#no specify in start - 0
#no specify in end - -1 or end
s = "Mes Que En Club"
print(s[2:])
print(s[4:7])

#lists - collection of elements - different data types - usually supported only in python
#array - collection of similar data types - ints, strings, or other types
q = ["Baggio", "Pirlo", "Bonucci", "Chiesa"]
print(q[-1::-1])

#every string is essential a character array
r = "cristano"
print(r[-1::-1])

#to check if a string is a palindrome, give parameters/input values to the function
#you first define a function, and each function should return something
#dont forget to call it, after you declare/define it
def palindrome(t):
    t1 = t[-1::-1]
    if t == t1:
        return True
    else:
        return False

print(palindrome("hannah"))
print(palindrome(r))
#he is not using strings, he is using ints

#built in functions
#range
for i in range(1, 5):
    print(i)
#length - len
print("prints the length of the object")
k = "fanabgoabngaonga"
print(len(q))
q = ["Baggio", "Pirlo", "Bonucci", "Chiesa", "Maldini"]
#iterating through a list
for i in q:
    print(i)
    print(len(i))
print(len(k))