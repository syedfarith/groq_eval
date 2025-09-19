

# groq-eval-score

A Python package to evaluate the **relevance** of LLM outputs using the Groq API.  
It compares input, expected output, and actual output, returning a **score between 0.0 and 1.0**.

## Installation

pip install groq-eval-score


## Usage


from groq_eval import GroqEvaluator

# Initialize evaluator
evaluator = GroqEvaluator(api_key="YOUR_API_KEY")

# Evaluate relevance
score = evaluator.evaluate(
    input_text="capital of france",
    expected_output="paris",
    actual_output="The capital of France is Paris."
)

print("Relevance Score:", score)  # Example: 1.0

## Features

* Returns a **relevance score** between 0.0 and 1.0
* Easy class-based interface
* Uses Groq API for fast and efficient evaluation

