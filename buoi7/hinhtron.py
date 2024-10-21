import pygame
import sys
import random

# Khởi tạo Pygame
pygame.init()

# Kích thước cửa sổ
chieu_dai = 800
chieu_rong = 500
w = pygame.display.set_mode((chieu_dai, chieu_rong))
pygame.display.set_caption('Hình tròn chuyển động')

# Định nghĩa các màu sắc
colors = [
    (255, 0, 0),    # Đỏ
    (0, 255, 0),    # Xanh lá
    (0, 0, 255),    # Xanh dương
    (255, 255, 0),  # Vàng
    (255, 0, 255),  # Hồng
    (0, 255, 255),  # Cyan
    (128, 0, 0),    # Nâu
    (0, 128, 0),    # Xanh đậm
    (0, 0, 128),    # Xanh dương đậm
    (128, 128, 0)   # Xám
]

# Tạo danh sách chứa tốc độ cho mỗi hình tròn
speeds = [random.randint(1, 5) for _ in range(10)]  # Tốc độ ngẫu nhiên từ 1 đến 5

# Vị trí và bán kính của các hình tròn
radii = 30
positions = [(random.randint(0, chieu_dai), random.randint(-chieu_rong, 0)) for _ in range(10)]

# Khung thời gian
FPS = 60
fpsClock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Vẽ nền
    w.fill((255, 255, 255))  # Màu trắng

    # Vẽ và di chuyển các hình tròn
    for i in range(10):
        # Cập nhật vị trí hình tròn
        positions[i] = (positions[i][0], positions[i][1] + speeds[i])
        
        # Nếu hình tròn đi ra ngoài màn hình, reset về trên
        if positions[i][1] > chieu_rong:
            positions[i] = (random.randint(0, chieu_dai), -radii)

        # Vẽ hình tròn
        pygame.draw.circle(w, colors[i], (positions[i][0], positions[i][1]), radii)

    # Cập nhật cửa sổ
    pygame.display.update()
    fpsClock.tick(FPS)
