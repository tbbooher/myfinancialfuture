class Year:
    "store and calculate data for a given Year"
    import datetime
    
    def __init__(self, initial_salary, year_value = datetime.date.today().year):
        #self.contents = contents or []
        salary = initial_salary
#     @property
#     def year_value(self)

    def salary(self):
        """this property is the total salary for the year"""
        pass

    def federal_income_tax(self):
        """calculate value of federal income tax for the year"""
        return salary*0.3
       

#     def state_income_tax

#     def real_estate_taxes

#     @property 
#     def income(self): ...
