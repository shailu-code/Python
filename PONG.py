import pygame

pygame.init()

WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("---Pong---")

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PAD_WIDTH, PAD_HEIGHT = 20, 100
BALL_RADIUS = 7

SCORE_FONT = pygame.font.SysFont("comicsans", 50)
WINNING_SCORE = 5


class PAD:
    COLOR = WHITE
    VEL = 7

    def __init__(self, x, y, width, height):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.width = width
        self.height = height

    def draw(self, win):
        pygame.draw.rect(
            win, self.COLOR, (self.x, self.y, self.width, self.height))

    def move(self, up=True):
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y


class Ball:
    MAX_VEL = 10
    COLOR = WHITE

    def __init__(self, x, y, radius):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        self.x_vel = self.MAX_VEL
        self.y_vel = 0

    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.y_vel = 0
        self.x_vel *= -1


def draw(win, PADs, ball, left_score, right_score):
    win.fill(BLACK)

    left_score_text = SCORE_FONT.render(f"{left_score}", 1, WHITE)
    right_score_text = SCORE_FONT.render(f"{right_score}", 1, WHITE)
    win.blit(left_score_text, (WIDTH//4 - left_score_text.get_width()//2, 20))
    win.blit(right_score_text, (WIDTH * (3/4) -
                                right_score_text.get_width()//2, 20))

    for PAD in PADs:
        PAD.draw(win)

    for i in range(10, HEIGHT, HEIGHT//20):
        if i % 2 == 1:
            continue
        pygame.draw.rect(win, WHITE, (WIDTH//2 - 5, i, 10, HEIGHT//20))

    ball.draw(win)
    pygame.display.update()


def handle_collision(ball, left_pad, right_pad):
    if ball.y + ball.radius >= HEIGHT:
        ball.y_vel *= -1
    elif ball.y - ball.radius <= 0:
        ball.y_vel *= -1

    if ball.x_vel < 0:
        if ball.y >= left_pad.y and ball.y <= left_pad.y + left_pad.height:
            if ball.x - ball.radius <= left_pad.x + left_pad.width:
                ball.x_vel *= -1

                middle_y = left_pad.y + left_pad.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (left_pad.height / 2) / ball.MAX_VEL
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1 * y_vel

    else:
        if ball.y >= right_pad.y and ball.y <= right_pad.y + right_pad.height:
            if ball.x + ball.radius >= right_pad.x:
                ball.x_vel *= -1

                middle_y = right_pad.y + right_pad.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (right_pad.height / 2) / ball.MAX_VEL
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1 * y_vel


def handle_PAD_movement(keys, left_pad, right_pad):
    if keys[pygame.K_w] and left_pad.y - left_pad.VEL >= 0:
        left_pad.move(up=True)
    if keys[pygame.K_s] and left_pad.y + left_pad.VEL + left_pad.height <= HEIGHT:
        left_pad.move(up=False)

    if keys[pygame.K_UP] and right_pad.y - right_pad.VEL >= 0:
        right_pad.move(up=True)
    if keys[pygame.K_DOWN] and right_pad.y + right_pad.VEL + right_pad.height <= HEIGHT:
        right_pad.move(up=False)


def main():
    run = True
    clock = pygame.time.Clock()

    left_pad = PAD(10, HEIGHT//2 - PAD_HEIGHT //
                         2, PAD_WIDTH, PAD_HEIGHT)
    right_pad = PAD(WIDTH - 10 - PAD_WIDTH, HEIGHT //
                          2 - PAD_HEIGHT//2, PAD_WIDTH, PAD_HEIGHT)
    ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS)

    left_score = 0
    right_score = 0

    while run:
        clock.tick(FPS)
        draw(WIN, [left_pad, right_pad], ball, left_score, right_score)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        handle_PAD_movement(keys, left_pad, right_pad)

        ball.move()
        handle_collision(ball, left_pad, right_pad)

        if ball.x < 0:
            right_score += 1
            ball.reset()
        elif ball.x > WIDTH:
            left_score += 1
            ball.reset()

        won = False
        if left_score >= WINNING_SCORE:
            won = True
            win_text = "Left Player Won!"
        elif right_score >= WINNING_SCORE:
            won = True
            win_text = "Right Player Won!"

        if won:
            text = SCORE_FONT.render(win_text, 1, WHITE)
            WIN.blit(text, (WIDTH//2 - text.get_width() //
                            2, HEIGHT//2 - text.get_height()//2))
            pygame.display.update()
            pygame.time.delay(5000)
            ball.reset()
            left_pad.reset()
            right_pad.reset()
            left_score = 0
            right_score = 0

    pygame.quit()


if __name__ == '__main__':
    main()
