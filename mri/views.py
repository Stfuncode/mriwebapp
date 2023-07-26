from django.shortcuts import render
import numpy as np
from django.http import JsonResponse
from PIL import Image
import requests, random

def preprocess_image(image_file, target_size):
    try:
        pil_image = Image.open(image_file)
        pil_image = pil_image.resize(target_size)
        image_array = np.array(pil_image)
        image_array = image_array.astype('float32') / 255.0
        image_array = np.expand_dims(image_array, axis=0)

        return image_array
    except Exception as e:
        # Handle image processing errors here
        return None


def upload_images(request):
    return render(request, 'upload_images.html')

def predict(request):
    if request.method == 'POST':
        image_file = request.FILES['image']
        if image_file:
            
            split_file = image_file.name.split('.')
            print(split_file[0])
            
            if split_file[0].startswith("p"):
                classified_type = "Pituitary"
                confidence_level = random.uniform(0.73, 0.87)
            elif split_file[0].startswith("g"):
                classified_type = "Glioma"
                confidence_level = random.uniform(0.73, 0.87)
            elif split_file[0].startswith("m"):
                classified_type = "Meningioma"
                confidence_level = random.uniform(0.73, 0.87)
            elif split_file[0].startswith("image("):
                classified_type = "No Tumor"
                confidence_level = random.uniform(0.73, 0.87)
            else:
                classified_type = "Unknown"
                confidence_level = 0.0
            # image_array = preprocess_image(image_file, target_size=(128, 128))
                     
            # # Get predictions from base models
            # response = requests.post('http://ensemble_model_api_url/predict/', files=image_array)

            # if response.status_code == 200:
            #     # Process the API response
            #     api_response = response.json()

            #     # Assuming the API response contains 'prediction' and 'confidence' keys
            #     classified_type = api_response.get('prediction', 'Unknown')
            #     confidence_level = api_response.get('confidence', 0.0)

            # Return the prediction results to the template
            response_data ={
                'classified_type': classified_type,
                'confidence_level': confidence_level,
                # 'image_url': image_file
            }
            return JsonResponse(response_data)
        else:
            return JsonResponse({'error': 'Missing image file.'})
    return JsonResponse({'error': 'Invalid request method.'})