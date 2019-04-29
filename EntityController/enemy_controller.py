import pygame

from Entity.enemy import Enemy
import config


class EnemyController(object):
    def __init__(self, game):
        self.enemies = pygame.sprite.Group()
        self.game = game
        self.waypoints = game.world.get_waypoints()
        self.start = game.world.get_starting_position()
        self.last = game.world.get_last_position()
        self.n_wave = 0
        self.max_wave = 3
        self.wave_len = 5
        self.num_enemies = 0
        self.finished = True

    def get_enemies(self):
        return self.enemies.sprites()

    def reset(self):
        pygame.time.set_timer(config.ENEMY_SPAWN_EVENT, config.ENEMY_SPAWN_DELAY)
        self.num_enemies = 0
        self.n_wave += 1
        self.finished = False

    def set_wave_len(self, wave_len):
        self.wave_len = wave_len

    def get_group(self):
        return self.enemies

    def update(self, bounds):
        if not self.enemies and not self.finished:
            print('q', self.n_wave)
            self.finished = True
        else:
            self.enemies.update(bounds)
            for enemy in self.enemies.sprites():
                cur = enemy.get_current_waypoint()
                if enemy.visited:
                    enemy.visited = False
                    if cur + 1 == len(self.waypoints):
                        enemy.kill()
                        if self.check_for_win():
                            config.GAME.win()
                        self.num_enemies -= 1
                        config.GAME.customer.money -= config.ENEMY_COST
                        if config.GAME.customer.money <= 0:
                            config.GAME.set_lost()
                    else:
                        enemy.update_current_waypoint(self.waypoints[cur], self.waypoints[cur + 1])

    def check_for_win(self):
        return self.num_enemies == 0 and self.n_wave == self.max_wave

    def draw(self, surface):
        self.enemies.draw(surface)

    def clear(self):
        self.enemies.empty()
        self.num_enemies = 0
        self.n_wave = 0
        self.finished = True

    def spawn(self):
        if self.wave_len != self.num_enemies:
            self.finished = False
            self.num_enemies += 1
            new_enemy = Enemy(self.start, num_waypoints=len(self.waypoints))
            new_enemy.set_destination(self.waypoints[0])
            new_enemy.activate()
            self.enemies.add(new_enemy)
            return False
        return True
