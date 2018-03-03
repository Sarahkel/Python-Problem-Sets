# Sarah Scholz 03/03/2018
# "Write a Python script that reads the Iris data set in and prints the four numerical values on each row in a nice format."
# helful code found on:
# https://stackoverflow.com/questions/25874582/how-to-format-a-line-in-python
# https://stackoverflow.com/questions/25342992/possible-to-add-newline-to-format-method//

with open("data/iris.csv") as f:
    for line in f: 
     print('{:5} {:5} {:5} {:5}'.format(line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3]))

    