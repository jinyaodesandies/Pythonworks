import random

eggcolor = []
eggweight = []
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


def color():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    egg_color = colors[random.randint(0, 5)]
    return egg_color


def weight():
    weight = random.randint(20, 45)
    return weight


def count(x):
    num = 0
    for elements in x:
        num += 1
    return num


for i in range(50):
    eggcolor.append(color())
    eggweight.append(weight())


class ISAeggs:
    def __init__(self, class_color, weight, colors):

        self.class_color = class_color
        self.weight = weight

    def collect(self):
        egg_colors = [0, 0, 0, 0, 0, 0]
        for i in range(len(eggcolor) - 1):
            for x in range(6):
                if colors[x] == class_color[i]:
                    egg_colors[x] += 1
            print(egg_colors)


egg = ISAeggs(eggcolor, eggweight, colors)
print(egg.collect())
