import random
from logo import logo , logo_text


print(logo)
print(logo_text)

# 1. Prepare full deck
cards_by_suit = {
    '♠': ['2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♠'],
    '♥': ['2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♥'],
    '♦': ['2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦', 'A♦'],
    '♣': ['2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣', 'A♣']
}

deck = []
for suit_cards in cards_by_suit.values():
    deck.extend(suit_cards)
random.shuffle(deck)

# 2. Initial cards
user = [deck.pop() for _ in range(4)]
computer = [deck.pop() for _ in range(4)]

card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
               '7': 7, '8': 8, '9': 9, '10': 10,
               'J': 11, 'Q': 12, 'K': 13, 'A': 14}

def get_rank(card): return card[:-1]
def get_suit(card): return card[-1]

user_turn = True

# Game loop
while user and computer:
    print("\n---------------------------")
    print("Your cards:", user)
    print("Computer has", len(computer), "cards.")

    if user_turn:
        # --- User plays first ---
        ui = int(input(f"Your turn! Choose index (0 to {len(user)-1}): "))
        user_card = user.pop(ui)
        suit_to_match = get_suit(user_card)
        print("You played:", user_card)

        # --- Computer tries to match suit ---
        matching = [c for c in computer if get_suit(c) == suit_to_match]
        if matching:
            comp_card = matching[0]
            computer.remove(comp_card)
        else:
            print("Computer has no matching suit. Drawing from deck...")
            drawn = None
            while deck:
                drawn = deck.pop()
                print("Computer drew:", drawn)
                computer.append(drawn)
                if get_suit(drawn) == suit_to_match:
                    comp_card = drawn
                    computer.remove(comp_card)
                    break
            else:
                # Deck finished, no match found, play any
                comp_card = computer.pop(0)
                print("No match even after drawing. Playing random:", comp_card)

        print("Computer played:", comp_card)

    else:
        # --- Computer plays first ---
        comp_card = computer.pop(0)
        suit_to_match = get_suit(comp_card)
        print("Computer played:", comp_card)

        matching = [c for c in user if get_suit(c) == suit_to_match]
        if matching:
            print("You have matching suit cards:", matching)
            ui = int(input(f"Choose index to match (0 to {len(user)-1}): "))
            user_card = user.pop(ui)
        else:
            print("No matching suit. Drawing from deck...")
            drawn = None
            while deck:
                drawn = deck.pop()
                print("You drew:", drawn)
                user.append(drawn)
                if get_suit(drawn) == suit_to_match:
                    user_card = drawn
                    user.remove(user_card)
                    break
            else:
                print("No match found. Choose any card to play.")
                ui = int(input(f"Choose index (0 to {len(user)-1}): "))
                user_card = user.pop(ui)

        print("You played:", user_card)

    # Compare
    user_val = card_values[get_rank(user_card)]
    comp_val = card_values[get_rank(comp_card)]

    if user_val > comp_val:
        print("🎉 You win this round!")
        user_turn = True
    elif user_val < comp_val:
        print("😈 Computer wins this round!")
        user_turn = False
    else:
        print("🤝 Tie! Turn remains same.")

    # Win condition check
    if not user:
        print("\n🏆 You played all your cards. You WIN!!")
        break
    if not computer:
        print("\n💻 Computer played all cards. You LOSE!")
        break
