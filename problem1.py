def count_vowels_and_consonants(text: str) -> dict:
    vowels = set("aeiouAEIOU")
    unli = 0
    undosh = 0

    for char in text:
        if char.isalpha():
            if char in vowels:
                unli += 1
            else:
                undosh += 1

    return {"unli": unli, "undosh": undosh}


if __name__ == "__main__":
    print(count_vowels_and_consonants("Salom Dunyo!"))
    print(count_vowels_and_consonants("Python 3!"))
    print(count_vowels_and_consonants("Hello, World!"))
