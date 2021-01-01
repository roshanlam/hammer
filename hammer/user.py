class User:
    def __init__(self, name, username, password):
        self.name = name
        self.username = name
        self.password = password
        self.loggedIn = True
    
    def home(user):
        print("Login, Register")
        user_input = input("What would you like to do:\n")
        if(user_input == "register" or user_input == "Register"):
            register()
        elif(user_input == "login" or user_input == "Login"):
            login(user)
        else:
            print("Choose a valid option")
            home('')
    
    def register():
        name = input("Name:\n")
        username = input("Username:\n")
        password = input("Password:\n")
        userr = User(name, username, password)
        print("Welcome, " + username.name)
        home(username)

    def login(user):
        l1 = input("Username:\n")
        l2 = input("Password:\n")
        if(l2 == user.password):
            print("Welcome,  " + user.name)
         else:
            print("Incorrect username or password")
            login(user)
          home('')
    home('')
