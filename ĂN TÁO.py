#Code của chế độ này tương tự như chế độ cổ điển
#Chỉ thay đổi số liệu của 1 vài dòng code liên quan đến táo và một số yếu tố khác để phù hợp với chế độ này hơn, được đánh dấu bằng kí hiệu '#(*)'
import pygame, sys , random
pygame.display.set_caption("Flappy Bird - ĂN TÁO")
icon = pygame.image.load('C:/Users/HP/PycharmProjects/pythonProject8/chim.png')
pygame.display.set_icon(icon)
def san2():
    screen.blit(san, (vitrisan, 670))
    screen.blit(san, (vitrisan+ 432, 670))
def taoongvatao():
    ViTriOng = random.choice([275,300,325,350,375,400,425,450,475,500,525])
    ong_duoi = ong.get_rect(midtop=(500, ViTriOng))
    ong_tren = ong.get_rect(midtop=(785, ViTriOng - 700)) #(*) Thay đổi vị trí xuất hiên của ống (thay đổi x) và khoảng cách (thay đổi y), đảm bảo game không quá khó

    ViTriTao = random.choice([275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550, 575, 600, 625, 650, 675, 700, 725, 750]) #(*) Vị trí y của biến quả táo, sử dụng random.choice()
    qua_tao = tao.get_rect(center=(500, ViTriTao)) #(*) Tạo hình chữ nhật cho táo
    return ong_duoi, ong_tren, qua_tao #(*)
def ongvataodichuyen(ongs,taos): #(*) Thay đổi thành hàm để cả ống và táo di chuyển
    for O in ongs:
        O.centerx -= 3.3
    for T in taos:
        T.centerx -= 4.5
    return ongs, taos
def veong(ongs):
    for O in ongs:
        if O.bottom >= 600:
            screen.blit(ong, O)
        else:
            ong_nguoc = pygame.transform.flip(ong,False,True)
            screen.blit(ong_nguoc,O)
def vetao(taos): #(*) Vẽ táo lên trên màn hình
    for T in taos:
        screen.blit(tao, T)

def VaCham(ongs):
    for O in ongs:
        if HCNchim.colliderect(O):
            sound_ChamCot.play()
            sound_Chet.play()
            return False
    if HCNchim.top <= -75 or HCNchim.bottom >= 670:
        sound_ChamCot.play()
        sound_Chet.play()
        return False
    return True
def GhiDiem(taos): #Hàm kiểm tra va chạm giữa chim và táo, qua đó tính điểm
    global diem
    for T in taos:
        if HCNchim.colliderect(T) and HCNchim.centerx == T.centerx: #Kiểm tra va chạm giữa chim và táo, thêm điều kiện nhỏ để phù hợp với phần giới thiệu của chế độ này
            listtao.remove(T)
            diem += 1
            sound_GhiDiem.play()
def CapNhatDiemCao(diem,Diemcao):
    if diem > Diemcao:
        Diemcao = diem
    return Diemcao
def HienDiem(trangthai):
    if trangthai == 'main game':
        HienThiDiem = phong.render(str(int(diem)),True,(255,255,255))
        HCNdiem = HienThiDiem.get_rect(center = (216,100))
        screen.blit(HienThiDiem,HCNdiem)
    if trangthai == 'game over':
        HienThiDiem = phong.render(f'Diem cua ban: {int(diem)}', True, (255, 255, 255))
        HCNdiem = HienThiDiem.get_rect(center=(216, 50))
        screen.blit(HienThiDiem, HCNdiem)

        HienThiDiemCao = phong.render(f'Diem Cao: {int(Diemcao)}', True, (255, 255, 255))
        HCNdiemcao = HienThiDiemCao.get_rect(center=(216, 560))
        screen.blit(HienThiDiemCao, HCNdiemcao)

        HienThiChoiLai = phong.render(f'Nhan T de choi lai', True, (255, 255, 255))
        HCNchoilai = HienThiChoiLai.get_rect(center=(216, 620))
        screen.blit(HienThiChoiLai, HCNchoilai)

        HienThiChuT = phong.render(f'T', True, (255,255,255))
        HCNchuT = HienThiChuT.get_rect(center=(152,500))
        screen.blit(HienThiChuT,HCNchuT)

        HienThiChuT2 = phong.render(f'T', True, (255, 255, 255))
        HCNchuT2 = HienThiChuT2.get_rect(center=(280, 500))
        screen.blit(HienThiChuT2, HCNchuT2)
