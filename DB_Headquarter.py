#SQL
#DB_Headquarter.py is to initialize the database called HM_game_data.db, including a default word bank (which is not set by users), initalize users data (name & password), users' score & streak. In other words, running this file would factory-reset the HM_game_data.db.
import sqlite3
conn = sqlite3.connect('HM_game_data.db')
cursor = conn.cursor()

cursor.execute(
    '''
    DROP TABLE IF EXISTS wordbank
    '''
)
cursor.execute('DROP table IF EXISTS users')

#Can merely execute 1 comment at a time in cursor.execute
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS wordbank (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    word TEXT UNIQUE,
    tip TEXT,
    difficulty INTEGER,
    custom_word BOOLEAN,
    playedByUser1 BOOLEAN DEFAULT False,
    playedByUser2 BOOLEAN DEFAULT False,
    playedByUser3 BOOLEAN DEFAULT False,
    playedByUser4 BOOLEAN DEFAULT False,
    playedByUser5 BOOLEAN DEFAULT False

    
   
    )
               ''')
conn.commit()
cursor.execute(
    '''
CREATE TABLE IF NOT EXISTS users (
    userID INTEGER PRIMARY KEY,
    registered BOOLEAN DEFAULT False,
    name TEXT UNIQUE,
    password TEXT,
    Hi_score INTEGER DEFAULT 0,
    Total_score INTEGER DEFAULT 0,
    Hi_streak INTEGER DEFAULT 0
    )
'''
)
conn.commit()
#the ? reduces workload,in which each '?' represents a data value afterhead
#words must be kept lower case
cursor.executemany('''
    INSERT INTO wordbank (word,tip,difficulty,custom_word) VALUES (?, ?, ?, ?)
''', [
    ('eggplant', 'a veggie that perfectly tastes well if it is deep fried and dipped in soy sauce', 1, False),
    ('propeller', 'rotating blades that could be found on the fan', 2, False),
    ('verandah', 'cosy outdoor structure attached to a luxury house', 3, False),
    ('trafficking', 'illegal trading activities of selling humans', 3, False),
    ('temperament', 'Persistent feeling or emotion come instinctively', 4, False),
    ('nefarious', 'to describe someone/animals that are very evil and demon-like', 5, False),
    ('brouhaha', 'a noisy or over-response to something, usually describe the audience members', 5, False),
    ('aspiration', 'goals you really want to achieve', 2, False),
    ('slither', 'to slip along a surface', 1, False),
    ('lavish', 'something that is produced in abundance', 3, False),
    ('omelete', 'A food made of fried eggs on a pan, with runny eggs in the middle', 1, False),
    ('mayhem', 'Chaotic scene, like many brawlers fighting each other', 4, False),
    ('rabbit', 'A fluffy and cute animal with two iconic long ears', 1, False),
    ('scaffolding', 'Temporary building structure used to assist the architects, usually built during constructions', 2, False),
    ('opaque', 'to describe something that are not transparent, i.e. solid colors', 5, False),
    ('soulmate', 'Mutual Close Friend with high acceptance', 2, False)
])
conn.commit()
#cursor.execute("UPDATE wordbank SET playedByUser1 = False, playedByUser2 = False, playedByUser3 = False WHERE")
for i in range(1,6):
    cursor.execute("INSERT INTO users (userID, name) VALUES (?,?)",(i,f"Available Slot {i}"))
conn.commit()



cursor.execute("SELECT * FROM wordbank;")
results = cursor.fetchall() 
for row in results:
    print(row)
print('==================================')


cursor.execute("SELECT * FROM users;")
results = cursor.fetchall() 
for row in results:
    print(row)
print('==================================')





cursor.execute("SELECT COUNT (*) FROM wordbank;")
results = cursor.fetchall()
print(results)