FROM nginx
ENV TZ="America/Sao_Paulo"
COPY fabrica_carro /opt/
COPY src /opt/
COPY run.sh /root/
USER root
CMD /root/run.sh
