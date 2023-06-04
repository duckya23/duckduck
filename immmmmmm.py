import pyimgur

CLIENT_ID = 'a7dad9515fe70de'
im = pyimgur.Imgur(CLIENT_ID)
image = im.get_image('f1WHMuW')

print(image.title)
print(image.link)