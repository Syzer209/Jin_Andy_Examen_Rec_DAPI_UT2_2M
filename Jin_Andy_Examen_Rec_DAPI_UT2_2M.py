
def check_username(nombre, apellidos):
    '''
    esta funcion sirve para corregir los nombres y apellidos que estan mal escrito
    :param nombre: identifica el primer dato del archivo que es el nombre
    :param apellidos: identifica el segundo dato del archivo que es el apellido
    :return: te devuelve el nombre y el apellido con la primera letra en mayuscula
    '''
    return nombre.title(), apellidos.title()

def check_nif(numeros):
    '''
    esta funcion sirve para corregir el numero de nif
    :param numeros: identifica el numero que tiene en el nif del archivo
    :return: te devuelve la letra dependiendo del numero que este asociado con una operacion la division entre 23 pero usamos el resto
    '''
    nif_dict = {"0":"T", "1":"R", "2":"W", "3":"A", "4":"G", "5":"M",
            "6":"Y", "7":"F", "8":"P", "9":"D", "10":"X", "11":"B",
            "12":"N", "13":"J", "14":"Z", "15":"S", "16":"Q", "17":"V",
            "18":"H", "19":"L", "20":"C", "21":"K", "22":"E"}
    indice = int(numeros)%23
    return nif_dict[str(indice)]

def calculate_bill(multas):
    '''
    esta funcion sirve para juntas todas las multas en un total de multas
    :param multas: identifica las diferentes multas
    :return: te devueve la suma de las distintas multas
    '''
    return str(int(multas[0]) + int(multas[1]) + int(multas[2]))

#def check_fhone(telefono)
countries_dict = {"30":"Grecia", "33":"Fracia", "34":"España", "351":"Portugal", "380":"Ucrania",
                  "39":"Italia", "41":"Suiza", "44":"Reino Unido", "49":"Alemania", "7":"Rusia"}

def check_DGT(ruta):
    '''
    esta funcion abre el archivo y llama a las otras funciones
    :param ruta: identifica el archivo
    :return: nos devuelve los datos que hay en el archivo
    '''
    file =  open(ruta, "r", encoding='utf-8')
    lineas = file.readlines()
    lineasCorregidas = []
    for linea in lineas:
        datos = linea.split(",")
        if datos[0] == "Nombre":
          datos.insert(4, "País")
          datos[6] = "Total Multas"
          del datos[-1]
          del datos[-1]
        else:
          # Cambiar username
          datos[0], datos[1] = check_username(datos[0], datos[1])

          # Cambiar nif
          nif = datos[2]
          numeros = nif[0:8]
          letra = check_nif(numeros)
          datos[2] = f"{numeros}{letra}"

          # Sumar las multas
          datos[5] = calculate_bill([datos[5], datos[6], datos[7]])
          del datos[-1]
          del datos[-1]

        datos = tuple(datos)
        datos = ",".join(datos)
        datos += "\n"
        lineasCorregidas.append(datos)
        print(datos)
        file.close()
        file =  open(ruta, "w", encoding='utf-8')
        file.writelines(tuple(lineasCorregidas))

check_DGT("Andy Jin Liu - DGT.csv")



