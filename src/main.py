#1) Load KNN Model into a variable
#2) Create controller variable, and have the controller connect with the RC Car
#	(ex.)
#	controller = ... [class constructor created in controller.py]
#	controller.connect()
#3) Create NeuroCrown capture variable and have it stream the input from the headset
#	(ex.)
#	EEG = ... [constructor of Capture class created in Realtime_Capture]
#	EEG.startStream()
#4) While loop with flag
#	5) Run EEG's data through KNN Model. KNN Model returns an id for an action. Send action to controller class.
#
#6) If flag is updated, stop loop and end all processes
#	(ex.)
#	controller.close()
#	EEG.stopStream()
