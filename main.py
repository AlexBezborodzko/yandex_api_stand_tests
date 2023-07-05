
# цвет чая: 0 - зеленый, 1 - чёрный, 2 - красный
color_tea = 1;
# есть ли лимон
has_lemon = True;
# есть ли сахар
has_sugar = False;

marisa_drinks_tea = color_tea == 1 and (has_lemon or has_sugar);
print("Пьет ли чай Мариса:", marisa_drinks_tea)

sergey_drinks_tea = not color_tea == 2 and (has_lemon or has_sugar)
print("Пьет ли чай Серёга:", sergey_drinks_tea);

sasha_drinks_tea = not color_tea == 2 and (has_lemon and has_sugar)
print("Пьет ли чай Саша:", sasha_drinks_tea)