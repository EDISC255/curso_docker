# siempre se va a  basar en otra
FROM python:latest 
# se ejecuta el comando dentro del contenedor
RUN pip install --upgrade pip
RUN pip install mysql-connector flask

#RUN apt install python-mysql-connector python- --noconfirm
RUN mkdir -p /home/app
WORKDIR /home/app
COPY . /home/app

#CMD [ "python" ,"-m", "flask", "run", "--host=0.0.0.0", "--debug=True"]
#crea un punto de entrada de ejecucion al momento de iniciar un contenedor (docker start)
CMD [ "python" ,"index.py"] 
EXPOSE 5000 