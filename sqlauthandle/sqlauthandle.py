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
        :alias (str): String identifier of the db conection.
        :reset_file (bool): Remove the config file before create a new one.
        
    Attributes:
        :alias ('str'): String identifier of the db conection.
        :fileconf (Path): The path to config file.
        :config (ConfigParser): The ConfigParser with the config options.
    '''
    def __init__(self,
                 alias='sqlauthandle',
                 reset_file=False):
        
        # seteamos la dirección del archivo de configuracion
        self.alias = alias
        self.fileconf = (Path('.sqlauthandle') / alias).with_suffix('.txt')
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
            Return an sqlalchemy.engine.base.Engine instance
        
        '''
        # fileconf='config.txt'
        
        ## Read configuracion
        dialect = self.config['credentials']['dialect']
        host = self.config['credentials']['host']
        port = self.config['credentials']['port']
        db_name = self.config['credentials']['db_name']
        user = self.config['credentials']['user']
        passwd = keyring.get_password(self.config['credentials']['alias'], user)
        
        ## Conectamos a db
        sql_url = dialect + '://' + user + ':' + passwd + '@' + host + \
                  ':' + port + '/' + db_name
    
        return create_engine(sql_url)
    
    
    def set_credentials(self, dialect, host, port, db_name, user, passwd):
        ''' Set the credentials to connect to SQL DB.

        Save dialect, host, port, db_name, user and app in config file. Save password 
        in system keyring.
                
        Args:
            :dialect (str): The dialect to config sqlalchemy engine. Some options are `postgresql`, `mysql`, `oracle`, `mssql`.
                See Sql Alchemy docs: https://docs.sqlalchemy.org/en/14/core/engines.html#sqlalchemy.create_engine  
            :host (str): Host url of DB server.  
            :port (str): Port number.
            :db_name: Name of database to conect.
            :user: User
            :passwd: Password
     
        Returns:
            NULL

        '''   
        
        # Seting credentials    
        self.config['credentials']['alias'] = self.alias
        self.config['credentials']['dialect'] = dialect
        self.config['credentials']['host'] = host
        self.config['credentials']['port'] = port
        self.config['credentials']['user'] = user
        self.config['credentials']['db_name'] = db_name
        
        with open(self.fileconf, 'w') as configfile:
            self.config.write(configfile)
        
        ## Seteamos el password en sistema
        keyring.set_password(self.alias,
                             user,
                             passwd)
    
        
    def __init_configfile(self):
        ''' Initialize the config file 
        
        Create a config file in .sqlauthandle folder with the alias name.
        
        Args:
            NULL
            
        Returns:
            NULL
        '''
        
        def_conf = '''
        [credentials]
            alias=
            dialect=
            host=
            port=
            user=
            db_name=
        '''
        if not self.fileconf.parent.is_dir():
            self.fileconf.parent.mkdir()
            
        self.config.read_string(def_conf)
        with open(self.fileconf, 'w') as configfile:
            self.config.write(configfile)