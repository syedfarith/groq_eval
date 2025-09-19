from groq_eval import GroqEvaluator

API_KEY = ""

evaluator = GroqEvaluator(api_key=API_KEY)

score = evaluator.evaluate(
    input_text="capital of france",
    expected_output="paris",
    actual_output="The capital of France is Paris."
)

print("Relevance Score:", score)
