
import pygame
import sys
import random
from pygame.locals import *


# Khởi tạo Pygame
pygame.init()
chieu_dai, chieu_rong = 800, 600
w = pygame.display.set_mode((chieu_dai, chieu_rong))
pygame.display.set_caption('Trò chơi né ô tô')

# Màu sắc
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Thiết lập các thông số trò chơi
FPS = 60
fpsClock = pygame.time.Clock()

# Hình ảnh nhân vật
nguoi_choi = pygame.Rect(chieu_dai // 2, chieu_rong // 2, 50, 50)
toc_do_nguoi_choi = 5
boost_speed = 10
boost_duration = 5 * FPS  # 5 giây
boost_cooldown = 10 * FPS  # 10 giây

# Thiết lập boost
is_boosting = False
boost_timer = 0
boost_cooldown_timer = 0

# Ô tô đối thủ
car_speed = 2  # Ô tô ban đầu di chuyển chậm hơn
car_increase_interval = 2 * FPS  # Thêm ô tô mỗi 2 giây
car_increase_timer = 0

# Tạo ô tô mới từ các cạnh màn hình
def tao_xe():
    huong = random.choice(['trai', 'phai', 'tren', 'duoi'])
    if huong == 'trai':
        return pygame.Rect(-50, random.randint(0, chieu_rong), 40, 80), 'trai'
    elif huong == 'phai':
        return pygame.Rect(chieu_dai + 50, random.randint(0, chieu_rong), 40, 80), 'phai'
    elif huong == 'tren':
        return pygame.Rect(random.randint(0, chieu_dai), -50, 40, 80), 'tren'
    else:
        return pygame.Rect(random.randint(0, chieu_dai), chieu_rong + 50, 40, 80), 'duoi'

# Bắt đầu với 1 ô tô
cars = [tao_xe()]

# Hàm kiểm tra va chạm
def kiem_tra_va_cham():
    for car, _ in cars:
        if nguoi_choi.colliderect(car):
            return True
    return False

# Hàm vẽ thanh hồi chiêu
def ve_thanh_hoi_chieu(thanh, tong_thanh, x, y, color):
    width = 200
    height = 20
    thanh_length = (thanh / tong_thanh) * width
    pygame.draw.rect(w, color, (x, y, thanh_length, height))
    pygame.draw.rect(w, WHITE, (x, y, width, height), 2)

# Vòng lặp chính
while True:
    w.fill((0, 150, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Di chuyển người chơi
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        nguoi_choi.x -= toc_do_nguoi_choi
    if keys[K_RIGHT]:
        nguoi_choi.x += toc_do_nguoi_choi
    if keys[K_UP]:
        nguoi_choi.y -= toc_do_nguoi_choi
    if keys[K_DOWN]:
        nguoi_choi.y += toc_do_nguoi_choi

    # Kiểm tra nhấn boost (tăng tốc)
    if keys[K_e] and boost_cooldown_timer == 0 and not is_boosting:
        is_boosting = True
        boost_timer = boost_duration
        boost_cooldown_timer = boost_cooldown

    # Cập nhật tốc độ boost
    if is_boosting:
        toc_do_nguoi_choi = boost_speed
        boost_timer -= 1
        if boost_timer <= 0:
            is_boosting = False
            toc_do_nguoi_choi = 5

    # Hồi chiêu boost
    if boost_cooldown_timer > 0:
        boost_cooldown_timer -= 1

    # Cập nhật vị trí ô tô
    for car, huong in cars:
            if huong == 'trai':
                car.x += car_speed
            elif huong == 'phai':
                car.x -= car_speed
            elif huong == 'tren':
                car.y += car_speed
            elif huong == 'duoi':
                car.y -= car_speed

    # Tạo thêm ô tô mỗi 2 giây
    car_increase_timer = car_increase_timer + 1
    if car_increase_timer >= car_increase_interval:
        car_increase_timer = 0
        cars.append(tao_xe())  # Thêm ô tô mới vào danh sách

    # Vẽ người chơi và ô tô
    pygame.draw.rect(w, GREEN, nguoi_choi)
    for car, _ in cars:
        pygame.draw.rect(w, RED, car)

    # Vẽ thanh hồi chiêu
    ve_thanh_hoi_chieu(boost_cooldown_timer, boost_cooldown, 10, 10, BLUE)  # Thanh boost

    # Kiểm tra va chạm
    if kiem_tra_va_cham():
        font = pygame.font.SysFont(None, 72)
        game_over_text = font.render("Game Over", True, WHITE)
        w.blit(game_over_text, (chieu_dai // 2 - 150, chieu_rong // 2 - 50))
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()

    # Cập nhật màn hình
    pygame.display.update()
    fpsClock.tick(FPS)
