import os
from config import *
from typing import Union, Iterable

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from UIO import Ui_MainWindow


class Sorter(QtWidgets.QMainWindow):
    def __init__(self):
        super(Sorter, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle('File Sorter')
        self.ui.lineEdit.setPlaceholderText('Enter path to the folder to sort')
        self.ui.pushButton.clicked.connect(self.sort)


    def sort(self):
        input_path = self.ui.lineEdit.text()
        if input_path == '':
            self.ui.label_3.setText('Enter path to the folder to start')
            self.ui.label.repaint()
            return self.sort()
        start_text = f'Sorting files by extensions in {input_path}'
        self.ui.label_3.setText(start_text)
        folder = Folder(fr'{input_path}')
        output = folder.sort_files_by_extension()
        self.ui.label_3.setText((f'{start_text}\n{output}'))
        self.ui.label.repaint()






class Folder:
    """Класс для сортировки файлов по папкам"""

    def __init__(self, path: Union[Path, str]) -> None:
        self.path = path

    def _get_file_path(self) -> Iterable:
        """Получение пути к файлу

        :return: итератор путей к файлу
        """
        return (file.path for file in os.scandir(self.path) if not file.is_dir())

    def _create_subfolder(self, subfolder_name: str) -> None:
        """Создание подпапки

        :param subfolder_name: имя подпапки
        :return: None
        """
        try:
            subfolder_path = self.path / subfolder_name
            if not subfolder_path.exists():
                subfolder_path.mkdir()

        except OSError as ex:
            return f'Не удалось создать директорию -> {repr(ex)}'

    def sort_files_by_extension(self) -> None:
        """Сортировка файлов по расширениям

        :return:
        """
        try:
            file_count = 0
            for filepath in self._get_file_path():
                path = Path(filepath)
                extension = path.suffix.split('.')[-1]

                if extension in extensions:
                    subfolder_name = get_subfolder_name_by_extension(extension)
                    self._create_subfolder(subfolder_name)

                    new_path = Path(self.path, subfolder_name, path.name)
                    path.rename(new_path)
                    file_count += 1
            return f'Файлов отсортировано: {file_count}'
        except Exception as ex:
            return f'Не удалось отсоритировать файлы -> {repr(ex)}'


def sorter_files() -> None:
    folder = Folder(folder_path)
    print(f'Сортировка файлов в {folder_path}')
    folder.sort_files_by_extension()


def sorter_files() -> None:
    folder = Folder(folder_path)
    print(f'Сортировка файлов в {folder_path}')
    folder.sort_files_by_extension()


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    application = Sorter()
    application.show()
    sys.exit(app.exec_())