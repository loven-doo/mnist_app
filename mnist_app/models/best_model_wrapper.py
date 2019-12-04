import torch
import torch.nn as nn

from mnist_app.models.model_wrapper_base import ModelWrapperBase


class BestModelWrapper(ModelWrapperBase):

    def __init__(self):
        self.model = nn.Sequential(nn.Linear(784, 128),
                                   nn.ReLU(),
                                   nn.Linear(128, 64),
                                   nn.ReLU(),
                                   nn.Linear(64, 10),
                                   nn.LogSoftmax(dim=1))
    
    @classmethod
    def load(cls, model_info, **kwargs):
        device = kwargs.get("device", "cpu").lower()

        model_wrapper = cls()
        model_wrapper.model.load_state_dict(torch.load(model_info["weights_path"], map_location=torch.device(device)))
        model_wrapper.model.eval()
        return model_wrapper

    def predict(self, img_tensor, **kwargs):
        return self.model(img_tensor.float())###

