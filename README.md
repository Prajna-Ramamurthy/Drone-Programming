# Drone Progrmming Project - Emergency Kits Delivering Drone

The Emergency Kit Delivering Drone can be used to deliver standardized kits of food and medical supplies, in emergencies like natural calamities, man-made disasters or times of war. During such times, until the victims can be rescued, it is essntial to make sure that they receive food and medicines. But there are situations where it is near impossible to reach the disaster affected ares. THe drones can go to places where no vehicle or human can reach. They can endure extreme conditions of temperature and pressure, or high altitudes. They can be sent to extremely dangerous war zones without wrrying about the risk of lives. The drones can also be used to deliver classified messages during war.

Solution Flowchart
1. Generation of QR Code - Conversion of commands from string to QR code
2. Location Calculation - Calculation of Latitude and Longitude from address
3. Takeoff - After scanning the Takeoff QR code
4. Mission - Going to the target location
5. Return to Launch - After scanning the Landing QR code

The user (who is sending the emergency kits) can enter the address of the drop-sites. The program will calculate the location in terms of latitudes and longitudes. 
The user must show the secret message QR code to the drone and only then the drone will take off. This will give the user enough time to load the emergency kit onto the drone. Finally, after reaching its final location, the drone will drop the package and return to launch position, after scanning the Landing QR Code. This process ensures the proper functioning of the drone.
The user should enter a secret code which will be converted to a QR code. This should be sent to the receiver. When the drone scans this QR code, only then it will drop the package. This feature is extremely helpful in delivering secret messages during times of war. 
