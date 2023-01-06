from typing import Any, ClassVar
from typing_extensions import Literal

from ._imaging import PixelAccess
from .ImageFile import ImageFile
from .PyAccess import PyAccess

class IcoFile:
    buf: Any
    entry: Any
    nb_items: Any
    def __init__(self, buf): ...
    def sizes(self): ...
    def getentryindex(self, size, bpp: bool = ...): ...
    def getimage(self, size, bpp: bool = ...): ...
    def frame(self, idx): ...

class IcoImageFile(ImageFile):
    format: ClassVar[Literal["ICO"]]
    format_description: ClassVar[str]
    @property
    def size(self): ...
    @size.setter
    def size(self, value) -> None: ...
    im: Any
    mode: Any
    def load(self) -> PixelAccess | PyAccess: ...
    def load_seek(self) -> None: ...
