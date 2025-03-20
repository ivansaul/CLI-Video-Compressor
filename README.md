<!-- markdownlint-disable MD033 MD036 MD041 MD045 MD046 -->

<div align="center">
    <img width="200" src="https://i.imgur.com/HeeZxH3.png" alt="Coco Logo">
</div>
<div align="center">

<h1 style="border-bottom: none">
    <b><a href="#">CLI Video Compressor</a></b>
</h1>

***`Pack`*** is a simple yet powerful CLI video compressor.

It reduces file sizes by up to 60% while maintaining high quality, using `FFmpeg` under the hood. Compress individual videos or entire folders with ease.

![GitHub repo size](https://img.shields.io/github/repo-size/ivansaul/CLI-Video-Compressor)
![GitHub stars](https://img.shields.io/github/stars/ivansaul/CLI-Video-Compressor)
![GitHub forks](https://img.shields.io/github/forks/ivansaul/CLI-Video-Compressor)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<a href="https://discord.gg/tDvybtJ7y9">
    <img alt="Discord Server" height="50" src="https://cdn.jsdelivr.net/npm/@intergrav/devins-badges@3/assets/cozy/social/discord-plural_vector.svg">
</a>

<p align="center">
    <a href="https://github.com/ivansaul/CLI-Video-Compressor/blob/master/README.md">English</a>
    ｜
    <a href="https://github.com/ivansaul/CLI-Video-Compressor/blob/master/README.es.md">Español</a>
</p>

</div>

---

![demo][demo]

## Installation | Upgrade

You might be sure that you have installed [*`Python 3.10+`*][python] and [*`FFmpeg`*][ffmpeg]. The CLI app uses `FFmpeg` under the hood, so make sure you have it installed and added to your PATH.

```console
pip install -U vidpack
```

<details>
    <summary>Prerequisites</summary>

    ```console
    # MacOS
    brew install ffmpeg

    # Ubuntu
    sudo apt install ffmpeg

    # ArchLinux
    sudo pacman -S ffmpeg

    # Fedora
    sudo dnf install ffmpeg
    ```

</details>

## Basic Usage

To compress a video or multiple videos, you will use the `pack` command, followed by the required input argument (a file or a directory).

```console
pack INPUT [OPTIONS]
```

> [!NOTE]
> `INPUT`: This is the file or directory you want to process. If you provide a directory, all videos within it will be compressed.

<!-- -->
> [!TIP]
> For additional help or to see all available options, you can use the command:
>
> ```console
> pack --help
> ```

## Options

Pack offers several options to customize the compression process:

- `--output`, `-o`: Specifies the output file to save the compressed video.
- `--quality`, `-q`: Defines the video quality level (0-100). Default value: 75.
- `--overwrite`, `-w`: Overwrites the output file if it already exists.
- `--delete-original`, `-d`: Deletes the original video after successful compression.
- `--codec`, `-c`: Specifies the video codec to use for compression(`h264`, `libx265`). Default is `h264`.

> [!IMPORTANT]
> The H265 (`libx265`) codec offers superior compression quality and produces smaller file sizes compared to `H264`. However, encoding with H265 is more time-consuming and requires significantly more processing power. If you have a modern GPU and enough time for encoding, H265 is an excellent choice for reducing file sizes without sacrificing quality.

## Usage Examples

To compress a video named `video.mp4`, simply run:

```console
pack video.mp4
```

This command will compress `video.mp4` with default settings(quality: 75) and save the result as `video_compressed.mp4` in the same directory.

<details>
    <summary>Show more examples</summary>

### Specify an output file

If you want to specify the name or location of the compressed file:

```console
pack video.mp4 --output compressed/small_video.mp4
```

This command will compress `video.mp4` and save the result as `small_video.mp4` in the `compressed` directory.

### Adjust compression quality

To compress a video with a specific quality (e.g., 60):

``` console
pack video.mp4 -q 60
```

This will compress the video with lower quality, resulting in a smaller file size.

### Compress all videos in a directory

To compress all videos in a directory:

```console
pack /path/to/my/videos
```

This command will compress all videos in the specified directory and save the results in the same directory.

### Overwrite existing files

If you want to overwrite existing compressed files:

```console
pack video.mp4 --output output.mp4 --overwrite
```

This will overwrite the file `output.mp4` if it already exists.

### Delete the original file after compression

To delete the original video file after successful compression:

```console
pack video.mp4 --delete-original
```

The original `video.mp4` will be deleted after compression.

### Specify a video codec

To compress a video with a specific video codec (e.g., libx265):

```console
pack video.mp4 --codec libx265
```

This will compress the video with the libx265 codec, resulting in a smaller file size. Currently, only `h264` and `libx265` codecs are supported.

### Use multiple options

You can combine multiple options in a single command:

```console
pack video.mp4 -o compressed.mp4 -q 80 -w -d
```

This command will compress `video.mp4` with a quality of 80, save the result as `compressed.mp4`, overwrite if the file exists, delete the original, and display detailed information during the process.

</details>

## Additional Notes

- The quality option (`-q`) affects both visual quality and file size. A lower value will result in a smaller file but lower visual quality, while a higher value will maintain better quality but with a larger file size.
- It's always recommended to backup your original videos before using the delete option (`-d`).

> [!TIP]
> If you are a Windows user, you can install `ffmpeg` and `python` manually or using package managers like [*`Scoop`*][scoop].
> Once you have installed a package manager, you can just run something like `scoop install python ffmpeg`.

<!-- -->
> [!TIP]
> Windows user can watch a tutorial video on YouTube about the installation process [[Here]][demo-windows].

## Contributors

<a href="https://github.com/ivansaul/CLI-Video-Compressor/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=ivansaul%2FCLI%2DVideo%2DCompressor"/>
</a>

## See my other projects

[![Bookmark Style Card](https://svg.bookmark.style/api?url=https://github.com/ivansaul/codigo_facilito_downloader&mode=light&style=horizontal)](https://github.com/ivansaul/codigo_facilito_downloader)
[![Bookmark Style Card](https://svg.bookmark.style/api?url=https://github.com/ivansaul/personal-portfolio&mode=light&style=horizontal)](https://github.com/ivansaul/personal-portfolio)
[![Bookmark Style Card](https://svg.bookmark.style/api?url=https://github.com/ivansaul/flutter_todo_app&mode=light&style=horizontal)](https://github.com/ivansaul/flutter_todo_app)

[python]:https://www.python.org/downloads/
[ffmpeg]:https://ffmpeg.org
[demo]:https://github.com/user-attachments/assets/9c9c672a-bfa3-418a-b7d1-89f0e7751146
[scoop]:https://scoop.sh
[demo-windows]: https://youtu.be/w1Pba7Bu0ZQ
