# # # from fastapi import FastAPI, HTTPException
# # # from fastapi.responses import StreamingResponse
# # # from pydantic import BaseModel
# # # from google import genai
# # # from google.genai import types
# # # from PIL import Image
# # # from io import BytesIO
# # # import base64
# # # import os
# # # from typing import Optional

# # # app = FastAPI(title="Gemini Image Generation API", version="1.0.0")

# # # # Initialize Gemini client
# # # # You should set this as an environment variable for security
# # # GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyA_MUCNRq0kBWuXmbMN3IfQhtCFZ0JCZUk")
# # # client = genai.Client(api_key=GEMINI_API_KEY)

# # # class ImageGenerationRequest(BaseModel):
# # #     prompt: str
# # #     return_base64: Optional[bool] = False

# # # class ImageGenerationResponse(BaseModel):
# # #     text_response: Optional[str] = None
# # #     image_base64: Optional[str] = None
# # #     message: str

# # # @app.get("/")
# # # async def root():
# # #     return {"message": "Gemini Image Generation API is running!"}

# # # @app.post("/generate-image", response_model=ImageGenerationResponse)
# # # async def generate_image(request: ImageGenerationRequest):
# # #     try:
# # #         # Generate content using Gemini
# # #         response = client.models.generate_content(
# # #             model="gemini-2.0-flash-preview-image-generation",
# # #             contents=request.prompt,
# # #             config=types.GenerateContentConfig(
# # #                 response_modalities=['TEXT', 'IMAGE']
# # #             )
# # #         )
        
# # #         text_response = None
# # #         image_base64 = None
        
# # #         # Process the response
# # #         for part in response.candidates[0].content.parts:
# # #             if part.text is not None:
# # #                 text_response = part.text
# # #             elif part.inline_data is not None:
# # #                 # Convert image data to PIL Image
# # #                 image = Image.open(BytesIO(part.inline_data.data))
                
# # #                 if request.return_base64:
# # #                     # Convert to base64 if requested
# # #                     buffer = BytesIO()
# # #                     image.save(buffer, format='PNG')
# # #                     image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
# # #                 else:
# # #                     # Save image to file
# # #                     image.save('generated_image.png')
        
# # #         return ImageGenerationResponse(
# # #             text_response=text_response,
# # #             image_base64=image_base64,
# # #             message="Image generated successfully!"
# # #         )
        
# # #     except Exception as e:
# # #         raise HTTPException(status_code=500, detail=f"Error generating image: {str(e)}")

# # # @app.get("/generate-image-stream/{prompt}")
# # # async def generate_image_stream(prompt: str):
# # #     """
# # #     Generate image and return it as a streaming response
# # #     """
# # #     try:
# # #         response = client.models.generate_content(
# # #             model="gemini-2.0-flash-preview-image-generation",
# # #             contents=prompt,
# # #             config=types.GenerateContentConfig(
# # #                 response_modalities=['TEXT', 'IMAGE']
# # #             )
# # #         )
        
# # #         # Find the image in the response
# # #         for part in response.candidates[0].content.parts:
# # #             if part.inline_data is not None:
# # #                 image_data = part.inline_data.data
# # #                 return StreamingResponse(
# # #                     BytesIO(image_data),
# # #                     media_type="image/png",
# # #                     headers={"Content-Disposition": "inline; filename=generated_image.png"}
# # #                 )
        
# # #         raise HTTPException(status_code=404, detail="No image found in response")
        
# # #     except Exception as e:
# # #         raise HTTPException(status_code=500, detail=f"Error generating image: {str(e)}")

# # # @app.post("/generate-image-file")
# # # async def generate_image_file(request: ImageGenerationRequest):
# # #     """
# # #     Generate image and return it as a file download
# # #     """
# # #     prompt_static = "A realistic photo for topic:"
# # #     try:
# # #         response = client.models.generate_content(
# # #             model="gemini-2.0-flash-preview-image-generation",
# # #             contents=prompt_static + request.prompt,
# # #             config=types.GenerateContentConfig(
# # #                 response_modalities=['TEXT', 'IMAGE']
# # #             )
# # #         )
        
# # #         # Find the image in the response
# # #         for part in response.candidates[0].content.parts:
# # #             if part.inline_data is not None:
# # #                 image_data = part.inline_data.data
# # #                 return StreamingResponse(
# # #                     BytesIO(image_data),
# # #                     media_type="image/png",
# # #                     headers={"Content-Disposition": "attachment; filename=generated_image.png"}
# # #                 )
        
# # #         raise HTTPException(status_code=404, detail="No image found in response")
        
# # #     except Exception as e:
# # #         raise HTTPException(status_code=500, detail=f"Error generating image: {str(e)}")

# # # # if __name__ == "__main__":
# # # #     import uvicorn
# # # #     uvicorn.run(app, host="0.0.0.0", port=8000)





# # from fastapi import FastAPI, HTTPException
# # from fastapi.responses import StreamingResponse
# # from pydantic import BaseModel
# # from google import genai
# # from google.genai import types
# # from PIL import Image
# # from io import BytesIO
# # import base64
# # import os
# # from typing import Optional

# # app = FastAPI(title="Gemini Image Generation API", version="1.0.0")

