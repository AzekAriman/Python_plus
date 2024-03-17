FROM ubuntu:20.04

WORKDIR /work

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC

RUN apt-get update

RUN apt-get install -y python3 python3-pip texlive-latex-extra && \
    rm -rf /var/lib/apt/lists/*

COPY . /work

RUN python3 -m pip install -r requirements.txt

CMD python3 main.py && pdflatex full_latex_document.tex