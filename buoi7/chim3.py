import pygame
import sys
from pygame.locals import *
import random

# Khởi tạo kích thước cửa sổ
chieu_dai = 800  # Chiều dài cửa sổ
chieu_rong = 500  # Chiều cao cửa sổ

# Khởi tạo Pygame
pygame.init()
w = pygame.display.set_mode((chieu_dai, chieu_rong))  # Tạo cửa sổ game
pygame.display.set_caption('Tiêu đề của game')

# Tạo nền của game
anh_nen = pygame.image.load('bg2.jpg')
anh_nen = pygame.transform.scale(anh_nen, (chieu_dai, chieu_rong))

# Tạo ảnh con chim
chim1 = pygame.image.load('chim1.jpg')
chim1 = pygame.transform.scale(chim1, (80, 70))
chim2 = pygame.image.load('chim2.jpg')
chim2 = pygame.transform.scale(chim2, (80, 70))

# Tạo vị trí ban đầu
x1 = 0
y1 = random.randint(0, chieu_rong - 70)  # Vị trí y ngẫu nhiên cho chim 1
x2 = chieu_dai
y2 = random.randint(0, chieu_rong - 70)  # Vị trí y ngẫu nhiên cho chim 2

# Khởi tạo khung thời gian
FPS = 60
fpsClock = pygame.time.Clock()

while True:  # Tạo vòng lặp game
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                y1 = max(0, y1 - 5)  # Di chuyển chim 1 lên
            if event.key == K_DOWN:
                y1 = min(chieu_rong - 70, y1 + 5)  # Di chuyển chim 1 xuống

    # Vẽ ảnh nền
    w.blit(anh_nen, (0, 0))
    w.blit(chim1, (x1, y1))  # Vẽ chim 1
    w.blit(chim2, (x2, y2))  # Vẽ chim 2

    # Cập nhật vị trí chim
    x1 += 1  # Chim 1 bay từ trái qua phải
    x2 -= 1  # Chim 2 bay từ phải qua trái

    # Reset vị trí chim khi ra khỏi màn hình
    if x1 > chieu_dai:
        x1 = 0
        y1 = random.randint(0, chieu_rong - 70)  # Đặt chim 1 ở vị trí ngẫu nhiên
    if x2 < 0:
        x2 = chieu_dai
        y2 = random.randint(0, chieu_rong - 70)  # Đặt chim 2 ở vị trí ngẫu nhiên

    pygame.display.update()  # Cập nhật màn hình
    fpsClock.tick(FPS)  # Điều chỉnh tốc độ khung hình
