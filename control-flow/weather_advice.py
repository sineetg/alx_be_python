weather_prompt  = input("What's the weather like today? (sunny/rainy/cold): ")


if weather_prompt == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather_prompt == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather_prompt == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")