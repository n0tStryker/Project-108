import plotly.express as pe
import plotly.figure_factory as pff
dresult = []
count =[]
for i in range(1,100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dresult.append(dice1+dice2)
    count.append(i)

fig=pff.create_distplot([dresult],["result"])
fig.show()