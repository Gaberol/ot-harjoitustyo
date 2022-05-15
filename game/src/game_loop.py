import pygame


class GameLoop:
    def __init__(self, board, renderer, event_queue, clock, tile_width, max_players):
        self._board = board
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock
        self._tile_width = tile_width
        self._max_players = max_players

        self._selected_tile = False
        self._player = 1

    def start(self):
        while True:
            if self._handle_events() == False:
                break

            self._render()

            self._clock.tick(60)

    def _handle_events(self):
        for event in self._event_queue.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                clicked_tile = self._board.mouse_event(pos)
                if clicked_tile[0] < 0 or clicked_tile[1] < 0: continue
                if clicked_tile == self._selected_tile: continue
                print(f"clicked at hex {clicked_tile[0], clicked_tile[1]} tile: {clicked_tile[2]} unit: {clicked_tile[3]}")
                
                if clicked_tile[2] == self._player:
                    if clicked_tile[3] > 0 and not self._selected_tile:
                        print("Selecting unit")
                        self._selected_tile = clicked_tile
                    elif self._selected_tile:
                        print("moving unit")
                        self._board.move_unit(self._selected_tile, clicked_tile)
                        self._selected_tile = False
                    else:
                        print("clicked empty tile")
                elif False:
                    pass
                else:
                    if self._selected_tile:
                        print("deselecting unit")
                        self._selected_tile = False
                    else:
                        print("clicked nothing")
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self._advance_turn()
            elif event.type == pygame.QUIT:
                return False

    def _render(self):
        self._renderer.render()

    def _advance_turn(self):
        if self._player == self._max_players:
            self._player = 1
        else:
            self._player += 1
