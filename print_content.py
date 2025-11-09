import os

# Base directory: project root
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Output file
output_file = os.path.join(BASE_DIR, "project_files_content.txt")

# File extensions to include
include_files = (".py",)

# Directories to skip
skip_dirs = ("__pycache__", ".venv")
important_files = ("settings.py", "urls.py", "wsgi.py", "asgi.py",
                   "models.py", "views.py", "admin.py","docker-compose.prod.yml","init_ssl.sh" ,"docker-compose.yml" ,"apps.py", "middleware.py", "tenant_header_middleware.py", "Dockerfile", "docker-compose.yml", "default-local.conf "," default-prod.conf")


with open(output_file, "w", encoding="utf-8") as f_out:
    for root, dirs, files in os.walk(BASE_DIR):
        # Skip unwanted directories
        dirs[:] = [d for d in dirs if d not in skip_dirs]

        for file in files:
            if   file in important_files:
                file_path = os.path.join(root, file)
                f_out.write(f"--- FILE: {file_path} ---\n\n")
                
                try:
                    with open(file_path, "r", encoding="utf-8") as f_in:
                        content = f_in.read()
                        f_out.write(content + "\n\n")
                except Exception as e:
                    f_out.write(f"Error reading file: {e}\n\n")

print(f"Export completed! Check the file: {output_file}")
