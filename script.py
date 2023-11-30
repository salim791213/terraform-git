import subprocess
import sys

nom_du_repo = sys.argv[1] if len(sys.argv) > 1 else "default_repo_name"
subprocess.run(["terraform", "apply", "-auto-approve", "-var", f"nom_du_repo={nom_du_repo}"])
