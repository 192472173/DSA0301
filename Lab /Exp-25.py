from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

prompt = input("Enter prompt: ")

response = client.responses.create(
    model="gpt-3.5-turbo-instruct",
    input=prompt
)

print(response.output_text)
