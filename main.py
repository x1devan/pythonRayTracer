from engine import RenderEngine
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
    # A Red Ball Sphere(Point(0, 0, 0), 0.5, Color.from_hex("#FF0000"))
    objects = [Sphere(Point(0, 0 - 0.2, 0), 0.1, Color.from_hex("#FF0000")), Sphere(Point(0, 0.25 - 0.2, 0), 0.1, Color.from_hex("#FFFF00")), Sphere(Point(0, 0.5 - 0.2, 0), 0.1, Color.from_hex("#00FF00"))]
    scene = Scene(camera, objects, WIDTH, HEIGHT)
    engine = RenderEngine()

    image = engine.render(scene)

    with open("test3.ppm", "w") as img_file:
        image.write_ppm(img_file)

if __name__ == "__main__":
    main()