from service import Point3D, Angle3D, Color


class Texture:
    pass


class Polygon:
    points: Point3D = []


class PolygonalModel:
    def __init__(self, textures: list[Texture]):
        self.polygons = [Polygon()]
        self.textures = textures


class Flash:
    location: Point3D
    angle: Angle3D
    color: Color
    power: float

    def rotate(self, angle: Angle3D):
        pass

    def move(self, point: Point3D):
        pass


class Camera:
    location: Point3D
    angle: Angle3D

    def rotate(self, angle: Angle3D):
        pass

    def move(self, point: Point3D):
        pass


class Scene:
    def __init__(self, id_: int, models: list[PolygonalModel], flashes: list[Flash], cameras: list[Camera]):
        self.id_ = id_
        if len(models) > 0:
            self.models = models
        else:
            raise ValueError('There must be at least one model in the list of polygonal models')

        if len(cameras) > 0:
            self.cameras = cameras
        else:
            raise ValueError('There must be at least one camera in the list of cameras')

        self.flashes = flashes

    def method1(self, flash: Flash):
        return flash

    def method2(self, camera: Camera):
        return camera
