help_ = {
    'main' : {
        # contact
        'contact' : '''
        \b
        make a contact notebook

        \b 
        use one of the blow commands to see how do the work
        example: contact add --help
        ''',
        # contact add
        'contact-add' : '''
        \b
        adds new user or category
        ''',
        'contact-add-user' : '''
        \b
        add new user
        
        \b
        type 'contact add user' and press enter
        it will ask you to enter a category name
        then one by one, asks for what to add
        ''',
        'contact-add-category' : '''
        \b
        add new category

        \b
        type 'contact add category' and press enter
        it will ask you to enter the category's name
        ''',
        # contact remove
        'contact-remove' : '''
        \b
        removes user or category
        ''',
        'contact-remove-user' : '''
        \b
        removes user

        \b
        type 'contact remove user' and press enter
        it will ask you the name of the user
        ''',
        'contact-remove-category' : '''
        \b
        removes a category

        \b
        type 'contact remove category' and press enter
        it will ask you the name of the category
        ''',
        # contact show
        'contact-show' : '''
        \b
        shows, one user or category
        or shows all users or only all users of one category
        ''',
        'contact-show-user' : '''
        \b
        shows one specific user

        \b
        type 'contact remove category' and press enter
        it will asks you to find by name or number
        and then shows infos about it
        ''',
        'contact-show-category' : '''
        \b
        shows all the users of a category

        \b
        type 'contact show category' and press enter
        it will ask you the name of the category
        ''',
        'contact-show-all' : '''
        \b
        it shows all the users or all the categories
        ''',
        'contact-show-all-users' : '''
        \b
        shows all the users

        \b
        type 'contact show all users' and press enter
        it will ask you some additional questions
        ''',
        'contact-show-all-categories' : '''
        \b
        shows all the categories

        \b
        type 'contact show all users' and press enter
        ''',
        # contact update
        'contact-update' : '''
        \b
        updates a user or a category
        Note: 'update category' actually renames it
        ''',
        'contact-update-user' : '''
        \b
        update users infos

        \b
        type 'contact update user' and press enter
        it will ask you the name of the user
        then asks to edit infos about it
        ''',
        'contact-update-category' : '''
        \b
        renames a category

        \b
        type 'contact update category' and press enter
        it will ask you the name of the category
        then the new name
        ''',
        # contact export
        'contact-export' : '''
        \b
        exports contacts to the location you want
        ''',
        # contact import
        'contact-import' : '''
        \b
        imports the current contact that you are logged in,
        to the directory that you want

        \b
        Note: don't forget to login to the username you want, first
        ''',
        # contact login
        'contact-login' : '''
        \b
        logins to the username that you want

        \b
        if you want to make a new user, also use this command
        for example:
            $ login newUser
        and then it asks to make the user or not
        ''',
        # contact logout
        'contact-logout' : '''
        \b
        logouts from the current notebook
        ''',
        'remove-username' : '''
        \b
        removes the username you enter
        '''
    },
    'options' : {
        '...-user-category' : '''
        \b
        category of the user
        ''',
        '...-category-name' : '''
        \b
        name of the category
        ''',
        '...-user-name' : '''
        \b
        name of the user
        ''',
        '...-show-...-order_method' : '''
        \b
        how to order the list (by name or number)
        ''',
        '...-show-...-full_information' : '''
        \b
        show all the data about user or not (only name and main number)
        ''',
        '...-show-user-method' : '''
        \b
        what do you want to find user
        find by name or number (main or second)
        ''',
        '...-show-user-value' : '''
        \b
        the value of that method
        for example, if find by name:
            hamidreza
        ''',
        '...-category-new_name' : '''
        \b
        new name for the category
        ''',
        '...-login-username' : '''
        \b
        the name of the username you want to login or make
        ''',
        '...-remove_username' : '''
        \b
        the name of the username to delete
        '''
    }
}