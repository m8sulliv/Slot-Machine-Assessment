# Slot-Maching-Assessment
Technical Interview for a Slot Machine Game

Imagine a simple three-reel slot machine. Each of the three reels contain a total of 72 symbols
and on each spin one of these symbols will be randomly chosen to land. In the mix of symbols is
a special bonus 7 symbol with the following frequencies:

Reel 1: 3 7s
Reel 2: 2 7s
Reel 3: 1 7s

Above each of the three reels is a seven-segment bonus meter. Whenever a bonus 7 symbol
lands on a reel it contributes to the bonus meter for its reel, increasing it by one. On a spin
where all seven segments on all three reels are filled, the player is awarded a bonus of 200 coins
and the bonus feature ends. All three meters are reset to zero for the next spin and a new
bonus feature begins. If a 7 lands on a reel whose meter is full but the other meters are not
completed, the player is awarded a bonus of 2 coins for that reel and the bonus feature
continues.

Write a mathematical proof of the average number of spins needed to complete a bonus
feature, as well as the average number of coins won. Provide a simulation which verifies your
results in a language of your choice. C++ or python is preferred but use anything you're
comfortable with.
