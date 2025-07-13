Para ejecutar este código, es necesario abrir el proyecto desde la terminal y ejecutarlo dentro de un entorno virtual de Python cuyo codigo para ejecutar es "fastapi dev"

aparte de eso se necesita de un modelo de dato de las siguientes caracteristicas:         
        id: str,
        name: str,
        description: str,
        price: float,
        quantity: int

Una vez teniendo el modelo de dato se tiene que ejecutar junto una base de datos locar que sea postgresql
y por ultimo instalar todo lo requerido del requiremenets.txt

<img width="273" height="87" alt="image" src="https://github.com/user-attachments/assets/8d789192-8d51-4839-b99e-7c5105d8e21c" />

en la siguiente imagen tiene que ir la conexion a la base de datos local aca un ejemplo:
<img width="784" height="87" alt="image" src="https://github.com/user-attachments/assets/2e72d34e-e4e4-4816-aa5b-70dd38fe152c" />


postgresql+psycopg2://{user}:{Password}@{host}:{port}/{db_name}

por ultimo el codigo contiene un archivo requirements.txt con todo lo que contiene el codigo

<img width="304" height="44" alt="image" src="https://github.com/user-attachments/assets/9f2b17f6-c861-429c-b22d-53c998f96d80" />

