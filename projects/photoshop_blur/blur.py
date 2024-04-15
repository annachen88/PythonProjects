"""
File: blur.py
Name: Anna
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: SimpleImage, Original picture
    :return new_img: SimpleImage, Blurred image
    Function: Blur the imported image
    Principle: Take the surrounding average value for each point and replace it back into the original RBG.
    """
    new_img = SimpleImage.blank(img.width, img.height)
    for y in range(img.height):
        for x in range(img.width):
            pixel = new_img.get_pixel(x, y)     # Getting pixel of new_img at x,y.
            total_red = 0       # The sum of red pixels of (x, y) and all its neighbors.
            total_blur = 0      # The sum of green pixels of (x, y) and all its neighbors.
            total_green = 0     # The sum of blue pixels of (x, y) and all its neighbors.
            total_num = 0       # Counting the number of neighbor at (x, y).

            if x == 0:
                row_left = x
            else:
                row_left = x - 1

            if y == 0:
                column_up = y
            else:
                column_up = y - 1

            if x == (img.width-1):
                row_right = x
            else:
                row_right = x + 1

            if y == (img.height-1):
                column_down = y
            else:
                column_down = y + 1

            for r in range(row_left, row_right+1):
                for c in range(column_up, column_down+1):
                    total_red += img.get_pixel(r, c).red
                    total_blur += img.get_pixel(r, c).blue
                    total_green += img.get_pixel(r, c).green
                    total_num += 1

            pixel.red = total_red / total_num
            pixel.green = total_green / total_num
            pixel.blue = total_blur / total_num

    return new_img


def main():
    """
    this program is to blur the images
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
