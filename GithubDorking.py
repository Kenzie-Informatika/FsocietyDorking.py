#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔═══════════════════════════════════════════════════════════════════╗
║              FSOCIETY RANSOMWARE v8.0 - ULTIMATE EDITION          ║
║                    HACK BY KENZIE                                 ║
╠═══════════════════════════════════════════════════════════════════╣
║     PRIVATE - FOR AUTHORIZED USE ONLY                             ║
║     UNAUTHORIZED ACCESS IS PROHIBITED                             ║
╚═══════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import time
import random
import ctypes
import threading
import tkinter as tk
from tkinter import ttk
from ctypes import wintypes

# ==================== PASSWORD ====================
SIM_PASSWORD = "kenzie6688"
MAX_ATTEMPTS = 3

# ==================== WINDOWS API ====================
user32 = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32

SW_MAXIMIZE = 3
SW_HIDE = 0
SW_SHOW = 5

SCREEN_WIDTH = user32.GetSystemMetrics(0)
SCREEN_HEIGHT = user32.GetSystemMetrics(1)

# ==================== THEME COLORS ====================
THEME = {
    'bg_primary': '#0a0a12',
    'bg_secondary': '#12121c',
    'bg_tertiary': '#1a1a24',
    'fg_primary': '#ff3366',
    'fg_secondary': '#00ffcc',
    'fg_accent': '#ffcc00',
    'fg_text': '#e0e0e0',
    'fg_dim': '#8888a0',
    'border_primary': '#ff3366',
    'border_secondary': '#00ffcc',
    'border_accent': '#ffcc00',
    'success': '#00ff99',
    'error': '#ff3366',
    'warning': '#ffaa00'
}

# ==================== ASCII ART ====================
FSOCIETY_LOGO = """
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    ░░  ███████╗███████╗ ██████╗  ██████╗██╗███████╗████████╗██╗   ██╗  ░░░░░░░░░░░░
    ░░  ██╔════╝██╔════╝██╔═══██╗██╔════╝██║██╔════╝╚══██╔══╝╚██╗ ██╔╝  ░░░░░░░░░░░░
    ░░  █████╗  ███████╗██║   ██║██║     ██║█████╗     ██║    ╚████╔╝   ░░░░░░░░░░░░
    ░░  ██╔══╝  ╚════██║██║   ██║██║     ██║██╔══╝     ██║     ╚██╔╝    ░░░░░░░░░░░░
    ░░  ██║     ███████║╚██████╔╝╚██████╗██║███████╗   ██║      ██║     ░░░░░░░░░░░░
    ░░  ╚═╝     ╚══════╝ ╚═════╝  ╚═════╝╚═╝╚══════╝   ╚═╝      ╚═╝     ░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                             H A C K   B Y  K E N Z I E
"""

# ==================== SYSTEM FILES ====================
SYSTEM_FILES = [
    ("ntoskrnl.exe", "NT Kernel & System", "12,847 KB"),
    ("winload.exe", "Windows Boot Loader", "1,234 KB"),
    ("hal.dll", "Hardware Abstraction Layer", "845 KB"),
    ("ntdll.dll", "NT Layer DLL", "2,156 KB"),
    ("kernel32.dll", "Windows Kernel API", "1,892 KB"),
    ("user32.dll", "Windows User API", "1,456 KB"),
    ("gdi32.dll", "Graphics Device Interface", "1,234 KB"),
    ("advapi32.dll", "Advanced API Services", "987 KB"),
    ("shell32.dll", "Windows Shell", "3,456 KB"),
    ("ole32.dll", "Object Linking & Embedding", "1,567 KB"),
    ("comctl32.dll", "Common Controls", "2,345 KB"),
    ("ws2_32.dll", "Winsock API", "678 KB"),
    ("dnsapi.dll", "DNS Client API", "789 KB"),
    ("iphlpapi.dll", "IP Helper API", "456 KB"),
    ("wininet.dll", "Internet API", "1,234 KB"),
    ("crypt32.dll", "Cryptography API", "1,567 KB"),
    ("wintrust.dll", "Trust Verification", "678 KB"),
    ("setupapi.dll", "Setup API", "1,345 KB"),
    ("mscoree.dll", ".NET Runtime", "567 KB"),
    ("mscorlib.dll", ".NET Library", "4,567 KB"),
    ("clbcatq.dll", "Component Category", "345 KB"),
    ("oleaut32.dll", "OLE Automation", "1,234 KB"),
    ("shlwapi.dll", "Shell Light API", "789 KB"),
    ("version.dll", "Version Checking", "234 KB"),
    ("winmm.dll", "Multimedia API", "567 KB"),
    ("ntfs.sys", "NTFS File System", "1,234 KB"),
    ("tcpip.sys", "TCP/IP Stack", "987 KB"),
    ("ndis.sys", "Network Driver", "756 KB"),
    ("volmgr.sys", "Volume Manager", "543 KB"),
    ("disk.sys", "Disk Driver", "432 KB"),
    ("usbhub.sys", "USB Hub Driver", "654 KB"),
    ("kbdclass.sys", "Keyboard Class", "234 KB"),
    ("mouclass.sys", "Mouse Class", "234 KB"),
    ("monitor.sys", "Monitor Driver", "345 KB"),
    ("partmgr.sys", "Partition Manager", "456 KB"),
    ("volsnap.sys", "Volume Snapshot", "567 KB"),
]

