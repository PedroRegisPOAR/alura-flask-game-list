import os
import time

from app import app


class ImageService:
    UPLOAD_PATH = "UPLOAD_PATH"
    DEFAULT_COVER = "default_cover.jpg"
    IMAGE_PREFIX = "capa"
    IMAGE_EXT = "jpg"

    def get(
        self,
        *_,
        id=None,
    ) -> str:
        target = self.__get_image_prefix(id)
        for name in os.listdir(self.__get_upload_path()):
            if target in name:
                return name
        return self.DEFAULT_COVER

    def add(
        self,
        *_,
        picture=None,
        id=None,
    ) -> None:
        self.__delete_image(id=id)
        picture_name = self.__new_name(id=id)
        picture.save(picture_name)

    def __get_upload_path(self):
        return app.config[self.UPLOAD_PATH]

    def __get_image_prefix(
        self,
        *_,
        id=None,
    ):
        return f"{self.IMAGE_PREFIX}{id}"

    def __new_name(
        self,
        *_,
        id=None,
    ) -> str:
        path = self.__get_upload_path()
        prefix = self.__get_image_prefix(id)
        timestamp = time.time()
        return f"{path}/{prefix}-{timestamp}.{self.IMAGE_EXT}"

    def __delete_image(
        self,
        *_,
        id=None,
    ) -> None:
        image = self.get(id=id)
        if image != self.DEFAULT_COVER:
            os.remove(os.path.join(self.__get_upload_path(), image))
