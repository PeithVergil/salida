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
from ..utilities.paths import assets, output
from ..utilities.medias import FASTFWD_2X, FASTFWD_4X, resize, speedx


MODULE_NAME = 'sculpt1'


def videos():
    video1 = VideoFileClip(assets(MODULE_NAME, '2021-01-23 17-34-21.mkv'))
    video2 = VideoFileClip(assets(MODULE_NAME, '2021-02-04 16-49-41.mkv'))
    video3 = VideoFileClip(assets(MODULE_NAME, '2021-02-07 18-33-29.mkv'))
    video4 = VideoFileClip(assets(MODULE_NAME, '2021-02-13 01-46-47.mkv'))

    return concatenate_videoclips([
        speedx(video4.subclip((53, 20), (53, 30))
                     .fx(vfx.fadein, 0.9), FASTFWD_2X),
        
        # video4.subclip((53, 45), (54, 0))
        #              .fx(vfx.fadein, 0.9),

        speedx(concatenate_videoclips([
            video1.subclip((0, 42), (0, 50))
                  .fx(vfx.fadein, 0.9),
            video1.subclip((1, 27), (1, 45)),
            # video1.subclip((3, 40), (6, 40)),
        #     video1.subclip((6, 50), (14, 20)),

            # video2.subclip((4, 0), (5, 20)),
            # video2.subclip((5, 30), (7, 5))
            #       .fx(vfx.fadein, 0.9),
            # video2.subclip((7, 20), (9, 0)),
            # video2.subclip((9, 38), (11, 3))
            #       .fx(vfx.fadein, 0.9),
        #     video2.subclip((11, 6), (14, 50)),
        #     video2.subclip((20, 30), (27, 0)),
            video2.subclip((27, 20), (28, 0))
                  .fx(vfx.fadein, 0.9),
        #     video2.subclip((41, 30), (41, 45)),
        #     video2.subclip((44, 50), (56, 30)),

        #     # video3.subclip((0, 52), (13, 50))
        #     #       .fx(vfx.fadein, 0.9),
        #     # video3.subclip((15, 35), (32, 20)),
        #     # video3.subclip((40, 10), (45, 30)),
        #     # video3.subclip((48, 30), (53, 0)),
        #     # video3.subclip((1, 6, 0), (1, 9, 0)),
        ]), FASTFWD_4X)
    ])


def tracks():
    return concatenate_audioclips([
        AudioFileClip(assets(MODULE_NAME, 'track1.mp3'))
            .fx(afx.volumex, 0.5),
        AudioFileClip(assets(MODULE_NAME, 'track2.mp3'))
            .fx(afx.volumex, 0.5),
        AudioFileClip(assets(MODULE_NAME, 'track3.mp3'))
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

    # final_video.write_videofile(output('sculpt1.mp4'))
    final_video.write_videofile(output('sculpt1-story.mp4'))


if __name__ == '__main__':
    main()
