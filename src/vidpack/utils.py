def convert_quality_to_crf(quality: int) -> int:
    """
    Convert a quality level from range [0, 100] to a Constant Rate Factor (CRF)
    value in range [23, 51]. Lower values mean (lower quality, higher compression).
    Higher values mean (higher quality, lower compression).

    Args:
        quality (int): The quality level to convert.

    Returns:
        int: The CRF value.
    """
    c, q = 51 - 23, 100 - 0
    return int(51 - quality * (c / q))
