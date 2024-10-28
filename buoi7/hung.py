import pygame, sys
from pygame.locals import *
import random

chieu_dai = 800  # Chiều dài cửa sổ
chieu_rong = 500  # Chiều cao cửa sổ
pygame.init()  # Khởi tạo game
w = pygame.display.set_mode((chieu_dai, chieu_rong))  # Tạo 1 cửa sổ game tên là w
pygame.display.set_caption('Hứng hoa quả demo nhóm 2')
# Thêm nhạc nền
pygame.mixer.init()  # Khởi tạo mô-đun mixer
pygame.mixer.music.load('nhacchen.mp3')  
pygame.mixer.music.play(-1)  # Phát nhạc liên tục (-1: lặp lại vô hạn)

w = pygame.display.set_mode((chieu_dai, chieu_rong))  # Tạo 1 cửa sổ game tên là w
pygame.display.set_caption('Tiêu đề của game')

# Khởi tạo giá trị ban đầu
score = 0  # Điểm ban đầu
lives = 3  # Số mạng ban đầu

# Tạo nền của game
anh_nen = pygame.image.load('bg2.jpg')
anh_nen = pygame.transform.scale(anh_nen, (chieu_dai, chieu_rong))

# Tạo ảnh các quả táo, cam, xoài
tao = pygame.image.load('tao.png')
tao = pygame.transform.scale(tao, (60, 70))
cam = pygame.image.load('cam.png')
cam = pygame.transform.scale(cam, (60, 70))
xoai = pygame.image.load('xoai.png')
xoai = pygame.transform.scale(xoai, (60, 70))

# Tạo vị trí ban đầu của các quả
x_tao, y_tao = 100, 0
x_cam, y_cam = 200, 0
x_xoai, y_xoai = 300, 0

# Tạo ảnh con gio (giỏ để hứng quả) và phóng to giỏ
gio = pygame.image.load('gio.png')
gio = pygame.transform.scale(gio, (120, 100))  # Phóng to giỏ lên (120, 100)

# Tạo vị trí ban đầu cho giỏ hứng
x_gio, y_gio = chieu_dai // 2, chieu_rong - 100  # Điều chỉnh vị trí dựa trên kích thước mới

# Khởi tạo khung thời gian
FPS = 60
fpsClock = pygame.time.Clock()

# Hàm kiểm tra nếu quả rơi trúng giỏ
def kiem_tra_hung_fruit(x_fruit, y_fruit):
    global score, lives
    if y_fruit >= y_gio and x_gio <= x_fruit <= (x_gio + 120):  # Điều chỉnh theo kích thước mới
        score += 5  # Cộng 5 điểm nếu hứng đúng
        return True
    elif y_fruit > chieu_rong:
        lives -= 1  # Mất 1 mạng nếu để quả rơi ra ngoài
        return True
    return False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Sử dụng pygame.key.get_pressed() để kiểm tra phím giữ
    keys = pygame.key.get_pressed()

    if keys[K_LEFT] and x_gio > 0:
        x_gio -= 5  # Di chuyển sang trái
    if keys[K_RIGHT] and x_gio < chieu_dai - 120:
        x_gio += 5  # Di chuyển sang phải

    # Kiểm tra game over
    if lives <= 0:
        print("Game Over! Your final score is:", score)
        pygame.quit()
        sys.exit()

    # Vẽ ảnh nền và các đối tượng
    w.blit(anh_nen, (0, 0))
    w.blit(gio, (x_gio, y_gio))  # Vẽ giỏ phóng to

    # Vẽ quả táo, cam, xoài
    w.blit(tao, (x_tao, y_tao))
    w.blit(cam, (x_cam, y_cam))
    w.blit(xoai, (x_xoai, y_xoai))

    # Cập nhật vị trí của các quả
    y_tao += 1
    y_cam += 2
    y_xoai += 3

    # Kiểm tra hứng quả và cập nhật điểm số
    if kiem_tra_hung_fruit(x_tao, y_tao):
        y_tao = 0  # Đặt lại vị trí quả táo
        x_tao = random.randint(0, chieu_dai - 60)
    if kiem_tra_hung_fruit(x_cam, y_cam):
        y_cam = 0  # Đặt lại vị trí quả cam
        x_cam = random.randint(0, chieu_dai - 60)
    if kiem_tra_hung_fruit(x_xoai, y_xoai):
        y_xoai = 0  # Đặt lại vị trí quả xoài
        x_xoai = random.randint(0, chieu_dai - 60)

    # Hiển thị điểm số và mạng sống
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    lives_text = font.render(f"Lives: {lives}", True, (255, 255, 255))
    w.blit(score_text, (10, 10))
    w.blit(lives_text, (chieu_dai - 150, 10))

    # Cập nhật màn hình
    pygame.display.update()
    fpsClock.tick(FPS)
