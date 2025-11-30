def main():
    decision = input("Welcome to Blackjack! Current Total: 0 Draw a card? y or n ")
    if decision.lower() == 'y':
        print(f"hit! {decision}")
    print(decision)

if __name__ == "__main__":
    main()