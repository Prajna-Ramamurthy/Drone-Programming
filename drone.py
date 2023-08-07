#import libraries
from dronekit import *
import time
import math
import pyqrcode
import cv2
from geopy.geocoders import Nominatim

cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()

#connect to vehicle
vehicle = connect('127.0.0.1:14551',baud=921600,wait_ready=True)
loc = Nominatim(user_agent="GetLoc")

Qrpass=input("Enter the Password to generate the QR Code:- ")
#genertaing the password of qrcode
url = pyqrcode.create(Qrpass)
url.svg("secret.svg", scale = 8)
url.png('secret.png', scale = 6)

print("Qr Code Successfully Generated and send to your System")

Qrpass1=input("Enter the Password to generate the QR Code for landing:- ")
#genertaing the password of qrcode
url = pyqrcode.create(Qrpass1)
url.svg("landing.svg", scale = 8)
url.png('landing.png', scale = 6)
print("Qr Code Successfully Generated and send to your System")

#move in the desired location
loc = Nominatim(user_agent="GetLoc")
# entering the location name
add=input("Enter the address:")
getLoc = loc.geocode(add)
# printing address
print(getLoc.address)
# printing latitude and longitude
print("Latitude = ", getLoc.latitude, "\n")
print("Longitude = ", getLoc.longitude)

#takeoff function
def arm_takeoff(height):
    #check if drone is ready
    while not vehicle.is_armable:
        print("Waiting for drone")
        time.sleep(1)

    #change mode and arm
    print("Arming")
    vehicle.mode=VehicleMode('GUIDED')
    vehicle.armed=True
    
    #check if drone is armed
    while not vehicle.armed:
        print("Waiting for arm\n")
        time.sleep(1)

    #takeoff
    print("Taking off")
    vehicle.simple_takeoff(height)

    #report values back every 1s and finally break out
    while True:
        print('Reached ',vehicle.location.global_relative_frame.alt)
        if(vehicle.location.global_relative_frame.alt>=height*0.95):
            print("Reached Target Altitude\n")
            break
        time.sleep(1)

def get_location_metres(original_location, dNorth, dEast):

    earth_radius = 6378137.0 #Radius of "spherical" earth
    #Coordinate offsets in radians
    dLat = dNorth/earth_radius
    dLon = dEast/(earth_radius*math.cos(math.pi*original_location.lat/180))

    #New position in decimal degrees
    newlat = original_location.lat + (dLat * 180/math.pi)
    newlon = original_location.lon + (dLon * 180/math.pi)
    if type(original_location) is LocationGlobal:
        targetlocation=LocationGlobal(newlat, newlon,original_location.alt)
    elif type(original_location) is LocationGlobalRelative:
        targetlocation=LocationGlobalRelative(newlat, newlon,original_location.alt)
    else:
        raise Exception("Invalid Location object passed")
        
    return targetlocation;

def get_distance_metres(aLocation1, aLocation2):

    dlat = aLocation2.lat - aLocation1.lat
    dlong = aLocation2.lon - aLocation1.lon
    return math.sqrt((dlat*dlat) + (dlong*dlong)) * 1.113195e5

while True:
    _,image=cap.read()
    res,,=detector.detectAndDecode(image)
    if res:
       print(res)
       if res==Qrpass:
           #takeoff
            arm_takeoff(10)

            point1 = LocationGlobalRelative(getLoc.latitude, getLoc.longitude,20)
            vehicle.simple_goto(point1)
            print("Going to target location")
            time.sleep(60)

       elif res==Qrpass1:
            print("Mission Accomplished. Returning to launch")
            vehicle.mode=VehicleMode('RTL')
            time.sleep(10)
            vehicle.close()
            cv2.destroyAllWindows()
            
    cv2.imshow('Video',image)
    cv2.waitKey(1)
