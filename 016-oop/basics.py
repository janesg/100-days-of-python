from turtle import Turtle, Screen
from prettytable import PrettyTable

# big_t = Turtle()
# big_t.shape("turtle")
# big_t.color("chartreuse")
#
# big_t.forward(25)
# big_t.right(90)
# big_t.forward(50)
# big_t.right(90)
# big_t.forward(50)
# big_t.right(90)
#
# my_screen = Screen()
# my_screen.exitonclick()

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table)
