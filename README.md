
# BOYRAZ DATA AUGMENTATİON
<p align="center">
<img src="https://www.resimyukle.org/images/2021/04/15/890855aa8c438ae049196d4e6be241d8.png" alt="2" border="0">
</p>


this program is used to augmentation images in your datasets.
In this way, it helps you to create a more effective dataset.

First, line location and count cannot ne empty.
İf location in input is Directory and this location extend jpg or png photos,
label with a red background will be correct, else label background will be error images.

-------------------------------

## ROTATE IMAGES

if you want rotate uy photos, u should use rotate button.
Location and count cannot be empty.

<p align="center">
<img src="https://www.resimyukle.org/images/2021/04/15/ee709177e33f70577dfcffbd7a2a60b1.png" alt="3" border="0">
</p>

the counter helps us how many photos we will make,
and rotate function do 3 times rotate 90 celcius your photos and save thats.

------------------------------


Is your photo too bright?
Then click brightness button.
This function use this formula //      img = img * (contrast / 127 + 1) - contrast - brightness  // SO for ONLY DARKENING

<p align="center">
<img src="https://www.resimyukle.org/images/2021/04/15/7a2f840637cb230053d9852b0bfc682e.png" alt="4" border="0">
</p>



---------
## IMAGE ZOOMING

<p align="center">
<img src="https://www.resimyukle.org/images/2021/04/15/af6dd2fd6997e7f1549c87871b5879e8.png" alt="6" border="0">
</p>

THİS FUNCTİON USE this formula // img = cv2.resize(img,(len(img) * zoom) , len(img[0]) * zoom)
// if parameter of zoom is 1, there is no change 
// if paramtere bigger than 1, ur photo will be big, else small


