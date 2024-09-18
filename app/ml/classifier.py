import torch
import clip
from PIL import Image
import io

# Загрузка модели
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

# Список классов для классификации
CLASSES = ["Buffalo", "Elephant", "Rhino", "Zebra"]

def classify_image(image_data: bytes) -> str:
    # Преобразование байтов изображения в объект PIL Image
    image = Image.open(io.BytesIO(image_data))
    
    # Предобработка изображения
    image_input = preprocess(image).unsqueeze(0).to(device)
    
    # Токенизация текста классов
    text_inputs = torch.cat([clip.tokenize(f"a photo of a {c}") for c in CLASSES]).to(device)

    # Получение эмбеддингов изображения и текста
    with torch.no_grad():
        image_features = model.encode_image(image_input)
        text_features = model.encode_text(text_inputs)

    # Вычисление сходства
    similarity = (100.0 * image_features @ text_features.T).softmax(dim=-1)
    
    # Получение индекса класса с наибольшим сходством
    values, indices = similarity[0].topk(1)

    # Возвращение предсказанного класса
    return CLASSES[indices[0]]
