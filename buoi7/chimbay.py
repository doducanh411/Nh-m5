import pygame
import sys
from pygame.locals import *  # Import QUIT và các hằng số khác
import random
# Khởi tạo Pygame và thiết lập cửa sổ
pygame.init()
chieu_dai = 800
chieu_rong = 600
w = pygame.display.set_mode((chieu_dai, chieu_rong))
pygame.display.set_caption('Trò chơi né chim')

background = pygame.image.load('bg2.jpg')  # Thay 'bg2.jpg' bằng đường dẫn đến ảnh nền của bạn
background = pygame.transform.scale(background, (chieu_dai, chieu_rong))  # Thay đổi kích thước ảnh nền cho phù hợp với cửa sổ
# Màu sắc
WHITE = (255, 255, 255)

# Tạo hình ảnh con chim của người chơi
chim_nguoi_choi = pygame.image.load('chim1.png')
chim_nguoi_choi = pygame.transform.scale(chim_nguoi_choi, (50, 40))
chieu_cao_chim = chim_nguoi_choi.get_height()
x_chim = 100
y_chim = chieu_rong // 2
van_toc_y = 0  # Tốc độ di chuyển của chim theo trục y
luc_trong_truong = 0.5  # Trọng lực tác động lên chim
luc_nhay = -10  # Lực khi nhấn phím để chim nhảy lên

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

# Khung thời gian
FPS = 60
fpsClock = pygame.time.Clock()

# Hàm kiểm tra va chạm
def kiem_tra_va_cham(x_chim, y_chim, ds_chim_doi_thu):
    for doi_thu in ds_chim_doi_thu:
        if (x_chim + 50 > doi_thu[0] and x_chim < doi_thu[0] + 60) and (y_chim + 40 > doi_thu[1] and y_chim < doi_thu[1] + 50):
            return True
    # Kiểm tra nếu chim chạm vào mép trên/dưới màn hình
    if y_chim <= 0 or y_chim >= chieu_rong - chieu_cao_chim:
        return True
    return False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE and not game_over:
                van_toc_y = luc_nhay  # Chim nhảy lên khi nhấn phím space

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
            diem += 1  # Tăng điểm khi né được chim đối thủ

        # Kiểm tra va chạm
        if kiem_tra_va_cham(x_chim, y_chim, ds_chim_doi_thu):
            game_over = True

    # Vẽ nền và các đối tượng
    w.fill((0, 150, 255))  # Màu nền xanh dương
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
