import os

def merge_files_from_directory(directory):
    files_data = []

    for file_name in os.listdir(directory): # Получаем список всех текстовых файлов в указанной директории
        if file_name.endswith('.txt'):  # Проверяем, что файл имеет расширение .txt
            file_path = os.path.join(directory, file_name)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.readlines()
                line_count = len(content)
                files_data.append((file_name, line_count, content))

        files_data.sort(key=lambda x: x[1])  # Сортируем по количеству строк

    for file_name, line_count, content in files_data:
        print(file_name)      # Имя файла
        print(line_count)     # Количество строк
        print(''.join(content))  # Содержимое файла

directory_path = 'C:/Users/User/Desktop/Files3'
merge_files_from_directory(directory_path)
