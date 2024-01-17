#nhập thư viện vào chương trình:
import pygame, sys , random

pygame.display.set_caption("Flappy Bird - CỔ ĐIỂN")
icon = pygame.image.load('C:/Users/HP/PycharmProjects/pythonProject8/chim.png')
pygame.display.set_icon(icon)
#Tạo các hàm cho game:
def san2():
    screen.blit(san, (vitrisan, 670))
    screen.blit(san, (vitrisan+432, 670)) #Tạo sàn thứ 2 với độ dài X bằng sàn thứ 1, 2 sàn sẽ liên tục lùi về đằng sau
def taoong():
    ViTriOng = random.choice([275,300,325,350,375,400,425,450,475,500,525,550])
    ong_duoi = ong.get_rect(midtop = (500,ViTriOng))
    ong_tren = ong.get_rect(midtop=(500, ViTriOng-725))
    return ong_duoi, ong_tren

def ongdichuyen(ongs):
    for O in ongs:
        O.centerx -= 3.3 #chỉnh tốc độ của ống
    return ongs
def veong(ongs):
    for O in ongs:
        if O.bottom >= 600:
            screen.blit(ong, O)
        else:
            ong_nguoc = pygame.transform.flip(ong,False,True)
            screen.blit(ong_nguoc,O)
def VaCham(ongs):
    for O in ongs:
        if HCNchim.colliderect(O): #Nếu HCN của chim không chạm phần trên màn hình hoặc chạm sàn nhưng chạm cột, game == False
            sound_ChamCot.play()
            sound_Chet.play()
            return False
    if HCNchim.top <= -75 or HCNchim.bottom >= 670: #Nếu HCN của chim chạm vào phần trên màn hình hoặc chạm vào sàn, game == False
        sound_ChamCot.play()
        sound_Chet.play()
        return False
    return True #Nếu HCN của chim không chạm vào gì, game == True, trò chơi vẫn tiếp tục

def CapNhatDiemCao(diem,Diemcao):
    if diem > Diemcao:
        Diemcao = diem
    return Diemcao
def HienDiem(trangthai):
    if trangthai == 'main game': #game == True
        HienThiDiem = phong.render(str(int(diem)),True,(255,255,255))
        HCNdiem = HienThiDiem.get_rect(center = (216,200))
        HCNtronnghin = HienThiDiem.get_rect(center = (216,250))
        screen.blit(HienThiDiem,HCNdiem)
        if diem % 500 == 0:
            screen.blit(HienThiDiem,HCNtronnghin) #Mỗi khi qua các mốc 500,1000,... sẽ hiện thông báo ngắn cho người chơi
    if trangthai == 'game over': #game == False
        HienThiDiem = phong.render(f'Diem cua ban: {int(diem)}', True, (255, 255, 255))
        HCNdiem = HienThiDiem.get_rect(center=(216, 50))
        screen.blit(HienThiDiem, HCNdiem)

        HienThiDiemCao = phong.render(f'Diem Cao: {int(Diemcao)}', True, (255, 255, 255))
        HCNdiemcao = HienThiDiemCao.get_rect(center=(216, 560))
        screen.blit(HienThiDiemCao, HCNdiemcao)

        HienThiChoiLai = phong.render(f'Nhan T de choi lai', True, (255,255,255))
        HCNchoilai = HienThiChoiLai.get_rect(center=(216,620))
        screen.blit(HienThiChoiLai, HCNchoilai)

        HienThiChuT = phong.render(f'T', True, (255,255,255))
        HCNchuT = HienThiChuT.get_rect(center=(152,500))
        screen.blit(HienThiChuT,HCNchuT)

        HienThiChuT2 = phong.render(f'T', True, (255, 255, 255))
        HCNchuT2 = HienThiChuT2.get_rect(center=(280, 500))
        screen.blit(HienThiChuT2, HCNchuT2)
def xoay_chim(chim1): #giúp chim xoay được
    chim2 = pygame.transform.rotozoom(chim1,-chim_move*2.8,1)
    return chim2
def HieuUngChimDapCanh():
    chim2 = listchim[chim_index]
    HCNchim2 = chim2.get_rect(center = (100,HCNchim.centery))
    return chim2, HCNchim2

pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.init()
#Tạo màn hình với kích cỡ 432x768
screen= pygame.display.set_mode((432,768))
#Tạo biến clock
clock = pygame.time.Clock()
#tạo phông
phong = pygame.font.Font('font.TTF',40)
#Tạo các biến cho trò chơi
trongluc = 0.24
chim_move = 0
game = True
diem = 0
Diemcao = 0
#chèn nền
nen = pygame.image.load('nen.png')
nen = pygame.transform.scale2x(nen)
#chèn sàn
san = pygame.image.load('san.png')
san = pygame.transform.scale2x(san)
vitrisan = 0
#Tạo chim
chimlen = pygame.transform.scale2x(pygame.image.load('C:/Users/HP/PycharmProjects/pythonProject8/chimlen.png'))
chimgiua = pygame.transform.scale2x(pygame.image.load('C:/Users/HP/PycharmProjects/pythonProject8/chim.png'))
chimxuong = pygame.transform.scale2x(pygame.image.load('C:/Users/HP/PycharmProjects/pythonProject8/chimxuong.png'))
listchim = [chimxuong,chimgiua,chimlen]
chim_index = 0
chim = listchim[chim_index]
HCNchim = chim.get_rect(center = (100,0))
#Giúp chim đập cánh
ChimDapCanh = pygame.USEREVENT + 1
pygame.time.set_timer(ChimDapCanh,25)
#tạo ống
ong = pygame.image.load('C:/Users/HP/PycharmProjects/pythonProject8/ong.png')
ong = pygame.transform.scale2x(ong)
listong= []
#timer cho ống
ongHienThi = pygame.USEREVENT
pygame.time.set_timer(ongHienThi, 1125) #thời gian xuất hiện ống
#tạo màn hình tổng kết
TongKet = pygame.transform.scale2x(pygame.image.load('C:/Users/HP/PycharmProjects/pythonProject8/TongKet.png'))
HCNTongKet = TongKet.get_rect(center = (216,290))
#chèn âm thanh
sound_DapCanh = pygame.mixer.Sound('C:/Users/HP/PycharmProjects/pythonProject8/sound_dapcanh.wav')
sound_ChamCot = pygame.mixer.Sound('C:/Users/HP/PycharmProjects/pythonProject8/sound_chamcot.wav')
sound_Chet = pygame.mixer.Sound('C:/Users/HP/PycharmProjects/pythonProject8/sound_chet.wav')
sound_1000d = pygame.mixer.Sound('C:/Users/HP/PycharmProjects/pythonProject8/sound_ghidiem.wav')
#vòng lặp của trò chơi
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN: #khi có phím được ấn xuống:
            if event.key == pygame.K_SPACE and game: #khi đang trong trò chơi(game == True), ấn phím cách để chim có thể bay
                chim_move = 0
                chim_move = chim_move -7.25
                sound_DapCanh.play()
            if event.key == pygame.K_t and game == False: #trong màn hình tổng kết(game == False), ấn T để chơi lại(game == True)
                game = True
                listong.clear()
                HCNchim.center= (100,0)
                chim_move = 0
                diem = 0
        if event.type == ongHienThi:
            listong.extend(taoong())
        if event.type == ChimDapCanh:
            if chim_index < 2:
                chim_index += 1
            else:
                chim_index = 0
            chim, HCNchim = HieuUngChimDapCanh()
    screen.blit(nen,(0,0)) #Hiển thị nền lên màn hình

    if game:
        #biểu diễn các hiệu ứng của chim lên màn hình
        chim_move += trongluc #trọng lực
        chim_xoay = xoay_chim(chim)
        HCNchim.centery += chim_move #HCN chim đi theo chim
        screen.blit(chim_xoay,HCNchim)
        #Kiểm tra va chạm giữa chim và ống, nếu chim va chạm với ống thì game = False, màn hình tổng kết xuất hiện
        game=VaCham(listong)
        #Vẽ các hiệu ứng của ống lên màn hình
        listong = ongdichuyen(listong)
        veong(listong)
        #Hiển thi hệ thống tính điểm
        diem += 5
        if diem % 1000 == 0:
            sound_1000d.play() #Mỗi khi đạt 1000,2000,... điểm sẽ phát ra
        HienDiem('main game')
    else:
        #Khi game == False, hiển thị màn hinh tổng kết
        screen.blit(TongKet, HCNTongKet)
        Diemcao = CapNhatDiemCao(diem,Diemcao)
        HienDiem('game over')


    vitrisan -= 1 #giúp sàn liên tục di chuyển
    san2() #Vẽ sàn lên màn hình
    if vitrisan <= -432:
        vitrisan = 0 #sau khi sàn thứ 1 di chuyển ra khỏi màn hình, nó lập tức chuyển sang sau sàn thứ 2 để tiếp tục di chuyển

    pygame.display.update()  # không có nó, khi chạy sẽ chỉ xuất hiện màn hình đen
    clock.tick(120) #Giúp màn hình trò chơi hiển thị với tốc độ 120fps