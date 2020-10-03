# block of organized & reusable code action or give some results
# Function definition with parameters
def add(x,y):
    x+y

#calling function with actual values
print(add(5,10))
#If we print this we will not get any output as function is not returning any value.For that we need to add return keyword

def add(x,y):
    return x+y

sum=add(5,10)
print(sum)

#return is not same as printing
def add(x,y):
    print(x+y)
add(100,10)
answer=add(100,10)
#It will return none
print(type(answer))

#another example
a=print("hello")
print(type(a))

##Excercise- Create a function to mutiply 2 numbers & return the answer

#reverse a word
word="pen"
print(word[::-1])
#define a function- take any word & reverse it
def rev(word):
    return word[::-1]

x=rev("anu")
print(x)