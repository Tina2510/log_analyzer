from faker import Faker
import random

fake = Faker()

log_level = ["INFO", "WARNING", "ERROR", "CRITICAL"]

http_code = [200, 201, 301, 400, 401, 403, 404, 500, 502]


with open("server_log.txt", "w") as file:
    for _ in range(10):
        date = fake.date()
        time = fake.time()
        level = random.choice(log_level)
        ip = fake.ipv4()
        status = random.choice(http_code)
        message = fake.sentence(nb_words=5)


        log = (
            f"{date} ,{time} , {level} , "
            f"IP:{ip} , STATUS:{status} , {message}\n"
        )

        file.write(log)
