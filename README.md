#S3PHOTOS

It's a site for posting images.

##Features
1. It previews the image before you post it.
2. It stores the images on cloudinary.

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
> This repos includes a utility that is ignores called `s3util.py` that supplies cloudinary keys and the `SECRET_KEY`.

4 Run migrations
```commandline
python manage.py makeigrations photos
python manage.py migrate
```

5 start server and use s3photos.