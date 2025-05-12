FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --no-deps --disable-pip-version-check --no-python-version-warning --progress-bar off -r requirements.txt

COPY . .

EXPOSE 5000

#CMD ["python", "md5_api.py"]

# 使用Gunicorn作为生产服务器
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "md5_api:app"]
