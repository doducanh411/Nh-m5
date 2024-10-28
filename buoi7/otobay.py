import pygame, sys
from pygame.locals import *

# Khởi tạo Pygame
pygame.init()

# Kích thước cửa sổ
chieu_dai = 800
chieu_rong = 500
w = pygame.display.set_mode((chieu_dai, chieu_rong))
pygame.display.set_caption('Ô tô chuyển động')

# Tải ảnh ô tô
oto1 = pygame.image.load('oto1.png')  # Tải ô tô 1
oto1 = pygame.transform.scale(oto1, (100, 60))  # Kích thước ô tô 1
oto2 = pygame.image.load('oto2.png')  # Tải ô tô 2
oto2 = pygame.transform.scale(oto2, (100, 60))  # Kích thước ô tô 2

# Vị trí ban đầu của các ô tô
x_oto1 = 0
y_oto1 = 100
x_oto2 = chieu_dai
y_oto2 = 200

# Tốc độ di chuyển
toc_do_oto1 = 5  # Tốc độ ô tô 1
toc_do_oto2 = 3  # Tốc độ ô tô 2

# Khung thời gian
FPS = 60
fpsClock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Di chuyển ô tô
    x_oto1 += toc_do_oto1
    x_oto2 -= toc_do_oto2

    # Reset vị trí nếu ô tô ra ngoài màn hình
    if x_oto1 > chieu_dai:
        x_oto1 = 0
    if x_oto2 < -100:  # 100 là chiều rộng của ô tô
        x_oto2 = chieu_dai

    # Vẽ nền (nếu có)
    w.fill((255, 255, 255))  # Màu trắng làm nền

    # Vẽ ô tô lên cửa sổ
    w.blit(oto1, (x_oto1, y_oto1))
    w.blit(oto2, (x_oto2, y_oto2))

    # Cập nhật cửa sổ
    pygame.display.update()
    fpsClock.tick(FPS)
