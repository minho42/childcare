#!/bin/zsh

cd /Users/minho/code/django/childcare || exit

echo "childcare: auto_db_update.sh"

source .venv/bin/activate

echo "starting django server: childcare"
nohup python3 manage.py runserver >django.log 2>&1 &
DJANGO_PID=$!

if redis-cli ping | grep -q "PONG"; then
    echo "redis is running: 🏓 PONG"

    echo "starting celery worker: childcare"
    nohup celery -A project worker --beat --scheduler django --loglevel=info >celery.log 2>&1 &
    CELERY_PID=$!

    tail -f celery.log &
    TAIL_PID=$!
else
    echo "redis not running, celery will not start"
    exit 1
fi

sleep 40

echo "committing changes..."
git add db.sqlite3
git commit -m "$(date '+%Y-%m-%d:%H:%M:%S-auto-db-update')"
git push

echo "cleaning up logs..."
trash django.log celery.log

echo "terminating processes..."
kill $DJANGO_PID
kill $CELERY_PID
kill $TAIL_PID

echo "done"
