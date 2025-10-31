# Plan to make Blackjack - Python
## Classes
- Game - main object where game is played and logic is handled
- Card - will spawn a card for hit
        - have the suit and number
        - used in game file
## Imports
- random
## Logic
- Gameplay

    - ask the user in the terminal if they want another card, have enter 'y' or 'n'
    - show current total
    - if get another card
        - only ask again and show total if total under 21
        - else show you lost, and ask to play a new round
    - if decide to exit just show total and end program

## Implementation
- Card
    - "__init__" suit, card number with random generated number 1-13 (ace, 2-10, jack, queen, king) then map to proper number or face, and another random generated for 1-4 (diamond, spade, clubs, heart) for suit
    - only init and make card if valid combo 
- Game
    - track seen cards, current total
    - init -> total, seen is a set with tuple (suit, number)
    - ask the user prompts

    program start
        Welcome to Blackjack! Current Total: 0 Draw a card?
        y or n

    if y then call Card init while card not valid (found in seen) -> reassign this card to a new value

        check if this value + current total is more than 21
        if yes then print went over!
        if not show current total, current cards and draw card

    if n then end program


        
