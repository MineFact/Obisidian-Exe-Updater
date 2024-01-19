

This ObsidianUpdater is used to automatically update the official Obsidian.1.X.X.exe file.<br> It fetches the latest release from GitHub, downloads it, and replaces the old executable. <br>If no Obsidian*.exe is found it downloads the latest one.

## Installation

1. Download the ObisdianUpdater.exe from releases
2. Put the updater in the same folder that the Obsidian*.exe is in.
3. Run the ObsidianUpdater.exe. It should search for the latest release and replace the old Obsidian*.exe with the new one.

## Dependencies

This script requires the `glob`, `shutil`, `sys`, and `requests` Python libraries.

If the required libraries are not installed, you can install them using pip, the Python package installer. Run the following command in your terminal:

```bash
pip install glob2 shutil sys requests
```

## Contributing

Contributions are welcome! Here are the steps to contribute:

1. Fork the repository on GitHub.
2. Clone the forked repository to your local machine.
3. Make your changes in a new branch.
4. Test your changes to ensure they are correct.
5. Commit your changes and push the branch to your GitHub repository.
6. Create a new pull request from your forked repository to the original repository.

Please make sure to update tests as appropriate and follow the coding style conventions of the project.

## Note

1. This script assumes that the Obsidian releases are hosted on GitHub and that the executable is named in the format `Obsidian*.exe`. If the hosting service or naming convention changes, the script may need to be updated.
2. Currently only a Windows exe is included in the realease. If you want to have an executable for another operating system you can create it yourself by cloning the repository and using pyinstaller to create an executable for your operating system:
```bash
pyinstaller --onefile --icon=updater.ico --name ObsidianUpdater updater.py
```
