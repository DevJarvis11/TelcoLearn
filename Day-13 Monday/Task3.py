import os

while True:
    print("\n1.ip test 2.latency 3.exit")
    c = input("Choice")

    if c == "1":
        ip = input("IP: ")
        print("reachable"if os.system(f"ping -c 1 {ip} > /dev/null") == 0 else "unreachable")
        break

    elif c =="2": 
        nums = [int(x) for x in input("values: ").split(",")]
        break

        print({"min":min(nums),"max":max(nums),"average": sum(nums)/len(nums)})
    elif c =="3":
        break

    else:
        print("invalid")
        break
