import pygame
import sys
import time
from pygame.locals import *

# Khởi tạo Pygame
pygame.init()
chieu_dai, chieu_rong = 800, 600
w = pygame.display.set_mode((chieu_dai, chieu_rong))
pygame.display.set_caption('Trò chơi xe tải đường đồi núi')

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Thiết lập các thông số trò chơi
FPS = 60
fpsClock = pygame.time.Clock()
start_time = time.time()  # Bắt đầu tính giờ
game_duration = 60  # 60 giây (1 phút)

# Tải hình ảnh
oto_img = pygame.image.load('oto.png')
oto_img = pygame.transform.scale(oto_img, (60, 40))  # Chỉnh kích thước ảnh xe tải
nui_img = pygame.image.load('nui.png')
nui_img = pygame.transform.scale(nui_img, (100, 200))  # Chỉnh kích thước ảnh núi

# Xe tải
xe_tai = oto_img.get_rect(center=(chieu_dai // 4, chieu_rong // 2))  # Lấy vị trí ban đầu của xe tải
toc_do_xe = 5

# Tạo núi (dùng hình ảnh)
mountains = [
    pygame.Rect(200, 150, 100, 200),
    pygame.Rect(400, 100, 100, 250),
    pygame.Rect(600, 200, 100, 200)
]

# Đích đến
finish_line = pygame.Rect(750, 0, 50, chieu_rong)

# Hàm kiểm tra va chạm
def kiem_tra_va_cham():
    for mountain in mountains:
        if xe_tai.colliderect(mountain):
            return True
    return False

# Hàm hiển thị thời gian lên màn hình
def hien_thi_thoi_gian():
    elapsed_time = time.time() - start_time
    remaining_time = max(0, game_duration - elapsed_time)
    font = pygame.font.SysFont(None, 36)
    time_text = font.render(f'Time left: {int(remaining_time)}s', True, BLACK)
    w.blit(time_text, (10, 10))
    return remaining_time

# Vòng lặp chính
while True:
    w.fill((135, 206, 235))  # Màu nền xanh trời

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Di chuyển xe tải
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        xe_tai.x -= toc_do_xe
    if keys[K_RIGHT]:
        xe_tai.x += toc_do_xe
    if keys[K_UP]:
        xe_tai.y -= toc_do_xe
    if keys[K_DOWN]:
        xe_tai.y += toc_do_xe

    # Vẽ xe tải và núi bằng hình ảnh
    w.blit(oto_img, xe_tai)  # Vẽ xe tải
    for i, mountain in enumerate(mountains):
        w.blit(nui_img, (mountain.x, mountain.y))  # Vẽ núi

    # Vẽ đích
    pygame.draw.rect(w, BLACK, finish_line)  # Vẽ đích

    # Hiển thị thời gian
    remaining_time = hien_thi_thoi_gian()

    # Kiểm tra va chạm
    if kiem_tra_va_cham() or remaining_time == 0:
        font = pygame.font.SysFont(None, 72)
        if remaining_time == 0:
            game_over_text = font.render("Time's up!", True, BLACK)
        else:
            game_over_text = font.render("Game Over", True, BLACK)
        w.blit(game_over_text, (chieu_dai // 2 - 150, chieu_rong // 2 - 50))
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()

    # Kiểm tra về đích
    if xe_tai.colliderect(finish_line):
        font = pygame.font.SysFont(None, 72)
        win_text = font.render("You Win!", True, BLACK)
        w.blit(win_text, (chieu_dai // 2 - 150, chieu_rong // 2 - 50))
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()

    # Cập nhật màn hình
    pygame.display.update()
    fpsClock.tick(FPS)
