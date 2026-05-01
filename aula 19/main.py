import os 


def criar_arquitetura():
    pastas = [
     
     'projeto/models',
     'projeto/views',
     'projeto/controller',
     'projeto/models/database',
     'projeto/teste'
    


    ]


    for pasta in pastas:
        os.makedirs(pasta, exist_ok=True)
               
        with open(os.path.join(pasta,"__init__.py"), 'w') as f: 
             pass
    print('arquitetura criada')


criar_arquitetura()    

