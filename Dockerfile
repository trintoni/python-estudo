FROM nginx
ENV TZ="America/Sao_Paulo"
COPY fabrica_carro /opt/
COPY src /opt/
USER root
CMD ls -ltr /opt
CMD ls -ltr /root