# stock-predictor-mlops
Deployment for Stock Predictor API


```bash
conda create -n stock-predictor python=3.8
```

```bash	
cd src
uvicorn main:app --reload --workers 1 --host 0.0.0.0 --port 8000
```


```bash
pip list --format=freeze > requirements_.txt
```

```bash
curl --header "Content-Type: application/json" --request POST --data '{"ticker":"MSFT", "days":7}' http://0.0.0.0:8000/predict
```

