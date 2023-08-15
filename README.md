# Nutrition
Web Application to search food and report calories and nutrients


## Setup
Obtain the API Key and App Id for Edanam. The key and id will be hidden by creating a .env file. The .env file should be placed inside (like the following example)

url = f"https://api.edamam.com/search?q={query}&app_id={app_id}&app_key={app_key}"

```sh
#this is the "env" file (in the root directory of the rope) The assigned name must be in CAPS. Eliminate spaces to avoid possible issues

#APP_ID="________"
#APP_KEY = "_____________"
```

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

```sh
pip install python-dotenv 
```

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

