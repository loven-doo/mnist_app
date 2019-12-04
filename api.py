import os
import time
import json
import socket

import cv2
import numpy as np
import torch
from flask import Flask, request

from mnist_app.constants import conf_constants
from mnist_app.models import ModelLoader


app = Flask("MNIST inferer")
model_loader = ModelLoader()


@app.route("/")
def index():
    return "Enter in your console: curl -F 'file=@%s' " % "&lt;local image path&gt;" + \
           "%s:%s/predict" % (socket.gethostbyname(socket.gethostname()), conf_constants.port)


@app.route("/predict", methods=["GET", "POST"])
def predict():  # This method should be tested automaticaly but from separate test system
    if request.method == 'POST':
        return _predict(request.files['file'])


def _predict(f):  # TODO: write unittest for this function
    f_path = os.path.join(conf_constants.upload_folder, str(int(time.time()))+"_"+os.path.basename(f.filename))
    f.save(f_path)
    # img_matrix = cv2.cvtColor(cv2.imread(f_path), cv2.COLOR_BGR2RGB)
    img_matrix = np.array([np.ravel(cv2.cvtColor(cv2.imread(f_path), cv2.COLOR_BGR2GRAY))]).astype(np.float64)
    img_tensor = torch.from_numpy(img_matrix)
    model = model_loader.model
    result = model.predict(img_tensor)[0]
    result_json = json.dumps(result.tolist(), indent=2)  # output can be the dict of digit logs
    os.remove(f_path)  # can be moved to a storage if needed
    return result_json


def run(port=None, model_path=None, nthreads=None, device=None, upload_folder=None, config_path=None):
    if config_path is not None:
        conf_constants.update_by_config(config_path)
        
    if port is not None:
        conf_constants.port = int(port)
    if model_path is not None:
        conf_constants.model_path = model_path
    if nthreads is not None:
        conf_constants.nthreads = int(nthreads)
    if device is not None:
        conf_constants.device = device
    if upload_folder is not None:
        conf_constants.upload_folder = upload_folder   

    print(conf_constants.__dict__)
    if not os.path.exists(conf_constants.upload_folder):
        os.makedirs(conf_constants.upload_folder)

    model_loader.from_conf_constants(conf_constants)

    app.run(debug=False, port=conf_constants.port, host='0.0.0.0')

