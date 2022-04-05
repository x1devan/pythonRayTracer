from image import Image
from color import Color


def main():
    WIDTH = 3
    HEIGHT = 2

    im = Image(WIDTH, HEIGHT)

    red = Color(1, 0, 0)
    green = Color(0, 1, 0)
    blue = Color(0, 0, 1)

    im.set_pixel(0, 0, red)
    im.set_pixel(1, 0, green)
    im.set_pixel(2, 0, blue)

    im.set_pixel(0, 1, red + green)
    im.set_pixel(1, 1, red + green + blue)
    im.set_pixel(2, 1, red * 0.001)


    with open("test2.ppm", "w") as img_file:
        im.write_ppm(img_file)

if __name__ == "__main__":
    main()