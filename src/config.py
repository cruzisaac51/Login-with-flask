class Config:
    SECRET_KEY = 'StXEJi82HvTlaPonbd1D8Q'



class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'IR6C6s6h@tube3N('
    MYSQL_DB = 'flask1'

config = {
    'development': DevelopmentConfig
}