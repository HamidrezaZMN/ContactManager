# colorizing terminal text
from program.side_scripts.colorizing.colorize import ctext

all_prompts = [
    ctext('enter category\'s name', 'GREEN'),
    ctext('enter user\'s name', 'CYAN'),
    ctext('order list by', 'YELLOW'),
    ctext('show full information', 'RED'),
    ctext('find user by', 'GREEN'),
    ctext('enter value', 'YELLOW'),
    ctext('enter the new name', 'RED'),
    ctext('enter your username', 'CYAN'),
    ctext('enter username', 'CYAN')
]


options_ = {
    # add
    'contact-add-user.category' : all_prompts[0],
    'contact-add-category.name' : all_prompts[0],
    # remove
    'contact-remove-user.name' : all_prompts[1],
    'contact-remove-category.name' : all_prompts[0],
    # show
    'contact-show-all-users.order_method' : all_prompts[2],
    'contact-show-all-users.full_information' : all_prompts[3],
    'contact-show-category.name' : all_prompts[0],
    'contact-show-category.order_method' : all_prompts[2],
    'contact-show-category.full_information' : all_prompts[3],
    'contact-show-user.method' : all_prompts[4],
    'contact-show-user.value' : all_prompts[5],
    # update
    'contact-update-user.name' : all_prompts[1],
    'contact-update-category.name' : all_prompts[0],
    'contact-update-category.new_name' : all_prompts[6],
    # login
    'contact-login.username' : all_prompts[7],
    # remove-username
    'contact-remove_username.name' : all_prompts[8]
}


others_ = {
    'contact' : {
        # login_to_user
        'login_to_user' : [
            ctext('logined to "{}"', 'YELLOW')
        ],
        # check_logined
        'check_logined' : [
            ctext('please login first', 'RED')
        ],
        # add
        'add-user' : [
            ctext('want to enter {}?', 'CYAN'),
            ctext('enter {}', 'YELLOW'),
            ctext('nothing entered bro', 'RED')
        ],
        # show
        'show-all-users' : [
            ctext('reverse the list', 'GREEN')
        ],
        'show-category' : [
            ctext('reverse the list', 'CYAN')
        ],
        'show-user' : [
            ctext('no user found', 'RED')
        ],
        # export
        'export' : [
            ctext('exported notebook successfully', 'GREEN'),
            ctext('something went wrong', 'RED'),
            ctext('couldn\'t export contact notebook', 'RED')
        ],
        # import
        'import' : [
            ctext('imported notebook successfully', 'GREEN'),
            ctext('something went wrong', 'RED'),
            ctext('couldn\'t import contact notebook', 'RED')
        ],
        #login
        'login' : [
            ctext('cant make user with this name', 'RED'),
            ctext('username does\'nt exist', 'GREEN'),
            ctext('create one', 'GREEN'),
            ctext('created notebook for user "{}"', 'WHITE'),
            ctext('nothing happened', 'RED')
        ],
        # logout
        'logout' : [
            ctext('loged out', 'YELLOW')
        ],
        # remove-username
        'remove-username' : [
            ctext('no username called {}', 'RED'),
            ctext('delete "{}"', 'MAGENTA'),
            ctext('username deleted successfully', 'GREEN'),
            ctext('somthing went wrong', 'YELLOW'),
            ctext('couldn\'t delete username', 'YELLOW'),
            ctext('nothing happened', 'YELLOW')
        ]
    },
    'HandleDB' : {
        'connect_db' : [
            ctext('{}', 'RED')
        ],
        'echo_all_users' : [
            ctext('\n{}', 'GREEN'),
            ctext('---------------------------------------------------', 'WHITE'),
            ctext('{}', 'CYAN')
        ],
        'add_user' : [
            ctext('no category called: "{}"', 'RED'),
            ctext('make the category', 'GREEN')
        ],
        'add_category' : [
            ctext('category already exists', 'RED')
        ],
        'remove_user' : [
            ctext('   {}. {}', 'CYAN'),
            ctext('\nenter number', 'GREEN'),
            ctext('delete user "{}"', 'RED'),
            ctext('nothing happened', 'YELLOW'),
            ctext('nothing found', 'YELLOW')
        ],
        'remove_category' : [
            ctext('delete category "{}"', 'RED'),
            ctext('nothing happened', 'YELLOW'),
            ctext('no category called "{}"', 'YELLOW')
        ],
        'show_users_of_category' : [
            ctext('ERROR: no category with that name found', 'CYAN')
        ],
        'show_user' : [
            ctext('   {}. {}', 'CYAN'),
            ctext('\nenter number', 'GREEN'),
            ctext('wrong input', 'RED'),
            ctext('{}', 'YELLOW')
        ],
        'show_all_categories' : [
            ctext('{}', 'YELLOW')
        ],
        'update_user' : [
            ctext('no user found', 'RED'),
            ctext('want to change {}', 'GREEN'),
            ctext('enter new value', 'YELLOW'),
            ctext('nothing entered bro', 'RED')
        ]
    }
}