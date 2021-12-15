"""Main module."""
from sqlalchemy import create_engine
import configparser
import keyring
# import getpass
from pathlib import Path

class Sqlauth:
    ''' This class generates an authentication file for Databases. In this file is saved:
        - Database provider: Postgres, for example.
        - Username: user identification.
        - Warning: It does not save any password in the file. However it access the computer to save it in the system.
    
    
    
    Args:
        :alias (str): String identifier of the db conection.
        :reset_file (bool): If true, the app will remove any file previusly created to update it with new information.
        
    Attributes:
        :alias ('str'):Name given to the conection. With this alias, the user will be able to interact with the aplication to validate her access to a chosen
        :fileconf (Path): The path to config file.
        :config (ConfigParser): The ConfigParser with the config options.
    '''
    def __init__(self, alias='sqlauthandle', reset_file=False):
        
        ## Recives config data to generarate the authenticator
        self.alias = alias
        self.fileconf = (Path('.sqlauthandle') / alias).with_suffix('.txt')
        self.config = configparser.ConfigParser()
        
        ## Intialize the config file if it does't exist
        if not self.fileconf.exists() or reset_file:
            self.__init_configfile()
        
        self.config.read(self.fileconf)

    ## After the config file with information has been created
    ## this funcion can be alled to connect the Database
    def connect_db(self):
        ''' Takes the config file already created and saved in the package directory
            to create a connection to the cosen database. No further information is
            needed to run this funcion as it takes a config file named after the alias
            to use the information needed.
        
        
        
        Args:
            NULL
            
        Returns:
            Return an sqlalchemy.engine.base.Engine instance capable of opening the Database.
        
        '''
        
        
        ## Reads configuracion file 
        dialect = self.config['credentials']['dialect']
        host = self.config['credentials']['host']
        port = self.config['credentials']['port']
        db_name = self.config['credentials']['db_name']
        user = self.config['credentials']['user']
        passwd = keyring.get_password(self.config['credentials']['alias'], user)
        
        ## Generates a url to connect to the Database
        sql_url = dialect + '://' + user + ':' + passwd + '@' + host + \
                  ':' + port + '/' + db_name

        return create_engine(sql_url)
    
    
    def set_credentials(self, dialect, host, port, db_name, user, passwd):
        ''' Sets the credentials to connect to a SQL DB.

        The user provides with the information to the aplication.
        This is the main funcion to create credential for the user.
        Here you provide the specific information needed in the database.
                
        Args:
            :dialect (str): The dialect to config sqlalchemy engine. Some options are `postgresql`, `mysql`, `oracle`, `mssql`.
                See Sql Alchemy docs: https://docs.sqlalchemy.org/en/14/core/engines.html#sqlalchemy.create_engine  
            :host (str): Host url of DB server.  
            :port (str): Port number. An example is: 5432 for postgres or localhost in case the DB is run locally.
            :db_name: Name of database to conect. This has to be the name given to the DB, not the alias chosen in the App.
            :passwd: Password. If run on bash, it wont be shown, However, if the user is using IPython, it wont be hidden while writing.
            :app: Name of application. It is used to save the password in the system keyring.
     
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
        
        ## Seves password on computer system.
        keyring.set_password(self.alias,
                             user,
                             passwd)
    
        
    def __init_configfile(self):
        ''' Initialize the config file 
        
        The App creates a config file to be filled with information provided by the user.
        
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