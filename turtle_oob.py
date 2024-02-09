from prettytable import PrettyTable
# from turtle import  Turtle, Screen


# timmy = Turtle()
# john = Turtle()
# print(timmy)

# timmy.shape("turtle")


# my_screen = Screen()
# my_screen.setup(width=500, height=600)
# print(my_screen.canvwidth)
# timmy.color('red')
# timmy.forward(100)
# john.left(20)
# john.forward(100)

# my_screen.exitonclick()


table = PrettyTable()
table.field_names=["Pokemon Name", "Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "fire"])


table.align = "r"

print(table)