from llama_cpp import Llama

llm = Llama(
    model_path="/Users/altaf/Projects/LLM/Llama/llama-2-7b-ggml/llama-2-7b.ggmlv3.q4_0.bin",
    verbose=True
)

response = llm("When was the moon landing?")

print(response['choices'][0]["text"])