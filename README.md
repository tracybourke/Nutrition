# Nutrition
Web Application to search food and report calories and nutrients


## Setup
Obtain the API Key and App Id for Edanam. The key and id will be hidden

url = f"https://api.edamam.com/search?q={query}&app_id={app_id}&app_key={app_key}"


Create a virtual environment

```sh
conda create -n edanam-env python=3.10
```
``sh
conda activate edanam-env
```

Install third-party package:

``sh
pip install -r requirements.txt
```

## Usage 

Run the report
```sh
python app/edanam.py
python -m app.edanam
```

```
Run the web app:

```sh
# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or try a ".env" file approach
export FLASK_APP=web_app
flask run
```

## Testing

Run tests:

```sh
pytest
```


## Deployment

## [Deployment Guide](/DEPLOYING.md)
