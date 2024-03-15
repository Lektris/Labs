#5.	Написати програму, яка знаходить мінімальний та максимальний елементи двовимірного масиву.
def знайти_мінімальний_максимальний(масив):
    мінімальний = максимальний = масив[0][0]  # Починаємо з першого елемента як початкових значень

    for рядок in масив:
        for елемент in рядок:
            if елемент < мінімальний:
                мінімальний = елемент
            elif елемент > максимальний:
                максимальний = елемент

    return мінімальний, максимальний

мій_масив = [
    [3, 7, 1],
    [9, 4, 8],
    [2, 5, 6]
]

мінімальний, максимальний = знайти_мінімальний_максимальний(мій_масив)
print("Мінімальний елемент:", мінімальний)
print("Максимальний елемент:", максимальний)