# ==================== PASSWORD DIALOG ====================
class PasswordDialog:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("")
        self.root.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}+0+0")
        self.root.configure(bg=THEME['bg_primary'])
        self.root.overrideredirect(True)
        self.root.attributes('-topmost', True)
        
        self.result = None
        self.attempts = 0
        self.create_ui()
        
    def create_ui(self):
        # Gradient overlay effect
        overlay = tk.Frame(self.root, bg=THEME['bg_primary'])
        overlay.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        # Main content container
        center_x = SCREEN_WIDTH // 2 - 350
        center_y = SCREEN_HEIGHT // 2 - 300
        
        main_container = tk.Frame(overlay, bg=THEME['bg_secondary'], 
                                  width=700, height=600)
        main_container.place(x=center_x, y=center_y)
        
        # Glow effect (multiple borders)
        for i in range(3):
            glow = tk.Frame(main_container, bg=THEME['border_primary'] if i == 0 else THEME['bg_secondary'], 
                           width=700 - (i*4), height=600 - (i*4))
            glow.place(x=i*2, y=i*2)
        
        # Content frame
        content = tk.Frame(main_container, bg=THEME['bg_secondary'])
        content.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)
        
        # Logo with gradient effect
        logo_lines = FSOCIETY_LOGO.split('\n')
        y_pos = 30
        for line in logo_lines:
            if line.strip():
                label = tk.Label(content, text=line, bg=THEME['bg_secondary'],
                                fg=THEME['fg_primary'], font=('Consolas', 12, 'bold'))
                label.place(x=20, y=y_pos)
                y_pos += 20
        
        # Title
        title = tk.Label(content, text="AUTHENTICATION REQUIRED",
                        bg=THEME['bg_secondary'], fg=THEME['fg_secondary'],
                        font=('Segoe UI', 18, 'bold'))
        title.place(x=180, y=250)
        
        # Attempts counter
        self.attempts_label = tk.Label(content, 
                                      text=f"ATTEMPTS: {self.attempts}/{MAX_ATTEMPTS}",
                                      bg=THEME['bg_secondary'], fg=THEME['fg_accent'],
                                      font=('Segoe UI', 12))
        self.attempts_label.place(x=280, y=300)
        
        # Password entry
        entry_bg = tk.Frame(content, bg=THEME['border_secondary'], width=300, height=45)
        entry_bg.place(x=200, y=350)
        
        self.password_var = tk.StringVar()
        password_entry = tk.Entry(entry_bg, textvariable=self.password_var,
                                  bg=THEME['bg_tertiary'], fg=THEME['fg_secondary'],
                                  font=('Consolas', 12, 'bold'),
                                  show='●', width=30,
                                  relief='flat', bd=5,
                                  insertbackground=THEME['fg_secondary'])
        password_entry.place(x=2, y=2, width=296, height=41)
        password_entry.focus()
        password_entry.bind('<Return>', lambda e: self.check_password())
        
        # Message label
        self.message_label = tk.Label(content, text="",
                                       bg=THEME['bg_secondary'], fg=THEME['error'],
                                       font=('Segoe UI', 10))
        self.message_label.place(x=200, y=405)
        
        # Buttons
        # OK Button
        ok_bg = tk.Frame(content, bg=THEME['border_secondary'], width=120, height=40)
        ok_bg.place(x=200, y=450)
        
        ok_btn = tk.Button(ok_bg, text="AUTHENTICATE",
                          bg=THEME['bg_tertiary'], fg=THEME['fg_secondary'],
                          activebackground=THEME['border_secondary'],
                          activeforeground=THEME['bg_primary'],
                          font=('Segoe UI', 10, 'bold'),
                          relief='flat', bd=0,
                          command=self.check_password)
        ok_btn.place(x=2, y=2, width=116, height=36)
        
        # Cancel Button
        cancel_bg = tk.Frame(content, bg=THEME['border_primary'], width=120, height=40)
        cancel_bg.place(x=340, y=450)
        
        cancel_btn = tk.Button(cancel_bg, text="DELETE BIOS",
                              bg=THEME['bg_tertiary'], fg=THEME['fg_primary'],
                              activebackground=THEME['border_primary'],
                              activeforeground=THEME['bg_primary'],
                              font=('Segoe UI', 10, 'bold'),
                              relief='flat', bd=0,
                              command=self.cancel)
        cancel_btn.place(x=2, y=2, width=116, height=36)
        
        # System info
        sys_info = [
            "SYSTEM ENCRYPTED",
            "ACCESS LEVEL: 0",
            "ENCRYPTION: AES-256",
            "STATUS: LOCKED"
        ]
        
        y_info = 510
        for info in sys_info:
            label = tk.Label(content, text=info,
                            bg=THEME['bg_secondary'], fg=THEME['fg_dim'],
                            font=('Consolas', 9))
            label.place(x=270, y=y_info)
            y_info += 20
        
    def check_password(self):
        entered = self.password_var.get()
        
        if entered == SIM_PASSWORD:
            self.result = "EXIT"
            self.root.destroy()
        else:
            self.attempts += 1
            self.attempts_label.config(text=f"ATTEMPTS: {self.attempts}/{MAX_ATTEMPTS}")
            
            if self.attempts >= MAX_ATTEMPTS:
                self.message_label.config(text="SECURITY PROTOCOL ACTIVATED", fg=THEME['warning'])
                self.root.after(1000, self.launch_ransomware)
            else:
                self.message_label.config(
                    text=f"INVALID CREDENTIALS - {MAX_ATTEMPTS - self.attempts} REMAINING",
                    fg=THEME['error'])
                self.password_var.set("")
                
    def launch_ransomware(self):
        self.result = "RANSOMWARE"
        self.root.destroy()
        
    def cancel(self):
        self.result = "CANCEL"
        self.root.destroy()
        
    def show(self):
        self.root.mainloop()
        return self.result

