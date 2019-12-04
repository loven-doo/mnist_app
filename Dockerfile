FROM nvidia/cuda:10.0-devel

ADD mnist_app /mnist_app/
ADD requirements.txt /

run apt-get update && apt-get install -y \
    python3.6 \
    python3-pip \
    libsm6 \
    libxext6 \
    libxrender-dev

run ln -s /usr/bin/python3.6 /usr/bin/python        

RUN python -m pip install -r requirements.txt


