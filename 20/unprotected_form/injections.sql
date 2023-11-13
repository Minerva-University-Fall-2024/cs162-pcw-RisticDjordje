--- run this file on users.db that is created by the unprotected_webserver.py

INSERT INTO users VALUES (1, "cs162_user", "cs162@minerva.kgi.edu", "longpasswordsaresecure");
INSERT INTO users VALUES (2, "admin", "admin@minerva.kgi.edu", "123456");
INSERT INTO users VALUES (3, "prof_smith", "smith@minerva.kgi.edu", "password123");


--- an attack which will identify a known user without knowing their password.
SELECT * FROM users WHERE username = ''