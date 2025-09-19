from groq import Groq

class GroqEvaluator:
    def __init__(self, api_key: str):
        self.client = Groq(api_key=api_key)

    def evaluate(self, input_text: str, expected_output: str, actual_output: str) -> float:
        completion = self.client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an AI output relevancy checker. "
                        "You will receive the input, expected output, and actual output. "
                        "You must return a relevancy score between 0.0 and 1.0. "
                        "Return only the score, no extra text."
                    ),
                },
                {
                    "role": "user",
                    "content": f"""
                    1. Input: {input_text}
                    2. Expected output: {expected_output}
                    3. Actual output: {actual_output}
                    """,
                },
            ],
        )

        return float(completion.choices[0].message.content.strip())
