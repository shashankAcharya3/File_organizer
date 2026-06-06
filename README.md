<div align="center">

# File Organizer

**An automated utility script for managing clutter and structuring local directories.**

<a href="https://github.com/shashankAcharya3/File_organizer/commits/main">
<img src="https://img.shields.io/badge/Maintained-Yes-151515.svg?style=flat-square" alt="Maintained">
</a>
<a href="https://github.com/shashankAcharya3/File_organizer/blob/main/LICENSE">
<img src="https://img.shields.io/badge/License-MIT-151515.svg?style=flat-square" alt="License">
</a>
<img src="https://img.shields.io/badge/Language-Python-151515.svg?style=flat-square" alt="Python">

</div>

---

### Overview

This repository contains a streamlined **File Organizer** designed to clean up cluttered directories (such as a local Downloads or Desktop folder) by automatically sorting files into designated sub-directories based on their file extensions. 

### Core Features

- **Automated Sorting:** Instantly categorizes files into standard folders (e.g., Documents, Images, Videos, Audio, Archives).
- **Customizable Logic:** Easily extendable to include custom file extensions and specialized target directories.
- **Cross-Platform:** Built using standard native libraries, ensuring compatibility across Windows, macOS, and Linux systems without heavy external dependencies.
- **Safe Execution:** Implements base-level conflict resolution to prevent accidental overwriting of files with identical names.

### System Architecture & Tech Stack

- **Language**: Python
- **Core Libraries**: `os`, `shutil`, `pathlib`

### Getting Started

To utilize the file organizer on your local machine, ensure you have Python 3.8+ installed. You can set up and run the script immediately using the combined commands below.

```bash
# 1. Clone the repository and navigate inside
git clone [https://github.com/shashankAcharya3/File_organizer.git](https://github.com/shashankAcharya3/File_organizer.git)
cd File_organizer

# 2. Review and configure the target directory
# Open the main script to set or verify the path of the folder you want to organize.

# 3. Execute the organizer script
python main.py
