# ------------------------------------------------------------------


# try:
#     Name = int(input("Enter name: "))
#     Age = int(input("Enter age: "))
#     City = input("Enter City: ")
# except:
#     print("Invalid input. Please enter valid data.")
# else:
#     print(f"Hello, my name is {Name}. I am {Age} years old and I live in {City}.")
# finally:
#     print("Thank you for using the program.")


# ------------------------------------------------------------------


# import subprocess
# import time

# ips = ["8.8.8.8", "1.1.1.1", "192.168.1.1", "10.0.2.15", "127.0.0.1"]

# for ip in ips:
#     print(f"\nPinging {ip}...")

#     try:
#         result = subprocess.run(
#             ["ping", "-n", "1", ip],
#             timeout=0.5
#         )

#         if result.returncode == 0:
#             print(f"IP {ip} is reachable\n")
#         else:
#             print(f"IP {ip} is not reachable\n")

#     except subprocess.TimeoutExpired:
#         print(f"Error pinging {ip}. Trying next IP...\n")


# ------------------------------------------------------------------

import logging
logging.basicConfig(filename='log.txt', level=logging.DEBUG)
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")


a = "Ankith M"
print(a[10])