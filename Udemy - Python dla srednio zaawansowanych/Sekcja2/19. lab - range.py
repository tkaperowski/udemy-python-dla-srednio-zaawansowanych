lista = ["red", "orange", "green", "violet", "blue", "yellow"]

def color_gen(lista, n):
    print('Cała lista: ', lista, id(lista))
    lista_final = lista.copy()
    lista_final = lista_final[:n]
    print('Lista kolorów: ', lista_final, id(lista_final))
    return lista_final


color_gen(lista, 2)


def get_list_of_colors(colors, n):
    return colors[:n]


colors = ["red", "orange", "green", "violet", "blue", "yellow"]

for i in range(1, len(colors) + 1):
    print(get_list_of_colors(colors, i))