def first_bar_graph():
    import numpy as n
    import matplotlib.pyplot as plt

    # Random gaussian data.
    Ntotal = 1000
    data = 0.05 * n.random.randn(Ntotal) + 0.5

    # This is  the colormap I'd like to use.
    cm = plt.cm.get_cmap('RdYlBu_r')

    # Get the histogramp
    Y,X = n.histogram(data, 25, normed=1)
    x_span = X.max()-X.min()
    C = [cm(((x-X.min())/x_span)) for x in X]

    plt.bar(X[:-1],Y,color=C,width=X[1]-X[0])
    plt.show()
first_bar_graph()


def second_bar_graph():
    import numpy as np
    import matplotlib.pyplot as plt

    Ntotal = 1000
    data = 0.05 * np.random.randn(Ntotal) + 0.5
    cm = plt.cm.get_cmap('RdYlBu_r')

    n, bins, patches = plt.hist(data, 25, normed=1, color='green')
    # To normalize your values
    col = (n-n.min())/(n.max()-n.min())
    for c, p in zip(col, patches):
        plt.setp(p, 'facecolor', cm(c))
    plt.show()

second_bar_graph()
