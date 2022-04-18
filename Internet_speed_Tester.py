import speedtest
wifi=speedtest.Speedtest()

print("Wifi download speed Is :",wifi.download())
print("Wifi Upload speed Is :",wifi.upload())