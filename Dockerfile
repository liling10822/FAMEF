FROM python:3.7-buster
RUN git clone https://github.com/liling10822/FAMEF.git
COPY setup.py /
CMD ["pip", "install", "-e", "."]
WORKDIR FAMEF
