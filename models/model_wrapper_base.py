from abc import ABCMeta, abstractmethod


class ModelWrapperBase(metaclass=ABCMeta):

    @classmethod
    @abstractmethod
    def load(cls, model_info, **kwargs):
        return

    @abstractmethod
    def predict(self, img_tensor, **kwargs):
        return

