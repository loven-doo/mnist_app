## APP Start
### From Docker image
NOTE, if you are planning to use GPU (NVIDIA) install nvidia-docker2 and check if graphics driver is installed on the target machine. If you are not planning - user simple 'docker' instead of 'nvidia-docker'   

Dowload and extract the Docker [image](https://drive.google.com/open?id=1tWu9vLMsKPbfpz_u2FmCLCI9CdAZ1Pjn) to the target machine   
Load the image on the target machine:
```
docker image load -i mnist_app.dimg
```
Optionally, you can run tests:
```
nvidia-docker run mnist_app python -m mnist_app.tests
```
Start the service:
```
nvidia-docker run -p <port>:<port> mnist_app python -m mnist_app -p <port>
```
For advanced options:
```
nvidia-docker run mnist_app python -m mnist_app -h
```
If you want to pass options via config file you can mount the directory with your config file to /configs directory inside the Docker container:
```
nvidia-docker run -p <port>:<port> -v </path/to/config/directory/>:/configs mnist_app python -m mnist_app -p <port> -c configs/default_config.yaml 
```

### From source
Clone the repo  
Then:
```
cd mnist_app
```

Install the reqirements:
```
pip install -r requirements.txt
```

Optionally, you can run tests:
```
python3 -m mnist_app.tests
```

Start the service:
```
python3 -m mnist_app
```

For advanced options:
```
python3 -m mnist_app -h
```

If you want to pass options via config file you can mount the directory with your config file to /configs directory inside the Docker container:
```
python3 -m mnist_app -c configs/default_config.yaml 
```

## APP usage
Infer handwritten digit:
```
curl -F 'file=@<local image path>' <app host ip>:5000/predict
```

## Create new Docker image
Clone the repo  
Then:
```
cd mnist_app
```

Build the image:
```
docker build -t mnist_app .
```

Save the image:
```
docker image save -o mnist_app.dimg mnist_app
```

To use got image on other machines you should copy obtained mnist_app.dimg file and load it on a target machine:
```
docker image load -i mnist_app.dimg
```

Now you can run it
