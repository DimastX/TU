import matplotlib.pyplot


def plot():

    data = (1, 2, 3, 4, 5)
    fig, simple_chart = matplotlib.pyplot.subplots()

    simple_chart.plot(data)
    matplotlib.pyplot.show()


#main
plot()
