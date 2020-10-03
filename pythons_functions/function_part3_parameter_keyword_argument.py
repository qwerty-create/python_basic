def about(name,age,likes="python"):
    sentence=("meet {} he is {} years old, and he likes to do {}".format(name,age,likes))
    return sentence
my_sentece=about("Jack",23)
my_sentence=about(age=23,name="Jack",likes="Football")
print(my_sentece)