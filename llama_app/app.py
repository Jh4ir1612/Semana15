from flask import Flask, render_template, request, jsonify
from transformers import AutoTokenizer, AutoModelForCausalLM
from dotenv import load_dotenv
import torch
import os

app = Flask(__name__)
load_dotenv()  # ✅ Cargar variables del archivo .env

# ID del modelo de Hugging Face
model_id = "meta-llama/Meta-Llama-3-8B-Instruct"

# Cargar tokenizer y modelo con token de Hugging Face
token = os.getenv("HF_TOKEN")
tokenizer = AutoTokenizer.from_pretrained(model_id, token=token)
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto", torch_dtype=torch.float16, token=token)

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

@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.get_json()
        prompt = data['prompt']
        
        output = pipeline(prompt, max_new_tokens=200, temperature=0.7, do_sample=True)[0]['generated_text'] # type: ignore
        
        return jsonify({'response': output})
    except Exception as e:
        import traceback
        traceback.print_exc()  # Para ver el error en consola
        return jsonify({'error': str(e)}), 500