# -*- coding: utf-8 -*-
from sqlauthandle.sqlauthandle import Sqlauth
import tkinter as tk
import getpass

def set_credentials():
    """Funcion designed to recive the user data and encript the password while creating a config file.
        It integrates with other function of the package to facilitate the usage of it.
        To facilitate user experience this app generates a Graphical user interphase.
    """
    
    ## Recives data
    alias = input('Server alias[sqlauthandle]: ') or 'sqlauthandle'
    dialect = input('Dialect [postgresql]: ') or 'postgresql'
    host = input('Host [localhost]: ') or 'localhost'
    port = input('Port [5432]: ') or '5432'
    user = input('User: ')
    db_name = input('Database name: ')
    passwd = getpass.getpass('Password: ')

    auth = Sqlauth(alias)
    ## Actually generates the process
    auth.set_credentials(dialect=dialect,
                         host=host,
                         port=port,
                         user=user,
                         db_name=db_name,
                         passwd=passwd)
  
#%%
## Generates a GIU to set the data with visual window
def gui_set_cred(): 
    root=tk.Tk()
     
    # # setting the windows size
    # root.geometry("600x400")
      
    # declaring string variable
    # for storing name and password
    alias_var=tk.StringVar()
    dialect_var=tk.StringVar()
    host_var=tk.StringVar()
    port_var=tk.StringVar()
    db_name_var=tk.StringVar()
    user_var=tk.StringVar()
    passw_var=tk.StringVar()
    
    # defining a function that will
    # get the name and password and
    # print them on the screen
    def submit():
        
        alias=alias_var.get()
        dialect=dialect_var.get()
        host=host_var.get()
        port=port_var.get()
        db_name=db_name_var.get()
        user=user_var.get()
        passwd=passw_var.get()
        
        
        auth = Sqlauth(alias) 
        
        auth.set_credentials(dialect=dialect,
                             host=host,
                             port=port,
                             db_name=db_name,
                             user=user,
                             passwd=passwd)
        root.destroy()
    
    # creating a label for
    alias_label = tk.Label(root, text = 'alias', font=('calibre',10, 'bold'))
    alias_entry = tk.Entry(root,textvariable = alias_var, font=('calibre',10,'normal'))
    
    dialect_label = tk.Label(root, text = 'Dialect+DBAPI', font=('calibre',10, 'bold'))
    dialect_entry = tk.Entry(root,textvariable = dialect_var, font=('calibre',10,'normal'))
    
    host_label = tk.Label(root, text = 'Host', font=('calibre',10, 'bold'))
    host_entry = tk.Entry(root,textvariable = host_var, font=('calibre',10,'normal'))
    
    port_label = tk.Label(root, text = 'Port', font=('calibre',10, 'bold'))
    port_entry = tk.Entry(root,textvariable = port_var, font=('calibre',10,'normal'))
    
    db_name_label = tk.Label(root, text = 'Database Name', font=('calibre',10, 'bold'))
    db_name_entry = tk.Entry(root,textvariable = db_name_var, font=('calibre',10,'normal'))
    
    user_label = tk.Label(root, text = 'User', font=('calibre',10, 'bold'))
    user_entry = tk.Entry(root,textvariable = user_var, font=('calibre',10,'normal'))
    
    passw_label = tk.Label(root, text = 'Password', font = ('calibre',10,'bold'))
    passw_entry=tk.Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')
    
    # creating a button using the widget
    # Button that will call the submit function
    sub_btn=tk.Button(root,text = 'Submit', command = submit)
    
    q_btn = tk.Button(root, 
              text='Quit', 
              command=root.destroy)
      
    # placing the label and entry in
    # the required position using grid
    # method
    alias_label.grid(row=0,column=0)
    alias_entry.grid(row=0,column=1)
    
    dialect_label.grid(row=1,column=0)
    dialect_entry.grid(row=1,column=1)
    
    host_label.grid(row=2,column=0)
    host_entry.grid(row=2,column=1)
    
    port_label.grid(row=3,column=0)
    port_entry.grid(row=3,column=1)
    
    db_name_label.grid(row=4,column=0)
    db_name_entry.grid(row=4,column=1)
    
    user_label.grid(row=5,column=0)
    user_entry.grid(row=5,column=1)
    
    passw_label.grid(row=6,column=0)
    passw_entry.grid(row=6,column=1)
    
    sub_btn.grid(row=7,column=1)
    q_btn.grid(row=7, column=2)
    
    # performing an infinite loop
    # for the window to display
    root.mainloop()
    