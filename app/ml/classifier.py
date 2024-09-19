import torch
import clip
from PIL import Image
import io

# Загрузка модели
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)
print('Model downloaded')
# Список классов для классификации
CLASSES = [
    "Pink small sparrow",
    "Gray black magpie",
    "Bat",
    "Light-colored ferret",
    "Pink flower",
    "White-backed Woodpecker",
    "Mole",
    "Hedgehog",
    "Blue bird with orange belly",
    "bird mottled hoopoe",
    "Blue flower",
    "Owl",
    "Dark-colored ferret",
    "Yellow flower"
]

MAPPIN = [
    "Урагус сибирский",
    "Серый сорокопут",
    "Рыжая вечерница",
    "Горностай",
    "Хохлатка полая",
    "Белоспинный дятел",
    "Обыкновенная кутора",
    "Обыкновенный еж",
    "Зимородок",
    "Удод",
    "Незабудка болотная",
    "Филин",
    "Лесной хорек",
    "Лютик длиннолистный"
]
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
    return MAPPIN[indices[0]]
