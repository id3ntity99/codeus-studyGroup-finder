if [[ "$VIRTUAL_ENV" != "" ]]; then
	echo "Virtual env is activated"
	python3 $(pwd)/manage.py runserver
else
	printf "Virtual env is NOT activated\nUse 'source venv/bin/activate' command to activate venv.\n"
fi