def xoay_chim(chim1):
    chim2 = pygame.transform.rotozoom(chim1,-chim_move*2.8,1)
    return chim2
def HieuUngChimDapCanh():
    chim2 = listchim[chim_index]
    HCNchim2 = chim2.get_rect(center = (100,HCNchim.centery))
    return chim2, HCNchim2

pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.init()

screen= pygame.display.set_mode((432,768))

clock = pygame.time.Clock()

trongluc = 0.24
chim_move = 0
game = True
diem = 0
Diemcao = 0


phong= pygame.font.Font('font.TTF',40)

nen = pygame.image.load('C:/Users/HP/PycharmProjects/pythonProject8/nen.png')
nen = pygame.transform.scale2x(nen)

san = pygame.image.load('C:/Users/HP/PycharmProjects/pythonProject8/san.png')
san = pygame.transform.scale2x(san)
vitrisan = 0

chimlen = pygame.transform.scale2x(pygame.image.load('C:/Users/HP/PycharmProjects/pythonProject8/chimlen.png'))
chimgiua = pygame.transform.scale2x(pygame.image.load('C:/Users/HP/PycharmProjects/pythonProject8/chim.png'))
chimxuong = pygame.transform.scale2x(pygame.image.load('C:/Users/HP/PycharmProjects/pythonProject8/chimxuong.png'))
listchim = [chimxuong,chimgiua,chimlen]
chim_index = 0
chim = listchim[chim_index]
HCNchim = chim.get_rect(center = (100,204))

ong = pygame.image.load('C:/Users/HP/PycharmProjects/pythonProject8/ong.png')
ong = pygame.transform.scale2x(ong)
listong= []

#(*) Tạo táo và list cho táo
tao = pygame.image.load('C:/Users/HP/PycharmProjects/pythonProject8/apple.png')
listtao = []

ongHienThi = pygame.USEREVENT
pygame.time.set_timer(ongHienThi, 1725)
taoHienThi = pygame.USEREVENT + 1 #(*)Đưa taoHienThi thành một event trong game
pygame.time.set_timer(taoHienThi, 500)
ChimDapCanh = pygame.USEREVENT + 2
pygame.time.set_timer(ChimDapCanh,25)

TongKet = pygame.transform.scale2x(pygame.image.load('C:/Users/HP/PycharmProjects/pythonProject8/TongKet.png'))
HCNTongKet = TongKet.get_rect(center = (216,290))

sound_DapCanh = pygame.mixer.Sound('C:/Users/HP/PycharmProjects/pythonProject8/sound_dapcanh.wav')
sound_ChamCot = pygame.mixer.Sound('C:/Users/HP/PycharmProjects/pythonProject8/sound_chamcot.wav')
sound_Chet = pygame.mixer.Sound('C:/Users/HP/PycharmProjects/pythonProject8/sound_chet.wav')
sound_GhiDiem = pygame.mixer.Sound('C:/Users/HP/PycharmProjects/pythonProject8/sound_ghidiem.wav')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game:
                chim_move = 0
                chim_move = chim_move -7.25
                sound_DapCanh.play()
            if event.key == pygame.K_t and game == False:
                game = True
                listong.clear()
                listtao.clear() #(*)
                HCNchim.center= (100,204)
                chim_move = 0
                diem = 0
        if event.type == ongHienThi: #(*)
            listong.extend(taoongvatao()) #(*)
        if event.type == taoHienThi: #(*)
            listtao.extend(taoongvatao()) #(*)
        if event.type == ChimDapCanh:
            if chim_index < 2:
                chim_index += 1
            else:
                chim_index = 0
            chim, HCNchim = HieuUngChimDapCanh()

    screen.blit(nen,(0,0))

    if game:

        chim_move += trongluc
        chim_xoay = xoay_chim(chim)
        HCNchim.centery += chim_move
        screen.blit(chim_xoay,HCNchim)
        game=VaCham(listong)
        GhiDiem(listtao) #(*) Đưa hàm def GhiDiem vào trong game
        listong,listtao = ongvataodichuyen(listong,listtao) #(*) Đổi thành vẽ các hiệu ứng của ống và táo lên màn hình
        veong(listong)
        vetao(listtao) #(*) Vẽ táo lên màn hình
        HienDiem('main game')
    else:
        screen.blit(TongKet, HCNTongKet)
        Diemcao = CapNhatDiemCao(diem,Diemcao)
        HienDiem('game over')


    vitrisan -= 1
    san2()
    if vitrisan <= -432:
        vitrisan = 0



    pygame.display.update()
    clock.tick(120)