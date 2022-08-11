from .entities.User import User
import re

class ModelUser():


    @classmethod
    def login(self, db, user):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, username, password, fullname FROM user
                    WHERE username = '{}'""".format(user.username)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                user = User(row[0], row[1], User.check_password(row[2], user.password),row[3])
                return user
            else:
                return None

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def sign_up(self, db, user):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, username, password, fullname FROM user
                    WHERE username = '{}'""".format(user.username)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row:
                msg = 'Account already exists !'
            elif not re.match(r'[A-Za-z0-9]+', user.fullname):
                msg = 'fullnamee must contain only characters !'
            elif not re.match(r'[A-Za-z0-9]+', user.username):
                msg = 'Username must contain only characters and numbers !'
            # elif not user.username or not user.password or not user.fullname:
            #     msg = 'Please fill out the form !'
            else:
                cursor.execute('INSERT INTO user VALUES("", % s, % s, % s)',(user.username, user.password, user.fullname, ))
                db.connection.commit()
                msg = 'You have successfully registered !'

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_by_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, username, fullname FROM user
                    WHERE id = '{}'""".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                logged_user = User(row[0], row[1], None, row[2])
                return logged_user
            else:
                return None

        except Exception as ex:
            raise Exception(ex)


