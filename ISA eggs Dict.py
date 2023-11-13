import random

egg_color = []
eggWeight = []
colors = ["red", "orange", "yellow", "green", "blue", "purple", "black", "grey", "navy", "silver", "gold"]


def color(colors):
    egg_color = colors[random.randint(0, len(colors) - 1)]
    return egg_color

#  Returns a random color from an array named color
def weight():
    weight = random.randint(20, 45)
    return weight

#  Returns a random weight between 20 and 45


for i in range(50):
    egg_color.append(color(colors))
    eggWeight.append(weight())


class ISAEggs:
    def __init__(self, class_color, weight):

        self.class_color = class_color

        self.class_weight = weight

        self.egg_colors = {
            "red": {
                "quantity": 0,
                "Total weight": 0
            },
            "orange": {
                "quantity": 0,
                "Total weight": 0
            },
            "yellow": {
                "quantity": 0,
                "Total weight": 0
            },
            "green": {
                "quantity": 0,
                "Total weight": 0
            },
            "blue": {
                "quantity": 0,
                "Total weight": 0
            },
            "purple": {
                "quantity": 0,
                "Total weight": 0
            },
        }
        for i in range(len(self.class_color) - 1):
            try:
                self.egg_colors[self.class_color[i]]["quantity"] += 1
                self.egg_colors[self.class_color[i]]["Total weight"] += self.class_weight[i]
            except KeyError:
                self.egg_colors.update({self.class_color[i]: {"quantity": 0, "Total weight": 0}})
                self.egg_colors[self.class_color[i]]["quantity"] += 1
                self.egg_colors[self.class_color[i]]["Total weight"] += self.class_weight[i]

    def collect(self):
        return self.egg_colors

    def ask(self, query):
        try:
            rpse = self.egg_colors[query]


        except KeyError:
            rpse = "This color is not present or there are no eggs of this color"
        return rpse

    def total_weight(self):
        total = 0
        for i in range(len(self.egg_colors)):
            total += self.egg_colors[self.class_color[i]]["Total weight"]
        return total


egg = ISAEggs(egg_color, eggWeight, colors)
color_tally = egg.collect

print(egg.ask(input("what color would you like to query?")))
print(color_tally())
print("The total weight is ",egg.total_weight())
