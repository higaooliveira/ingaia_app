FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /appication
WORKDIR /appication
RUN apt-get update && apt-get install -y \
		gcc \
		gettext \

	--no-install-recommends && rm -rf /var/lib/apt/lists/*

COPY ["./requirements.txt", "/application/"]
RUN pip install --upgrade pip && pip install -r /application/requirements.txt
ADD . /appication/