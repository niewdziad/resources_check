from typing import List, Tuple

# Dostępne zasoby w magazynie
storage = {
    'wood': 100,
    'stone': 50,
    'bricks': 200,
    'glass': 30
}

def has_enough_resources(required_resources: List[Tuple[str, int]]) -> bool:
    # Iterujemy przez każdy zasób wymagany do budowy
    for resource, quantity in required_resources:
        # Sprawdzamy czy istnieją odpowiednie zasoby w magazynie
        if resource in storage and storage[resource] >= quantity:
            continue  # Jeśli tak, przechodzimy do kolejnego zasobu
        else:
            return False  # Jeśli brakuje zasobu lub jego ilość jest niewystarczająca, zwracamy False
    return True  # Jeśli dla każdego zasobu wystarczająca ilość została znaleziona, zwracamy True

# Przykłady użycia funkcji has_enough_resources
print(has_enough_resources([("wood", 50), ("stone", 20), ("bricks", 100), ("glass", 20)])) # True
print(has_enough_resources([("wood", 150), ("stone", 20), ("bricks", 50), ("glass", 20)])) # False
