class Event:

    def __init__(self, name, date, attendees):
        """Inicializa una instancia de la clase Event.

        Parámetros:
        name (str): nombre del evento.
        date (str): fecha del evento.
        attendees (int): cantidad de asistentes al evento.
        """

        self.name = name
        self.date = date
        self.attendees = attendees

def nombre_eventos(*args):
  """Devuelve una lista con los nombres de los eventos

    Parámetros:
    *args=nro indeterminado de eventos

    Devuelve:
    Lista_nombre= lista con los nombres de los eventos
    """
  Lista_nombres=[]
  for event in args:
            if event.name not in Lista_nombres:
              Lista_nombres.append(event.name)
            return Lista_nombres

event1 = Event('PyCon', '2021-10-15', 100)
event2 = Event('Smaltalks', '2021-10-20', 50)
event3 = Event('PyCon', '2021-10-25', 200)
event4 = Event('Smaltalks', '2021-10-30', 150)
event5 = Event('JavaOne', '2021-11-05', 300)
print(nombre_eventos(event1,event2,event3,event4,event5))
"Revisar"
