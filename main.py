# Made by Oziris34,
# prohibited to resell, rebrand or use this in any exploitative form for own personal or financial gaini
# 2024 all right reserved





import os
import subprocess
import time
import shutil
from tqdm import tqdm
from colorama import Fore, Style, init
import base64

init()

def cs2_lag_reducer():
    def simulate_step(step_name, duration=3):
        print(f"{Fore.YELLOW}{step_name}{Style.RESET_ALL}")
        for _ in tqdm(range(duration), desc=step_name, unit="s"):
            time.sleep(1)

    def generate_hash():
        data = "CS2LagReducerConfigData"
        hash_bytes = base64.b64encode(data.encode('utf-8'))
        return hash_bytes.decode('utf-8')

    def optimize_system():
        print(f"{Fore.CYAN}Optimizing system settings...{Style.RESET_ALL}")

        if os.name == 'nt':
            try:
                subprocess.run(['powercfg', '/setactive', 'SCHEME_MIN'], check=True)
                print(f"{Fore.GREEN}Power plan set to High Performance.{Style.RESET_ALL}")

                services = ["SysMain", "WSearch"]
                for service in services:
                    subprocess.run(['sc', 'stop', service], check=True)
                    subprocess.run(['sc', 'config', service, 'start=disabled'], check=True)
                    print(f"{Fore.GREEN}Disabled service: {service}.{Style.RESET_ALL}")

            except subprocess.CalledProcessError:
                print(f"{Fore.RED}Failed to apply system optimizations.{Style.RESET_ALL}")

        elif os.name == 'posix':
            try:
                subprocess.run(['sudo', 'cpupower', 'frequency-set', '-g', 'performance'], check=True)
                print(f"{Fore.GREEN}CPU set to performance mode.{Style.RESET_ALL}")
            except subprocess.CalledProcessError:
                print(f"{Fore.RED}Failed to set CPU to performance mode.{Style.RESET_ALL}")

    def optimize_network():
        print(f"{Fore.CYAN}Optimizing network settings...{Style.RESET_ALL}")

        if os.name == 'nt':
            try:
                subprocess.run(['netsh', 'interface', 'tcp', 'set', 'global', 'autotuninglevel=highlyrestricted'], check=True)
                print(f"{Fore.GREEN}Quality of Service (QoS) enabled.{Style.RESET_ALL}")

            except subprocess.CalledProcessError:
                print(f"{Fore.RED}Failed to apply network optimizations.{Style.RESET_ALL}")

        elif os.name == 'posix':
            try:
                subprocess.run(['sudo', 'sysctl', '-w', 'net.ipv4.tcp_tw_reuse=1'], check=True)
                subprocess.run(['sudo', 'sysctl', '-w', 'net.ipv4.tcp_tw_recycle=1'], check=True)
                print(f"{Fore.GREEN}Network settings adjusted.{Style.RESET_ALL}")
            except subprocess.CalledProcessError:
                print(f"{Fore.RED}Failed to apply network optimizations.{Style.RESET_ALL}")

    def clean_temp_files():
        print(f"{Fore.CYAN}Cleaning temporary files...{Style.RESET_ALL}")
        temp_dirs = [
            os.path.join(os.getenv('TEMP', ''), '*'),
            os.path.join(os.getenv('TMP', ''), '*')
        ]
        for temp_dir in temp_dirs:
            try:
                if os.path.isdir(temp_dir):
                    shutil.rmtree(temp_dir, ignore_errors=True)
                else:
                    os.remove(temp_dir)
                print(f"{Fore.GREEN}Temporary files deleted from {temp_dir}.{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}Failed to delete temporary files from {temp_dir}: {e}{Style.RESET_ALL}")

    def set_high_priority(process_name):
        print(f"{Fore.CYAN}Setting CS2 process to high priority...{Style.RESET_ALL}")

        if os.name == 'nt':
            try:
                subprocess.run(['wmic', 'process', 'where', f'name="{process_name}"', 'call', 'setpriority', '128'], check=True)
                print(f"{Fore.GREEN}CS2 process priority set to high.{Style.RESET_ALL}")
            except subprocess.CalledProcessError:
                print(f"{Fore.RED}Failed to set CS2 process priority.{Style.RESET_ALL}")

        elif os.name == 'posix':
            try:
                process_id = subprocess.check_output(['pgrep', process_name]).decode().strip()
                subprocess.run(['sudo', 'renice', '-n', '-10', '-p', process_id], check=True)
                print(f"{Fore.GREEN}CS2 process priority adjusted.{Style.RESET_ALL}")
            except subprocess.CalledProcessError:
                print(f"{Fore.RED}Failed to adjust CS2 process priority.{Style.RESET_ALL}")

    def add_ini_configuration(file_path):
        try:
            with open(file_path, 'w') as file:
                file.write("[LagReducerConfig]\n")
                file.write("OptimizeNetwork=True\n")
                file.write("CleanTempFiles=True\n")
                file.write("HighPriority=True\n")
                file.write(f"Hash={generate_hash()}\n")
            print(f"{Fore.GREEN}Configuration file added successfully!{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Failed to add configuration file: {e}{Style.RESET_ALL}")

    print(f"{Fore.CYAN}CS2 Lag Reducer made by Trnwrck{Style.RESET_ALL}")
    time.sleep(3)
    
    a = input("Is CS2 opened and running? (yes/no): ").strip().lower()
    
    if a == "yes":
        print(f"{Fore.YELLOW}Locating...{Style.RESET_ALL}")
        time.sleep(3)
        print(f"{Fore.GREEN}Located!{Style.RESET_ALL}")
        time.sleep(3)

        simulate_step("Adding .ini configuration file")
        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        config_file_path = os.path.join(script_dir, "CS2_LagReducer.ini")
        
        add_ini_configuration(config_file_path)
        
        simulate_step("Optimizing system settings")
        optimize_system()
        
        simulate_step("Optimizing network settings")
        optimize_network()
        
        simulate_step("Cleaning temporary files")
        clean_temp_files()
        
        simulate_step("Setting high priority for CS2 process")
        set_high_priority("cs2.exe")
        
        print(f"{Fore.CYAN}All optimizations completed! Enjoy a smoother gaming experience!{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Please open CS2 and run this script again.{Style.RESET_ALL}")

if __name__ == "__main__":
    cs2_lag_reducer()
