product_name = input("Enter Product Name: ")
platform = input("Enter Platform (Instagram/LinkedIn/Email): ")
tone = input("Enter Tone (Professional/Friendly/Funny): ")

print("\n===== GENERATED MARKETING COPY =====\n")

if platform.lower() == "instagram":
    print(f"✨ Introducing {product_name}! ✨")
    print(f"Experience innovation like never before. Perfect for your lifestyle. #Trending #Innovation")

elif platform.lower() == "linkedin":
    print(f"We are excited to introduce {product_name}.")
    print(f"A professional solution designed to improve productivity and efficiency.")

elif platform.lower() == "email":
    print(f"Subject: Introducing {product_name}")
    print(f"Discover the benefits of {product_name} and elevate your experience today.")

else:
    print(f"{product_name} is now available!")

print(f"\nTone Applied: {tone}")