"""Main module."""
from sqlalchemy import create_engine
import configparser
import keyring
import keyring
import getpass

def conectar_db():
    ''' Crea conexión a db
    
    Crea conexión base de datos
    
    Args:
        NULL
        
    Returns:
        Return an _engine.Engine instance
    
    '''
    fileconf='config.txt'
    
    ## Cargamos configuraciones
    config = configparser.ConfigParser()
    config.read(fileconf)
    usuario = config['credenciales']['usuario']
    host = config['postgres']['host']
    puerto = config['postgres']['puerto']
    db = config['db']['db']
    passwd = keyring.get_password("postgres_ie", usuario)
    
    ## Conectamos a db
    sql_url = 'postgresql://' + usuario + ':' + passwd + '@' + host + \
              ':' + puerto + '/' + db

    return create_engine(sql_url)


def set_credenciales():
    ''' Setea las credenciales para conectar_db
    
    Setea el nombre de usuario y la contraseña para conectar_db. Solicita
    al usuario que ingrese nombre de usuario y contraseña. Guarda usuario
    en archivo de configuración config.txt.
    
    Args:
        NULL
        
    Returns:
        NULL
    
    '''
    
    # seteamos la dirección del archivo de configuracion
    fileconf = 'config.txt'
    
    # Seteamos el usuario
    usuario = input('Ingrese usuario: ')
    
    # Guardamos el usuario en config file
    config = configparser.ConfigParser()
    config.read(fileconf)
    config['credenciales']['usuario'] = usuario
    with open(fileconf, 'w') as configfile:
        config.write(configfile)
    
    ## Seteamos el password en sistema
    keyring.set_password("postgres_ie",
                         usuario,
                         getpass.getpass('Ingrese contraseña: '))