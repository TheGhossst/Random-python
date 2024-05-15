def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def dayOfProgrammer(year):
    if isLeapYear(year):
        feb_days = 29
    else:
        feb_days = 28
        
    if year > 1918:
        days_before_256th = 31 + feb_days + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30
        day = (256 - days_before_256th) % 30 + 1
        return f"{day}.09.{year}"
    
    elif year < 1918:
        days_before_256th = 31 + feb_days + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30
        day = (256 - days_before_256th) % 30 + 1
        return f"{day}.09.{year}"
    
    else:
        days_before_256th = 31 + 15 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30
        day = (256 - days_before_256th) % 30 + 1
        return f"{day}.09.{year}"


if __name__ == '__main__':
    year = int(input().strip())
    print(isLeapYear(1800))
    result = dayOfProgrammer(year)
    print(result)