import pygame

class Brick(pygame.Rect):
    def __init__(self, x, y , health = 1, color = None):
        super().__init__(x, y, 75, 20)
        ### 벽돌 구분을 위해 색과 체력 추가 ###
        self.color = color if color is not None else (255, 255, 255)
        self.health = health
        ###

### 스테이지마다 체력이 2인 벽돌을 적절히 생성 ###
def get_stage_1_bricks():
    bricks = []
    for i in range(6):
        for j in range(8):
            if (i + j) % 4 == 0:
                bricks.append(Brick(20 + j * 85, 20 + i * 30, health=2, color=( 0, 0,255)))  # 두 번 깨야 하는 벽돌
            else:
                bricks.append(Brick(20 + j * 85, 20 + i * 30, health=1, color=(255, 255, 255)))
    return bricks


def get_stage_2_bricks():
    bricks = []
    for i in range(6):
        for j in range(8):
            if (i + j) % 2 == 0:
                if (i + j) % 4 == 0:
                    bricks.append(Brick(20 + j * 85, 20 + i * 30, health=2, color=( 0, 0,255)))  # 두 번 깨야 하는 벽돌
                else:
                    bricks.append(Brick(20 + j * 85, 20 + i * 30, health=1, color=(255, 255, 255)))
    return bricks

def get_stage_3_bricks():
    bricks = []
    for i in range(6):
        for j in range(8):
            if i % 2 == 0:
                if j % 4 == 0:
                    bricks.append(Brick(20 + j * 85, 20 + i * 30, health=2, color=(0, 0,255)))  # 두 번 깨야 하는 벽돌
                else:
                    bricks.append(Brick(20 + j * 85, 20 + i * 30, health=1, color=(255, 255, 255)))
            else:
                if j % 4 == 1:
                    bricks.append(Brick(20 + j * 85 + 42, 20 + i * 30, health=2, color=( 0, 0, 255)))  # 두 번 깨야 하는 벽돌
                else:
                    bricks.append(Brick(20 + j * 85 + 42, 20 + i * 30, health=1, color=(255, 255, 255)))
    return bricks

def get_stage_4_bricks():
    bricks = []
    for i in range(6):
        for j in range(8):
            if (i * j) % 3 != 0:
                if (i + j) % 4 == 0:
                    bricks.append(Brick(20 + j * 85, 20 + i * 30, health=2, color=(255, 0, 0)))  # 두 번 깨야 하는 벽돌
                else:
                    bricks.append(Brick(20 + j * 85, 20 + i * 30, health=1, color=(255, 255, 255)))
    return bricks

###
