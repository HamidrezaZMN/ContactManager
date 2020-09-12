# main libraries
import click, os, sys, datetime, configparser, glob
# database
from program.side_scripts.database.HandleDB import DATABASE
# help options texts
from program.side_scripts.text_items.help_options import help_
# click options prompt texts
from program.side_scripts.text_items.click_options import options_, others_

# import and export tools
from shutil import copy
from tkinter.filedialog import askdirectory, askopenfilename


# side methods
# makes appropriate method
# inp: full name      out: fullName
def make_method(method):
    method = method.strip().split(' ')
    m_ = method[0]
    if len(method)==2:
        m_ += method[1].title()
    return m_

# returns current time time
# month/day/year hour:minute:second
def current_time():
    datetime_ = datetime.datetime.now()
    date = datetime_.strftime('%x')
    time = datetime_.strftime('%X')
    return date + ' ' + time

def show_all_usernames():
    texts = others_['contact']['login']
    all_dbs = [i[:-3] for i in glob.glob('*.db')]
    all_usernames = 'all the usernames:\n'
    for database_ in all_dbs:
        all_usernames += f'    {database_}\n'
    all_usernames += '\n\n'

    return all_usernames

def is_logined():
    try:
        config = configparser.ConfigParser()
        config.read('auth.config')
        username = config['user-data']['USERNAME']

        all_dbs = [i[:-3] for i in glob.glob('*.db')]

        if username in all_dbs:
            return True
    except:
        pass
    return False

def login_to_user(username):
    f = open('auth.config', 'w')
    f.write('\n'.join([
        '[user-data]',
        f'USERNAME={username}'
    ]))
    f.close()

    click.echo(others_['contact']['login_to_user'][0].format(username))

def database_name():
    try:
        config = configparser.ConfigParser()
        config.read('auth.config')
        return config['user-data']['USERNAME']
    except:
        return ''

def check_logined():
    if not is_logined():
        click.echo(others_['contact']['check_logined'][0])
        sys.exit()




# contact
# containing: add, remove, update, show
# main command
@click.group(help=help_['main']['contact'])
def contact():
    pass




# contact add
# containing: user, category
# adds a new category or a user to a category
@contact.group(help=help_['main']['contact-add'])
def add():
    check_logined()
    pass

# contact add user
@add.command(help=help_['main']['contact-add-user'])
@click.option(
    '--category', '-c',
    prompt=options_['contact-add-user.category'],
    help=help_['options']['...-user-category']
)
def user(category):
    global db
    items = [
        'full name',
        'main number',
        'second number',
        'house address',
        'work address',
        'added date',
        'description'
    ]
    infos = {}
    temp = 0
    # get data and save into 'infos'
    for i in range(len(items)):
        m_ = make_method(items[i])
        if m_ == 'addedDate':
            infos[m_] = current_time()
        else:
            if click.confirm(others_['contact']['add-user'][0].format(items[i])):
                inp = click.prompt(others_['contact']['add-user'][1].format(items[i]))
                infos[m_] = inp.strip()
                temp += 1
    # if any data is entered
    if temp == 0:
        click.echo(others_['contact']['add-user'][2])
    else:
        db.add_user(infos, category.strip())

# contact add category
@add.command(help=help_['main']['contact-add-category'])
@click.option(
    '--name', '-n',
    prompt=options_['contact-add-category.name'],
    help=help_['options']['...-category-name']
)
def category(name):
    global db
    db.add_category(name.strip())




# contact remove
# containing: user, category
# removes a whole category, or a user of a category
@contact.group(help=help_['main']['contact-remove'])
def remove():
    check_logined()
    pass

# contact remove user
@remove.command(help=help_['main']['contact-remove-user'])
@click.option(
    '--name', '-n',
    prompt=options_['contact-remove-user.name'],
    help=help_['options']['...-user-name']
)
def user(name):
    global db
    db.remove_user(name)

# contact remove category
@remove.command(help=help_['main']['contact-remove-category'])
@click.option(
    '--name', '-n',
    prompt=options_['contact-remove-category.name'],
    help=help_['options']['...-category-name']
)
def category(name):
    global db
    db.remove_category(name.strip())




# contact show
# containing: all, category, categories
# shows information from user(s) accordingly
@contact.group(help=help_['main']['contact-show'])
def show():
    check_logined()
    pass

# contact show all users
# contains: users, categories
# shows name of all users or all categories
@show.group(help=help_['main']['contact-show-all'])
def all():
    pass

# contact show all users
@all.command(help=help_['main']['contact-show-all-users'])
@click.option(
    '--order-method', '-o',
    type=click.Choice(
        [
            'full name',
            'added date',
            'no order'
        ],
        case_sensitive=True
    ),
    prompt=options_['contact-show-all-users.order_method'],
    help=help_['options']['...-show-...-order_method']
)
@click.option(
    '--full-information', '-f',
    is_flag=True,
    prompt=options_['contact-show-all-users.full_information'],
    help=help_['options']['...-show-...-full_information']
)
def users(order_method, full_information, reverse=False):
    global db
    _m = make_method(order_method)
    if _m != 'noOrder':
        reverse = click.confirm(others_['contact']['show-all-users'][0])
    db.show_all_users(full_information, _m, reverse)

# contact show all categories
@all.command(help=help_['main']['contact-show-all-categories'])
def categories():
    global db
    db.show_all_categories()

