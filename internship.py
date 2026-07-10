from google import genai

client = genai.Client(api_key="AQ.Ab8RN6LE-aJFbT16HNuHo6lUJ76CdNqrBY4FonnjsL6EdKezRA")

for model in client.models.list():
    print(model.name)