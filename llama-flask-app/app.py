from flask import Flask, render_template, request, jsonify
from transformers import AutoTokenizer, AutoModelForCausalLM
from dotenv import load_dotenv
import torch
import os

app = Flask(__name__)
load_dotenv()

model_id = "meta-llama/Llama-3.2-1B"  # Modelo público y ligero

token = os.getenv("HF_TOKEN")
tokenizer = AutoTokenizer.from_pretrained(model_id, use_fast=False, token=token)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="cpu",
    torch_dtype=torch.float32,  # Cambiado a float32 para CPU
    token=token,
    low_cpu_mem_usage=True  # Opcional para ahorrar RAM
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    prompt = request.json.get("prompt", "")
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(**inputs, max_new_tokens=200)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)