#!/bin/zsh

cd /Users/minho/code/django/childcare || exit

echo "childcare: auto_db_update.sh"

source .venv/bin/activate

echo "starting django server: childcare"
nohup python3 manage.py runserver 8999 >django.log 2>&1 &
DJANGO_PID=$!

/opt/homebrew/bin/redis-cli config set stop-writes-on-bgsave-error no
if /opt/homebrew/bin/redis-cli ping | grep -q "PONG"; then
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

sleep 30

echo "committing changes..."
git add db.sqlite3
git commit -m "$(date '+%Y-%m-%d:%H:%M:%S-auto-db-update')"
git push

echo "cleaning up logs..."
/opt/homebrew/bin/trash django.log celery.log

echo "terminating processes..."
# kill $DJANGO_PID
# kill $CELERY_PID
# kill $TAIL_PID

if [ -n "$DJANGO_PID" ] && ps -p $DJANGO_PID >/dev/null; then
    echo "Terminating Django process with PID: $DJANGO_PID"
    kill $DJANGO_PID
else
    echo "Django process with PID $DJANGO_PID is not running"
fi

if [ -n "$CELERY_PID" ] && ps -p $CELERY_PID >/dev/null; then
    echo "Terminating Celery process with PID: $CELERY_PID"
    kill $CELERY_PID
else
    echo "Celery process with PID $CELERY_PID is not running"
fi

if [ -n "$TAIL_PID" ] && ps -p $TAIL_PID >/dev/null; then
    echo "Terminating tail process with PID: $TAIL_PID"
    kill $TAIL_PID
else
    echo "Tail process with PID $TAIL_PID is not running"
fi

echo "done"
