```mermaid
 classDiagram
 Board "1" ..> "2..8" Player
 Board "1" --> "40" Square
 Player "2.8" --> "40" Square
 class Board{
     move_player(id)
 }
 class Player{
     id
     position
 }
 class Square{
     id
     next_square
 }
```
