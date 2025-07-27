from dotenv import load_dotenv
import os
load_dotenv()
from langchain_core.runnables import Runnable
from huggingface_hub import InferenceClient


class HFBBLLM(Runnable):
    def __init__(self, model_id, temperature=0.3):
        token = os.getenv("HUGGINGFACEHUB_API_TOKEN") 
        if not token:
            raise ValueError("HUGGINGFACEHUB_API_TOKEN not found in environment variables.")
        self.model_id = model_id
        self.client = InferenceClient(token=token)
        self.temperature = temperature

    @property
    def _llm_type(self):
        return "huggingface_chat"

    def _call(self, prompt, **kwargs):
    
        if not isinstance(prompt.text, str):
            raise ValueError("Input to _call must be a prompt string.")
            

        # Format messages for chat model
        messages = [
            {"role": "system", "content": "You are a concise AI assistant. Answer strictly from the provided context.Do not invent answers or create new questions or unnecessarily expand content."},
            {"role": "user", "content": prompt.text}
        ]


        # Call Hugging Face chat model
        response = self.client.chat.completions.create(
            model=self.model_id,
            messages=messages,
            temperature=self.temperature,
            **kwargs
        )

        return response.choices[0].message["content"]

    def invoke(self, input, config=None, **kwargs):
        return self._call(input, **kwargs)