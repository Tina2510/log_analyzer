import re
ip_pattern = r"\bIP:\d+\.\d+\.\d+\.\d+\b"
error_code = r"\bSTATUS:(2\d{2}|3\d{2}|4\d{2}|5\d{2})\b"
unique_ips = set()
status_count = {}

with open("server_log.txt","r") as file:
    for l in file:
        l = l.strip() 
        ip = re.search(ip_pattern, l)
        if ip:
            unique_ips.add(ip.group())

        status = re.search(error_code, l)
        if status:
            code = status.group()

            if code in status_count:
                status_count[code]+=1
            else:
                status_count[code] = 1    

with open ("log_summary.txt", "w") as summary:
    summary.write("Log summary \n")
    summary.write("Total unique IPs: " + str(len(unique_ips)) + "\n") 
    summary.write("HTTP status code count: \n")
    for code in status_count:
        summary.write(code +": " + str(status_count[code]) + "\n")  


      