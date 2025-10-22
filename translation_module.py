# translation_module.py
import torch
from transformers import MarianMTModel, MarianTokenizer

# Local Nepali -> English model folder
NE_MODEL_PATH = r"C:/Users/Cabc4/Desktop/translation module/models/nep-en"

def load_nepal_translation_model():
    """
    Loads the local Nepali -> English model.
    """
    # Load tokenizer
    tokenizer = MarianTokenizer.from_pretrained(NE_MODEL_PATH)
    
    # Load PyTorch model
    model = MarianMTModel.from_pretrained(NE_MODEL_PATH)
    model.eval()
    
    return tokenizer, model

def translate_text(text, lang_code):
    """
    Translate text based on selected language.
    """
    if lang_code == "ne":  # Nepali
        tokenizer, model = load_nepal_translation_model()
        inputs = tokenizer(text, return_tensors="pt", padding=True)
        with torch.no_grad():
            translated = model.generate(**inputs)
        translated_text = tokenizer.batch_decode(translated, skip_special_tokens=True)[0]
        return translated_text
    
    elif lang_code == "si":  # Sinhalese
        return "Translation not available for Sinhalese yet."
    
    else:
        return text
