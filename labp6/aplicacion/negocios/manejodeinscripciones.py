from aplicacion.modelos.usuario import Usuario
from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios

#==========================
#  Clase storemanager
#  NO TIENE VARIABLES !!!
#==========================
class ManejoDeInscripciones:
    #================================================================
    #  Decorador staticmethod
    #  El objeto solo tiene la funcion inscribirUsuario
    #  ENVUELVE LA FUNCION SIN LLAMAR VARIABLES LOCALES
    #  el objeto ManejoDeInscripciones es la interface intercambiale
    #================================================================
    @staticmethod
    def inscribirUsuario(usuario: Usuario, repositorioDeUsuarios: RepositorioDeUsuarios) -> None:
        print("------> Guardando usuario ... \n")
        repositorioDeUsuarios.abrir()
        repositorioDeUsuarios.guardar(usuario)
        repositorioDeUsuarios.cerrar()
