import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="----------",
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS atm_data")
mycursor.execute("USE atm_data")
mycursor.execute("CREATE TABLE IF NOT EXISTS card_details(id INT AUTO_INCREMENT PRIMARY KEY ,username VARCHAR(255), card_no VARCHAR(255), pin_no VARCHAR(255), issue_date VARCHAR(255), expiry_date VARCHAR(255), balance VARCHAR(255))")
mycursor.execute("DESCRIBE card_details")
columns = mycursor.fetchall()



sql = "INSERT INTO card_details(username,card_no ,pin_no ,issue_date ,expiry_date,balance) VALUES (%s, %s,%s,%s, %s,%s)"
val = [('JohnDoe', '1234567812345678', '1234', '2021-01-15', '2025-01-15', '5000'),
         ('JaneSmith', '2345678923456789', '2345', '2021-03-20', '2025-03-20', '3000'),
        ('AliceJohnson', '3456789034567890', '3456', '2021-05-10', '2025-05-10', '2500'),
        ('BobBrown', '4567890145678901', '4567', '2022-02-05', '2026-02-05', '1000'),
        ('CharlieDavis', '5678901256789012', '5678', '2022-06-15', '2026-06-15', '7000'),
        ('DavidMiller', '6789012367890123', '6789', '2023-01-18', '2027-01-18', '12000'),
        ('EvaGarcia', '7890123478901234', '7890', '2023-04-22', '2027-04-22', '800'),
        ('FayHill', '8901234589012345', '8901', '2021-11-03', '2025-11-03', '4000'),
        ('GeorgeMoore', '9012345690123456', '9012', '2022-09-07', '2026-09-07', '3500'),
        ('HannahTaylor', '1234567812345679', '1235', '2020-07-25', '2024-07-25', '5500'),
        ('IanWright', '2345678923456790', '2346', '2020-12-17', '2024-12-17', '9000'),
        ('JackAnderson', '3456789034567901', '3457', '2021-02-10', '2025-02-10', '6000'),
        ('KimberlyThomas', '4567890145678912', '4568', '2021-08-29', '2025-08-29', '11000'),
        ('LucasJackson', '5678901256789023', '5679', '2022-05-05', '2026-05-05', '700'),
        ('MeganWhite', '6789012367890134', '6780', '2022-12-13', '2026-12-13', '3000'),
        ('NathanRoberts', '7890123478901245', '7891', '2023-03-17', '2027-03-17', '4500'),
        ('OliviaWalker', '8901234589012356', '8902', '2023-08-04', '2027-08-04', '3500'),
        ('PaulScott', '9012345690123467', '9013', '2022-01-09', '2026-01-09', '2500'),
        ('QuincyYoung', '1234567812345680', '1236', '2021-10-30', '2025-10-30', '1500'),
        ('RebeccaAdams', '2345678923456801', '2347', '2021-05-19', '2025-05-19', '5000'),
        ('EmmaWilson', '9876543298765432', '1234', '2024-11-01', '2029-11-01', '4500'),
        ('LiamAnderson', '8765432187654321', '2345', '2024-11-05', '2029-11-05', '8000'),
        ('OliviaMartinez', '7654321098765432', '3456', '2024-11-10', '2029-11-10', '12000'),
        ('NoahClark', '6543210987654321', '4567', '2024-11-15', '2029-11-15', '9800'),
        ('AvaHall', '5432109876543210', '5678', '2024-11-20', '2029-11-20', '6500'),
        ('EthanMoore', '4321098765432109', '6789', '2024-11-25', '2029-11-25', '7200'),
        ('IsabellaMiller', '3210987654321098', '7890', '2024-12-01', '2029-12-01', '5100'),
        ('MasonGarcia', '2109876543210987', '8901', '2024-12-05', '2029-12-05', '8800'),
        ('SophiaHarris', '1098765432109876', '9012', '2024-12-10', '2029-12-10', '4300'),
        ('LoganLee', '9087654321098765', '0123', '2024-12-15', '2029-12-15', '7500'),
        ('MiaMartinez', '8076543210987654', '1234', '2024-12-20', '2029-12-20', '8700'),
        ('LucasTaylor', '7065432109876543', '2345', '2024-12-25', '2029-12-25', '6500'),
        ('AmeliaThomas', '6054321098765432', '3456', '2025-01-01', '2030-01-01', '9800'),
        ('ElijahAnderson', '5043210987654321', '4567', '2025-01-05', '2030-01-05', '5200'),
        ('HarperJohnson', '4032109876543210', '5678', '2025-01-10', '2030-01-10', '4700'),
        ('BenjaminKing', '3021098765432109', '6789', '2025-01-15', '2030-01-15', '7900'),
        ('EvelynScott', '2010987654321098', '7890', '2025-01-20', '2030-01-20', '8600'),
        ('JamesGreen', '1009876543210987', '8901', '2025-01-25', '2030-01-25', '9200'),
        ('AbigailWright', '0198765432109876', '9012', '2025-02-01', '2030-02-01', '6600'),
        ('DanielHill', '9876543212345678', '0123', '2025-02-05', '2030-02-05', '8400')
        
]


mycursor.executemany(sql, val)
mydb.commit()




