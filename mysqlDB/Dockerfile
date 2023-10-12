FROM mysql

ENV MYSQL_ROOT_PASSWORD root

ENV MYSQL_USER temp_app

ENV MYSQL_PASSWORD temp_app

ENV MYSQL_DATABASE temp_app

COPY ./insert.sql /tmp

CMD [ "mysqld", "--init-file=/tmp/insert.sql" ]