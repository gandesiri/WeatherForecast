import requests
def get_weather_data():
    city = input("Enter the name of the city (e.g., London): ")
    url = f"https://samples.openweathermap.org/data/2.5/forecast/hourly?q={city}&appid=b6907d289e10d714a6e88b30761fae22"

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch weather data.")
        return None


def get_weather_for_date(weather_data, target_date):
    for entry in weather_data['list']:
        if entry['dt_txt'].startswith(target_date):
            return entry['main']['temp']
    return None


def get_wind_speed_for_date(weather_data, target_date):
    for entry in weather_data['list']:
        if entry['dt_txt'].startswith(target_date):
            return entry['wind']['speed']
    return None


def get_pressure_for_date(weather_data, target_date):
    for entry in weather_data['list']:
        if entry['dt_txt'].startswith(target_date):
            return entry['main']['pressure']
    return None


def main():
    weather_data = get_weather_data()

    if not weather_data:
        return

    while True:
        print("\nChoose an option:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice (0-3): ")

        if choice == '1':
            date = input("Enter the date in the format 'YYYY-MM-DD': ")
            temperature = get_weather_for_date(weather_data, date)
            if temperature is not None:
                print(f"The temperature on {date} is {temperature}°K.")
            else:
                print("No weather data available for the specified date.")

        elif choice == '2':
            date = input("Enter the date in the format 'YYYY-MM-DD': ")
            wind_speed = get_wind_speed_for_date(weather_data, date)
            if wind_speed is not None:
                print(f"The wind speed on {date} is {wind_speed} m/s.")
            else:
                print("No wind speed data available for the specified date.")

        elif choice == '3':
            date = input("Enter the date in the format 'YYYY-MM-DD': ")
            pressure = get_pressure_for_date(weather_data, date)
            if pressure is not None:
                print(f"The pressure on {date} is {pressure} hPa.")
            else:
                print("No pressure data available for the specified date.")

        elif choice == '0':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()