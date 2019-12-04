import os
import yaml


TESTS_DIR = os.path.join("mnist_app", "tests")


class ConfConstants(object):

    known_model_wrappers = ("BestModelWrapper",)

    def __init__(self):
        self.port = 5000
        self.model_path = "mnist_app/models/best_model/best_model.json"
        self.nthreads = 4
        self.device = "CPU"
        self.upload_folder = "mnist_app/uploads"

    def update_by_config(self, config_path):
        with open(config_path) as config_f:
            params_dict = yaml.load(config_f, Loader=yaml.FullLoader)
        self.port = int(params_dict.get("port", self.port))
        self.model_path = params_dict.get("model_path", self.model_path)
        self.nthreads = int(params_dict.get("nthreads", self.nthreads))
        self.device = params_dict.get("device", self.device)
        self.upload_folder = params_dict.get("upload_folder", self.upload_folder)


conf_constants = ConfConstants()

