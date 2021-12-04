"""Main module."""
from sqlalchemy import create_engine
import configparser
import keyring
# import getpass
from pathlib import Path

class Sqlauth:
    ''' Authorization class to manage authentication in SQL Databases
    
    Let you handle and save SQL DB authentication configuration information. 
    
    Args:
        fileconf (str): String path to config file
        reset_file (bool): Remove `fileconf` before create a new one.
        
    Attributes:
         self.fileconf (Path): ...
         config (ConfigParser): ...
    '''
    def __init__(self,
                 fileconf='./auth_config.txt',
                 reset_file=False):
        
        # seteamos la dirección del archivo de configuracion
        self.fileconf = Path(fileconf)
        self.config = configparser.ConfigParser()
        
        ## Intialize the config file if it does't exist
        if not self.fileconf.exists() or reset_file:
            self.__init_configfile()
        
        self.config.read(self.fileconf)


    def conect_db(self):
        ''' Create a SQL DB conection
        
        Create a SQL DB conection with object setted parameters
        
        Args:
            NULL
            
        Returns:
            Return an _engine.Engine instance
        
        '''
        # fileconf='config.txt'
        
        ## Read configuracion
        sql_server = self.config['credentials']['sql_server']
        host = self.config['credentials']['host']
        port = self.config['credentials']['port']
        db_name = self.config['credentials']['db_name']
        user = self.config['credentials']['user']
        passwd = keyring.get_password(self.config['credentials']['app'], user)
        
        ## Conectamos a db
        sql_url = sql_server + '://' + user + ':' + passwd + '@' + host + \
                  ':' + port + '/' + db_name
    
        return create_engine(sql_url)
    
    
    def set_credentials(self, sql_server, host, port, db_name, user, passwd, app='sqlauth'):
        ''' Set the credentials to connect to SQL DB
        
        Setea el nombre de usuario y la contraseña para conectar_db. Solicita
        al usuario que ingrese nombre de usuario y contraseña. Guarda usuario
        en archivo de configuración config.txt.
        
        Args:
            NULL
            
        Returns:
            NULL
        
        '''   
        
        # Seting credentials    
        self.config['credentials']['app'] = app
        self.config['credentials']['sql_server'] = sql_server
        self.config['credentials']['host'] = host
        self.config['credentials']['port'] = port
        self.config['credentials']['user'] = user
        self.config['credentials']['db_name'] = db_name
        
        with open(self.fileconf, 'w') as configfile:
            self.config.write(configfile)
        
        ## Seteamos el password en sistema
        keyring.set_password(app,
                             user,
                             passwd)
    
        
    def __init_configfile(self):
        ''' Initialize the config file 
        
        Create a file named auth_config.txt in the working directory
        
        Args:
            NULL
            
        Returns:
            NULL
        '''
        
        def_conf = '''
        [credentials]
            app=
            sql_server=
            host=
            port=
            user=
            db_name=
        '''
        self.config.read_string(def_conf)
        with open(self.fileconf, 'w') as configfile:
            self.config.write(configfile)