```mermaid
 classDiagram
 Board "1" --> "2..8" Player
 Player "2.8" --> "40" Square
 class Board{
     player_in_turn
     next_turn()
 }
 class Player{
     id
     position
     move()
 }
 class Square{
     id
     next_square
 }
```
