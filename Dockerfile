#
FROM python:3.13.3-slim

#
COPY . ./

#
RUN pip install -r requirements.txt

#
CMD ["python", "main.py"]