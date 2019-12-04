import yaml


class ConfConstants(object):

    known_model_wrappers = ("BestModelWrapper",)

    def __init__(self):
        self.port = 5000
        self.model_path = "mnist_app/models/best_model/best_model.json"
        self.nthreads = 4
        self.device = "CPU"
        self.upload_folder = "mnist_app/uploads"

    def update_by_config(self, config_path):
        pass


conf_constants = ConfConstants()

