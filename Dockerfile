FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

copy . .

CMD ["python", "-m", "gunicorn", "-w", "4", "'blog:create_app()'", "-d"]
