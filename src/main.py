"""Point d'entrée."""

from collector import get_system_info
from formatter import save_report


def main():
    print("🔍 Scanning system...")
    info = get_system_info()
    
    print(f"OS: {info['platform']['system']} {info['platform']['release']}")
    print(f"CPU: {info['cpu']['usage_percent']}% used")
    print(f"RAM: {info['memory']['usage_percent']}% used")
    print(f"disk: {info['disk']['usage_percent']}% used")
    
    filepath = save_report(info)
    print(f"\n Report saved: {filepath}")


if __name__ == "__main__":
    main()