# OpenCV Image Translation.
Image translation using OpenCV.
## Contents :
I have used the following functions/methods:

| Function        |Action                                                                        |
|----------------:|------------------------------------------------------------------------------|
|cv2.imread()              | We read the image                                                   |
|cv2.warpAffine()          |  We rotate the image using the rotation matrix                      |


## Test Image used: 
I have used image-15.png that can be found in the repository.

![Source Image Sequence](image-15.png)
![Source Image Sequence](translated_image.jpg)

## Summary:

```python
# create the translation matrix using tx and ty, it is a NumPy array 
translation_matrix = np.array([
    [1, 0, tx],
    [0, 1, ty]
], dtype=np.float32)
```

