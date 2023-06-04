import pyimgur

CLIENT_ID = 'a7dad9515fe70de'
PATH1 = 'finpie.jpg'
PATH2 = 'groupbar.jpg'
title = "Uploaded with PyImgur"

im = pyimgur.Imgur(CLIENT_ID)
uploaded_image1 = im.upload_image(PATH1, title=title)
uploaded_image2 = im.upload_image(PATH2, title=title)

print(uploaded_image1.link)
print(uploaded_image2.link)