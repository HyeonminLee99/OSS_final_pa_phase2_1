import pygame

class Brick(pygame.Rect):
    def __init__(self, x, y , health = 1, color = None):
        super().__init__(x, y, 75, 20)
        ### 벽돌 구분을 위해 색과 체력 추가 ###
        self.color = color
        self.health = health
        ###

### 스테이지마다 체력이 2인 벽돌을 적절히 생성 ###
def get_stage_1_bricks():
    return [Brick(20 + j * 85, 20 + i * 30) for i in range(6) for j in range(8)]

def get_stage_2_bricks():
    bricks = []
    for i in range(6):
        for j in range(8):
            if (i + j) % 2 == 0:
                bricks.append(Brick(20 + j * 85, 20 + i * 30))
    return bricks

def get_stage_3_bricks():
    bricks = []
    for i in range(6):
        for j in range(8):
            if i % 2 == 0:
                bricks.append(Brick(20 + j * 85, 20 + i * 30))
            else:
                bricks.append(Brick(20 + j * 85 + 42, 20 + i * 30))
    return bricks

def get_stage_4_bricks():
    bricks = []
    for i in range(6):
        for j in range(8):
            if (i * j) % 3 != 0:
                bricks.append(Brick(20 + j * 85, 20 + i * 30))
    return bricks
