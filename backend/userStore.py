# This is the connector that will handle the user store. This will grab users by id, get their hierarchy, etc
import pickle

class User:
    # Class to represent a user. Essentially a struct
    def __init__(self, uid, name, phonenum, parent=None, photo=None):
        # We are going to store as many things as user objects as possible in this
        # to avoid unnecessary references to the tree structure
        # By doing this, we can essentially go back and forth due to
        # python's referencing. Trust me I know what this means I think.
        self.name = name
        self.uid = uid
        self.phonenum = phonenum
        self.employees = [] # Initially empty, will populate during user addition
        self.parent = parent
        self.photo = photo

    def add_employee(self, user):
        self.employees.append(user)

class UserStore:
    def __init__(self):
        # This loads the userDB state into python's memory for later usage
        try:
            with open('phish_db/users.db', 'rb+') as f:
                # If the user DB exists, bring it into memory.
                # In terms of structure, I'm going to cheat a little to only use one file
                # This object will be a list containing two dicts. One for the user reps and another
                # for the tree rep.
                self.__user_db_container = pickle.load(f)
        except FileNotFoundError:
            # UserDB doesn't exist, create a new representation
            self.__user_db_container = []
            for _ in range(2):
                self.__user_db_container.append(dict())
            self.__user_db_container.append([]) # This will be in index 2, so this is the user tree
        # We should now have a user container. Let's break it into the two key parts
        self.user_tree = self.__user_db_container[2]
        self.__name_lookup_tree = self.__user_db_container[1]
        self.user_objs = self.__user_db_container[0]
        # We should be good to continue

    def __del__(self):
        # Called when var goes out of scope or program ends
        # Need to save the userDB
        with open('phish_db/users.db', 'wb+') as f:
            pickle.dump(self.__user_db_container, f)

    def get_user(self, uid):
        # Given a uid, retrieve the user's data
        return self.user_objs[uid]

    def lookup_user(self, name):
        # Given a name, find the associated user. Assuming no duplicate names here.
        return self.__name_lookup_tree[name]

    def add_user(self, name, phonenum, parent=None, photo=None):
        # This will add a user to the tree. Required params are name and phone number. Optional is parent (represented by name)
        # If specified, it will add this user to the employees
        # of the parent specified. If not, it will be located at the top of the tree.
        uid = len(self.user_objs) + 1 # Sequential uids. Not secure but we can easily change this later since grabbing uids is agnostic
        
        # We need to do a few things: create the user object, add it to the tree in the proper location, and add it to the user
        # objs dict. Everything *should* stay in sync when done.
        new_user = User(uid, name, phonenum, parent, photo)
        self.user_objs[uid] = new_user
        self.__name_lookup_tree[name] = new_user
        
        if parent:
            # Now we just need to add this user to the employees of the given parent (if any). This will avoid unnecessary re-calcs of the org
            parent = self.lookup_user(parent)
            parent.add_employee(new_user)
        else:
            # This is a top level user, add to tree directly
            self.user_tree.append(new_user)
