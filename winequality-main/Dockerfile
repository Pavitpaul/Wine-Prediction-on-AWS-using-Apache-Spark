ARG IMAGE_VARIANT=slim-buster
ARG OPENJDK_VERSION=8
ARG PYTHON_VERSION=3.7

FROM python:${PYTHON_VERSION}-${IMAGE_VARIANT} AS py3
FROM openjdk:${OPENJDK_VERSION}-${IMAGE_VARIANT}

COPY --from=py3 / /

WORKDIR /app

# ARG PYSPARK_VERSION=3.2.0
#RUN pip --no-cache-dir install pyspark==${PYSPARK_VERSION}
RUN pip --no-cache-dir install pyspark
RUN pip --no-cache-dir install pandas
RUN pip --no-cache-dir install matplotlib
RUN pip --no-cache-dir install -U scikit-learn scipy matplotlib
RUN pip --no-cache-dir install findspark

COPY . .

# CMD while true; do sleep 1000; done
ENTRYPOINT ["python","./wine_quality_docker.py"]