# # # Initialize Gemini client
# # # You should set this as an environment variable for security
# # GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyA_MUCNRq0kBWuXmbMN3IfQhtCFZ0JCZUk")
# # client = genai.Client(api_key=GEMINI_API_KEY)

# # class ImageGenerationRequest(BaseModel):
# #     prompt: str
# #     return_base64: Optional[bool] = False
# #     add_realistic_prefix: Optional[bool] = False  # Tùy chọn thêm prefix "realistic photo"

# # class ImageGenerationResponse(BaseModel):
# #     text_response: Optional[str] = None
# #     image_base64: Optional[str] = None
# #     message: str

# # @app.get("/")
# # async def root():
# #     return {"message": "Gemini Image Generation API is running!"}

# # @app.post("/generate-image", response_model=ImageGenerationResponse)
# # async def generate_image(request: ImageGenerationRequest):
# #     try:
# #         # Sử dụng prompt người dùng nhập vào
# #         prompt = request.prompt
# #         if request.add_realistic_prefix:
# #             prompt = f"A realistic photo for topic: {request.prompt}"
        
# #         # Generate content using Gemini
# #         response = client.models.generate_content(
# #             model="gemini-2.0-flash-preview-image-generation",
# #             contents=prompt,
# #             config=types.GenerateContentConfig(
# #                 response_modalities=['TEXT', 'IMAGE']
# #             )
# #         )
        
# #         text_response = None
# #         image_base64 = None
        
# #         # Process the response
# #         for part in response.candidates[0].content.parts:
# #             if part.text is not None:
# #                 text_response = part.text
# #             elif part.inline_data is not None:
# #                 # Convert image data to PIL Image
# #                 image = Image.open(BytesIO(part.inline_data.data))
                
# #                 if request.return_base64:
# #                     # Convert to base64 if requested
# #                     buffer = BytesIO()
# #                     image.save(buffer, format='PNG')
# #                     image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
# #                 else:
# #                     # Save image to file
# #                     image.save('generated_image.png')
        
# #         return ImageGenerationResponse(
# #             text_response=text_response,
# #             image_base64=image_base64,
# #             message="Image generated successfully!"
# #         )
        
# #     except Exception as e:
# #         raise HTTPException(status_code=500, detail=f"Error generating image: {str(e)}")

# # @app.post("/generate-image-stream")
# # async def generate_image_stream(request: ImageGenerationRequest):
# #     """
# #     Generate image from custom prompt and return it as a streaming response
# #     """
# #     try:
# #         # Sử dụng prompt người dùng nhập vào
# #         prompt = request.prompt
# #         if request.add_realistic_prefix:
# #             prompt = f"A realistic photo for topic: {request.prompt}"
            
# #         response = client.models.generate_content(
# #             model="gemini-2.0-flash-preview-image-generation",
# #             contents=prompt,
# #             config=types.GenerateContentConfig(
# #                 response_modalities=['TEXT', 'IMAGE']
# #             )
# #         )
        
# #         # Find the image in the response
# #         for part in response.candidates[0].content.parts:
# #             if part.inline_data is not None:
# #                 image_data = part.inline_data.data
# #                 return StreamingResponse(
# #                     BytesIO(image_data),
# #                     media_type="image/png",
# #                     headers={"Content-Disposition": "inline; filename=generated_image.png"}
# #                 )
        
# #         raise HTTPException(status_code=404, detail="No image found in response")
        
# #     except Exception as e:
# #         raise HTTPException(status_code=500, detail=f"Error generating image: {str(e)}")

# # @app.post("/generate-image-file")
# # async def generate_image_file(request: ImageGenerationRequest):
# #     """
# #     Generate image from custom prompt and return it as a file download
# #     """
# #     try:
# #         # Sử dụng prompt người dùng nhập vào
# #         prompt = request.prompt
# #         if request.add_realistic_prefix:
# #             prompt = f"A realistic photo for topic: {request.prompt}"
            
# #         response = client.models.generate_content(
# #             model="gemini-2.0-flash-preview-image-generation",
# #             contents=prompt,
# #             config=types.GenerateContentConfig(
# #                 response_modalities=['TEXT', 'IMAGE']
# #             )
# #         )
        
# #         # Find the image in the response
# #         for part in response.candidates[0].content.parts:
# #             if part.inline_data is not None:
# #                 image_data = part.inline_data.data
# #                 return StreamingResponse(
# #                     BytesIO(image_data),
# #                     media_type="image/png",
# #                     headers={"Content-Disposition": "attachment; filename=generated_image.png"}
# #                 )
        
# #         raise HTTPException(status_code=404, detail="No image found in response")
        
# #     except Exception as e:
# #         raise HTTPException(status_code=500, detail=f"Error generating image: {str(e)}")

# # # Endpoint GET đơn giản cho việc test nhanh (giữ lại cho compatibility)
# # @app.get("/generate-image-stream/{prompt}")
# # async def generate_image_stream_get(prompt: str):
# #     """
# #     Generate image and return it as a streaming response (GET method for quick testing)
# #     """
# #     try:
# #         response = client.models.generate_content(
# #             model="gemini-2.0-flash-preview-image-generation",
# #             contents=prompt,
# #             config=types.GenerateContentConfig(
# #                 response_modalities=['TEXT', 'IMAGE']
# #             )
# #         )
        
