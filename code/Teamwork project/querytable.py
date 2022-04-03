import sqlite3

bs = sqlite3.connect('bikeshare.db')
cursor = bs.cursor()

print('---location column---')
cursor.execute(f'''PRAGMA table_info([bike])''')
for i in cursor.fetchall():
    print(i)
print()

print('---location column---')
cursor.execute(f'''PRAGMA table_info([location])''')
for i in cursor.fetchall():
    print(i)
print()

print('---operations column---')
cursor.execute(f'''PRAGMA table_info([operations])''')
for i in cursor.fetchall():
    print(i)
print()

print('---ride column---')
cursor.execute(f'''PRAGMA table_info([ride])''')
for i in cursor.fetchall():
    print(i)
print()

print('---user column---')
cursor.execute(f'''PRAGMA table_info([user])''')
for i in cursor.fetchall():
    print(i)
print()
