import matplotlib.pyplot as plt


def generate_bar_chart(labels, values):
    fig, ax = plt.subplots()
    bar_labels_months = ['Enero (1)', 'Febrero (2)', 'Marzo (3)', 'Abril (4)', 'Mayo (5)', 'Junio (6)', 'Julio (7)',
                         'Agosto (8)', 'Septiembre (9)', 'Octubre (10)', 'Noviembre (11)', 'Diciembre (12)']
    bar_colors = ['tab:red', 'tab:orange', 'tab:blue', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive',
                  'tab:cyan', 'tab:orange', 'tab:green', 'tab:blue']

    ax.bar(labels, values, label=bar_labels_months, color=bar_colors)

    ax.set_ylabel('Frequency of acts of violence')
    ax.set_title('Frequency of acts of violence vs months of year')
    ax.legend(title='Colors of months', bbox_to_anchor=(1.05, 1), loc='upper right')
    plt.tight_layout()

    plt.show()


def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.show()
