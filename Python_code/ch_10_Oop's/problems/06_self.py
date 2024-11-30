# Can you change the self-parameter inside a class to something else (say
# “harry”). Try changing self to “slf” or “harry” and see the effects.

class Selfish:
    def __init__(slf,name):
        slf.name=name
        print(slf.name)


p=Selfish("vijay")