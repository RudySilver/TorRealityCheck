#!/usr/bin/env python3
import os
import sys
import subprocess
import socket

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
BOLD = "\033[1m"
RESET = "\033[0m"

def banner():
    print(f"""
{BOLD}============================================================
TOR MYTH BREAKER
Because believing marketing is not OPSEC
============================================================{RESET}
""")

def check_tor_process():
    try:
        out = subprocess.check_output(["pgrep", "-x", "tor"], stderr=subprocess.DEVNULL)
        return bool(out.strip())
    except subprocess.CalledProcessError:
        return False

def check_routing():
    try:
        routes = subprocess.check_output(["ip", "route"], text=True)
        for line in routes.splitlines():
            if line.startswith("default"):
                return False, line
        return True, None
    except Exception as e:
        return False, str(e)

def check_ipv6():
    try:
        with open("/proc/sys/net/ipv6/conf/all/disable_ipv6") as f:
            return f.read().strip() == "1"
    except Exception:
        return False

def main():
    banner()

    tor_running = check_tor_process()

    print(f"{BOLD}CHECK 1  Tor Process{RESET}")
    if tor_running:
        print(f"{GREEN}[OK]{RESET} Tor is running")
    else:
        print(f"{RED}[FAIL]{RESET} Tor is NOT running")
        print("You are not anonymous.")
        print("You are not even *trying*.")
        print("\nVerdict: You don’t need Tor myths  you need Tor itself.")
        sys.exit(1)

    print(f"\n{BOLD}CHECK 2  Traffic Routing{RESET}")
    routed, route_info = check_routing()
    if routed:
        print(f"{GREEN}[OK]{RESET} No obvious clearnet default route detected")
    else:
        print(f"{RED}[FAIL]{RESET} Traffic bypasses Tor")
        print(f"Route: {route_info}")

    print(f"\n{BOLD}CHECK 3  IPv6 Leakage{RESET}")
    ipv6_disabled = check_ipv6()
    if ipv6_disabled:
        print(f"{GREEN}[OK]{RESET} IPv6 disabled")
    else:
        print(f"{RED}[FAIL]{RESET} IPv6 is ENABLED")
        print("Tor does NOT protect IPv6.")
        print("Congrats, you leaked without knowing.")

    print(f"\n{BOLD}============================================{RESET}")

    if tor_running and (not routed or not ipv6_disabled):
        print(f"""{RED}{BOLD}
VERDICT: TOR MYTH CONFIRMED ❌

Tor is running.
You are NOT anonymous.

Tor hides paths, not your system.
Your setup leaks like a 70yo Mom.
Your confidence is the vulnerability.

I didn’t say this.
Your network did.
{RESET}""")
        sys.exit(2)

    print(f"""{GREEN}{BOLD}
VERDICT: BASIC TOR ISOLATION ✅

No obvious leaks detected.
This does NOT mean you are safe.

Tor is not magic.
Believing it is that’s how people get caught.
{RESET}""")

if __name__ == "__main__":
    main()
