# resources_check
#


from typing import List, Tuple
Importuje List i Tuple z modułu typing, co umożliwia deklarację typów argumentów funkcji.


storage = {
    'wood': 100,
    'stone': 50,
    'bricks': 200,
    'glass': 30
}
Definiuje słownik storage, który przechowuje dostępne zasoby w magazynie. Klucze to nazwy zasobów, a wartości to ich ilości.


def has_enough_resources(required_resources: List[Tuple[str, int]]) -> bool:
Definiuje funkcję has_enough_resources, która przyjmuje listę krotek required_resources, gdzie każda krotka zawiera nazwę zasobu i jego wymaganą ilość. Funkcja zwraca wartość logiczną (True lub False).


for resource, quantity in required_resources:
Iteruje przez każdą krotkę w required_resources, przypisując nazwę zasobu do resource i ilość do quantity.


if resource in storage and storage[resource] >= quantity:
    continue
else:
    return False
Sprawdza, czy zasób jest obecny w magazynie i czy jego ilość jest większa lub równa wymaganej ilości. Jeśli tak, przechodzi do następnej iteracji pętli. W przeciwnym razie zwraca False, oznaczając brak wystarczających zasobów.


return True
Jeśli żaden zasób nie spowodował zwrócenia False, to oznacza, że wystarczające zasoby są dostępne, więc zwraca True.


print(has_enough_resources([("wood", 50), ("stone", 20), ("bricks", 100), ("glass", 20)])) # True
print(has_enough_resources([("wood", 150), ("stone", 20), ("bricks", 50), ("glass", 20)])) # False
Wywołuje funkcję has_enough_resources z przykładowymi zestawami zasobów i wyświetla wyniki, aby sprawdzić, czy funkcja działa zgodnie z oczekiwaniami.