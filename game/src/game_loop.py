import pygame


class GameLoop:
    def __init__(self, board, renderer, event_queue, clock, tile_width):
        self._board = board
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock
        self._tile_width = tile_width

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
                if clicked_tile[0] >= 0 and clicked_tile[1] >= 0:
                    print(f"clicked at hex {clicked_tile[0], clicked_tile[1]} tile: {clicked_tile[2]} unit: {clicked_tile[3]}")
                    if clicked_tile[3] > 0:
                        self._board.move_unit(pos, clicked_tile, (0, 0))
            elif event.type == pygame.QUIT:
                return False

    def _render(self):
        self._renderer.render()
