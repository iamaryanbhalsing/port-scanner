import socket
import threading
import sys
import argparse

def scan_port(target, port, open_ports):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # 1 second timeout
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    except:
        pass

def port_scanner(target, start_port, end_port):
    print(f"Scanning {target} from port {start_port} to {end_port}...")
    open_ports = []
    threads = []
    
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(target, port, open_ports))
        threads.append(thread)
        thread.start()
        
        # Limit number of threads to avoid overwhelming the system
        if len(threads) >= 100:
            for t in threads:
                t.join()
            threads = []
    
    # Join remaining threads
    for t in threads:
        t.join()
    
    open_ports.sort()
    if open_ports:
        print("Open ports found:")
        for port in open_ports:
            try:
                service = socket.getservbyport(port)
                print(f"Port {port}: {service}")
            except:
                print(f"Port {port}: Unknown service")
    else:
        print("No open ports found in the specified range.")
    
    return open_ports

def main():
    parser = argparse.ArgumentParser(description="Simple Port Scanner")
    parser.add_argument("target", nargs="?", help="Target IP address (e.g., 127.0.0.1)")
    parser.add_argument("-s", "--start", type=int, default=1, help="Start port (default: 1)")
    parser.add_argument("-e", "--end", type=int, default=100, help="End port (default: 100)")
    
    args = parser.parse_args()
    
    if not args.target:
        print("=== Simple Port Scanner ===")
        target = input("Enter target IP address (e.g., 127.0.0.1): ").strip()
        try:
            start_port = int(input("Enter start port (1-65535) [default 1]: ") or 1)
            end_port = int(input("Enter end port (start-65535) [default 100]: ") or 100)
        except ValueError:
            print("Invalid input! Ports must be numbers.")
            sys.exit(1)
    else:
        target = args.target
        start_port = args.start
        end_port = args.end
    
    if start_port < 1 or end_port > 65535 or start_port > end_port:
        print("Invalid port range!")
        sys.exit(1)
    
    port_scanner(target, start_port, end_port)

if __name__ == "__main__":
    main()
