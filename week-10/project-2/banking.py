import zenith

class RetailBanking(zenith.Zenith):
  
  
    def unique_services(self):
      return ["Retirement and education accounts", 
              "Loans and mortgages",
              "Checking and saving"]

class CommercialBanking(zenith.Zenith):
    def unique_services(self):
      return ["Advisory services"]
    
class GlobalBanking(zenith.Zenith):   
    def unique_services(self):
      return [
            "Multi-currency management services and products",
            "Foreign currency accounts",
            "Foreign currency credit cards",
            "Transborder advisory services",
            "Liquidity management"
        ]