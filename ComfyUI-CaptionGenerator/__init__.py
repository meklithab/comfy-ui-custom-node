from transformers import BlipProcessor, BlipForConditionalGeneration
import torch
from PIL import Image
import numpy as np

class CaptionGenerator:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",)
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Caption",)
    FUNCTION = "generate_caption"
    CATEGORY = "image/captioning"

    def generate_caption(self, image):
        try:
           
            image = image[0]
            
            # Convert to proper format for BLIP
            image_np = (image.cpu().numpy() * 255).astype(np.uint8)
            pil_image = Image.fromarray(image_np)
            
           
            processor = BlipProcessor.from_pretrained('Salesforce/blip-image-captioning-base')
            model = BlipForConditionalGeneration.from_pretrained('Salesforce/blip-image-captioning-base')
            
            device = "cuda" if torch.cuda.is_available() else "cpu"
            model.to(device)
            
          
            inputs = processor(images=pil_image, return_tensors="pt").to(device)
            output = model.generate(**inputs, max_length=50)
            caption = processor.decode(output[0], skip_special_tokens=True)
            
            return (caption,)
            
        except Exception as e:
            return (f"Error: {str(e)}",)

NODE_CLASS_MAPPINGS = {
    "CaptionGenerator": CaptionGenerator
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CaptionGenerator": "Custom Caption Generator"
}