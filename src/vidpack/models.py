from dataclasses import dataclass, replace
from enum import Enum
from pathlib import Path


class VideoCodec(str, Enum):
    """
    Enum representing the supported video codecs.
    """

    # use h264 instead of libx264 for better compatibility
    # see: https://superuser.com/a/1587184
    H264 = "h264"
    H265 = "libx265"


@dataclass(frozen=True)
class CompressParams:
    src: Path
    dst: Path | None = None
    quality: int = 75
    vcodec: VideoCodec = VideoCodec.H264
    overwrite: bool = False
    delete_original: bool = False

    @property
    def default_dst(self) -> Path:
        return self.src.with_name(self.src.stem + "_compressed" + self.src.suffix)

    def copy_with(self, **kwargs) -> "CompressParams":
        return replace(self, **kwargs)
