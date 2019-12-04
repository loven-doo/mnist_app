### APP start
Clone the repo  
Install the reqirements:  
```
pip install -r mnist_app/requirements.txt
```
Start the service:  
```
python -m mnist_app
```
Infer handwritten digit:  
```
curl -F 'file=@<local image path>' <app host ip>:5000/predict
```

