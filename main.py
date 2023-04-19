import pygame
import sys
import time
import os
from photo_positioning import *
from Buttons import *
from back import *
from prizma_size import *
from PIL import Image

pygame.init()
FPS = 60
screen_sizes = [[500, 500], [1920, 1080], [2560, 1440], [3440, 1440], [2160, 1620]]
screen_size_choose = 0
screen_size = screen_sizes[screen_size_choose]
W, H = screen_size[0], screen_size[1]
dis = pygame.display.set_mode((W, H))
pygame.display.set_caption('ProjectMagdeev')
clock = pygame.time.Clock()

icon = pygame.image.load('images/awesome_icon.bmp')

sizes_dict = dict()
sizes_dict = {
    'main': [W // 2, H // 2],
    'back': [0, H],
    '0_settings': [W // 2, 350], #screen_size[1] // 2 + размер кнопки + 100 (чтобы не сливались)
    '1_settings': [W // 2, 700],
    '2_settings': [W // 2, 900],
    '3_settings': [W // 2, 900],
    '4_settings': [W // 2, H // 2 + 200],
}

pygame.display.set_icon(icon)

is_photo = 0
is_image = 0
is_settings = 0
is_screenshot = 0
is_guide = 0
is_guide_button_pressed = 0
is_main_programm = 0
is_menu = 1
run = 1
while run:
    for event in pygame.event.get():
        screen_size = screen_sizes[screen_size_choose]
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and is_menu:
            x, y = event.pos
            if settings_button.collide_point(x, y):
                is_settings = True
                is_menu = False
            elif main_button.collide_point(x, y):
                is_main_programm = True
                is_menu = False
        if event.type == pygame.MOUSEBUTTONDOWN and (is_settings or is_main_programm):
            x, y = event.pos
            if back_button.collide_point(x, y):
                is_menu = True
                is_settings = False
                is_main_programm = False
                is_guide = False
                is_guide_button_pressed = False

        if event.type == pygame.MOUSEBUTTONDOWN and is_settings:
            x, y = event.pos
            if screen_size_change_button.collide_point(x, y):
                if screen_size_choose != 4:
                    screen_size_choose += 1
                else:
                    screen_size_choose = 0


        if event.type == pygame.MOUSEBUTTONDOWN and is_main_programm:
            x, y = event.pos
            if show_button.collide_point(x, y):
                app = QApplication(sys.argv)
                ex = Prizma_Size()
                ex.showDialog()
                cube_size = int(ex.hey)
                make_four_photos()
                is_photo = 1
                photo_up_surf = pygame.image.load('images\im_up.png')
                photo_up_rect = photo_up_surf.get_rect(midbottom=(W // 2, (H // 2) - (cube_size // 2)))
                photo_right_surf = pygame.image.load('images\im_right.png')
                photo_right_rect = photo_right_surf.get_rect(midleft=((W // 2) + (cube_size // 2), H // 2))
                photo_down_surf = pygame.image.load('images\im_down.png')
                photo_down_rect = photo_down_surf.get_rect(midtop=(W // 2, (H // 2) + (cube_size // 2)))
                photo_left_surf = pygame.image.load('images\im_left.png')
                photo_left_rect = photo_left_surf.get_rect(midright=((W // 2) - (cube_size // 2), (H // 2)))
                is_screenshot = 1
                is_guide = 0
                is_guide_button_pressed = 0
            if guide_button.collide_point(x, y):
                is_guide = 1
                is_guide_button_pressed = 1


    if screen_size_choose == 0:
        screen_size = screen_sizes[screen_size_choose]
        W, H = screen_size[0], screen_size[1]
        dis = pygame.display.set_mode((W, H), pygame.RESIZABLE)
        if is_guide_button_pressed == 0:
            guide_button = Show_Button(W, H - 120, 'images/guide_bg_0.png')
        settings_button = Button(W // 2, (sizes_dict.get('0_settings'))[1], 'images/settings_button_0.png')
        main_button = Button(W // 2, H // 2, 'images/main_button_0.png')
        back_button = Back_Button(0, H, 'images/back_button_0.png')
        screen_size_change_button = Button(W // 2, H // 2, 'images/screen_size_change_button_0.png')

        show_button = Show_Button(W, H, 'images/show_button_0.png')

        guide_bg = Background('images/guide_bg.png', [0,0])
        menu_bg = Background('images/menu_universal_bg.png', [0,0])
        main_bg = Background('images/main_universal_bg.png', [0,0])
        settings_bg = Background('images/settings_bg_0.png', [0,0])
    elif screen_size_choose == 1:
        screen_size = screen_sizes[screen_size_choose]
        W, H = screen_size[0], screen_size[1]
        dis = pygame.display.set_mode((W, H), pygame.RESIZABLE)

        guide_button = Show_Button(W, H - 120, 'images/guide_bg_0.png')
        settings_button = Button(W // 2, (sizes_dict.get('1_settings'))[1], 'images/settings_button_1.png')
        main_button = Button(W // 2, H // 2, 'images/main_button_1.png')
        back_button = Back_Button(0, H, 'images/back_button_1.png')
        screen_size_change_button = Button(W // 2, H // 2, 'images/screen_size_change_button_1.png')

        show_button = Show_Button(W, H, 'images/show_button_0.png')

        menu_bg = Background('images/menu_universal_bg.png', [0,0])
        main_bg = Background('images/main_universal_bg.png', [0,0])
        settings_bg = Background('images/settings_bg_1.png', [0,0])
    elif screen_size_choose == 2:
        screen_size = screen_sizes[screen_size_choose]
        W, H = screen_size[0], screen_size[1]
        dis = pygame.display.set_mode((W, H), pygame.RESIZABLE)

        guide_button = Show_Button(W, H - 120, 'images/guide_bg_0.png')
        settings_button = Button(W // 2, (sizes_dict.get('2_settings'))[1], 'images/settings_button_2.png')
        main_button = Button(W // 2, H // 2, 'images/main_button_2.png')
        back_button = Back_Button(0, H, 'images/back_button_2.png')
        screen_size_change_button = Button(W // 2, H // 2, 'images/screen_size_change_button_2.png')

        show_button = Show_Button(W, H, 'images/show_button_1.png')

        menu_bg = Background('images/menu_universal_bg.png', [0,0])
        main_bg = Background('images/main_universal_bg.png', [0,0])
        settings_bg = Background('images/settings_bg_2.png', [0,0])


    elif screen_size_choose == 3:
        screen_size = screen_sizes[screen_size_choose]
        W, H = screen_size[0], screen_size[1]
        dis = pygame.display.set_mode((W, H), pygame.RESIZABLE)

        guide_button = Show_Button(W, H - 120, 'images/guide_bg_0.png')
        settings_button = Button(W // 2, (sizes_dict.get('3_settings'))[1], 'images/settings_button_3.png')
        main_button = Button(W // 2, H // 2, 'images/main_button_3.png')
        back_button = Back_Button(0, H, 'images/back_button_3.png')
        screen_size_change_button = Button(W // 2, H // 2, 'images/screen_size_change_button_3.png')

        show_button = Show_Button(W, H, 'images/show_button_1.png')

        menu_bg = Background('images/menu_universal_bg.png', [0,0])
        main_bg = Background('images/main_universal_bg.png', [0,0])
        settings_bg = Background('images/settings_bg_3.png', [0,0])
    elif screen_size_choose == 4:

        screen_size = screen_sizes[screen_size_choose]
        W, H = screen_size[0], screen_size[1]
        dis = pygame.display.set_mode((W, H), pygame.RESIZABLE)
        if is_guide_button_pressed == 0:
            guide_button = Show_Button(W, H - 400, 'images/guide_bg_0.png')
        settings_button = Button(W // 2, (sizes_dict.get('4_settings'))[1], 'images/settings_button_1.png')
        main_button = Button(W // 2, H // 2, 'images/main_button_1.png')
        back_button = Back_Button(0, H - 200, 'images/back_button_2.png')
        screen_size_change_button = Button(W // 2, H // 2, 'images/screen_size_change_button_4.png')

        show_button = Show_Button(W, H - 200, 'images/show_button_1.png')

        menu_bg = Background('images/menu_universal_bg.png', [0,0])
        main_bg = Background('images/main_universal_bg.png', [0,0])
        settings_bg = Background('images/settings_bg_4.png', [0,0])
    guide_bg = Background('images/guide_bg.png', [0,0])

    if is_menu:

        dis.blit(menu_bg.image, menu_bg.rect)
        dis.blit(settings_button.image, settings_button.rect)
        dis.blit(main_button.image, main_button.rect)
    if is_settings:
        dis.blit(settings_bg.image, settings_bg.rect)
        dis.blit(back_button.image, back_button.rect)
        dis.blit(screen_size_change_button.image, screen_size_change_button.rect)
    if is_main_programm:
        dis.blit(main_bg.image, main_bg.rect)
        if is_photo == 0:
            dis.blit(back_button.image, back_button.rect)
            dis.blit(show_button.image, show_button.rect)
        if is_guide_button_pressed == 0 and is_photo == 0:
            dis.blit(guide_button.image, guide_button.rect)

    if is_photo and is_main_programm:
        dis.blit(photo_left_surf, photo_left_rect)
        dis.blit(photo_up_surf, photo_up_rect)
        dis.blit(photo_right_surf, photo_right_rect)
        dis.blit(photo_down_surf, photo_down_rect)
        if is_screenshot:

            dis.blit(photo_left_surf, photo_left_rect)
            dis.blit(photo_up_surf, photo_up_rect)
            dis.blit(photo_right_surf, photo_right_rect)
            dis.blit(photo_down_surf, photo_down_rect)
            pygame.image.save(dis,"final_image\Final_image.png")
            is_screenshot = 0
    if is_guide:
        dis.blit(guide_bg.image, guide_bg.rect)
        dis.blit(back_button.image, back_button.rect)
        if is_guide_button_pressed == 0:
            dis.blit(guide_button.image, guide_button.rect)

    pygame.display.update()
    clock.tick(FPS)
if is_photo:
    os.remove('images\im_up.png')
    os.remove('images\im_down.png')
    os.remove('images\im_right.png')
    os.remove('images\im_left.png')
exit()
