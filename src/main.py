from dotenv import load_dotenv
import os

def print_author():
    load_dotenv()  # загружаем переменные из .env
    author = os.getenv("AUTHOR")  # получаем значение
    print(f"Автор проекта: {author}")


# проверка
print_author()
