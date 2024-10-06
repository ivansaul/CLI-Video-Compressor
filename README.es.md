<!-- markdownlint-disable MD033 MD036 MD041 MD045 MD046 -->

<div align="center">
    <img width="200" src="https://i.imgur.com/HeeZxH3.png" alt="Coco Logo">
</div>
<div align="center">

<h1 style="border-bottom: none">
    <b><a href="#">CLI Video Compressor</a></b>
</h1>

***`Pack`*** es un compresor de videos CLI simple pero poderoso.

Reduce el tamaño de los archivos hasta un 60% mientras mantiene una alta calidad, utilizando `FFmpeg` como un sub-proceso. Comprime videos individuales o carpetas enteras con facilidad.

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

## Instalación

Asegúrate de haber instalado [*`Python 3.10+`*][python] y [*`FFmpeg`*][ffmpeg]. La aplicación CLI usa `FFmpeg` internamente, así que asegúrate de tenerlo instalado y agregado a tu PATH.

```console
pip install -U vidpack
```

<details>
    <summary>Requisitos previos</summary>

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

## Uso básico

Para comprimir un video o varios videos, usa el comando `pack`, seguido del argumento de entrada requerido (un archivo o un directorio).

```console
pack INPUT [OPTIONS]
```

> [!NOTE]
> `INPUT`: Este es el archivo o directorio que deseas procesar. Si proporcionas un directorio, todos los videos dentro de él serán comprimidos.

<!-- -->
> [!TIP]
> Para obtener ayuda adicional o ver todas las opciones disponibles, puedes usar el comando:
>
> ```console
> pack --help
> ```

## Opciones

Pack ofrece varias opciones para personalizar el proceso de compresión:

- `--output`, `-o`: Especifica el archivo de salida donde se guardará el video comprimido.
- `--quality`, `-q`: Define el nivel de calidad del video (0-100). Valor predeterminado: 75.
- `--overwrite`, `-w`: Sobrescribe el archivo de salida si ya existe.
- `--delete-original`, `-d`: Elimina el video original después de la compresión exitosa.
- `--verbose`, `-v`: Habilita el modo de depuración para obtener más información durante el proceso.

## Ejemplos de uso

Para comprimir un video llamado `video.mp4`, simplemente ejecuta:

```console
pack video.mp4
```

Este comando comprimirá `video.mp4` con los ajustes predeterminados (calidad: 75) y guardará el resultado como `video_compressed.mp4` en el mismo directorio.

<details>
    <summary>Ver más ejemplos</summary>

### Especificar un archivo de salida

Si deseas especificar el nombre o la ubicación del archivo comprimido:

```console
pack video.mp4 --output compressed/small_video.mp4
```

Este comando comprimirá `video.mp4` y guardará el resultado como `small_video.mp4` en el directorio `compressed`.

### Ajustar la calidad de la compresión

Para comprimir un video con una calidad específica (por ejemplo, 60):

``` console
pack video.mp4 -q 60
```

Esto comprimirá el video con menor calidad, resultando en un archivo más pequeño.

### Comprimir todos los videos en un directorio

Para comprimir todos los videos en un directorio:

```console
pack /ruta/a/mis/videos
```

Este comando comprimirá todos los videos en el directorio especificado y guardará los resultados en el mismo directorio.

### Sobrescribir archivos existentes

Si deseas sobrescribir archivos comprimidos existentes:

```console
pack video.mp4 --output output.mp4 --overwrite
```

Esto sobrescribirá el archivo `output.mp4` si ya existe.

### Eliminar el archivo original después de la compresión

Para eliminar el archivo de video original después de una compresión exitosa:

```console
pack video.mp4 --delete-original
```

El archivo original `video.mp4` será eliminado después de la compresión.

### Usar múltiples opciones

Puedes combinar múltiples opciones en un solo comando:

```console
pack video.mp4 -o compressed.mp4 -q 80 -w -d -v
```

Este comando comprimirá `video.mp4` con una calidad de 80, guardará el resultado como `compressed.mp4`, sobrescribirá el archivo si existe, eliminará el original y mostrará información detallada durante el proceso.

</details>

## Notas adicionales

- La opción de calidad (`-q`) afecta tanto la calidad visual como el tamaño del archivo. Un valor más bajo resultará en un archivo más pequeño pero con menor calidad visual, mientras que un valor más alto mantendrá mejor calidad pero con un archivo más grande.
- Siempre es recomendable hacer una copia de seguridad de tus videos originales antes de usar la opción de eliminación (`-d`).
- El modo detallado (`-v`) es útil para diagnosticar problemas o entender mejor el proceso de compresión.

> [!TIP]
> Si eres usuario de Windows, puedes instalar `ffmpeg` y `python` manualmente o usando gestores de paquetes como [*`Scoop`*][scoop].
> Una vez que hayas instalado un gestor de paquetes, solo debes ejecutar algo como `scoop install python ffmpeg`.

## Contribuidores

<a href="https://github.com/ivansaul/CLI-Video-Compressor/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=ivansaul%2FCLI%2DVideo%2DCompressor"/>
</a>

## Mira mis otros proyectos

[![Bookmark Style Card](https://svg.bookmark.style/api?url=https://github.com/ivansaul/codigo_facilito_downloader&mode=light&style=horizontal)](https://github.com/ivansaul/codigo_facilito_downloader)
[![Bookmark Style Card](https://svg.bookmark.style/api?url=https://github.com/ivansaul/personal-portfolio&mode=light&style=horizontal)](https://github.com/ivansaul/personal-portfolio)
[![Bookmark Style Card](https://svg.bookmark.style/api?url=https://github.com/ivansaul/flutter_todo_app&mode=light&style=horizontal)](https://github.com/ivansaul/flutter_todo_app)

[python]:https://www.python.org/downloads/
[ffmpeg]:https://ffmpeg.org
[demo]:https://github.com/user-attachments/assets/9c9c672a-bfa3-418a-b7d1-89f0e7751146
[scoop]:https://scoop.sh