# #         # Find the image in the response
# #         for part in response.candidates[0].content.parts:
# #             if part.inline_data is not None:
# #                 image_data = part.inline_data.data
# #                 return StreamingResponse(
# #                     BytesIO(image_data),
# #                     media_type="image/png",
# #                     headers={"Content-Disposition": "inline; filename=generated_image.png"}
# #                 )
        
# #         raise HTTPException(status_code=404, detail="No image found in response")
        
# #     except Exception as e:
# #         raise HTTPException(status_code=500, detail=f"Error generating image: {str(e)}")

# # # if __name__ == "__main__":
# # #     import uvicorn
# # #     uvicorn.run(app, host="0.0.0.0", port=8000)



# from fastapi import FastAPI, HTTPException
# from fastapi.responses import StreamingResponse
# from pydantic import BaseModel
# from google import genai
# from google.genai import types
# from PIL import Image
# from io import BytesIO
# import base64
# import os
# import random
# from typing import Optional, List

# app = FastAPI(title="Medical Image Generation API", version="2.0.0")

# # Initialize Gemini client
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyA_MUCNRq0kBWuXmbMN3IfQhtCFZ0JCZUk")
# client = genai.Client(api_key=GEMINI_API_KEY)

# class MedicalImageRequest(BaseModel):
#     disease_name: str  # Tên bệnh
#     symptoms: Optional[str] = ""  # Triệu chứng
#     patient_age: Optional[str] = "adult"  # child, adult, elderly
#     return_base64: Optional[bool] = False

# class ImageGenerationResponse(BaseModel):
#     text_response: Optional[str] = None
#     image_base64: Optional[str] = None
#     message: str
#     generated_prompt: Optional[str] = None

# class MultiSceneResponse(BaseModel):
#     disease: str
#     symptoms: str
#     scenes: List[dict]
#     message: str

# # Template cảnh điều trị y khoa
# MEDICAL_SCENES = {
#     "consultation": [
#         "doctor examining patient with {disease}, {symptoms}, medical consultation in clinic, stethoscope examination, {age_group}, professional healthcare setting",
#         "physician discussing {disease} diagnosis, patient showing {symptoms}, hospital consultation room, medical charts, {age_group}, healthcare consultation",
#         "medical specialist evaluating {disease} symptoms including {symptoms}, clinical examination, modern medical office, {age_group}"
#     ],
    
#     "treatment": [
#         "patient with {disease} receiving medical treatment, {symptoms} being addressed, hospital treatment room, medical equipment, {age_group}, therapeutic care",
#         "medical procedure for {disease} patient, treating {symptoms}, healthcare professionals providing care, {age_group}, clinical treatment",
#         "therapeutic intervention for {disease}, managing {symptoms}, hospital setting, medical staff, {age_group}, healing process"
#     ],
    
#     "emergency": [
#         "emergency medical care for {disease} patient, acute {symptoms}, hospital emergency room, urgent treatment, {age_group}, critical care",
#         "paramedics treating {disease} emergency, patient with {symptoms}, ambulance setting, emergency medical response, {age_group}",
#         "urgent medical intervention for {disease}, severe {symptoms}, emergency department, medical team, {age_group}"
#     ],
    
#     "recovery": [
#         "patient recovering from {disease}, {symptoms} improving, rehabilitation setting, physical therapy, {age_group}, healing progress",
#         "{disease} patient in recovery phase, {symptoms} subsiding, hospital room, supportive care, {age_group}, getting better",
#         "post-treatment recovery for {disease}, managing residual {symptoms}, medical monitoring, {age_group}, wellness journey"
#     ],
    
#     "medication": [
#         "patient with {disease} taking medication, treating {symptoms}, pharmacy consultation, prescription drugs, {age_group}, pharmaceutical care",
#         "medication administration for {disease}, addressing {symptoms}, healthcare worker giving medicine, {age_group}, drug therapy",
#         "{disease} patient receiving medication, managing {symptoms}, hospital pharmacy, medical supervision, {age_group}"
#     ],
    
#     "home_care": [
#         "home healthcare for {disease} patient, managing {symptoms} at home, family support, comfortable environment, {age_group}, personalized care",
#         "patient with {disease} receiving care at home, {symptoms} monitoring, visiting nurse, domestic setting, {age_group}, home treatment",
#         "home-based care for {disease}, family helping with {symptoms}, comfortable home environment, {age_group}, supportive care"
#     ]
# }

# # Context theo độ tuổi
# AGE_CONTEXTS = {
#     "child": "pediatric patient, child healthcare, colorful children's hospital environment, gentle medical care for kids",
#     "adult": "adult patient, professional medical setting, standard healthcare environment",
#     "elderly": "elderly patient, geriatric care, senior-friendly medical environment, age-appropriate healthcare"
# }

# def create_medical_prompt(disease: str, symptoms: str, scene_type: str, age_group: str) -> str:
#     """Tạo prompt y khoa tự động"""
    
#     # Chọn template cảnh
#     if scene_type == "random":
#         scene_type = random.choice(list(MEDICAL_SCENES.keys()))
    
