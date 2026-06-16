product = input("Enter Product Name: ")
platform = input("Enter Platform: ")
tone = input("Enter Tone: ")

prompt = f"""
You are an expert marketing copywriter.

Product Name: {product}
Platform: {platform}
Tone: {tone}

Generate a marketing advertisement suitable for the selected platform and tone.

Platform Rules:
- Instagram: short, catchy, hashtags
- LinkedIn: professional
- Email: include subject line

Output only the advertisement.
"""

print(prompt)