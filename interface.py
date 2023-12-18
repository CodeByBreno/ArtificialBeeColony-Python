import matplotlib.pyplot as plt;

SAMPLING_AMOUNT = 100;

def plot_graph(function, top, bottom, answer, fitness):
    abcissas = [];
    ordenadas = [];

    dx = round((top - bottom)/SAMPLING_AMOUNT, 2);

    x = bottom;
    for i in range(0, SAMPLING_AMOUNT):
        x = x + dx;
        abcissas.append(x);
        ordenadas.append(round(function(x),2));

    build_graph(abcissas, ordenadas, answer, fitness);

def build_graph(abcissas, ordenadas, x, fx):
    plt.plot(abcissas, ordenadas);
    plt.xlabel("x");
    plt.ylabel("F(x)");
    plt.title("Seminário IA - Artificial Bee Colony");

    plot_point(x, fx);

    plt.show();

def plot_point(x, fx):
    plt.scatter(x, fx, color="green", marker="o", label="Ponto");
    