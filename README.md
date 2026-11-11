# NASA Space Mission Control

NASA Space Mission Control is a small terminal-based Python project that connects to NASA's public APIs and lets you explore the Astronomy Picture of the Day (APOD) from the command line.

This project is designed for quick access to NASA space imagery and metadata without opening a browser. It can display:

- Today's APOD
- Today's APOD with a terminal image preview
- APOD for a specific date
- APOD for a specific date with a terminal image preview

It is a simple CLI app built with Python, `requests`, `rich`, and `rich-pixels`.

## What the project does

The app shows a menu in the terminal and lets the user choose a NASA APOD action.

Available options:

1. Today's APOD
2. Today's APOD with image
3. APOD by date
4. APOD by date with image
0. Exit

When a user selects an option, the program requests data from NASA's APOD API and prints the title, date, image URL, and permalink. If image mode is enabled, it also renders the image in the terminal.

## Project structure

- `main.py` – command-line menu and app flow
- `config.py` – API configuration and environment loading
- `services/adop.py` – NASA APOD fetching and image display logic
- `requirements.txt` – Python dependencies
- `.env` – local environment file containing your NASA API key

## Features

- Easy NASA APOD lookup from the terminal
- Date-based APOD queries
- Option to display an image preview in the terminal
- Lightweight setup using a virtual environment
- Uses environment variables for secure API key storage

## Installation

1. Clone the repository:

```bash
git clone <your-repository-url>
cd NASA-Space-missioon-control
```

2. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your NASA API key:

```env
NASA_API_KEY=your_nasa_api_key_here
```

You can get a free API key from NASA's API portal.

## Run the project

Start the app with:

```bash
python main.py
```

You will see a menu like this:

```text
1.Today’s APOD
2.Today’s APOD with image
3.APOD by date
4.APOD by date with image
0.Exit
```

Then choose a number and follow the prompt.

## Sample output

Example output from the program:

```text
1.Today’s APOD
2.Today’s APOD with image
3.APOD by date
4.APOD by date with image
0.Exit

> 1
=========================================================================================
Title: Mars in Motion
Date: 2026-11-11
Image Link: https://example.com/space-image.jpg
Permalink: https://apod.nasa.gov/apod/astropix.html
```

If you choose an image option, the terminal will also render the image in a pixel-art style before or after the metadata output.

## Notes

- The app expects a valid `NASA_API_KEY` in the `.env` file.
- The project is intended as a small educational or personal CLI project for exploring NASA data.
- The interface is simple and works well for quick astronomy lookups from a terminal.

## Requirements

The project dependencies are listed in `requirements.txt`, including:

- `requests`
- `python-dotenv`
- `rich`
- `rich-pixels`
- `Pillow`

## License

This project is for personal or learning use unless a different license is added by the repository owner.
