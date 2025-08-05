import random
import string

# Default leet mapping
BASE_LEET_MAP = {
    "a": ["@", "4"], "s": ["$", "5"], "i": ["1", "!"], 
    "e": ["3"], "o": ["0"], "t": ["7"], "b": ["8"]
}

DEFAULT_SYMBOLS = list("!@#$%^&*_-+=?.<>")

def build_leet_map(allowed_chars):
    leet_map = {}
    for k, v in BASE_LEET_MAP.items():
        if allowed_chars:
            filtered = [c for c in v if c.isdigit() or c in allowed_chars]
            leet_map[k] = filtered if filtered else [c for c in v if c.isdigit()]
        else:
            leet_map[k] = v
    return leet_map

def leet_transform(word, leet_map):
    return "".join(random.choice(leet_map.get(ch.lower(), [ch])) if random.random() < 0.4 else ch for ch in word)

def random_case(word):
    return "".join(ch.upper() if random.random() < 0.5 else ch.lower() for ch in word)

def insert_random_chars(word, symbols):
    for _ in range(random.randint(1, 3)):
        pos = random.randint(0, len(word))
        word = word[:pos] + random.choice(symbols + list(string.digits)) + word[pos:]
    return word

def double_random_letters(word):
    return "".join(ch * (2 if random.random() < 0.2 else 1) for ch in word)

def inject_date_patterns(word, date_parts, symbols):
    """Inject dates in multiple mixed realistic patterns with random separators"""
    if not date_parts:
        return word

    dd, mm, yyyy = date_parts
    yy = yyyy[-2:] if yyyy else ""
    
    # pick random separators for extra randomness
    sym1 = random.choice(symbols)
    sym2 = random.choice(symbols + ["-", "_", ".", "#", "@"])

    patterns = []

    # If full date is available
    if dd and mm and yyyy:
        patterns += [
            f"{word}{sym1}{dd}{sym2}{mm}{sym1}{yy}",
            f"{word}{sym1}{yyyy}{sym2}{mm}{sym1}{dd}",
            f"{word}{sym1}{yy}{sym2}{mm}{sym1}{dd}",
            f"{dd}{sym1}{mm}{sym2}{yyyy}{sym1}{word}",
            f"{word.upper()}{sym2}{dd}{sym1}{yyyy}",
            f"{word.lower()}{sym1}{mm}{sym2}{yyyy}",
            f"{yyyy}{sym2}{word}{sym1}{dd}",
            f"{dd}{sym1}{word}{sym2}{yy}",
            f"{yy}{sym2}{word}{sym1}{mm}{sym2}{dd}",
            f"{word}{sym1}{dd}{sym2}{mm}{sym1}{yyyy[::-1]}",
        ]

    # If only year is provided
    elif yyyy:
        patterns += [
            f"{word}{sym1}{yyyy}",
            f"{yyyy}{sym2}{word}",
            f"{word}{sym2}{yy}",
            f"{yy}{sym1}{word}",
            f"{word.upper()}{sym2}{yyyy}",
            f"{word.lower()}{sym1}{yy}{sym2}{yyyy}",
            f"{yyyy[::-1]}{sym1}{word}",
        ]

    return random.choice(patterns)


def generate_variations(base, count, date_parts=None, custom_symbols=None):
    symbols = custom_symbols if custom_symbols else DEFAULT_SYMBOLS
    leet_map = build_leet_map(custom_symbols)
    words = set()

    while len(words) < count:
        w = base
        if random.random() < 0.5: w = leet_transform(w, leet_map)
        if random.random() < 0.5: w = random_case(w)
        if random.random() < 0.4: w = insert_random_chars(w, symbols)
        if random.random() < 0.3: w = double_random_letters(w)
        if date_parts and random.random() < 0.6: w = inject_date_patterns(w, date_parts, symbols)
        if random.random() < 0.2: w = w[::-1]
        if custom_symbols and random.random() < 0.3: w += random.choice(symbols)
        words.add(w)

    return list(words)

def main():
    base_input = input("Enter a name or email ID: ").strip()
    base_word = base_input.split("@")[0] if "@" in base_input else base_input
    base_word = base_word.replace(" ", "")  # ✅ Remove spaces from name


    print("How many words should the wordlist contain?")
    print("1] 100")
    print("2] 1000")
    print("3] 10000")
    print("4] Custom number")

    while True:
        choice = input("Choose an option (1/2/3/4): ").strip()
        if choice == "1":
            word_count = 100
            break
        elif choice == "2":
            word_count = 1000
            break
        elif choice == "3":
            word_count = 10000
            break
        elif choice == "4":
            try:
                word_count = int(input("Enter custom number of words: ").strip())
                if word_count > 0: break
            except ValueError:
                print("Invalid number. Try again.")
        else:
            print("Invalid choice, please select 1, 2, 3, or 4.")

    # ✅ Ask about birth date/year naturally
    print("Do you have any dates that resemble the person (e.g., birth date)?")
    print("1] Yes, birth date (dd/mm/yyyy)")
    print("2] Yes, only year (yyyy)")
    print("3] No, skip this")

    date_parts = None
    format_choice = input("Choose an option (1/2/3): ").strip()

    if format_choice == "1":
        birth_date = input("Enter your birth date [dd/mm/yyyy]: ").strip()
        try:
            dd, mm, yyyy = birth_date.split("/")
            if len(dd) == 2 and len(mm) == 2 and len(yyyy) == 4:
                date_parts = (dd, mm, yyyy)
        except:
            print("Invalid date format. Skipping date patterns.")

    elif format_choice == "2":
        yyyy = input("Enter your birth year [yyyy]: ").strip()
        if yyyy.isdigit() and len(yyyy) == 4:
            date_parts = ("", "", yyyy)

    # ✅ Ask about custom special characters
    use_custom = input("Do you have any specific special characters that should only be used? (y/n): ").strip().lower()
    custom_symbols = None
    if use_custom == "y":
        chars = input("If yes, please enter those characters: ").strip()
        if chars:
            custom_symbols = list(chars)

    # ✅ Generate final wordlist
    wordlist = generate_variations(base_word, word_count, date_parts, custom_symbols)
    filename = f"wordlist_{base_word}.txt"

    with open(filename, "w") as f:
        f.write("\n".join(wordlist))

    print(f"[+] Wordlist generated with {word_count} variations saved as {filename}")

if __name__ == "__main__":
    main()