#     template = random.choice(MEDICAL_SCENES.get(scene_type, MEDICAL_SCENES["treatment"]))
#     age_context = AGE_CONTEXTS.get(age_group, AGE_CONTEXTS["adult"])
    
#     # Tạo prompt
#     prompt = template.format(
#         disease=disease,
#         symptoms=symptoms if symptoms else "typical symptoms",
#         age_group=age_context
#     )
    
#     # Thêm từ khóa chất lượng
#     prompt += ", professional medical photography, realistic healthcare scene, high quality medical documentation, clean hospital environment"
    
#     return prompt

# @app.get("/")
# async def root():
#     return {"message": "Medical Image Generation API - Just enter disease name and symptoms!"}

# @app.post("/generate-medical-image", response_model=ImageGenerationResponse)
# async def generate_medical_image(request: MedicalImageRequest):
#     """
#     Tạo ảnh y khoa chỉ với tên bệnh và triệu chứng
#     """
#     try:
#         # Tạo prompt tự động
#         scene_type = random.choice(list(MEDICAL_SCENES.keys()))
#         generated_prompt = create_medical_prompt(
#             disease=request.disease_name,
#             symptoms=request.symptoms,
#             scene_type=scene_type,
#             age_group=request.patient_age
#         )
        
#         # Thêm prefix realistic
#         full_prompt = f"A realistic photo for topic: {generated_prompt}"
        
#         # Generate content using Gemini
#         response = client.models.generate_content(
#             model="gemini-2.0-flash-preview-image-generation",
#             contents=full_prompt,
#             config=types.GenerateContentConfig(
#                 response_modalities=['TEXT', 'IMAGE']
#             )
#         )
        
#         # Kiểm tra response hợp lệ
#         if not response or not response.candidates or not response.candidates[0].content.parts:
#             raise HTTPException(status_code=500, detail="No valid response from Gemini API")
        
#         text_response = None
#         image_base64 = None
        
#         # Xử lý response
#         for part in response.candidates[0].content.parts:
#             if part.text is not None:
#                 text_response = part.text
#             elif part.inline_data is not None:
#                 image = Image.open(BytesIO(part.inline_data.data))
                
#                 if request.return_base64:
#                     buffer = BytesIO()
#                     image.save(buffer, format='PNG')
#                     image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
#                 else:
#                     filename = f"{request.disease_name.replace(' ', '_').lower()}.png"
#                     image.save(filename)
        
#         return ImageGenerationResponse(
#             text_response=text_response,
#             image_base64=image_base64,
#             message=f"Medical image for {request.disease_name} generated successfully!",
#             generated_prompt=generated_prompt
#         )
        
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error generating image: {str(e)}")

# @app.post("/generate-multiple-scenes", response_model=MultiSceneResponse)
# async def generate_multiple_scenes(request: MedicalImageRequest):
#     """
#     Tạo nhiều cảnh khác nhau cho cùng một bệnh
#     """
#     try:
#         scenes = []
#         scene_types = ["consultation", "treatment", "emergency", "recovery", "medication", "home_care"]
        
#         for scene in scene_types:
#             prompt = create_medical_prompt(
#                 disease=request.disease_name,
#                 symptoms=request.symptoms,
#                 scene_type=scene,
#                 age_group=request.patient_age
#             )
            
#             scenes.append({
#                 "scene_type": scene,
#                 "scene_description": scene.replace("_", " ").title(),
#                 "prompt": prompt,
#                 "api_request": {
#                     "prompt": prompt,
#                     "return_base64": request.return_base64,
#                     "add_realistic_prefix": True
#                 }
#             })
        
#         return MultiSceneResponse(
#             disease=request.disease_name,
#             symptoms=request.symptoms,
#             scenes=scenes,
#             message=f"Generated {len(scenes)} different medical scenes for {request.disease_name}"
#         )
        
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error generating multiple scenes: {str(e)}")

# @app.post("/generate-image-stream")
# async def generate_image_stream(request: MedicalImageRequest):
#     """
#     Tạo ảnh y khoa và trả về dưới dạng stream
#     """
#     try:
#         # Tạo prompt tự động
#         scene_type = random.choice(list(MEDICAL_SCENES.keys()))
#         generated_prompt = create_medical_prompt(
#             disease=request.disease_name,
#             symptoms=request.symptoms,
#             scene_type=scene_type,
#             age_group=request.patient_age
#         )
        
#         full_prompt = f"A realistic photo for topic: {generated_prompt}"
        
#         response = client.models.generate_content(
#             model="gemini-2.0-flash-preview-image-generation",
#             contents=full_prompt,
#             config=types.GenerateContentConfig(
#                 response_modalities=['TEXT', 'IMAGE']
#             )
#         )
        
#         if not response or not response.candidates or not response.candidates[0].content.parts:
#             raise HTTPException(status_code=500, detail="No valid response from API")
        
#         # Tìm ảnh trong response
#         for part in response.candidates[0].content.parts:
#             if part.inline_data is not None:
#                 image_data = part.inline_data.data
#                 filename = f"{request.disease_name.replace(' ', '_').lower()}.png"
#                 return StreamingResponse(
#                     BytesIO(image_data),
#                     media_type="image/png",
#                     headers={"Content-Disposition": f"inline; filename={filename}"}
#                 )
        
#         raise HTTPException(status_code=404, detail="No image found in response")
        
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error generating image: {str(e)}")

