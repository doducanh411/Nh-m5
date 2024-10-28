import pygame
import sys
from pygame.locals import *
import random

# Khởi tạo Pygame và thiết lập cửa sổ
pygame.init()
chieu_dai = 800
chieu_rong = 600
w = pygame.display.set_mode((chieu_dai, chieu_rong))
pygame.display.set_caption('Trò chơi né chim')

# Màu sắc
WHITE = (255, 255, 255)

# Tạo hình ảnh nền
background = pygame.image.load('bg2.jpg')
background = pygame.transform.scale(background, (chieu_dai, chieu_rong))

# Tạo hình ảnh con chim của người chơi
chim_nguoi_choi = pygame.image.load('chim1.png')
chim_nguoi_choi = pygame.transform.scale(chim_nguoi_choi, (60, 40))
chieu_cao_chim = chim_nguoi_choi.get_height()
x_chim = 100
y_chim = chieu_rong // 2
van_toc_y = 0
luc_trong_truong = 0.5
luc_nhay = -10

# Tạo hình ảnh các chim đối thủ
chim_doi_thu = pygame.image.load('chim2.png')
chim_doi_thu = pygame.transform.scale(chim_doi_thu, (60, 50))

# Tạo danh sách các chim đối thủ (x, y)
ds_chim_doi_thu = [[chieu_dai, random.randint(0, chieu_rong - 50)]]

# Tốc độ di chuyển của chim đối thủ
toc_do_chim_doi_thu = 5

# Khởi tạo biến điều khiển trò chơi
game_over = False
diem = 0
paused = False

# Khung thời gian
FPS = 60
fpsClock = pygame.time.Clock()

# Khởi tạo nhạc nền và hiệu ứng
pygame.mixer.init()

# Thêm nhạc nền
pygame.mixer.music.load('nhacnen.mp3')
pygame.mixer.music.play(-1)  # Phát lặp lại liên tục

# Thêm hiệu ứng âm thanh khi vượt qua chướng ngại vật
sound_effect = pygame.mixer.Sound('pass.mp3')

# Hàm kiểm tra va chạm không có khoảng cách va chạm
def kiem_tra_va_cham(x_chim, y_chim, ds_chim_doi_thu):
    bien_x = 5  # Biên cho chiều ngang
    bien_y = 5  # Biên cho chiều dọc

    for doi_thu in ds_chim_doi_thu:
        if (x_chim + 50 - bien_x > doi_thu[0] and x_chim + bien_x < doi_thu[0] + 60) and \
           (y_chim + 40 - bien_y > doi_thu[1] and y_chim + bien_y < doi_thu[1] + 50):
            return True
    if y_chim <= 0 or y_chim >= chieu_rong - chieu_cao_chim:
        return True
    return False

# Hàm chọn độ khó, thêm nền
def chon_do_kho():
    global toc_do_chim_doi_thu
    # Hiển thị menu chọn độ khó
    while True:
        # Thêm hình nền cho màn chọn độ khó
        w.blit(background, (0, 0))

        font = pygame.font.SysFont(None, 48)
        text_easy = font.render(f" 1 easy", True, WHITE)
        text_medium = font.render(f"2 normal", True, WHITE)
        text_hard = font.render(f" 3 hard", True, WHITE)
        w.blit(text_easy, (chieu_dai // 2 - 100, chieu_rong // 2 - 50))
        w.blit(text_medium, (chieu_dai // 2 - 150, chieu_rong // 2))
        w.blit(text_hard, (chieu_dai // 2 - 100, chieu_rong // 2 + 50))

        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_1:
                    toc_do_chim_doi_thu = 4  # Độ khó dễ
                    return
                elif event.key == K_2:
                    toc_do_chim_doi_thu = 8  # Độ khó trung bình
                    return
                elif event.key == K_3:
                    toc_do_chim_doi_thu = 12  # Độ khó khó
                    return

# Vòng lặp chính của trò chơi
while True:
    if not game_over:
        # Nếu chưa chọn độ khó, cho phép người chơi chọn độ khó
        if toc_do_chim_doi_thu == 5:  # Mặc định là độ khó dễ
            chon_do_kho()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE and not game_over and not paused:
                van_toc_y = luc_nhay
            if event.key == K_p:  # Nhấn P để tạm dừng
                paused = not paused  # Đảo ngược trạng thái tạm dừng

    if not paused:
        if not game_over:
            # Trọng lực tác động lên chim
            van_toc_y += luc_trong_truong
            y_chim += van_toc_y

            # Cập nhật vị trí của các chim đối thủ
            ds_chim_doi_thu = [[doi_thu[0] - toc_do_chim_doi_thu, doi_thu[1]] for doi_thu in ds_chim_doi_thu]

            # Thêm chim đối thủ mới khi cần
            if ds_chim_doi_thu[-1][0] < chieu_dai - 300:
                ds_chim_doi_thu.append([chieu_dai, random.randint(0, chieu_rong - 50)])

            # Loại bỏ chim đối thủ ra khỏi danh sách nếu đã ra khỏi màn hình
            if ds_chim_doi_thu[0][0] < -60:
                ds_chim_doi_thu.pop(0)
                diem += 1
                sound_effect.play()  # Phát âm thanh khi vượt qua chướng ngại vật

            # Kiểm tra va chạm
            if kiem_tra_va_cham(x_chim, y_chim, ds_chim_doi_thu):
                game_over = True

    # Vẽ nền và các đối tượng
    w.blit(background, (0, 0))
    w.blit(chim_nguoi_choi, (x_chim, y_chim))

    for doi_thu in ds_chim_doi_thu:
        w.blit(chim_doi_thu, (doi_thu[0], doi_thu[1]))

    # Hiển thị điểm
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {diem}", True, WHITE)
    w.blit(score_text, (10, 10))

    # Cập nhật màn hình
    pygame.display.update()
    fpsClock.tick(FPS)

    # Nếu game over, hiện thông báo và chờ người chơi nhấn space để chơi lại
    if game_over:
        font = pygame.font.SysFont(None, 72)
        game_over_text = font.render("Game Over", True, WHITE)
        w.blit(game_over_text, (chieu_dai // 2 - 150, chieu_rong // 2 - 50))
        pygame.display.update()
        pygame.time.delay(2000)
        ds_chim_doi_thu = [[chieu_dai, random.randint(0, chieu_rong - 50)]]
        y_chim = chieu_rong // 2
        van_toc_y = 0
        diem = 0
        game_over = False
