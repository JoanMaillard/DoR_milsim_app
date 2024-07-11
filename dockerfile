FROM python:3.12.4

COPY "${pwd}/requirements.txt" /
RUN pip install -r /requirements.txt
CMD ["fastapi", "run", "app/api/main.py", "--port", "8080"]