# @app.get("/medical-scenes")
# async def get_medical_scenes():
#     """
#     Lấy danh sách các loại cảnh y khoa có thể tạo
#     """
#     return {
#         "available_scenes": list(MEDICAL_SCENES.keys()),
#         "age_groups": list(AGE_CONTEXTS.keys()),
#         "scene_descriptions": {
#             "consultation": "Cảnh khám bệnh, tư vấn y khoa",
#             "treatment": "Cảnh điều trị, chữa bệnh",
#             "emergency": "Cảnh cấp cứu y tế",
#             "recovery": "Cảnh hồi phục, phục hồi sức khỏe",
#             "medication": "Cảnh dùng thuốc, điều trị bằng thuốc",
#             "home_care": "Cảnh chăm sóc tại nhà"
#         },
#         "usage_example": {
#             "disease_name": "tiểu đường",
#             "symptoms": "mệt mỏi, khát nước nhiều, đi tiểu thường xuyên",
#             "patient_age": "adult",
#             "return_base64": False
#         }
#     }

# @app.get("/generate-simple/{disease_name}")
# async def generate_simple_image(disease_name: str, symptoms: str = ""):
#     """
#     Endpoint đơn giản - chỉ cần tên bệnh
#     """
#     try:
#         scene_type = random.choice(list(MEDICAL_SCENES.keys()))
#         generated_prompt = create_medical_prompt(
#             disease=disease_name,
#             symptoms=symptoms,
#             scene_type=scene_type,
#             age_group="adult"
#         )
        
#         full_prompt = f"A realistic photo for topic: {generated_prompt}"
        
#         response = client.models.generate_content(
#             model="gemini-2.0-flash-preview-image-generation",
#             contents=full_prompt,
#             config=types.GenerateContentConfig(
#                 response_modalities=['TEXT', 'IMAGE']
#             )
#         )
        
#         if not response or not response.candidates or not response.candidates[0].content.parts:
#             raise HTTPException(status_code=500, detail="No valid response from API")
        
#         for part in response.candidates[0].content.parts:
#             if part.inline_data is not None:
#                 image_data = part.inline_data.data
#                 filename = f"{disease_name.replace(' ', '_').lower()}.png"
#                 return StreamingResponse(
#                     BytesIO(image_data),
#                     media_type="image/png",
#                     headers={"Content-Disposition": f"inline; filename={filename}"}
#                 )
        
#         raise HTTPException(status_code=404, detail="No image found in response")
        
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error generating image: {str(e)}")

# # if __name__ == "__main__":
# #     import uvicorn
# #     uvicorn.run(app, host="0.0.0.0", port=8000)




from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import base64
import os
import random
import time
from typing import Optional, List

app = FastAPI(title="Medical Image Generation API", version="2.0.0")

# Danh sách các API keys
API_KEYS = [
    "AIzaSyA_MUCNRq0kBWuXmbMN3IfQhtCFZ0JCZUk",  # Key gốc
    "AIzaSyBKFGzHBMktgWq7zILIm1xOaTSItQE-VmU",
    "AIzaSyCK-DCqDab3qm6Xr4gKkWzn4OzddHJ1xN8",
    "AIzaSyDDnUWW0rS_WyzxqNvRf59IGgCMULMAFjQ",
    "AIzaSyBIedfbcynLwn8g0RT-2P8Wr2BV5XeHRZI",
    "AIzaSyD_XB2o62faHH1Hw0UIFqQ_ypRQ7tTGJXw",
    "AIzaSyBebpFnXALAh8MTPTzpeG_Q_Ihg1he9PPE",
    "AIzaSyASIoVsLPcGiZ2GavqyrPWxX7N7sPZWR8k",
    "AIzaSyDaCGsny8b_ZlcYE80eT1UAx9ASUJLRKmM",
    "AIzaSyBGXooqV1aa6SZc-wQLmvG2GenYGhpIuh4",
    "AIzaSyAQyYkkPP08XjFvd62p1zDEHZzdPlpm03o",
    "AIzaSyBtsDFxfutDCLtbuUjYCZTIXhm_nomBXUc",
    "AIzaSyARutxAJiYKzwKDPzIn5THfc7AlOib0dMc",
    "AIzaSyBK4Jep3kc--b0DDBIT8nWu2AZQIyK4as8",
    "AIzaSyAR3hwUBUPEWKPkNJptMHwfCozRlFEYApI",
    "AIzaSyDNsjbn7kpWc8T6BM73XiuqHfELp8qCJb4",
    "AIzaSyCPsUUcMTAX3jDWF2J5aV6rSCQcWvDDIYU"
]

