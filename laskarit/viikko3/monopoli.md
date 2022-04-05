```mermaid
 classDiagram
 Game "1" ..> "2..8" Player
 Player "2.8" --> "40" Square
 class Game{
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
