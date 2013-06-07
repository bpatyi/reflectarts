Reflect Arts
============

    mkvirtualenv --no-site-packages reflect
    pip install -r requirements.txt
    python manage.py syncdb
    python manage.py loaddata fixtures/*.json
