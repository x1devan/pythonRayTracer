from image import Image
from color import Color
from point import Point
from scene import Scene
from vector import Vector
from sphere import Sphere

def main():
    WIDTH = 320
    HEIGHT = 200

    camera = Vector(0, 0, -1)

    objects = [Sphere(Point(0, 0, 0), 0.5), Color.from_hex("#FF000")]
    scene = Scene(camera, objects, WIDTH, HEIGHT)
    engine = RenderEngine()

    image = engine.render(scene)

    with open("test3.ppm", "w") as img_file:
        image.write_ppm(img_file)

if __name__ == "__main__":
    main()