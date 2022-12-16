import speedtest
import time

def bytes_to_mb(bytes):
  KB = 1024 
  MB = KB * 1024 
  return int(bytes/MB)


s=speedtest.Speedtest()
print("Tesing....\n")

d= s.download()
u = s.upload()
ping = round(s.results.ping)

print(f"Download speed:{bytes_to_mb(d)/8:.2f} MBps")
print(f"Upload speed:{bytes_to_mb(u)/8:.2f} MBps")
print(f"Ping:{ping:.2f} Ms")