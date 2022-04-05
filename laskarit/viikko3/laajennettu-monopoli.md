```mermaid
 classDiagram
 Board "1" ..> "2..8" Player
 Start "1" --> Square
 Jail "1" --> Square
 class Board{
     move_player(id)
 }
 class Player{
     id
     money
     position
 }
 class Square{
     id
     next_square
 class Start{
     id
     next_square
 class Jail{
     id
     next_square
 }
```
