def find_top_seller(products: dict, sales: dict) -> str:
    return max(products, key=lambda item: products[item] * sales[item])


if __name__ == "__main__":
    print(find_top_seller(
        {"Olma": 5000, "Banan": 8000, "Uzum": 7000},
        {"Olma": 10,   "Banan": 5,    "Uzum": 8}
    ))
