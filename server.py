# -*- coding: utf-8 -*-
__author__ = 'Nikitin'




if __name__ == "__main__":

    from socket import * # получить конструктор сокета и константы
    myHost = '' # '' = все доступные интерфейсы хоста
    myPort = 50007 # использовать незарезервированный номер порта
    sockobj = socket(AF_INET, SOCK_STREAM) # создать объект сокета TCP
    sockobj.bind((myHost, myPort)) # связать с номером порта сервера
    sockobj.listen(5) # не более 5 ожидающих запросов
    while True: # пока процесс работает
        connection, address = sockobj.accept() # ждать запроса
        # очередного клиента
        print('Server connected by', address) # соединение является
        # новым сокетом
        while True:
            data = connection.recv(1024) # читать следующую строку из сокета
            if not data: break # отправить ответ клиенту
            connection.send(b'Echo=>' + data) # и так, пока от клиента поступают
        connection.close() # данные, после чего закрыть сокет