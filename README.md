
# BOYRAZ DATA AUGMENTATİON
<p align="center">
<img src="https://user-images.githubusercontent.com/82450697/115392969-d8b31900-a1e9-11eb-9803-5e5e8c6e960d.PNG" alt="2" border="0">
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
<img src="https://user-images.githubusercontent.com/82450697/115393023-e5d00800-a1e9-11eb-84c4-9925dd2cbba0.PNG" alt="3" border="0">
</p>

the counter helps us how many photos we will make,
and rotate function do 3 times rotate 90 celcius your photos and save thats.

------------------------------


Is your photo too bright?
Then click brightness button.
This function use this formula //      img = img * (contrast / 127 + 1) - contrast - brightness  // SO for ONLY DARKENING

<p align="center">
<img src="https://user-images.githubusercontent.com/82450697/115393192-1748d380-a1ea-11eb-9395-be36e1e24ecb.PNG" alt="4" border="0">
</p>



---------
## IMAGE ZOOMING

<p align="center">
<img src="https://user-images.githubusercontent.com/82450697/115393272-292a7680-a1ea-11eb-80fe-9c37953f3d84.PNG" alt="6" border="0">
</p>

THİS FUNCTİON USE this formula // img = cv2.resize(img,(len(img) * zoom) , len(img[0]) * zoom)
// if parameter of zoom is 1, there is no change 
// if paramtere bigger than 1, ur photo will be big, else small


