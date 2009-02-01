require "date"

class FinancialYear

  attr :salary, true
  attr :year, true

  def initialize(salar, year=Date.today.year, state_of_residence = "VA")
    @year = year
    @salary = salary
    @state_of_residence = state_of_residence
  end

  def increase_salary(increase_percentage)
    @salary *= 1+increase_percentage.to_f/100
  end

  def federal_income_tax
    puts "this will be x% of #{@salary}"
  end
end
