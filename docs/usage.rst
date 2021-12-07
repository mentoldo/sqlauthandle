=====
Usage
=====

To use sqlauthandle in a project::

    from sqlauthandle.sqlauthandle import Sqlauth
    import getpass

Choose an alias name and instantiate Sqlauth.
::

    auth = Sqlauth(alias='postgres_dev', reset_file=True)


and set the credentials::

    auth.set_credentials(dialect='postgresql',
                         host='localhost',
                         port='5432',
                         user='usuario',
                         db_name='customers',
                         passwd=getpass.getpass('Password: '))

It will ask you for password interactively. The password will be saved encryptedly in your
system keyring.
(Hint: Qt console does not support input password mode. If you don't want yo show your password on the screen, you
need to use another console.)
The dialect, host, port, user, db_name and passwd are saved in a config file in ``.sqlauthande/``.
You can add this folder to ``.gitignore`` file if you don't want to follow config files with Git

Then, you can authenticate at DB with::

    auth.conect_db()

It returns a ``sqlalchemy.engine.base.Engine`` from `sqlalchemy <https://docs.sqlalchemy.org/en/14/tutorial/engine.html>`_ package.
You can use it, for example, with pandas::

    pd.read_sql('clients', auth.conect_db())


CLI interface
-------------

You can set your credentials interactively directly from shell

.. code-block:: console


    $ sqlauthandle
    Sqlauthandle
    See sqlauthandle documentation at https://sqlauthandle.readthedocs.io/
    Alias [sqlauthandle]: postgres_dev
    Dialect [postgresql]:
    Host [localhost]:
    Port [5432]:
    User: usuario
    Database name: customers
    Password:

Then, on your Python project, you can instantiate Sqlauth with the alias::

    auth = Sqlauth(alias='postgres_dev', reset_file=True)
