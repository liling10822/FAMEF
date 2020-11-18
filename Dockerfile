FROM python:3.7-buster
COPY setup.py /
CMD ["pip", "install", "-e", "."]
CMD ["somef", "describe", "-r", "https://github.com/dgarijo/Widoco/", "-o", "test.json", "-t", "0.8"]

