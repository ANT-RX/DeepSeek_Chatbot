# Creamos una clase de tipo chat

class chat:
    """
    Clase de tipo chat con el que vamos a realizar las consultas.
    chat(client, system_prompt, user_prompt, max_tok)
    """
    def __init__(self, client, system_prompt: str, user_prompt: str, max_tok: int):
        self.client = client
        self.system_prompt = system_prompt
        self.user_prompt = user_prompt
        self.max_tok = max_tok

    def answer(self):
        response = self.client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": self.user_prompt},
            ],
            stream=False,
            max_tokens=self.max_tok
        )
        return response.choices[0].message.content
    