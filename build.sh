#/bin/bsh

#build the project
echo "building the project..."
python3 -m pip install -r requirements.txt

echo "make migrations..."
python3 manage.py makemigrations 
python3 manage.py migrate

echo "collect static"
python3 manage.py collectstatic

