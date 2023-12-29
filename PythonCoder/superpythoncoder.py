import subprocess
import random
from programs_list import PROGRAMS_LIST
from colorama import Fore
from tqdm import tqdm

def generate_code(code_request_args):
    return subprocess.run(["/usr/local/bin/python3.10", "generatecode.py"] + code_request_args)

def format_code():
    return subprocess.run(["black", "created_code.py"], stdout=subprocess.DEVNULL)

def run_generated_code():
    return subprocess.run(["/usr/local/bin/python3.10", "created_code.py"], stderr=subprocess.PIPE, stdout=subprocess.PIPE)

def get_generated_code():
    with open("created_code.py", "r") as file:
        return file.read()

def get_code_request_args():
    code_request = input("\nTell me, which program would you like me to code for you?\nIf you don't have an idea,just press enter and I will choose a random program to code\n")
    if not code_request:
        code_request = PROGRAMS_LIST[random.randrange(0, len(PROGRAMS_LIST))]
    return [code_request]

def validate_generated_code(result):
    if result.returncode == 0:
        print(Fore.GREEN + "Code creation completed successfully !")
        format_code()
        subprocess.call(["open", "created_code.py"])
        return True
    else:
        print(Fore.YELLOW + f"Error running generated code! error: {result.stderr}")
        return False

def main():
    code_request_args = get_code_request_args()
    succeeded = False
    for item in tqdm(range(5), desc="Processing", unit="try"):
        generate_code(code_request_args)
        result = run_generated_code()
        succeeded = validate_generated_code(result)
        if succeeded:
            return
        generated_code = get_generated_code()
        code_request_args.append(generated_code)
        code_request_args.append(result.stderr)

    print(Fore.RED + "Code generation FAILED")

main()



