from enum import Enum


class VideoCodec(str, Enum):
    """
    Enum representing the supported video codecs.
    """

    # use h264 instead of libx264 for better compatibility
    # see: https://superuser.com/a/1587184
    H264 = "h264"
    H265 = "libx265"
