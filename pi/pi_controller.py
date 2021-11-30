import math
import requests
import argparse


#Write you own function that moves the dron from one place to another 
#the function returns the drone's current location while moving
#====================================================================================================
def your_function(current, destination):
    #print(current)

    if (destination[0] - current[0]) > 0:
        default_long = 1/10000
    else: 
        default_long = -1/10000

    if (destination[1] - current[1]) > 0:
        default_la = 1/10000
    else: 
        default_la = -1/10000

    #print(default_la, default_long)

 
    longitude = float(current[0] + default_long)
    latitude = float(current[1] + default_la)
    
    if abs(longitude - destination[0]) < 1/1000:
        longitude = destination[0]
        
    if abs(latitude - destination[1]) < 1/1000:
        latitude = destination[1]
    
    print(longitude, latitude)
    
  
   # longitude = destination[0]
    #latitude = destination[1]

    return (longitude, latitude)
#====================================================================================================


#(13.21003993027314, 55.71115995) current
#(13.18293993027314, 55.71775995) from
#(13.1876027, 55.7058176)         to


def run(current_coords, from_coords, to_coords, SERVER_URL):
    # Compmelete the while loop:
    # 1. Change the loop condition so that it stops sending location to the data base when the drone arrives the to_address
    # 2. Plan a path with your own function, so that the drone moves from [current_address] to [from_address], and the from [from_address] to [to_address]. 
    # 3. While moving, the drone keeps sending it's location to the database.
    #====================================================================================================
    drone_coords = current_coords
    while drone_coords != from_coords:
        drone_coords = your_function(drone_coords, from_coords)
        with requests.Session() as session:
            drone_location = {'longitude': drone_coords[0],
                              'latitude': drone_coords[1]
                        }
            resp = session.post(SERVER_URL, json=drone_location)


    while drone_coords != to_coords:
            drone_coords = your_function(drone_coords, to_coords)
            with requests.Session() as session:
                drone_location = {'longitude': drone_coords[0],
                                'latitude': drone_coords[1]
                            }
                resp = session.post(SERVER_URL, json=drone_location)
  #====================================================================================================

   
if __name__ == "__main__":
    SERVER_URL = "http://127.0.0.1:5001/drone"

    parser = argparse.ArgumentParser()
    parser.add_argument("--clong", help='current longitude of drone location' ,type=float)
    parser.add_argument("--clat", help='current latitude of drone location',type=float)
    parser.add_argument("--flong", help='longitude of input [from address]',type=float)
    parser.add_argument("--flat", help='latitude of input [from address]' ,type=float)
    parser.add_argument("--tlong", help ='longitude of input [to address]' ,type=float)
    parser.add_argument("--tlat", help ='latitude of input [to address]' ,type=float)
    args = parser.parse_args()

    current_coords = (args.clong, args.clat)
    from_coords = (args.flong, args.flat)
    to_coords = (args.tlong, args.tlat)

    print(current_coords)
    print(from_coords)
    print(to_coords)

    run(current_coords, from_coords, to_coords, SERVER_URL)

