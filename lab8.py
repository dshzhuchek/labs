from PIL import Image, ImageDraw, ImageFont
def g1():
    p = Image.open('IMG_0623.JPG')
    p2 = p.crop((20,20,440,440))
    p2.show()
    p2.save('p2.JPG')

def g2():
    otkr = {
        '8 марта' : 'IMG_0624.JPG',
        '23 февраля' : 'IMG_0626.JPG',
        'новый год' : 'IMG_0627.JPG',
        '14 февраля' : 'IMG_0629.JPG',
        'день рождения' : 'IMG_0628.JPG'
    }
    o = []
    prazd = input('Введите название праздника:')
    if prazd in otkr:
        card = Image.open(otkr[prazd])
        card.show()
    else:
        print('Открытки к данному празднику нет')
def g3():
    name = input('Как зовут того, кого вы хотите поздравить?') + ' ,поздравляю!'
    p = Image.open('IMG_0623.JPG')
    p2 = p.crop((20, 20, 440, 440))
    draw = ImageDraw.Draw(p2)
    font = ImageFont.truetype('arial.ttf',36)
    draw.text((50,50), name, font=font, fill=(255,0,0))
    p2.save('p3.PNG')
    p2.show()
g3()