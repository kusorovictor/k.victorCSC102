class delivery_service:
  
  def __init__(self, location, weight):
    self.location = location
    self.weight = weight
    self.cost = 0
    
  #calculate cost for pau based on weight
  def pau_calculate_cost(self):
    if self.weight >= 10:
      self.cost = 2000
    else:  
      self.cost = 1500
    
  #calculate cost for epe based on weight 
  def epe_calculate_cost(self):
    if self.weight >= 10:
      self.cost = 5000
    else:  
      self.cost = 4000   