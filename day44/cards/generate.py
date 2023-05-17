from PIL import Image, ImageDraw, ImageFont
import os, sys
""" This script creates a standard playing deck of cards(52).
Tested on windows and linux - OS users will have to modify the
font type and font location.
Usage: python3 script_name.py"""
 
def build_deck(value,suit,polygon):
    if suit == 'hearts':
        fill_color= 'red'
    elif suit == 'diamonds':
        fill_color= 'red'
    else:
        fill_color= 'black'
    im = Image.new("RGB", (360, 430),'lightgray')
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("Chalkduster.ttf", 50)
    draw.text((50, 50), text=value, fill=fill_color, font=font, stroke_width=2,stroke_fill="#0f0")
    if value == '10':
        draw.text((220,300),text=value,fill= fill_color, font=font,
                  stroke_width=2,stroke_fill='#0f0')
    else:
        draw.text((275,300),text=value,fill= fill_color, font=font,
                  stroke_width=2,stroke_fill='#0f0')
    draw.polygon(polygon, fill= fill_color,outline='yellow')
    path= f'{suit}_{value}.png'
    total_path= os.path.join(create_dir,path)
    im.save(total_path,'png')
 
def main():
    baseCards= ['A','2','3','4','5','6','7','8','9',
                         '10','J','Q','K',]
    diamonds= [(174.5, 281.5), (105.5, 197.5), (178.5, 125.5),
               (243.5, 195.5)]
    hearts= [(176.5, 155.5), (190.5, 136.5), (212.5, 119.5),
             (243.5, 116.5), (267.5, 135.5), (261.5, 170.5),
             (247.5, 198.5), (218.5, 228.5), (201.5, 250.5),
             (190.5, 269.5), (172.5, 256.5), (146.5, 234.5),
             (122.5, 202.5), (107.5, 180.5), (99.5, 150.5),
             (107.5, 122.5), (126.5, 108.5), (147.5, 111.5),
             (165.5, 134.5)]
    spades= [(175.5, 134.5), (159.5, 157.5), (141.5, 186.5),
             (129.5, 226.5), (137.5, 249.5), (165.5, 256.5),
             (185.5, 250.5), (190.5, 283.5), (206.5, 283.5),
             (203.5, 253.5), (217.5, 258.5), (240.5, 259.5),
             (256.5, 244.5), (256.5, 215.5), (235.5, 180.5),
             (206.5, 151.5), (186.5, 123.5)]
    clubs= [(158.5, 120.5), (175.5, 120.5), (196.5, 132.5),
            (202.5, 149.5), (201.5, 173.5), (191.5, 186.5),
            (211.5, 178.5), (230.5, 170.5), (252.5, 183.5),
            (253.5, 205.5), (237.5, 228.5), (219.5, 241.5),
            (195.5, 243.5), (181.5, 228.5), (185.5, 271.5),
            (169.5, 270.5), (171.5, 233.5), (158.5, 240.5),
            (140.5, 248.5), (106.5, 232.5), (98.5, 207.5),
            (108.5, 182.5), (136.5, 176.5), (131.5, 165.5),
            (120.5, 137.5), (137.5, 122.5)]    
     
    suits= {'diamonds':diamonds,'hearts':hearts,
            'spades':spades,'clubs':clubs}    
    for key,value in suits.items():        
        for card in baseCards:                       
            build_deck(card, key ,value)
    print('your deck is complete!')
    
if __name__ == '__main__':
    create_dir= 'card_deck_1'
    os.makedirs(create_dir, exist_ok=True)
    if sys.platform == 'linux':
        font = ImageFont.truetype("Tests/fonts/FreeMono.ttf", 120)
    elif sys.platform == 'win32':
        font= imageFont.truetype('arial.ttf', 120)
    elif sys.platform == 'darwin':
        'find a font location that works'
        #font= imageFont.truetype('arial.ttf', 120)
        pass 
    main()
     