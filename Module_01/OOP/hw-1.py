
import abc
from datetime import date

# Абстрактный класс для медиа-файлов
class Multimedia(abc.ABC):
    def __init__(self, name, size, created):
        self.__name = name
        self.__size = size
        self.__created = created
    
    @property
    def name(self):
        return self.__name
    #
    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def size(self):
        return self.__size
    #
    @size.setter
    def size(self, size):
        self.__size = size
    
    @property
    def created(self):
        return self.__created
    
    @abc.abstractmethod
    def open(self): pass
    
    @abc.abstractmethod
    def save(self): pass

    @abc.abstractmethod
    def edit(self): pass
    
    @abc.abstractmethod
    def delete(self): pass

    def __str__(self):
        return f'Name: {self.__name}; Size: {self.__size}; Created: {self.__created}'


# Абстрактный класс для аудио, видео-файлов
class MultimediaAudioVideo(Multimedia):
    def __init__(self, name, size, created, duration):
        super().__init__(name, size, created)
        self.__duration = duration
    
    @property
    def duration(self):
        return self.__duration
    
    def volume(self, value): pass # регулировка громкости


class PhotoFile(Multimedia):
    def __init__(self, name, size, created, width, height):
        super().__init__(name, size, created)
        self.__width = width
        self.__height = height
    
    @property
    def width(self):
        return self.__width
    #
    @width.setter
    def width(self, width):
        self.__width = width
    
    @property
    def height(self):
        return self.__height
    #
    @height.setter
    def height(self, height):
        self.__height = height
    
    def open(self):
        raise Exception('No implementation')
    def save(self):
        raise Exception('No implementation')
    def edit(self):
        raise Exception('No implementation')
    def delete(self):
        raise Exception('No implementation')
    
    def contrast(self, value): pass # изменить контраст
    def brightness(self, value): pass # изменить яркость


class AudioFile(MultimediaAudioVideo):
    def __init__(self, name, size, created, duration, ext='mp3'):
        super().__init__(name, size, created, duration)
        # расширение
        self.__ext = ext
    
    @property
    def ext(self):
        return self.__ext
    
    def open(self):
        raise Exception('No implementation')
    def save(self):
        raise Exception('No implementation')
    def edit(self):
        raise Exception('No implementation')
    def delete(self):
        raise Exception('No implementation')


class VideoFile(MultimediaAudioVideo):
    def __init__(self, name, size, created, duration, codec):
        super().__init__(name, size, created, duration)
        # кодек
        self.__codec = codec
    
    @property
    def codec(self):
        return self.__codec
    
    def open(self):
        raise Exception('No implementation')
    def save(self):
        raise Exception('No implementation')
    def edit(self):
        raise Exception('No implementation')
    def delete(self):
        raise Exception('No implementation')

triller = VideoFile('Как выучить ML', 10000, date(2024, 1, 24), 90, 'codec')
triller.volume(55)

try:
    triller.duration = -1
except AttributeError as ex:
    print(f'ERROR: {ex}', end='\n\n')

print(triller, end='\n\n')
print(f'Duration: {triller.duration}')


if __name__ == '__main__':
    print(end='\n\n')
    print('END!!!' );
    #input();


