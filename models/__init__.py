import json

from mnist_app.constants import ConfConstants
from mnist_app.models.best_model_wrapper import BestModelWrapper


class ModelLoader(object):

    def __init__(self, model=None):
        self.model = model

    
    def from_conf_constants(self, conf_constants):
        assert isinstance(conf_constants, ConfConstants), "ERROR"
        with open(conf_constants.model_path) as model_info_f:
            model_info = json.load(model_info_f)
        if model_info["model_wrapper"] in ConfConstants.known_model_wrappers:
            self.model = eval(model_info["model_wrapper"]).load(model_info, 
                                                                device=conf_constants.device)

