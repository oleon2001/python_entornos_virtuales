import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['A', 'B', 'C']
    x = [200, 340, 120]

    fig, ax = plt.subplots()
    ax.pie(x, labels=labels)
    plt.savefig('pie.png')
    plt.close()