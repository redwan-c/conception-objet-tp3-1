def list_from_yaml(data):
    ans =[]
    for d in data:
        if d["type"]=="Box":
            ans.append(Box.from_yaml(d))
        elif d["type"]=="Things":
            ans.append(Things.from_yaml(d))
    return ans

class Box:

    @staticmethod
    def from_yaml(data):
        return Box(is_open=data["is_open"], capacity=data["capacity"]) 

    def __init__(self):
        self._contents = []
        self._status=True
        self._capacity=None
        
    def add(self,truc):
        self._contents.append(truc)

    def _contains_(self, truc):
        return truc in self._contents

    def remove(self, truc):
        self._contents.remove(truc)

    def is_open(self):
        return self._status

    def open(self):
        self._status=True

    def close(self):
        self._status=False
  
    def action_look(self):
        if self.is_open():
            return "la boite contient:" + ", ".join(self._contents)
        else:
            return "la boite est fermée"
    
    def set_capacity(self, c):
        self._capacity=c

    def capacity(self):
        return self._capacity

    def has_room_for(self,t):
        return self._capacity is None or t.volume() <= self._capacity;

class Thing:

    @staticmethod
    def from_yaml(data):
        return Things(v=data["volume"], name=data["name"]) 

    def __init__(self,v):
        self.volume=v
    
    def __repr__(self):
        return self._name

    def __set_name__(self, name):
        self._name=name

    def has_name__(self, name):
        return self._name==name

    def volume(self):
        return self._volume
