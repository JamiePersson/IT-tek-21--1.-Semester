class DCMotor:      
  def __init__(self, D2_STBY, D2_PHA_A, D2_EN_A, min_duty=750, max_duty=1023):
        self.D2_STBY = D2_STBY
        self.D2_PHA_A = D2_PHA_A
        self.D2_EN_A = D2_EN_A
        self.min_duty = min_duty
        self.max_duty = max_duty

  def forward(self,speed):
    self.speed = speed
    self.D2_EN_A.duty(self.duty_cycle(self.speed))
    self.D2_STBY.value(0)
    self.D2_PHA_A.value(1)
    
  def backwards(self, speed):
        self.speed = speed
        self.D2_EN_A.duty(self.duty_cycle(self.speed))
        self.D2_STBY.value(1)
        self.D2_PHA_A.value(0)

  def stop(self):
    self.D2_EN_A.duty(0)
    self.D2_STBY.value(0)
    self.D2_PHA_A.value(0)
    
  def duty_cycle(self, speed):
   if self.speed <= 0 or self.speed > 100:
        duty_cycle = 0
   else:
    duty_cycle = int(self.min_duty + (self.max_duty - self.min_duty)*((self.speed-1)/(100-1)))
    return duty_cycle
