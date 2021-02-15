from moviepy.editor import vfx, afx


SLOWMO_2X = 1.0 / 2
SLOWMO_2X = 1.0 / 3
SLOWMO_4X = 1.0 / 4

FASTFWD_2X = 2
FASTFWD_3X = 3
FASTFWD_4X = 4


def speedx(clip, speed=SLOWMO_2X):
    """Change the playback speed of a given video clip.

    Args:
        clip (VideoFileClip): A moviepy video clip instance.
            Example:
                clip = VideoFileClip('/path/to/clip.mp4')

        speed (float): A float value that will be multiplied to the
            current playback speed of the clip.
            Example:
                # Speed up the playback four times.
                speedx(clip, speed=4).

    Returns:
        VideoFileClip
    """
    return clip.fx(vfx.speedx, speed)


def resize(clip, size=None):
    """Resize a given video clip.

    Args:
        clip (VideoFileClip): A moviepy video clip instance.
            Example:
                clip = VideoFileClip('/path/to/clip.mp4')

        size (tuple): A tuple containing the new width and height.
            Example:
                resize(clip, size=(1920, 1080))

    Returns:
        VideoFileClip
    """
    if size is None:
        return clip.fx(vfx.resize, height=720)
    return clip.fx(vfx.resize, size)