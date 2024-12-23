import os
import subprocess


def run_script(script_path):
    try:
        print("==========================")
        print(f"Running: {script_path}\n")
        result = subprocess.run(
            ["python", script_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8"
        )

        if result.stderr:
            print(f"Errors from {script_path}:\n{result.stderr}")

    except Exception as e:
        print(f"Failed to run {script_path}: {e}")


def display_txt_files(task_dir):
    """
    Находит и выводит содержимое txt/input.txt и txt/output.txt, если они существуют.
    """
    txt_dir = os.path.join(task_dir, "txtf")
    input_file = os.path.join(txt_dir, "input.txt")
    output_file = os.path.join(txt_dir, "output.txt")

    if os.path.exists(input_file):
        print("\nContents of input:\n")
        with open(input_file, "r", encoding="utf-8") as f:
            print(f.read())

    if os.path.exists(output_file):
        print("\nContents of output:\n")
        with open(output_file, "r", encoding="utf-8") as f:
            print(f.read())


def main():
    run_all_file = "run_all.bat"
    with open(run_all_file, 'r') as f:
        lines = f.readlines()

    scripts = [line.strip() for line in lines if line.strip()]
    for script in scripts:
        run_script(script)
        task_dir = os.path.dirname(os.path.dirname(script))
        display_txt_files(task_dir)


if __name__ == "__main__":
    main()
