

def calc_monthly_funds(intern_salary, allowance):
    return intern_salary + allowance

def calc_yearly_funds(monthly_funds):
    return monthly_funds * 12

def main():
    monthly_funds = calc_monthly_funds(1000, 250)
    yearly_funds = calc_yearly_funds(monthly_funds)

if __name__ == "__main__":
    main()