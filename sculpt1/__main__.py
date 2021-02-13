import os.path as _path

from moviepy.editor import (
    concatenate_videoclips,
    concatenate_audioclips,
    CompositeVideoClip,
    CompositeAudioClip,
    VideoFileClip,
    AudioFileClip,
    vfx,
    afx,
)


SLOWMO_2X = 1.0 / 2
SLOWMO_2X = 1.0 / 3
SLOWMO_4X = 1.0 / 4

FASTFWD_2X = 2
FASTFWD_3X = 3
FASTFWD_4X = 4


def root(*paths):
    return _path.join(_path.dirname(_path.dirname(_path.abspath(__file__))), *paths)


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


def videos():
    video1 = VideoFileClip(root('assets', 'sculpt1', '2021-01-23 17-34-21.mkv'))
    video2 = VideoFileClip(root('assets', 'sculpt1', '2021-02-04 16-49-41.mkv'))
    video3 = VideoFileClip(root('assets', 'sculpt1', '2021-02-07 18-33-29.mkv'))
    video4 = VideoFileClip(root('assets', 'sculpt1', '2021-02-13 01-46-47.mkv'))

    return concatenate_videoclips([
        speedx(video4.subclip((53, 20), (53, 40))
                     .fx(vfx.fadein, 0.9), FASTFWD_2X),
        
        video4.subclip((53, 45), (54, 0))
                     .fx(vfx.fadein, 0.9),

        speedx(concatenate_videoclips([
            video1.subclip((0, 42), (2, 50))
                  .fx(vfx.fadein, 0.9),
            video1.subclip((3, 40), (6, 40)),
            video1.subclip((6, 50), (14, 20)),

            video2.subclip((4, 0), (5, 20)),
            video2.subclip((5, 30), (7, 5))
                  .fx(vfx.fadein, 0.9),
            video2.subclip((7, 20), (9, 0)),
            video2.subclip((9, 38), (11, 3))
                  .fx(vfx.fadein, 0.9),
            video2.subclip((11, 6), (14, 50)),
            video2.subclip((20, 30), (27, 0)),
            video2.subclip((27, 20), (40, 40))
                  .fx(vfx.fadein, 0.9),
            video2.subclip((41, 30), (41, 45)),
            video2.subclip((44, 50), (56, 30)),

            # video3.subclip((0, 52), (13, 50))
            #       .fx(vfx.fadein, 0.9),
            # video3.subclip((15, 35), (32, 20)),
            # video3.subclip((40, 10), (45, 30)),
            # video3.subclip((48, 30), (53, 0)),
            # video3.subclip((1, 6, 0), (1, 9, 0)),
        ]), FASTFWD_4X)
    ])


def tracks():
    return concatenate_audioclips([
        AudioFileClip(root('assets', 'sculpt1', 'track1.mp3'))
            .fx(afx.volumex, 0.5),
        AudioFileClip(root('assets', 'sculpt1', 'track2.mp3'))
            .fx(afx.volumex, 0.5),
        AudioFileClip(root('assets', 'sculpt1', 'track3.mp3'))
            .fx(afx.volumex, 0.5),
    ])


def main():
    master_video = videos()
    master_audio = tracks()

    final_video = resize(master_video)

    # Just loop the audio until the end of the video.
    final_audio = master_audio.audio_loop(duration=final_video.duration)

    # For debugging purposes only.
    # final_video.preview(fps=30, audio=False)

    final_video = final_video.set_audio(final_audio)

    final_video.write_videofile(root('output', 'sculpt1.mp4'))


if __name__ == '__main__':
    main()