# ==================== RANSOMWARE APP ====================
class RansomwareApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("")
        self.root.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}+0+0")
        self.root.configure(bg=THEME['bg_primary'])
        self.root.overrideredirect(True)
        self.root.attributes('-topmost', True)
        
        self.files_found = []
        self.encrypted_count = 0
        self.total_files = len(SYSTEM_FILES) * 2
        
        self.create_ui()
        self.start_scan()
        
    def create_ui(self):
        # Main container dengan glow effect
        main_container = tk.Frame(self.root, bg=THEME['bg_primary'])
        main_container.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        # Header dengan gradient
        header = tk.Frame(main_container, bg=THEME['bg_secondary'], height=100)
        header.place(relx=0, rely=0, relwidth=1)
        
        # Logo kecil
        logo_lines = FSOCIETY_LOGO.split('\n')[:3]
        y_pos = 10
        for line in logo_lines:
            if line.strip():
                label = tk.Label(header, text=line, bg=THEME['bg_secondary'],
                                fg=THEME['fg_primary'], font=('Consolas', 10, 'bold'))
                label.place(x=20, y=y_pos)
                y_pos += 15
        
        # Title
        title = tk.Label(header, text="FSOCIETY ENCRYPTION PROTOCOL",
                        bg=THEME['bg_secondary'], fg=THEME['fg_secondary'],
                        font=('Segoe UI', 16, 'bold'))
        title.place(x=SCREEN_WIDTH//2 - 150, y=35)
        
        # Status indicator
        status_frame = tk.Frame(header, bg=THEME['bg_tertiary'], width=150, height=30)
        status_frame.place(x=SCREEN_WIDTH-180, y=35)
        
        status_dot = tk.Frame(status_frame, bg=THEME['success'], width=10, height=10)
        status_dot.place(x=10, y=10)
        
        status_text = tk.Label(status_frame, text="ACTIVE", bg=THEME['bg_tertiary'],
                              fg=THEME['success'], font=('Segoe UI', 10, 'bold'))
        status_text.place(x=30, y=5)
        
        # Main content area
        content = tk.Frame(main_container, bg=THEME['bg_primary'])
        content.place(relx=0.02, rely=0.12, relwidth=0.96, relheight=0.8)
        
        # LEFT PANEL - File list
        left_panel = tk.Frame(content, bg=THEME['bg_secondary'], width=SCREEN_WIDTH-400)
        left_panel.pack(side='left', fill='both', expand=True, padx=(0,10))
        left_panel.pack_propagate(False)
        
        # Panel title
        list_title = tk.Frame(left_panel, bg=THEME['bg_tertiary'], height=40)
        list_title.pack(fill='x')
        
        title_text = tk.Label(list_title, text="█ ENCRYPTED SYSTEM FILES",
                              bg=THEME['bg_tertiary'], fg=THEME['fg_secondary'],
                              font=('Consolas', 12, 'bold'))
        title_text.place(x=20, y=10)
        
        # File list container dengan scroll
        list_container = tk.Frame(left_panel, bg=THEME['bg_secondary'])
        list_container.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Canvas untuk scroll
        canvas = tk.Canvas(list_container, bg=THEME['bg_secondary'],
                          highlightthickness=0)
        canvas.pack(side='left', fill='both', expand=True)
        
        scrollbar = tk.Scrollbar(list_container, orient='vertical',
                                 command=canvas.yview,
                                 bg=THEME['bg_tertiary'])
        scrollbar.pack(side='right', fill='y')
        
        canvas.configure(yscrollcommand=scrollbar.set)
        
        self.file_frame = tk.Frame(canvas, bg=THEME['bg_secondary'])
        canvas.create_window((0, 0), window=self.file_frame, anchor='nw')
        
        self.file_frame.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
        
        # RIGHT PANEL - Progress
        right_panel = tk.Frame(content, bg=THEME['bg_secondary'], width=350)
        right_panel.pack(side='right', fill='y')
        right_panel.pack_propagate(False)
        
        # Progress section
        progress_frame = tk.Frame(right_panel, bg=THEME['bg_tertiary'])
        progress_frame.pack(fill='x', padx=15, pady=15)
        
        progress_title = tk.Label(progress_frame, text="█ ENCRYPTION PROGRESS",
                                  bg=THEME['bg_tertiary'], fg=THEME['fg_accent'],
                                  font=('Consolas', 11, 'bold'))
        progress_title.pack(pady=(10,5))
        
        self.progress_var = tk.DoubleVar()
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("red.Horizontal.TProgressbar",
                       background=THEME['fg_primary'],
                       troughcolor=THEME['bg_primary'],
                       bordercolor=THEME['bg_tertiary'],
                       lightcolor=THEME['fg_primary'],
                       darkcolor=THEME['fg_primary'])
        
        self.progress_bar = ttk.Progressbar(progress_frame, style="red.Horizontal.TProgressbar",
                                            variable=self.progress_var,
                                            maximum=100, length=280, mode='determinate')
        self.progress_bar.pack(pady=10)
        
        self.percent_label = tk.Label(progress_frame, text="0%",
                                      bg=THEME['bg_tertiary'], fg=THEME['fg_text'],
                                      font=('Segoe UI', 24, 'bold'))
        self.percent_label.pack()
        
        # Current file
        current_frame = tk.Frame(right_panel, bg=THEME['bg_tertiary'])
        current_frame.pack(fill='x', padx=15, pady=10)
        
        current_title = tk.Label(current_frame, text="█ CURRENT TARGET",
                                 bg=THEME['bg_tertiary'], fg=THEME['fg_secondary'],
                                 font=('Consolas', 11, 'bold'))
        current_title.pack(pady=(10,5))
        
        self.current_label = tk.Label(current_frame, text="initializing...",
                                      bg=THEME['bg_tertiary'], fg=THEME['fg_text'],
                                      font=('Consolas', 10),
                                      wraplength=280)
        self.current_label.pack(pady=10)
        
        # Statistics
        stats_frame = tk.Frame(right_panel, bg=THEME['bg_tertiary'])
        stats_frame.pack(fill='x', padx=15, pady=10)
        
        stats_title = tk.Label(stats_frame, text="█ SYSTEM STATISTICS",
                               bg=THEME['bg_tertiary'], fg=THEME['fg_primary'],
                               font=('Consolas', 11, 'bold'))
        stats_title.pack(pady=(10,5))
        
        self.stats_labels = {}
        stats_items = [
            ("Files Processed:", "0"),
            ("Encrypted:", "0"),
            ("System Core:", "0"),
            ("Kernel Objects:", "0"),
            ("User Data:", "0")
        ]
        
        for label, value in stats_items:
            frame = tk.Frame(stats_frame, bg=THEME['bg_tertiary'])
            frame.pack(fill='x', pady=2, padx=10)
            
            lbl = tk.Label(frame, text=label, bg=THEME['bg_tertiary'],
                          fg=THEME['fg_dim'], font=('Consolas', 9))
            lbl.pack(side='left')
            
            val_lbl = tk.Label(frame, text=value, bg=THEME['bg_tertiary'],
                              fg=THEME['fg_text'], font=('Consolas', 9, 'bold'))
            val_lbl.pack(side='right')
            
            self.stats_labels[label] = val_lbl
        
        # System warning
        warning_frame = tk.Frame(right_panel, bg=THEME['bg_tertiary'])
        warning_frame.pack(fill='x', padx=15, pady=10)
        
        warning_text = tk.Label(warning_frame,
                               text="UNAUTHORIZED ACCESS DETECTED\nENCRYPTION IN PROGRESS",
                               bg=THEME['bg_tertiary'], fg=THEME['error'],
                               font=('Consolas', 9, 'bold'))
        warning_text.pack(pady=10)
        
    def add_file(self, filename, description, size, status, color):
        # Create file item
        item = tk.Frame(self.file_frame, bg=THEME['bg_secondary'])
        item.pack(fill='x', pady=1)
        
        # Border effect
        border = tk.Frame(item, bg=color, height=2)
        border.pack(fill='x')
        
        # Content
        content = tk.Frame(item, bg=THEME['bg_tertiary'])
        content.pack(fill='x', padx=10, pady=5)
        
        # Status indicator
        status_frame = tk.Frame(content, bg=color, width=20, height=20)
        status_frame.pack(side='left', padx=(0,10))
        status_frame.pack_propagate(False)
        
        status_char = "E" if status == "ENCRYPTED" else "S"
        status_label = tk.Label(status_frame, text=status_char,
                                bg=color, fg=THEME['bg_primary'],
                                font=('Consolas', 10, 'bold'))
        status_label.pack(expand=True)
        
        # File info
        info_text = f"{filename:<30} {size:>10}  {description}"
        info_label = tk.Label(content, text=info_text,
                              bg=THEME['bg_tertiary'], fg=THEME['fg_text'],
                              font=('Consolas', 9))
        info_label.pack(side='left', fill='x', expand=True)
        
        # Auto scroll
        self.file_frame.update_idletasks()
        canvas = self.file_frame.master
        canvas.yview_moveto(1.0)
        
    def update_stats(self):
        system_count = len([f for f in self.files_found if 'sys' in f[0] or 'dll' in f[0]])
        kernel_count = len([f for f in self.files_found if 'kernel' in f[1].lower() or 'nt' in f[0]])
        user_count = len([f for f in self.files_found if 'user' in f[1].lower() or 'desktop' in f[0]])
        
        self.stats_labels["Files Processed:"].config(text=str(len(self.files_found)))
        self.stats_labels["Encrypted:"].config(text=str(self.encrypted_count))
        self.stats_labels["System Core:"].config(text=str(system_count))
        self.stats_labels["Kernel Objects:"].config(text=str(kernel_count))
        self.stats_labels["User Data:"].config(text=str(user_count))
        
    def start_scan(self):
        self.scan_thread = threading.Thread(target=self.scan_files, daemon=True)
        self.scan_thread.start()
        
    def scan_files(self):
        total_files = len(SYSTEM_FILES) * 2
        
        for i in range(total_files):
            file_info = random.choice(SYSTEM_FILES)
            filename, description, size = file_info
            
            self.files_found.append(file_info)
            
            # 60% chance encrypted
            if random.random() > 0.4:
                status = "ENCRYPTED"
                color = THEME['fg_primary']
                self.encrypted_count += 1
            else:
                status = "PROCESSED"
                color = THEME['fg_secondary']
            
            # Update UI
            self.root.after(0, lambda f=filename, d=description, s=size, st=status, c=color:
                           self.add_file(f, d, s, st, c))
            
            # Update progress
            progress = int((i + 1) / total_files * 100)
            self.root.after(0, lambda p=progress, fn=filename: self.update_progress(p, fn))
            
            if i % 3 == 0:
                self.root.after(0, self.update_stats)
            
            time.sleep(random.uniform(0.01, 0.03))
        
        self.root.after(0, self.scan_complete)
        
    def update_progress(self, progress, current_file):
        self.progress_var.set(progress)
        self.percent_label.config(text=f"{progress}%")
        self.current_label.config(text=current_file)
        
    def scan_complete(self):
        self.progress_var.set(100)
        self.percent_label.config(text="100%")
        self.show_ransom_note()
        
    def show_ransom_note(self):
        # Generate key
        key_hash = 0
        for c in SIM_PASSWORD:
            key_hash = (key_hash + ord(c)) % 10000
        key = f"FSOCIETY-{key_hash:04d}-KENZIE"
        
        note_win = tk.Toplevel(self.root)
        note_win.title("")
        note_win.geometry(f"700x500+{SCREEN_WIDTH//2-350}+{SCREEN_HEIGHT//2-250}")
        note_win.configure(bg=THEME['bg_primary'])
        note_win.overrideredirect(True)
        note_win.attributes('-topmost', True)
        
        # Glow effect
        for i in range(5):
            glow = tk.Frame(note_win, bg=THEME['fg_primary'], 
                           width=700 - (i*4), height=500 - (i*4))
            glow.place(x=i*2, y=i*2)
        
        content = tk.Frame(note_win, bg=THEME['bg_secondary'])
        content.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)
        
        note_lines = [
            "╔═══════════════════════════════════════════════════════════════════╗",
            "║                    ENCRYPTION PROTOCOL ACTIVE                     ║",
            "╠═══════════════════════════════════════════════════════════════════╣",
            "║                                                                   ║",
            "║  SYSTEM ENCRYPTION KEY GENERATED                                  ║",
            "║  AES-256 │ RSA-4096 │ SECURE BOOT                                 ║",
            "║                                                                   ║",
            "║                                                                   ║",
           f"║  {key}                                                            ║",
            "║                                                                   ║",
            "║  ACCESS CODE: **********                                          ║",
            "║                                                                   ║",
            "╚═══════════════════════════════════════════════════════════════════╝"
        ]
        
        y_pos = 50
        for line in note_lines:
            color = THEME['fg_primary'] if "FSOCIETY" in line else THEME['fg_text']
            label = tk.Label(content, text=line, bg=THEME['bg_secondary'],
                            fg=color, font=('Consolas', 11))
            label.place(x=30, y=y_pos)
            y_pos += 30
        
        # Button
        btn_bg = tk.Frame(content, bg=THEME['border_secondary'], width=200, height=45)
        btn_bg.place(x=250, y=400)
        
        close_btn = tk.Button(btn_bg, text="RESTART",
                              bg=THEME['bg_tertiary'], fg=THEME['fg_secondary'],
                              font=('Segoe UI', 11, 'bold'),
                              relief='flat', bd=0,
                              command=lambda: [note_win.destroy(), self.root.destroy()])
        close_btn.place(x=2, y=2, width=196, height=41)
        
    def run(self):
        self.root.mainloop()

# ==================== WINDOWS ERROR ====================
def show_error():
    ctypes.windll.user32.MessageBoxW(
        0,
        "Windows Critical Error\n\n"
        "Error Code: 0x800F0922\n"
        "Component: Windows Kernel\n"
        "System files corrupted\n\n"
        "FSOCIETY - HACK BY KENZIE",
        "System Error",
        0x00000010 | 0x00000000
    )

# ==================== MAIN ====================
def main():
    hwnd = kernel32.GetConsoleWindow()
    if hwnd:
        user32.ShowWindow(hwnd, SW_HIDE)
    
    show_error()
    
    password_dialog = PasswordDialog()
    result = password_dialog.show()
    
    if result == "RANSOMWARE":
        app = RansomwareApp()
        app.run()
    elif result == "EXIT":
        sys.exit(0)

if __name__ == "__main__":
    main()
