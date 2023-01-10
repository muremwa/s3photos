# S3PHOTOS

It's a site for posting images.The site is served [here](https://s3photos.pythonanywhere.com).

## Features
1. It previews the image before you post it.
2. It stores the images on cloudinary*.
3. Has a [React](https://reactjs.org/)-based front end on the url `/open/`.

## Using s3photos locally.
1 Clone this repo.
```commandline
git clone https://github.com/muremwa/s3photos.git
```  

2 Install requirements (database is just sqlite3).
```commandline
pip install requirements.txt
```
 
3 Add a utility to add your own `SECRET_KEY` and  cloudinary keys or   
opt to just use local storage.  
> This repo includes a utility that is ignored called `s3util.py` that supplies cloudinary keys and the `SECRET_KEY`.  

`s3photos/utilities/s3util.py`
```python
import json
import pathlib
import os


home = str(pathlib.Path(__file__).parent)


def secret_key() -> str:
    """return the secret key"""
    with open(os.path.join(home, 'secret_key.txt'), 'r') as f:
        key = f.read().strip()
    return key


def cloudinary_keys(pre_key: dict) -> dict:
    """return a dict with cloud keys"""
    with open(os.path.join(home, 'keys.json'), 'r') as f:
        keys = json.load(f)
    pre_key.update(keys)

    return pre_key

```

4 Run migrations
```commandline
python manage.py makeigrations photos
python manage.py migrate
```

5 start server and use s3photos.
