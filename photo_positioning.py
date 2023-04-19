from PIL import Image
import pygame

def make_four_photos():
    im_up = Image.open('user_images\myimage.png')
    im_left = im_up.rotate(90)
    im_right = im_up.rotate(270)
    im_down = im_up.rotate(180)
    im_up.save('images\im_up.png')
    im_down.save('images\im_down.png')
    im_left.save('images\im_left.png')
    im_right.save('images\im_right.png')


