import mysql.connector

#creating database

mydb = mysql.connector.connect(
    host="localhost",
    user="",
    password="",#your database passsword
    database="dbms_mini_proj"#create your own database from mysql and add its name here
)
mycursor = mydb.cursor()

def createTables():
    # creating tables in social media projet
    mycursor.execute("DROP TABLE IF EXISTS Users")
    sql = '''
    CREATE TABLE users(
                    username varchar(50) PRIMARY KEY,
                    mobile varchar(20) NOT NULL,
                    email varchar(50) NOT NULL UNIQUE,
                    password varchar(16) NOT NULL DEFAULT 'password',
                    first_Name varchar(50) NOT NULL,
                    last_Name varchar(50),
                    birthdate varchar(50),
                    is_active BOOLEAN,
                    created_AT DATETIME
                    )
    '''
    mycursor.execute(sql)
    print("TABLE : User IS CREATED !!")

    # creating table Contacts in social media projet
    mycursor.execute("DROP TABLE IF EXISTS Contacts")
    sql = '''
    CREATE TABLE Contacts(
                    contact_uname varchar(50) PRIMARY KEY,
                    username varchar(50),
                    first_Name varchar(50) NOT NULL,
                    last_Name varchar(50),
                    phone_number varchar(10) NOT NULL UNIQUE,
                    email varchar(20) NOT NULL UNIQUE,
                    FOREIGN KEY(username) REFERENCES users(username)
                    )
    '''
    mycursor.execute(sql)
    print("TABLE : Contacts IS CREATED !!")

    # creating table Messaging in social media projet
    mycursor.execute("DROP TABLE IF EXISTS Messaging")
    sql = '''
    CREATE TABLE Messaging(
                    sender_uname varchar(50),
                    receiver_uname varchar(50),
                    message varchar(1000),
                    Time_Stamp DATETIME,
                    FOREIGN KEY(sender_uname) REFERENCES Users(username),
                    FOREIGN KEY(receiver_uname) REFERENCES Users(username)
                    )
    '''
    mycursor.execute(sql)
    print("TABLE : Messaging IS CREATED !!")

    # creating table Deleted_Messages in social media projet
    mycursor.execute("DROP TABLE IF EXISTS Del_Msg")
    sql = '''
    CREATE TABLE Del_Msg(
                    msg_sender varchar(50) PRIMARY KEY,
                    Deleted_message varchar(1000),
                    Delete_Time DATETIME
                    )
    '''
    mycursor.execute(sql)
    print("TABLE : Deleted Messages IS CREATED !!")

    # creating table Posts in social media projet
    mycursor.execute("DROP TABLE IF EXISTS Posts")
    sql = '''
    CREATE TABLE Posts(
                    post_from varchar(50),
                    post varchar(1000),
                    Post_Time DATETIME,
                    FOREIGN KEY(post_from) REFERENCES users(username)
                    )
    '''
    mycursor.execute(sql)
    print("TABLE : Posts IS CREATED !!")

createTables()

def createFunctions():
    #Function To Count Number Of Contacts
    sql = '''
CREATE FUNCTION count_contacts (user varchar(50))
RETURNS INT
DETERMINISTIC
BEGIN
   DECLARE value INT;

   SET value = 0;
   SELECT count(*) INTO value FROM contacts WHERE contacts.username = user;

   RETURN value;
END
'''
    mycursor.execute(sql)
    print("FUNCTION : To Count Number Of Contacts CREATED !")

    #Function To Count Number of Posts
    sql=''' 
CREATE FUNCTION count_posts (user varchar(50))
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE value INT;

    SET value = 0;
    SELECT count(*) INTO value FROM posts WHERE posts.post_from = user;

    RETURN value;
END
'''
    mycursor.execute(sql)
    print("FUNCTION : to Count Number Of Posts CREATED !!")

    #Function to count number of messages
    sql='''
CREATE FUNCTION count_messages (user varchar(50))
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE value INT;

    SET value = 0;
    SELECT count(*) INTO value FROM messaging WHERE messaging.sender_uname = user;

    RETURN value;
END
'''
    mycursor.execute(sql)
    print("FUNCTION : to count number of messages CREATED !!")
createFunctions()

def createProcedures():
    #Procedure to Display All Contacts
    sql='''
CREATE PROCEDURE display_contacts (IN user varchar(50))
BEGIN

    SELECT first_Name,Last_name,contact_uname FROM contacts WHERE contacts.username = user;

END
'''
    mycursor.execute(sql)
    print("PROCEDURE : To Display All Contacts CREATED !!")
createProcedures()

def createTriggers():
    #Trigger which works after delete on messages
    sql = '''
create TRIGGER delMsg 
AFTER DELETE
ON messaging 
FOR EACH ROW
BEGIN
    INSERT into del_msg VALUES(old.sender_uname,old.Message, old.Time_Stamp);
END
'''
    mycursor.execute(sql)
    print("TRIGGER : Which Sends Messages To Del_Message Table after deleted from messaging")

    #Trigger which works before inserting into contacts which inserts into users also
    sql = '''
create TRIGGER contact_user 
AFTER INSERT
ON contacts 
FOR EACH ROW
BEGIN
    INSERT into users(username,mobile,email,first_Name,last_Name) VALUES(contact_uname,phone_number,email,first_Name,last_Name);
END
    '''
    mycursor.execute(sql)
    print("TRIGGER : Which Inserts Into Messages if User has receiver as a contact")

createTriggers()

def createViews():
    #Creating a view ADMIn which can view all details
    sql = '''CREATE VIEW user_admin AS (select * from users GROUP BY username);'''
    mycursor.execute(sql)
    print("VIEW : User_ADMIN Created !!")

    #Create a contact admin view
    sql = '''CREATE VIEW contact_admin AS (select * from contacts GROUP BY username);'''
    mycursor.execute(sql)
    print("VIEW : Contact_ADMIN Created !!")

    #Create a message admin view
    sql = '''CREATE VIEW msg_admin AS (select * from messaging GROUP BY sender_uname);'''
    mycursor.execute(sql)
    print("VIEW : Message_ADMIN Created !!")

    #Create a post admin view
    sql = '''CREATE VIEW post_admin AS (select * from posts GROUP BY post_from);'''
    mycursor.execute(sql)
    print("VIEW : Post_ADMIN Created !!")
createViews()

def createRoles():
    #Create A Role Admin with select,insert and update privileges
    sql = '''CREATE ROLE admin;'''
    mycursor.execute(sql)
    sql = '''GRANT INSERT, UPDATE, DELETE ON dbms_mini_proj TO admin;'''
    mycursor.execute(sql)
    print("ROLE ADMIN CREATED !!")

    #Create A Role User with select privilege only
    sql = '''CREATE ROLE user;'''
    mycursor.execute(sql)
    sql = '''GRANT INSERT ON dbms_mini_proj TO user;'''
    mycursor.execute(sql)
    print("ROLE USER CREATED !!")
#createRoles()
