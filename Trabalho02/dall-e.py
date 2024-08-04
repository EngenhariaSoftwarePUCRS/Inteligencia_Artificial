from openai import OpenAI


# Generated at https://platform.openai.com/account/api-keys
API_KEY = 'sk-proj-or-something'


try:
    client = OpenAI(api_key=API_KEY)
    images = client.images.generate(
        prompt='Mônica arremessando o Sansão no Cebolinha'
    )
    print(images)
except Exception as e:
    print(f'Erro: {e}')
