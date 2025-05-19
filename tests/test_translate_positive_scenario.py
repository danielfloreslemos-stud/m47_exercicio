from utils.core import get_translation

#Assuming the json response is something like {"translation": "word_translated"}
def test_translation_apple_spanish():
    response = get_translation("apple", "es-ES")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    data = response.json()
    assert "translation" in data, "'translation' key is missing in response"
    assert data["translation"] == "manzana", f"Expected 'manzana', got '{data['translation']}'"