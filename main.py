from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import base64
import os
from typing import Optional

app = FastAPI(title="Gemini Image Generation API", version="1.0.0")

# Initialize Gemini client
# You should set this as an environment variable for security
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyA_MUCNRq0kBWuXmbMN3IfQhtCFZ0JCZUk")
client = genai.Client(api_key=GEMINI_API_KEY)

class ImageGenerationRequest(BaseModel):
    prompt: str
    return_base64: Optional[bool] = False

class ImageGenerationResponse(BaseModel):
    text_response: Optional[str] = None
    image_base64: Optional[str] = None
    message: str

@app.get("/")
async def root():
    return {"message": "Gemini Image Generation API is running!"}

@app.post("/generate-image", response_model=ImageGenerationResponse)
async def generate_image(request: ImageGenerationRequest):
    try:
        # Generate content using Gemini
        response = client.models.generate_content(
            model="gemini-2.0-flash-preview-image-generation",
            contents=request.prompt,
            config=types.GenerateContentConfig(
                response_modalities=['TEXT', 'IMAGE']
            )
        )
        
        text_response = None
        image_base64 = None
        
        # Process the response
        for part in response.candidates[0].content.parts:
            if part.text is not None:
                text_response = part.text
            elif part.inline_data is not None:
                # Convert image data to PIL Image
                image = Image.open(BytesIO(part.inline_data.data))
                
                if request.return_base64:
                    # Convert to base64 if requested
                    buffer = BytesIO()
                    image.save(buffer, format='PNG')
                    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
                else:
                    # Save image to file
                    image.save('generated_image.png')
        
        return ImageGenerationResponse(
            text_response=text_response,
            image_base64=image_base64,
            message="Image generated successfully!"
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating image: {str(e)}")

@app.get("/generate-image-stream/{prompt}")
async def generate_image_stream(prompt: str):
    """
    Generate image and return it as a streaming response
    """
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash-preview-image-generation",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_modalities=['TEXT', 'IMAGE']
            )
        )
        
        # Find the image in the response
        for part in response.candidates[0].content.parts:
            if part.inline_data is not None:
                image_data = part.inline_data.data
                return StreamingResponse(
                    BytesIO(image_data),
                    media_type="image/png",
                    headers={"Content-Disposition": "inline; filename=generated_image.png"}
                )
        
        raise HTTPException(status_code=404, detail="No image found in response")
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating image: {str(e)}")

@app.post("/generate-image-file")
async def generate_image_file(request: ImageGenerationRequest):
    """
    Generate image and return it as a file download
    """
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash-preview-image-generation",
            contents=request.prompt,
            config=types.GenerateContentConfig(
                response_modalities=['TEXT', 'IMAGE']
            )
        )
        
        # Find the image in the response
        for part in response.candidates[0].content.parts:
            if part.inline_data is not None:
                image_data = part.inline_data.data
                return StreamingResponse(
                    BytesIO(image_data),
                    media_type="image/png",
                    headers={"Content-Disposition": "attachment; filename=generated_image.png"}
                )
        
        raise HTTPException(status_code=404, detail="No image found in response")
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating image: {str(e)}")

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)