# Quản lý trạng thái API keys
class APIKeyManager:
    def __init__(self, keys: List[str]):
        self.keys = keys
        self.current_index = 0
        self.failed_keys = set()
        self.last_rotation_time = {}
        self.rotation_cooldown = 300  # 5 phút cooldown cho mỗi key
    
    def get_current_key(self) -> str:
        """Lấy API key hiện tại"""
        return self.keys[self.current_index]
    
    def get_current_client(self) -> genai.Client:
        """Tạo client với API key hiện tại"""
        return genai.Client(api_key=self.get_current_key())
    
    def rotate_key(self, reason: str = "rate_limit"):
        """Chuyển sang API key tiếp theo"""
        current_key = self.get_current_key()
        self.failed_keys.add(current_key)
        self.last_rotation_time[current_key] = time.time()
        
        print(f"🔄 Rotating API key due to: {reason}")
        print(f"❌ Failed key: ...{current_key[-10:]}")
        
        # Tìm key tiếp theo khả dụng
        original_index = self.current_index
        while True:
            self.current_index = (self.current_index + 1) % len(self.keys)
            
            # Nếu đã quay hết vòng
            if self.current_index == original_index:
                # Reset tất cả failed keys nếu đã cooldown
                self._reset_cooled_down_keys()
                if not self.failed_keys:
                    break
                # Nếu vẫn không có key nào khả dụng, chờ một chút
                print("⏳ All keys exhausted, waiting 60 seconds...")
                time.sleep(60)
                self._reset_cooled_down_keys()
                break
            
            # Nếu key này không bị failed hoặc đã hết cooldown
            current_key = self.get_current_key()
            if current_key not in self.failed_keys:
                break
        
        new_key = self.get_current_key()
        print(f"✅ Switched to new key: ...{new_key[-10:]}")
        
    def _reset_cooled_down_keys(self):
        """Reset các key đã hết thời gian cooldown"""
        current_time = time.time()
        cooled_keys = []
        
        for key in list(self.failed_keys):
            if current_time - self.last_rotation_time.get(key, 0) > self.rotation_cooldown:
                cooled_keys.append(key)
                self.failed_keys.discard(key)
        
        if cooled_keys:
            print(f"🔓 Reset {len(cooled_keys)} cooled down keys")
    
    def get_status(self) -> dict:
        """Lấy trạng thái hiện tại của key manager"""
        current_time = time.time()
        key_status = []
        
        for i, key in enumerate(self.keys):
            status = {
                "index": i,
                "key_suffix": f"...{key[-10:]}",
                "is_current": i == self.current_index,
                "is_failed": key in self.failed_keys,
                "cooldown_remaining": 0
            }
            
            if key in self.last_rotation_time:
                remaining = self.rotation_cooldown - (current_time - self.last_rotation_time[key])
                status["cooldown_remaining"] = max(0, remaining)
            
            key_status.append(status)
        
        return {
            "current_key_index": self.current_index,
            "total_keys": len(self.keys),
            "failed_keys_count": len(self.failed_keys),
            "keys_status": key_status
        }

# Khởi tạo API Key Manager
key_manager = APIKeyManager(API_KEYS)

class MedicalImageRequest(BaseModel):
    disease_name: str  # Tên bệnh
    symptoms: Optional[str] = ""  # Triệu chứng
    patient_age: Optional[str] = "adult"  # child, adult, elderly
    return_base64: Optional[bool] = False

class ImageGenerationResponse(BaseModel):
    text_response: Optional[str] = None
    image_base64: Optional[str] = None
    message: str
    generated_prompt: Optional[str] = None
    api_key_used: Optional[str] = None

class MultiSceneResponse(BaseModel):
    disease: str
    symptoms: str
    scenes: List[dict]
    message: str

# Template cảnh điều trị y khoa
MEDICAL_SCENES = {
    "consultation": [
        "doctor examining patient with {disease}, {symptoms}, medical consultation in clinic, stethoscope examination, {age_group}, professional healthcare setting",
        "physician discussing {disease} diagnosis, patient showing {symptoms}, hospital consultation room, medical charts, {age_group}, healthcare consultation",
        "medical specialist evaluating {disease} symptoms including {symptoms}, clinical examination, modern medical office, {age_group}"
    ],
    
    "treatment": [
        "patient with {disease} receiving medical treatment, {symptoms} being addressed, hospital treatment room, medical equipment, {age_group}, therapeutic care",
        "medical procedure for {disease} patient, treating {symptoms}, healthcare professionals providing care, {age_group}, clinical treatment",
        "therapeutic intervention for {disease}, managing {symptoms}, hospital setting, medical staff, {age_group}, healing process"
    ],
    
    "emergency": [
        "emergency medical care for {disease} patient, acute {symptoms}, hospital emergency room, urgent treatment, {age_group}, critical care",
        "paramedics treating {disease} emergency, patient with {symptoms}, ambulance setting, emergency medical response, {age_group}",
        "urgent medical intervention for {disease}, severe {symptoms}, emergency department, medical team, {age_group}"
    ],
    
    "recovery": [
        "patient recovering from {disease}, {symptoms} improving, rehabilitation setting, physical therapy, {age_group}, healing progress",
        "{disease} patient in recovery phase, {symptoms} subsiding, hospital room, supportive care, {age_group}, getting better",
        "post-treatment recovery for {disease}, managing residual {symptoms}, medical monitoring, {age_group}, wellness journey"
    ],
    
    "medication": [
        "patient with {disease} taking medication, treating {symptoms}, pharmacy consultation, prescription drugs, {age_group}, pharmaceutical care",
        "medication administration for {disease}, addressing {symptoms}, healthcare worker giving medicine, {age_group}, drug therapy",
        "{disease} patient receiving medication, managing {symptoms}, hospital pharmacy, medical supervision, {age_group}"
    ],
    
    "home_care": [
        "home healthcare for {disease} patient, managing {symptoms} at home, family support, comfortable environment, {age_group}, personalized care",
        "patient with {disease} receiving care at home, {symptoms} monitoring, visiting nurse, domestic setting, {age_group}, home treatment",
        "home-based care for {disease}, family helping with {symptoms}, comfortable home environment, {age_group}, supportive care"
    ]
}

