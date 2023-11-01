from model_elements import PolygonalModel, Flash, Camera, Scene


class IModelChangedObserver:
    def apply_update_model(self):
        pass


class IModelChanger:
    def notify_change(self, sender: IModelChanger):
        pass


class ModelStore(IModelChanger):

    def __init__(self, change_observers: list[IModelChangedObserver]):
        # super().__init__()
        self.models = [PolygonalModel([])]
        self.flashes = [Flash()]
        self.cameras = [Camera()]
        self.scenes = [Scene(0, models=self.models, flashes=self.flashes, cameras=self.cameras)]
        self._change_observers = change_observers

    def get_scena(self, id_: int):
        for scene in self.scenes:
            if scene.id_ == id_:
                return scene

    def notify_change(self, sender: IModelChanger):
        pass
