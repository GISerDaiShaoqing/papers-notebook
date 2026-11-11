# Dai_PNS · Paper Note Studio

Dai_PNS (Paper Note Studio) is a cross-platform workspace for reading papers and maintaining the research notes in this repository. It includes a publisher DOI shortcut, a local PDF reader with copy/paste and highlight annotations, and a configurable AI drawer for selected-text translation and paper reading.

## Development

Python 3.10 or newer is required. From this directory:

```bash
python -m pip install -e ".[build]"
python -m papernote run --root ..
```

On Windows, the Miniconda interpreter can create the local environment and build `Dai_PNS.exe`:

```powershell
D:\Users\DELL\miniconda3\python.exe -m venv .venv
.venv\Scripts\python.exe -m pip install -e ".[build]"
.\build_exe.ps1
```

The packaged desktop application is `app/dist/Dai_PNS.exe`. The `app/.venv/Scripts/papernote.exe` file is a command-line entry point that expects a subcommand such as `run`; it is not the desktop launcher and closes after printing usage when double-clicked without arguments.

The app detects the repository when launched from the checkout. If it cannot find it, it asks the user to select the repository folder. PDF highlights are saved to a separate copy; the source PDF is left unchanged.

## AI settings

The assistant accepts OpenAI-compatible chat completion endpoints, including OpenAI, DeepSeek, Qwen, Kimi, GLM, and local Ollama services. Configure the base URL, model, and API key in the AI drawer. API keys are stored through the operating system's credential store when available. Text is sent only after the user starts a translation, paper-reading, or chat request.

Long PDFs are read in page-labelled sections and summarized into a Chinese draft using the five complete notes as the format reference. The assistant never writes that draft into a note automatically.

## Cross-platform builds

Build on the current operating system with `python build.py`. GitHub Actions builds Windows x64, macOS Apple Silicon, and Linux x64 artifacts on their respective native runners. Artifacts are attached to the workflow run; publishing a GitHub release remains a separate repository action.

