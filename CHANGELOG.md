# CHANGELOG

## v0.2.1 (2024-10-07)

### Fix

* fix: inherit str in VideoCodec enum for Typer compatibility

Inherit from `str` in `VideoCodec` enum to ensure it behaves like a string, resolving Typer compatibility issue. ([`d6251f1`](https://github.com/ivansaul/CLI-Video-Compressor/commit/d6251f134bef02e214f81afce918abc0b45b5ba7))

* fix: enforce valid quality range

Added validation to ensure the quality argument falls within a valid range (0-100). This prevents potential errors and ensures that the user&#39;s input is always treated correctly. ([`631e60d`](https://github.com/ivansaul/CLI-Video-Compressor/commit/631e60d83d2e514dfe3e5d5a889bdcd74a6f6098))

### Unknown

* Merge pull request #19 from ivansaul/fix/cli-arguments-validations

Fix cli arguments validations ([`30dbf9a`](https://github.com/ivansaul/CLI-Video-Compressor/commit/30dbf9ab953748bacb5d5f4844102711ea5affc2))

## v0.2.0 (2024-10-07)

### Documentation

* docs: update language switcher HTML for proper GitHub rendering ([`70e21b7`](https://github.com/ivansaul/CLI-Video-Compressor/commit/70e21b7840b0f7e07997445aaacdf45ae07b65d1))

* docs: add Spanish README

Add a Spanish translation of the README.md ([`414d595`](https://github.com/ivansaul/CLI-Video-Compressor/commit/414d59517e7c616923ecb0956971e4e944df0fe3))

### Feature

* feat: add support for libx265 video codec

Adds the ability to choose between h264 and libx265 video codecs for compression, offering a more efficient compression option for users with modern GPUs. ([`61c71ab`](https://github.com/ivansaul/CLI-Video-Compressor/commit/61c71ab496db58894760dc88a49b03f4224ce949))

### Unknown

* Merge pull request #18 from ivansaul/feature/add-codec-option

feat: add support for libx265 video codec ([`1f1aed8`](https://github.com/ivansaul/CLI-Video-Compressor/commit/1f1aed8017f1b748030df885672cdf46dffad940))

* Merge pull request #17 from ivansaul/develop

docs: update language switcher HTML for proper GitHub rendering ([`efe91f8`](https://github.com/ivansaul/CLI-Video-Compressor/commit/efe91f8e3945df61e423401f9d6f83c69ae706ca))

* Merge pull request #16 from ivansaul/develop

docs: add Spanish README ([`731aa00`](https://github.com/ivansaul/CLI-Video-Compressor/commit/731aa002d28c17a8344c13ee7dd3a838321be2f6))

## v0.1.1 (2024-10-06)

### Documentation

* docs: update README.md

Update the README to reflect the new package name &#34;vidpack&#34; and provide the installation command using pip ([`568da86`](https://github.com/ivansaul/CLI-Video-Compressor/commit/568da8686a752f457e44087fb349ed16b2cfd6d7))

### Fix

* fix: update `pack` script path in `pyproject.toml`

The `pack` script was previously referencing the wrong path, causing an error when trying to run the command. This commit fixes the issue by updating the path to correctly point to the `vidpack.cli:app` entry point. ([`1e46b00`](https://github.com/ivansaul/CLI-Video-Compressor/commit/1e46b0096b1d8e5302e8185e015c48d099a3fdb6))

### Unknown

* Merge pull request #15 from ivansaul/develop

Fix script path and update README.md ([`91b115d`](https://github.com/ivansaul/CLI-Video-Compressor/commit/91b115dbdef19d6ced02a1a9e078eec144d7c93d))

## v0.1.0 (2024-10-06)

### Chore

* chore: initial project setup

Adds basic project structure, dependencies, and testing infrastructure.

The project utilizes Typer for CLI handling, ffmpeg for video compression, and a comprehensive testing suite with pytest and Ruff for linting. ([`ebcfd39`](https://github.com/ivansaul/CLI-Video-Compressor/commit/ebcfd3915822bdab65e86244b15cf3e0b7666ca2))

### Documentation

* docs: update README.md ([`67aff8c`](https://github.com/ivansaul/CLI-Video-Compressor/commit/67aff8c302854e38c83f8c5a483fea2b87e3acb7))

* docs: update README.md

Add demo GIF to README.md ([`2b7b5a8`](https://github.com/ivansaul/CLI-Video-Compressor/commit/2b7b5a86998fd5867f4f07af67793ea03a204eb9))

* docs: update README.md

Update user guide with detailed usage instructions and examples ([`67730c1`](https://github.com/ivansaul/CLI-Video-Compressor/commit/67730c11d2066904f690fbccef9c99daf2d29459))

### Feature

* feat: automate releases with semantic versioning

Adds a GitHub Actions workflow to automate the release process, including semantic versioning, publishing to PyPI, and GitHub Release Assets. ([`fcfecf3`](https://github.com/ivansaul/CLI-Video-Compressor/commit/fcfecf33e806cf4bc062f48b58de18878c00f938))

* feat: add short option aliases for CLI arguments

Add short option aliases (`-o`, `-q`, `-w`, `-d`, `-v`) to the CLI arguments for improved usability and consistency. ([`999cf0a`](https://github.com/ivansaul/CLI-Video-Compressor/commit/999cf0a989fd6bbfae1fd1ca3be6234979656112))

* feat: add video quality control

Adds a new `quality` option to allow users to control the output video quality.

The quality level is a number between 0 and 100, where a lower number means higher compression and lower quality, and a higher number means lower compression and higher quality. The default quality level is 75. ([`c76f6d9`](https://github.com/ivansaul/CLI-Video-Compressor/commit/c76f6d9ee09ec339c5edc308078a69917b892282))

* feat: add option to delete original video

Add a new command-line option (`--delete-original`) to allow users to delete the original video file after compression. This provides a convenient way to clean up space after processing. The option is disable by default. ([`b5e3625`](https://github.com/ivansaul/CLI-Video-Compressor/commit/b5e3625d0a26b1c18094bba6b0db07fa5d840766))

* feat: add functionality for bulk compression

- The input CLI argument can be a file or a directory. If a directory is provided, all videos in the directory will be processed.

- Rename`utils.py` to `core.py` for better organization and consistency with the project structure. This change ensures all core functionality resides within the `core` module. ([`4d2495b`](https://github.com/ivansaul/CLI-Video-Compressor/commit/4d2495b2c65544e7a74e8b997d2478e064d3c03a))

* feat: add core functionality for video compression

Adds basic CLI interface, video compression logic, and helper functions for managing input/output files.

Includes basic tests for the implemented functionality. ([`e25f212`](https://github.com/ivansaul/CLI-Video-Compressor/commit/e25f2122d64d5d37f4564a9277f61ad77927fe13))

### Fix

* fix: update PyPI action to use `release/v1` tag ([`1119b4a`](https://github.com/ivansaul/CLI-Video-Compressor/commit/1119b4ae5fa11ea52df0979e55ad2fe62be6aac3))

* fix: publish to PyPI

Switch release workflow to publish to the official PyPI repository instead of Test PyPI.  Also, update the versioning to correctly publish with `master` branch instead of `develop`. ([`8e74db8`](https://github.com/ivansaul/CLI-Video-Compressor/commit/8e74db8c9b4342fc70ddae196bd765652d3f8ea1))

* fix: update PyPI action for testPYPI ([`f3ce44a`](https://github.com/ivansaul/CLI-Video-Compressor/commit/f3ce44a8989d7185eec007e8b1eef0b96b2a104f))

* fix: re-handle &#34;File already exists&#34; error on Linux ([`af5c067`](https://github.com/ivansaul/CLI-Video-Compressor/commit/af5c0677fa5e6e10a9f58e03ae97f05e312dad79))

* fix: handle potential &#34;File already exists&#34; error on Linux

The `ffmpeg` command sometimes throws an error indicating that the output file already exists, even when using the `-n` (overwrite) flag. This commit introduces logic to detect and handle such errors, particularly on Linux systems. ([`44f47a3`](https://github.com/ivansaul/CLI-Video-Compressor/commit/44f47a34c26486be245091181ba3c0fa7ec4d9a9))

* fix: file already exists error on Linux

Prevented errors on Linux with the &#39;-n&#39; (no overwrite) option in ffmpeg when the output file exists; no error occurs on macOS. ([`e8bc3aa`](https://github.com/ivansaul/CLI-Video-Compressor/commit/e8bc3aa1c4047c94e71df0bf281d4476f7a3a199))

* fix: add missing override argument

Add the override argument to the compress_video function call. ([`0acb3ae`](https://github.com/ivansaul/CLI-Video-Compressor/commit/0acb3ae51474768fbdbd0959d68203ee11c9d9d2))

### Refactor

* refactor: rename project to &#39;vidpack&#39;

Move code to &#39;src&#39; directory, updated package name, and adjusted dependencies, scripts, and tests to reflect the new project name. ([`aba52a2`](https://github.com/ivansaul/CLI-Video-Compressor/commit/aba52a2fe27c9ad1e330875033b0a410175e390f))

* refactor(compress_video): change from subprocess to ffmpeg-python

Change from using subprocess and ffmpeg_progress_yield to ffmpeg-python for video compression and progress tracking. ([`94efc83`](https://github.com/ivansaul/CLI-Video-Compressor/commit/94efc838f055dc72c08c18647a02f268d07fc99a))

### Unknown

* Merge pull request #14 from ivansaul/develop

fix: update PyPI action to use `release/v1` tag ([`a0e8179`](https://github.com/ivansaul/CLI-Video-Compressor/commit/a0e81798a61e2695e8e03c978b1b1e8db01ff196))

* Merge pull request #13 from ivansaul/develop

Setup semantic versioning ([`47b03f9`](https://github.com/ivansaul/CLI-Video-Compressor/commit/47b03f9fce50836f8ed2d948791c73d23ce48097))

* Merge pull request #12 from ivansaul/feature/semantic-release

feat: automate releases with semantic versioning ([`5f22cf7`](https://github.com/ivansaul/CLI-Video-Compressor/commit/5f22cf7fce8503413be98f2c791800ce3dfbfdee))

* Merge pull request #11 from ivansaul/develop

Add new features and important fixes ([`42554d3`](https://github.com/ivansaul/CLI-Video-Compressor/commit/42554d3aa397abc998f32701d32a99312a343c7d))

* Merge pull request #10 from ivansaul/docs/update-readme

docs: update README.md ([`c0d322c`](https://github.com/ivansaul/CLI-Video-Compressor/commit/c0d322cbc2d668cb68ea885707d5de6bedbd7ec6))

* Merge pull request #9 from ivansaul/docs/update-readme

docs: update README.md ([`f611e92`](https://github.com/ivansaul/CLI-Video-Compressor/commit/f611e9279ab71b44ebadae3cd9519dac7bb895ea))

* Merge pull request #8 from ivansaul/feature/setup-short-commands

feat: add short option aliases for CLI arguments ([`ef67376`](https://github.com/ivansaul/CLI-Video-Compressor/commit/ef673764802d5d0a9cf9d41c3eaa54868e30aa21))

* Merge pull request #7 from ivansaul/feature/add-quality-option

feat: add video quality control ([`a22713e`](https://github.com/ivansaul/CLI-Video-Compressor/commit/a22713ed832f994ddcd14a410d05f39cd6828141))

* Merge pull request #6 from ivansaul/feature/bulk-compression

feat: add functionality for bulk compression ([`b99ec07`](https://github.com/ivansaul/CLI-Video-Compressor/commit/b99ec073f8b8ff56353224eefe3e4b90554956b4))

* Merge pull request #5 from ivansaul/refactor/compress-video

refactor(compress_video): change from subprocess to ffmpeg-python ([`7cbdb85`](https://github.com/ivansaul/CLI-Video-Compressor/commit/7cbdb8558742bc941ad34f9389df401cd1bca080))

* Merge pull request #4 from ivansaul/develop

typo: replace &#39;override&#39; with &#39;overwrite&#39; ([`f16d64d`](https://github.com/ivansaul/CLI-Video-Compressor/commit/f16d64d9bed6433e52f506bb9b20215c4dc66b60))

* typo: replace &#39;override&#39; with &#39;overwrite&#39; ([`1b945af`](https://github.com/ivansaul/CLI-Video-Compressor/commit/1b945affc752a839599be0c280dfa564c25a39e9))

* Merge pull request #3 from ivansaul/develop

fix: file already exists error on Linux ([`eb5e143`](https://github.com/ivansaul/CLI-Video-Compressor/commit/eb5e1435417668ce1c8d726ea5805069965c025f))

* Merge pull request #2 from ivansaul/develop

fix: add missing override argument ([`b20ff22`](https://github.com/ivansaul/CLI-Video-Compressor/commit/b20ff22f0576fef258f49ec41f70735c68487222))

* Merge pull request #1 from ivansaul/develop

feat: add core functionality for video compression ([`ac8679f`](https://github.com/ivansaul/CLI-Video-Compressor/commit/ac8679f808218632df3d48c897af1aabe639285b))

* Initial commit ([`a7e30f9`](https://github.com/ivansaul/CLI-Video-Compressor/commit/a7e30f9c1665dc0fd183fc618dde4e7c5425ff4d))