# Context theo độ tuổi
AGE_CONTEXTS = {
    "child": "pediatric patient, child healthcare, colorful children's hospital environment, gentle medical care for kids",
    "adult": "adult patient, professional medical setting, standard healthcare environment",
    "elderly": "elderly patient, geriatric care, senior-friendly medical environment, age-appropriate healthcare"
}

def create_medical_prompt(disease: str, symptoms: str, scene_type: str, age_group: str) -> str:
    """Tạo prompt y khoa tự động"""
    
    # Chọn template cảnh
    if scene_type == "random":
        scene_type = random.choice(list(MEDICAL_SCENES.keys()))
    
    template = random.choice(MEDICAL_SCENES.get(scene_type, MEDICAL_SCENES["treatment"]))
    age_context = AGE_CONTEXTS.get(age_group, AGE_CONTEXTS["adult"])
    
    # Tạo prompt
    prompt = template.format(
        disease=disease,
        symptoms=symptoms if symptoms else "typical symptoms",
        age_group=age_context
    )
    
    # Thêm từ khóa chất lượng
    prompt += ", professional medical photography, realistic healthcare scene, high quality medical documentation, clean hospital environment"
    
    return prompt

def generate_content_with_retry(prompt: str, max_retries: int = 3):
    """Tạo content với retry và rotation API key"""
    
    for attempt in range(max_retries):
        try:
            client = key_manager.get_current_client()
            current_key = key_manager.get_current_key()
            
            print(f"🔑 Attempt {attempt + 1}/{max_retries} with key: ...{current_key[-10:]}")
            
            response = client.models.generate_content(
                model="gemini-2.0-flash-preview-image-generation",
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_modalities=['TEXT', 'IMAGE']
                )
            )
            
            print(f"✅ Success with key: ...{current_key[-10:]}")
            return response, current_key
            
        except Exception as e:
            error_str = str(e).lower()
            print(f"❌ Error with key ...{key_manager.get_current_key()[-10:]}: {str(e)}")
            
            # Kiểm tra các loại lỗi cần rotation
            if any(error_code in error_str for error_code in ['429', 'quota', 'rate limit', 'too many requests']):
                print("🚫 Rate limit detected, rotating key...")
                key_manager.rotate_key("rate_limit")
            elif 'api key' in error_str or 'authentication' in error_str or 'invalid' in error_str:
                print("🔐 API key issue detected, rotating key...")
                key_manager.rotate_key("auth_error")
            else:
                # Lỗi khác, thử lại với cùng key
                if attempt < max_retries - 1:
                    print(f"⏳ Retrying in 2 seconds...")
                    time.sleep(2)
                continue
            
            # Nếu đã thử tất cả keys
            if attempt == max_retries - 1:
                raise HTTPException(
                    status_code=500, 
                    detail=f"All API keys exhausted. Last error: {str(e)}"
                )
    
    raise HTTPException(status_code=500, detail="Max retries exceeded")

@app.get("/")
async def root():
    return {
        "message": "Medical Image Generation API - Now with API Key Rotation!",
        "api_status": key_manager.get_status()
    }

@app.get("/api-status")
async def get_api_status():
    """Kiểm tra trạng thái các API keys"""
    return key_manager.get_status()

