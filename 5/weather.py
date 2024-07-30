import random

def generate_weather_data():
    start_date = 10  #July 10
    end_date = 32    #August 1 is day 32)
    
    weather_data = []

    for day in range(start_date, end_date + 1):
        # Create date
        if day <= 31:
            date = f"2024-07-{day:02}"  # July dates
        else:
            date = f"2024-08-0{day - 31}"  # August dates
        
        # Generate random weather data
        max_temp = round(random.uniform(20, 35), 1)  # Max temperature between 20°C and 35°C
        min_temp = round(random.uniform(10, 20), 1)  # Min temperature between 10°C and 20°C
        humidity = round(random.uniform(50, 100), 1)  # Humidity between 50% and 100%
        
        weather_data.append({
            'Date': date,
            'MaxTemp': max_temp,
            'MinTemp': min_temp,
            'Humidity': humidity
        })

    return weather_data

def find_extreme_temperatures(weather_data):
    highest_temp = max(weather_data, key=lambda x: x['MaxTemp'])
    lowest_temp = min(weather_data, key=lambda x: x['MinTemp'])
    return highest_temp, lowest_temp

def count_days_above_30(weather_data):
    count = sum(1 for day in weather_data if day['MaxTemp'] > 30)
    return count

def average_humidity(weather_data):
    total_humidity = sum(day['Humidity'] for day in weather_data)
    average = total_humidity / len(weather_data)
    return round(average, 2)

weather_data = generate_weather_data()

highest_temp, lowest_temp = find_extreme_temperatures(weather_data)
print(f"Highest Temperature: {highest_temp}")
print(f"Lowest Temperature: {lowest_temp}")

days_above_30 = count_days_above_30(weather_data)
print(f"Number of days with temperatures above 30°C: {days_above_30}")

avg_humidity = average_humidity(weather_data)
print(f"Average Humidity: {avg_humidity}%")
