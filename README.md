# Housing Price Prediction API

A machine learning project that predicts house prices from property features. The model is trained in Google Colab, saved as `model.joblib`, served through FastAPI, packaged with Docker, and checked automatically using GitHub Actions.

## Features

- Random Forest regression model
- 12 input features for house characteristics
- FastAPI prediction endpoint and interactive Swagger documentation
- Docker image for running the API in a container
- GitHub Actions CI workflow for tests and Docker image builds

## Dataset

The project uses a housing dataset downloaded from Kaggle. It contains 545 records and the target column `price`.

Input features:

- Numerical: `area`, `bedrooms`, `bathrooms`, `stories`, `parking`
- Categorical: `mainroad`, `guestroom`, `basement`, `hotwaterheating`, `airconditioning`, `prefarea`, `furnishingstatus`

## Model evaluation

The initial evaluation on the held-out test set produced these results:

| Metric | Result |
|---|---:|
| MAE | 1,026,432.09 |
| RMSE | 1,403,563.81 |
| R² | 0.6103 |

MAE and RMSE are in the same units as the dataset's `price` column. These results should be updated if the final saved model is retrained with a different split, preprocessing, or configuration.

## Project structure

```text
housing-price-api/
├── .github/
│   └── workflows/
│       └── ci.yml
├── Dockerfile
├── main.py
├── model.joblib
├── requirements.txt
├── test_main.py
└── README.md
```

The training notebook may be kept separately or added to the repository if required by the assignment.

## Run locally

### 1. Install dependencies

Use a Python environment with a scikit-learn version compatible with the saved model. This project pins scikit-learn to `1.9.1` in `requirements.txt`.

Windows PowerShell example:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

### 2. Start the API

Run from the project directory, where `main.py` and `model.joblib` are located:

```powershell
uvicorn main:app --reload
```

Open the interactive API docs at <http://127.0.0.1:8000/docs>.

## Prediction endpoint

### `POST /predict`

Example JSON request:

```json
{
  "area": 6000,
  "bedrooms": 3,
  "bathrooms": 2,
  "stories": 2,
  "mainroad": "yes",
  "guestroom": "no",
  "basement": "no",
  "hotwaterheating": "no",
  "airconditioning": "yes",
  "parking": 1,
  "prefarea": "yes",
  "furnishingstatus": "furnished"
}
```

Example response shape:

```json
{
  "predicted_price": 6500000.0
}
```

The number above is illustrative; the actual prediction is returned by the loaded model.

### `GET /`

Returns a message confirming that the API is running.

## Run with Docker

Make sure Docker Desktop is running, then run these commands from the project directory:

```powershell
docker build -t housing-price-api .
docker run --rm -p 8000:8000 housing-price-api
```

Open <http://localhost:8000/docs> to test the API running inside the container. In another terminal, `docker ps` can be used to check running containers.

## Tests

Install the test dependencies and run the test suite:

```powershell
python -m pip install pytest httpx
pytest -v
```

The tests check that the home endpoint responds successfully and that `/predict` returns a predicted price.

## Continuous integration

GitHub Actions is configured in `.github/workflows/ci.yml`. On pushes and pull requests targeting `main`, it:

1. Checks out the repository.
2. Sets up Python.
3. Installs the application and test dependencies.
4. Runs `pytest -v`.
5. Builds the Docker image.

To verify CI, open the repository's **Actions** tab and inspect the latest workflow run. A green check means the configured job passed.

## Notes

- Keep the training and serving scikit-learn versions compatible when loading `model.joblib`.
- Only load `joblib` files you trust; serialized model files can execute code during loading.
- This project is for educational demonstration and should not be used as the sole basis for real estate valuation decisions.
