# class CLLocation
#  	func distanceFromLocation(_ location:CLLocation) -> Double


# class CLLocationManager (can treat it as singleton)
#  	func startUpdatingLocation()
# 	 func stopUpdatingLocation()


# protocol CLLocationManagerDelegate
#  	func locationManager(_ locationManager: CLLocationManager, 
# didUpdate toLocation:CLLocation, 
# fromLocation:CLLocation)

# class MKMapView
# 	 func addLocation(_ location:CLLocation) 

FROM_LOCATION = None

class Button:

	BUTTON_STATE = 0

	def buttonPressed():
		if BUTTON_STATE == 0:
			CLLocationManager.startUpdatingLocation()
			BUTTON_STATE = 1
			FROM_LOCATION = None
		else:
			CLLocationManager.stopUpdatingLocation()
			BUTTON_STATE = 0

class TextView:

class ViewController: CLLocationManagerDelegate

	TOTAL_DISTANCE = 0

	def __init__(self):
		mapView = MKMapView()
		textView = textView()
		button = Button()

	def didUpdate(toLocation, fromLocation):
		if FROM_LOCATION:
			TOTAL_DISTANCE += fromLocation.distanceFromLocation(toLocation)
			self.textView.label = TOTAL_DISTANCE
			self.mapView.addLocation(toLocation)

		FROM_LOCATION = fromLocation
			
		

CLLocationManagerDelegate: