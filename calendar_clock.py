import calendar
import time
from datetime import datetime

def display_calendar():
    yy = ano
    m = mes

    print(calendar.month(yy, m))
    print(f"Dia: {dia}" )


def clock():
        current_time = time.strftime("%H:%M:%S", time.localtime())
        print("Hora atual:", current_time)     


data_atual = datetime.now()

dia = data_atual.day
mes = data_atual.month
ano = data_atual.year

display_calendar()
clock()
