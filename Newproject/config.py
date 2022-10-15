from pathlib import Path
from itertools import chain

folder_path = Path(r'C:\Users\IT-Academy-Gomel\Downloads')

subfolder_name_to_extension = {
    'video': ('mp4', 'mov', 'avi', 'wmv', 'mpg', 'mpeg', 'm4v', 'h264'),
    'audio': ('mp3', 'wav', 'wma', 'mid', 'ogg', 'flac'),
    'image': ('jpg', 'png', 'jpeg', 'svg', 'tif', 'tiff'),
    'archives': ('zip', 'rar', '7z', 'z', 'gz', 'deb'),
    'text': ('txt', 'pdf', 'doc', 'docx', 'rtf', 'odt'),
    'spreadsheet': ('xls', 'xlsx', 'xlsm'),
    'presentation': ('pptx', 'ppt'),
    'book': ('epub', 'fb2', 'mobi'),
    'gif': ('gif',),
    'torrent': ('torrent',),
    'exe': ('exe',),
    'html': ('html', 'xml'),
    'figma': ('fig',),
}

subfolder_names = tuple(subfolder_name_to_extension.keys())

extensions = tuple(chain.from_iterable(
    subfolder_name_to_extension.values()
))


def get_subfolder_name_by_extension(extension: str) -> str:
    """Получение имени подпапки исходя из расширения

    :param extension: расширение
    :return: имя подпапки
    """
    for subfolder_name, tuple_of_extinsions in subfolder_name_to_extension.items():
        if extension in tuple_of_extinsions:
            return subfolder_name