# contact show category
@show.command(help=help_['main']['contact-show-category'])
@click.option(
    '--name', '-n',
    prompt=options_['contact-show-category.name'],
    help=help_['options']['...-category-name']
)
@click.option(
    '--order-method', '-o',
    type=click.Choice(
        [
            'full name',
            'added date',
            'no order'
        ],
        case_sensitive=True
    ),
    prompt=options_['contact-show-category.order_method'],
    help=help_['options']['...-show-...-order_method']
)
@click.option(
    '--full-information', '-f',
    is_flag=True,
    prompt=options_['contact-show-category.full_information'],
    help=help_['options']['...-show-...-full_information']
)
def category(name, order_method, full_information, reverse=False):
    global db
    _m = make_method(order_method)
    if _m != 'noOrder':
        reverse = click.confirm(others_['contact']['show-category'][0])
    db.show_users_of_category(name.strip(), full_information, _m, reverse)

# contact show user
@show.command(help=help_['main']['contact-show-user'])
@click.option(
    '--method', '-m',
    type=click.Choice(
        ['name', 'number'],
        case_sensitive=False
    ),
    prompt=options_['contact-show-user.method'],
    help=help_['options']['...-show-user-method']
)
@click.option(
    '--value', '-v',
    prompt=options_['contact-show-user.value'],
    help=help_['options']['...-show-user-value']
)
def user(method, value):
    global db

    if not db.show_user(value, method):
        click.echo(others_['contact']['show-user'][0])




# contact update
# contains: user, category
@contact.group(help=help_['main']['contact-update'])
def update():
    check_logined()
    pass

# contact update user
# changes user infos
@update.command(help=help_['main']['contact-update-user'])
@click.option(
    '--name', '-n',
    prompt=options_['contact-update-user.name'],
    help=help_['options']['...-user-name']
)
def user(name):
    global db
    db.update_user(name)

# contact update category
# changes category's name
@update.command(help=help_['main']['contact-update-category'])
@click.option(
    '--name', '-n',
    prompt=options_['contact-update-category.name'],
    help=help_['options']['...-category-name']
)
@click.option(
    '--new-name', '-n',
    prompt=options_['contact-update-category.new_name'],
    help=help_['options']['...-category-new_name']
)
def category(name, new_name):
    db.update_category(name.strip(), new_name)




# contact export
# exports the database
@contact.command(help=help_['main']['contact-export'])
def EXPORT():
    check_logined()
    try:
        dir_to_save = askdirectory(
            initialdir = '/',
            title = 'choose a directory to save the contact notebook'
        )
        data_base_dir = os.getcwd()+'/'+db.db_name
        copy(data_base_dir, dir_to_save)
        click.echo(others_['contact']['export'][0])
    except:
        click.echo(others_['contact']['export'][1])
        click.echo(others_['contact']['export'][2])




# contact import
# imports the database
@contact.command(help=help_['main']['contact-import'])
def IMPORT():
    texts = others_['contact']['import']
    try:
        db_dir = askopenfilename(
            initialdir = '/',
            title = 'select a contact notebook',
            filetypes = (
                ('database files', '*.db*'),
                ('all files', '*.*')
            )
        )
        db_dest = os.getcwd()
        copy(db_dir, db_dest)
        click.echo([0])
    except:
        click.echo(texts[1])
        click.echo(texts[2])




# contact login
# makes or/and logins to a username
@contact.command(help=help_['main']['contact-login'])
@click.option(
    '--username', '-u',
    prompt=show_all_usernames() + options_['contact-login.username'],
    help=help_['options']['...-login-username']
)
def login(username):
    texts = others_['contact']['login']
    # print(texts)
    all_dbs = [i[:-3] for i in glob.glob('*.db')]
    
    username = username.strip()
    if username == 'auth':
        click.echo(texts[0])
        sys.exit()

    if username in all_dbs:
        login_to_user(username)
    else:
        click.echo(texts[1])
        if click.confirm(texts[2]):
            db = open(username+'.db', 'w', closefd=True)
            click.echo(texts[3].format(username))
            login_to_user(username)
        else:
            click.echo(texts[4])




# logouts from current username
@contact.command(help=help_['main']['contact-logout'])
def logout():
    try:
        f = open('auth.config', 'w', closefd=True)
    except:
        pass
    click.echo(others_['contact']['logout'][0])




# removes a username
@contact.command(help=help_['main']['remove-username'])
@click.option(
    '--name', '-n',
    prompt=show_all_usernames() + options_['contact-remove_username.name'],
    help=help_['options']['...-remove_username']
)
def remove_username(name):
    texts = others_['contact']['remove-username']

    all_dbs = [i[:-3] for i in glob.glob('*.db')]

    if name not in all_dbs:
        click.echo(texts[0].format(name))
        sys.exit()
    
    if click.confirm(texts[1].format(name)):
        try:
            f = open('auth.config', 'w', closefd=True)
            os.remove(name+'.db')
            click.echo(texts[2])
        except:
            click.echo(texts[3])
            click.echo(texts[4])
    else:
        click.echo(texts[5])




if __name__ == "__main__":
    if database_name() != '':
        db = DATABASE(database_name())
        db.connect_db()
    try:
        contact()
    except KeyboardInterrupt:
        print('\nkeyboard interrupted\nnothing happened')
    finally:
        try:
            db.close_db()
        except:
            pass