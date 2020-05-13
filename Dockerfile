FROM python:latest
RUN pip install pandas
RUN pip install flask
RUN mkdir -p /etc/attribution/files
COPY license.py /etc/attribution/license.py
COPY app.py /etc/attribution/app.py
COPY templates/index.html /etc/attribution/templates/index.html
COPY templates/wait.html /etc/attribution/templates/wait.html
WORKDIR /etc/attribution
EXPOSE 5000
CMD ["python","app.py"]
