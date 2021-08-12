
def converter(temp,unit,unit1):
    if unit=="Celsius" and unit1=="Fahrenheit":
        conv_ans=temp*(9 / 5) + 32
        return conv_ans
    elif unit=="Fahrenheit" and unit1=="Celsius":
        conv_ans=(temp - 32.0) * 5.0 / 9.0
        return conv_ans

    #elif unit == unit1:
     #   return temp
    elif unit=="Celsius" and unit1=="Kelvin":
        conv_ans = (temp + 273.15)
        return conv_ans
    elif unit=="Kelvin" and unit1=="Celsius":
        conv_ans = (temp - 273.15)
        return conv_ans
    elif unit=="Kelvin" and unit1=="Fahrenheit":
        conv_ans = (temp * 1.8 - 459.7)
        return conv_ans
    elif unit=="Fahrenheit" and unit1=="Kelvin":
        conv_ans  = ((temp - 32) / 1.8 + 273)
        return conv_ans
    else:
        pass