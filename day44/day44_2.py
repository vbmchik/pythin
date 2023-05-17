class Time():
    
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour  #0-23
        self.minute=minute #0-59
        self.second=second #0-59
        
    @property
    def hour(self):
        return self._hour
        
    @hour.setter
    def hour(self, hour):
        if not 0<=hour<24:
            raise ValueError(f'Hour {hour} must be in 0-23')
        self._hour = hour
        
    @property
    def minute(self):
        return self._minute

    @minute.setter
    def minute(self, minute):
        if not 0 <= minute < 60:
            raise ValueError(f'Minute {minute} must be in 0-59')
        self._minute = minute
        
    @property
    def second(self):
        return self._second
    
    @second.setter
    def second(self, second):
        if not 0 <= second < 60:
            raise ValueError(f'Second {second} must be in 0-59')
        self._second = second
        
    def set_time(self, hour=0, minute=0, second=0):
        self.hour = hour  # 0-23
        self.minute = minute  # 0-59
        self.second = second  # 0-59
        
    def __repr__(self):
        return f"Time(hour={self.hour}, minute={self.minute}, second={self.second})"
    
    def __str__(self) -> str:
        return ( ( '12' if self.hour in (0,12) else str(self.hour%12)) +
                f":{self.minute:0>2}:{self.second:0>2}" +
                ( ' AM' if self.hour < 12 else ' PM' ) )
            
wake = Time(0,2,3)
print(str(wake))

