#/bin/bsh

#build the project

echo "make migrations..."
python3.9 manage.py makemigrations 
python3.9 manage.py migrate

echo "collect static"
python3.9 manage.py collectstatic

