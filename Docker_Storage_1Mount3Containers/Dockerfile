FROM alpine

COPY write_hostname_script.sh /usr/local/bin/write_hostname_script.sh

RUN chmod +x /usr/local/bin/write_hostname_script.sh

ENTRYPOINT ["/usr/local/bin/write_hostname_script.sh"]
