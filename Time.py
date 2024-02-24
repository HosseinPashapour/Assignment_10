class Time :

    def __init__ ( self , sec , min , h ) :
        
        #properties
        self.seconds = sec
        self.minuts = min
        self.hour = h 

    #methods
    def hour_to_second(self):
        #convert second to hour for example 1 h => 3600 s
        ...

    def minute_to_second(self):
        #convert minutes to seconds for example 60 m => 1 h
        ...
    
    def second_to_hour(self):
        #convert second to hour for example 3600 s => 1 h
        ...

    def H_12(self):
        #convert time to 12 hours for example 14:00:00 => 2pm
        ...
    
    def H_2(self):
        #convert time to 24 hours for example 2pm => 14:00:00
        ...

    def show_time(self):
        # for using A.M. and P.M
        ...
        
    def time_difference(self): 
        #between two regions
        ...