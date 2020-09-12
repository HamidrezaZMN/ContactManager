import os, click, sys
import sqlite3
from sqlite3 import Error
# click options prompt texts
from program.side_scripts.text_items.click_options import others_
# cd to path of all databases
os.chdir(os.path.dirname(os.path.realpath(__file__)))
os.chdir('DataBases')

class DATABASE():
    ################## initializing
    def __init__(self, db_name):

        # name of the db
        self.db_name = f'{db_name}.db'
        # path of the db
        self.db_path = 'side_scripts/database/'+self.db_name
        # all the users
        # it  is used to print in a order
        self.all_users = []
        # titles of the table
        self.titles =', '.join([
            'fullName', 
            'mainNumber', 
            'secondNumber', 
            'houseAddress', 
            'workAddress',
            'addedDate', 
            'description'
        ])




    ################## connection
    # connects to database
    def connect_db(self):
        try:
            self.con = sqlite3.connect(self.db_name)
            self.cur = self.con.cursor()
        except Error:
            click.echo(
                others_['HandleDB']['connect_db'][0].format(Error)
            )
            self.exit_()

    # disconnects from database
    def close_db(self):
        self.con.close()
    



    ################## side methods
    # executes sql command
    def exec_(self, command):
        self.cur.execute(command)

    # fetches all tables (categories)
    # :: SELECT name FROM sqlite_master ... :: #
    def fetch_all_tables(self):
        self.exec_(
            'SELECT name FROM sqlite_master WHERE TYPE="table"'
        )
        self.tables = [table[0] for table in self.cur.fetchall()]

    # prints fullName and mainNumber of all users of the given category
    # :: SELECT * FROM TABLE :: #
    def extract_all_from_category(self, category):
        self.exec_(
            f'SELECT * FROM {category}'
        )
        rows = self.cur.fetchall()
        self.all_users += list(rows)

    # updates the user, given the attribute (type_)
    # :: UPDATE TABLE SET ..... WHERE ... :: #
    def update_user_by_type(self, full_name, attribute, value, table):
        self.exec_(
            f'UPDATE {table} SET {attribute}="{value}" WHERE fullName="{full_name}"'
        )
        self.con.commit()

    # sorts all_usere
    # methods: order by fullName, addedDate
    # reverse > boolean
    def sort_users(self, order_method, reverse):
        def order_by_fullName(list_):
            return list_[0]
        
        def order_by_date(list_):
            date_time =  list_[-2].split(' ')
            _date_ = date_time[0].split('/')
            _time_ = date_time[1].split(':')
            _date_[2] = '20' + _date_[2]
            _date_ = list(map(int, _date_))
            _time_ = list(map(int, _time_))
            _date_[0], _date_[1] = _date_[1], _date_[0]

            month_days = {
                1 : 31,
                2 : 28,
                3 : 31,
                4 : 30,
                5 : 31,
                6 : 30,
                7 : 31,
                8 : 31,
                9 : 30,
                10 : 31,
                11 : 30,
                12 : 31
            }

            d_ = [1, month_days[_date_[1]], 365]
            t_ = [3600, 60, 1]
            for i in range(3):
                _date_[i] *= d_[i]
                _time_[i] *= t_[i]
            _date_ = sum(_date_); _time_ = sum(_time_)
            _time_ = _time_ / (3600*24)
            return _date_ + _time_
        
        if order_method == 'fullName':
            self.all_users.sort(key=order_by_fullName, reverse=reverse)
        elif order_method == 'addedDate':
            self.all_users.sort(key=order_by_date, reverse=reverse)

    # finds every user with attribute=value in self.all_users then adds them to list_
    def find_user_by_attribute(self, value, attribute, list_):
        items = [
            'fullName',
            'mainNumber',
            'secondNumber',
            'houseAddress',
            'workAddress',
            'addedDate',
            'description'
        ]
        ind = items.index(attribute)
        for user in self.all_users:
            if user[ind] != None:
                if value in user[ind]:
                    list_.append(user)
    
    # prints all_users appropriately
    def echo_all_users(self, verbose_mode):
        texts = others_['HandleDB']['echo_all_users']
        titles_ = 'fullName, mainNumber'
        if verbose_mode:
            titles_ += ', secondNumber, houseAddress, workAddress, addedDate, description'
        if len(self.all_users) != 0:
            click.echo(texts[0].format(titles_))
            click.echo(texts[1])
            for row in self.all_users:
                t = ', '.join([str(i) for i in row[:len(titles_.split(', '))]])
                click.echo(texts[2].format(t))

    # exit the program but also close the database
    def exit_(self):
        self.close_db()
        sys.exit()




    ################## add
    # adds new user
    # :: INSERT INTO TABLE ... :: #
    def add_user(self, infos, category):
        self.fetch_all_tables()
        # make the category if not exists
        if category not in self.tables:
            click.echo(others_['HandleDB']['add_user'][0].format(category))
            inp = click.confirm(others_['HandleDB']['add_user'][1])
            if inp:
                self.add_category(category)
            else:
                self.exit_()
        # make the titles and values (fullName=...)
        titles = ', '.join(infos.keys())
        values = ''
        for v in infos.values():
            if v == None:
                values += 'None, '
            else:
                values += f'"{v}", '
        values = values[:-2]
        
        # side method
        def user_exists(attr):
            print(f'user with that {attr} found')
            self.exit_()

        # if user exists, tell that and end the program
        for table in self.tables:
            self.exec_(
                f'SELECT * FROM {table}'
            )
            users = self.cur.fetchall()
            for user in users:
                for key, value in infos.items():
                    if key=='fullName':
                        if user[0]==value!=None:
                            user_exists('name')
                    elif key=='mainNumber':
                        if user[1]==value!=None:
                            user_exists('number')
                    elif key=='secondNumber':
                        if user[2]==value!=None:
                            user_exists('number(second one)')
        # insert the user
        self.exec_(
            f'INSERT INTO {category}({titles}) VALUES({values})'
        )
        self.con.commit()

    # adds new category
    # :: CREATE TABLE :: #
    def add_category(self, category):
        self.fetch_all_tables()
        if category in self.tables:
            click.echo(others_['HandleDB']['add_category'][0])
            self.exit_()
        else:
            self.exec_(
                '''CREATE TABLE {}(
                    fullName TEXT, 
                    mainNumber TEXT, 
                    secondNumber TEXT, 
                    houseAddress TEXT, 
                    workAddress TEXT,
                    addedDate TEXT, 
                    description TEXT
                )
                '''.format(category)
            )




    ################## remove
    # removes a user
    # :: DELETE FROM TABLE WHERE ... :: #
    def remove_user(self, name):
        texts = others_['HandleDB']['remove_user']

        choice_text = ''

        self.fetch_all_tables()
        for table in self.tables:
            self.extract_all_from_category(table)
        all_found = []
        self.find_user_by_attribute(name, 'fullName', all_found)
            
        if len(all_found) != 0:
            if len(all_found) > 1:
                for i in range(len(all_found)):
                    click.echo(texts[0].format(
                        i+1, all_found[i][0]
                    ))
                inp = click.prompt(texts[1], type=int)
                self.chosen_user = all_found[inp-1]
            else:
                self.chosen_user = all_found[0]
            if click.confirm(texts[2].format(self.chosen_user[0])):
                self.exec_(
                    f'DELETE FROM {table} WHERE fullName="{self.chosen_user[0]}"'
                )
                self.con.commit()
            else:
                click.echo(texts[3])
        else:
            click.echo(texts[4])

    # removes a category
    # :: DROP TABLE :: #
    def remove_category(self, category):
        texts = others_['HandleDB']['remove_category']
        self.fetch_all_tables()
        if category in self.tables:
            if click.confirm(texts[0].format(category)):
                self.exec_(
                    f'DROP TABLE {category}'
                )
                self.con.commit()
            else:
                click.echo(texts[1])
        else:
            click.echo(texts[2].format(category))




    ################## show
    # shows all users of all categories
    # :: SELECT fullName, mainNumber FROM TABLE :: #
    def show_all_users(self, verbose_mode, order_method, reverse):
        self.fetch_all_tables()
        for table in self.tables:
            self.extract_all_from_category(table)
        self.sort_users(order_method, reverse)
        self.echo_all_users(verbose_mode)

    # shows all users of the given category
    # :: SELECT fullName, mainNumber FROM TABLE :: #
    def show_users_of_category(self, category, verbose_mode, order_method, reverse):
        self.fetch_all_tables()
        if category in self.tables:
            self.extract_all_from_category(category)
            self.sort_users(order_method, reverse)
            self.echo_all_users(verbose_mode)
        else:
            click.echo(others_['HandleDB']['show_users_of_category'][0])

    # shows a specific user
    # :: SELECT * FROM TABLE WHERE ... :: #
    def show_user(self, value, attribute):
        texts = others_['HandleDB']['show_user']
        self.fetch_all_tables()
        for table in self.tables:
            self.extract_all_from_category(table)
        all_found = []
        if attribute == 'name':
            self.find_user_by_attribute(value, 'fullName', all_found)
        elif attribute == 'number':
            self.find_user_by_attribute(value, 'mainNumber', all_found)
            self.find_user_by_attribute(value, 'secondNumber', all_found)

        if len(all_found) != 0:
            if len(all_found) > 1:
                for i in range(len(all_found)):
                    click.echo(texts[0].format(
                        i+1, all_found[i][0]
                    ))
                inp = click.prompt(texts[1], type=int)
                try:
                    self.chosen_user = all_found[inp-1]
                except:
                    click.echo(texts[2])
                    self.exit_()
            else:
                self.chosen_user = all_found[0]
            self.user_table = table
            text = ''.join([
                '\nfull name          : {}',
                '\nmain number        : {}',
                '\nsecond number      : {}',
                '\nhouse address      : {}',
                '\nwork address       : {}',
                '\nadded Date         : {}',
                '\ndescription        : {}',
                '\n'
            ]).format(*self.chosen_user)
            click.echo(texts[3].format(text))
            return True
        else:
            return False

    # shows name of the all categories
    # :: SELECT name FROM sqlite_master WHERE TYPE="table" :: #
    def show_all_categories(self):
        self.fetch_all_tables()
        self.tables.sort()
        texts = others_['HandleDB']['show_all_categories']
        [click.echo(texts[0].format(table)) for table in self.tables]


    

    ################## others
    # updates a user
    def update_user(self, name):
        texts = others_['HandleDB']['update_user']
        flag = self.show_user(name, 'name')
        if not flag:
            click.echo(texts[0])
            self.exit_()
        
        # side method
        def make_method(method):
            method = method.strip().split(' ')
            m_ = method[0]
            if len(method)==2:
                m_ += method[1].title()
            return m_

        items = [
            'full name',
            'main number',
            'second number',
            'house address',
            'work address',
            'description'
        ]
        infos = {}
        temp = 0
        # get data and save into 'infos'
        for i in range(len(items)):
            method = make_method(items[i])
            if click.confirm(texts[1].format(items[i])):
                inp = click.prompt(texts[2])
                infos[method] = inp.strip()
                temp += 1
        
        if temp == 0:
            click.echo(texts[3])
        else:
            for attr, value in infos.items():
                self.update_user_by_type(self.chosen_user[0], attr, value, self.user_table)

    # updates a category (renames it)
    # :: RENAME CATEGORY :: #
    def update_category(self, category, new_name):
        self.exec_(
            f'ALTER TABLE {category} RENAME TO {new_name}'
        )