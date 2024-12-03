# Windows ENV Variable

### Modify PATH Environment Variable (if needed)

Add python.exe location:

- Step 1: Open the Environment Variables as described earlier.
- Step 2: Under System Variables, select the Path variable and click Edit.
- Step 3: Add the path to the folder where python.exe is located
  (usually in a directory like C:\Users\user\AppData\Local\Programs\Python\Python3x\).

# VS Code ENV Setup

### Setting Up Python in VS Code Terminal

If Python works in Command Prompt but not in PowerShell within VS Code, it might be due to the Python path not being set correctly in the VS Code environment.

### Ensure Python is in VS Code’s PATH

- Open **VS Code** and navigate to the **PowerShell terminal**.
- Run the following command to check the PATH environment variable:
  ```bash
  echo $env:PATH
  ```

### Set the PATH in VS Code Manually

If the above steps don’t work, manually add Python’s path in the VS Code settings:

- Go to File > Preferences > Settings.
- Search for "terminal integrated env".
- Click Edit in settings.json.
- Add Python’s installation path to the environment variables for PowerShell:

```json
"terminal.integrated.env.windows": {
    "PATH": "C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python3x\\;${env:PATH}"
}
```

Replace Python3x with your installed Python version directory.
