import subprocess
import os
import sys
import platform

def install_ffmpeg():
    if platform.system() == "Linux":
        print("Installing ffmpeg for Ubuntu/Linux...")
        subprocess.check_call(['sudo', 'apt-get', 'update'])
        subprocess.check_call(['sudo', 'apt-get', 'install', 'ffmpeg', '-y'])

def setup_venv():
    venv_dir = "taichi_env"
    # Check the operating system to determine the correct path for the virtual environment's scripts
    if sys.platform == "win32":
        venv_bin_path = os.path.join(venv_dir, 'Scripts')
        python_executable = "python.exe"
        pip_executable = "pip.exe"
    else:
        venv_bin_path = os.path.join(venv_dir, 'bin')
        python_executable = "python3"
        pip_executable = "pip"

    if not os.path.exists(venv_dir):
        print("Creating virtual environment...")
        subprocess.check_call([python_executable, '-m', 'venv', venv_dir])

    pip_path = os.path.join(venv_bin_path, pip_executable)
    print("Installing dependencies from requirements.txt...")
    subprocess.check_call([pip_path, 'install', '-r', 'requirements.txt'])
    return venv_bin_path, python_executable

def run_script_in_venv(venv_bin_path, python_executable, script_path):
    python_path = os.path.join(venv_bin_path, python_executable)
    print(f"Running script {script_path} in the virtual environment...")
    subprocess.check_call([python_path, script_path])

if __name__ == "__main__":
    # Install ffmpeg before setting up the venv, as it's a system package not a Python package
    install_ffmpeg()

    venv_bin_path, python_executable = setup_venv()
    working_scripts = [
        'main.py',
    ]
    for script_path in working_scripts:
        run_script_in_venv(venv_bin_path, python_executable, script_path)