@app.post("/generate-medical-image", response_model=ImageGenerationResponse)
async def generate_medical_image(request: MedicalImageRequest):
    """
    Tạo ảnh y khoa chỉ với tên bệnh và triệu chứng
    """
    try:
        # Tạo prompt tự động
        scene_type = random.choice(list(MEDICAL_SCENES.keys()))
        generated_prompt = create_medical_prompt(
            disease=request.disease_name,
            symptoms=request.symptoms,
            scene_type=scene_type,
            age_group=request.patient_age
        )
        
        # Thêm prefix realistic
        full_prompt = f"A realistic photo for topic: {generated_prompt}"
        
        # Generate content với retry
        response, used_key = generate_content_with_retry(full_prompt)
        
        # Kiểm tra response hợp lệ
        if not response or not response.candidates or not response.candidates[0].content.parts:
            raise HTTPException(status_code=500, detail="No valid response from Gemini API")
        
        text_response = None
        image_base64 = None
        
        # Xử lý response
        for part in response.candidates[0].content.parts:
            if part.text is not None:
                text_response = part.text
            elif part.inline_data is not None:
                image = Image.open(BytesIO(part.inline_data.data))
                
                if request.return_base64:
                    buffer = BytesIO()
                    image.save(buffer, format='PNG')
                    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
                else:
                    filename = f"{request.disease_name.replace(' ', '_').lower()}.png"
                    image.save(filename)
        
        return ImageGenerationResponse(
            text_response=text_response,
            image_base64=image_base64,
            message=f"Medical image for {request.disease_name} generated successfully!",
            generated_prompt=generated_prompt,
            api_key_used=f"...{used_key[-10:]}"
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating image: {str(e)}")

@app.post("/generate-multiple-scenes", response_model=MultiSceneResponse)
async def generate_multiple_scenes(request: MedicalImageRequest):
    """
    Tạo nhiều cảnh khác nhau cho cùng một bệnh
    """
    try:
        scenes = []
        scene_types = ["consultation", "treatment", "emergency", "recovery", "medication", "home_care"]
        
        for scene in scene_types:
            prompt = create_medical_prompt(
                disease=request.disease_name,
                symptoms=request.symptoms,
                scene_type=scene,
                age_group=request.patient_age
            )
            
            scenes.append({
                "scene_type": scene,
                "scene_description": scene.replace("_", " ").title(),
                "prompt": prompt,
                "api_request": {
                    "prompt": prompt,
                    "return_base64": request.return_base64,
                    "add_realistic_prefix": True
                }
            })
        
        return MultiSceneResponse(
            disease=request.disease_name,
            symptoms=request.symptoms,
            scenes=scenes,
            message=f"Generated {len(scenes)} different medical scenes for {request.disease_name}"
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating multiple scenes: {str(e)}")

@app.post("/generate-image-stream")
async def generate_image_stream(request: MedicalImageRequest):
    """
    Tạo ảnh y khoa và trả về dưới dạng stream
    """
    try:
        # Tạo prompt tự động
        scene_type = random.choice(list(MEDICAL_SCENES.keys()))
        generated_prompt = create_medical_prompt(
            disease=request.disease_name,
            symptoms=request.symptoms,
            scene_type=scene_type,
            age_group=request.patient_age
        )
        
        full_prompt = f"A realistic photo for topic: {generated_prompt}"
        
        # Generate content với retry
        response, used_key = generate_content_with_retry(full_prompt)
        
        if not response or not response.candidates or not response.candidates[0].content.parts:
            raise HTTPException(status_code=500, detail="No valid response from API")
        
        # Tìm ảnh trong response
        for part in response.candidates[0].content.parts:
            if part.inline_data is not None:
                image_data = part.inline_data.data
                filename = f"{request.disease_name.replace(' ', '_').lower()}.png"
                return StreamingResponse(
                    BytesIO(image_data),
                    media_type="image/png",
                    headers={
                        "Content-Disposition": f"inline; filename={filename}",
                        "X-API-Key-Used": f"...{used_key[-10:]}"
                    }
                )
        
        raise HTTPException(status_code=404, detail="No image found in response")
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating image: {str(e)}")

@app.get("/medical-scenes")
async def get_medical_scenes():
    """
    Lấy danh sách các loại cảnh y khoa có thể tạo
    """
    return {
        "available_scenes": list(MEDICAL_SCENES.keys()),
        "age_groups": list(AGE_CONTEXTS.keys()),
        "scene_descriptions": {
            "consultation": "Cảnh khám bệnh, tư vấn y khoa",
            "treatment": "Cảnh điều trị, chữa bệnh",
            "emergency": "Cảnh cấp cứu y tế",
            "recovery": "Cảnh hồi phục, phục hồi sức khỏe",
            "medication": "Cảnh dùng thuốc, điều trị bằng thuốc",
            "home_care": "Cảnh chăm sóc tại nhà"
        },
        "usage_example": {
            "disease_name": "tiểu đường",
            "symptoms": "mệt mỏi, khát nước nhiều, đi tiểu thường xuyên",
            "patient_age": "adult",
            "return_base64": False
        },
        "api_status": key_manager.get_status()
    }

@app.get("/generate-simple/{disease_name}")
async def generate_simple_image(disease_name: str, symptoms: str = ""):
    """
    Endpoint đơn giản - chỉ cần tên bệnh
    """
    try:
        scene_type = random.choice(list(MEDICAL_SCENES.keys()))
        generated_prompt = create_medical_prompt(
            disease=disease_name,
            symptoms=symptoms,
            scene_type=scene_type,
            age_group="adult"
        )
        
        full_prompt = f"A realistic photo for topic: {generated_prompt}"
        
        # Generate content với retry
        response, used_key = generate_content_with_retry(full_prompt)
        
        if not response or not response.candidates or not response.candidates[0].content.parts:
            raise HTTPException(status_code=500, detail="No valid response from API")
        
        for part in response.candidates[0].content.parts:
            if part.inline_data is not None:
                image_data = part.inline_data.data
                filename = f"{disease_name.replace(' ', '_').lower()}.png"
                return StreamingResponse(
                    BytesIO(image_data),
                    media_type="image/png",
                    headers={
                        "Content-Disposition": f"inline; filename={filename}",
                        "X-API-Key-Used": f"...{used_key[-10:]}"
                    }
                )
        
        raise HTTPException(status_code=404, detail="No image found in response")
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating image: {str(e)}")

# Reset API keys endpoint (chỉ dùng khi cần thiết)
@app.post("/reset-api-keys")
async def reset_api_keys():
    """
    Reset trạng thái tất cả API keys - chỉ dùng khi cần thiết
    """
    global key_manager
    key_manager = APIKeyManager(API_KEYS)
    return {
        "message": "All API keys reset successfully",
        "status": key_manager.get_status()
    }

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
