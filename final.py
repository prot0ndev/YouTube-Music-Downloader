#!/usr/bin/env python3
"""
YouTube Music Downloader - Modern Fluent UI
Author: Botiwa
Modern, fluent design with glassmorphism effects and smooth animations
"""

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, filedialog
import subprocess
import os
import sys
import threading
from pathlib import Path
import webbrowser
import json
import re
import time
from concurrent.futures import ThreadPoolExecutor
import queue

# Set appearance mode
ctk.set_appearance_mode("dark")

class ModernTheme:
    """Modern fluent design theme with glassmorphism effects"""
    
    def __init__(self):
        # Modern color palette - Deep blues with accent colors
        self.colors = {
            # Backgrounds - Modern dark theme
            'bg_primary': '#0A0A0B',           # Deep black
            'bg_secondary': '#111114',         # Dark gray
            'bg_tertiary': '#1A1A1E',          # Medium gray
            'bg_card': '#1E1E23',              # Card background
            'bg_surface': '#252529',           # Surface color
            'bg_glass': '#1A1A1E',             # Glass effect
            
            # Modern accent colors
            'accent_primary': '#007AFF',       # iOS Blue
            'accent_secondary': '#5856D6',     # Purple
            'accent_success': '#34C759',       # Green
            'accent_warning': '#FF9500',       # Orange
            'accent_error': '#FF3B30',         # Red
            'accent_pink': '#FF2D92',          # Pink
            'accent_teal': '#5AC8FA',          # Teal
            'accent_indigo': '#5856D6',        # Indigo
            
            # Text colors
            'text_primary': '#FFFFFF',         # Pure white
            'text_secondary': '#EBEBF5',       # Light gray
            'text_tertiary': '#8E8E93',        # Medium gray
            'text_quaternary': '#48484A',      # Dark gray
            
            # Interactive elements
            'border': '#38383A',               # Border color
            'border_active': '#007AFF',        # Active border
            'hover': '#2C2C2E',                # Hover state
            'pressed': '#1C1C1E',              # Pressed state
            
            # Gradients (for future use)
            'gradient_start': '#007AFF',
            'gradient_end': '#5856D6',
        }

class AnimationManager:
    """Handle smooth animations and transitions"""
    
    def __init__(self):
        self.animations = {}
        
    def fade_in(self, widget, duration=300):
        """Fade in animation"""
        # Placeholder for fade animation
        pass
        
    def slide_in(self, widget, direction="left", duration=300):
        """Slide in animation"""
        # Placeholder for slide animation
        pass

class ModernDownloader:
    """Modern YouTube Music Downloader with fluent design"""
    
    def __init__(self):
        self.theme = ModernTheme()
        self.animation_manager = AnimationManager()
        self.optimizer = ThreadPoolExecutor(max_workers=4)
        self.music_urls = []
        self.playlist_items = []
        self.playlist_include_states = {}
        
        self.setup_window()
        self.create_modern_interface()
        self.check_dependencies()
        
    def setup_window(self):
        """Setup main window with modern styling"""
        self.root = ctk.CTk()
        self.root.title("YouTube Music Downloader - Modern UI")
        self.root.configure(fg_color=self.theme.colors['bg_primary'])
        
        # Modern window sizing and positioning
        self.root.state('zoomed')
        self.root.minsize(1400, 900)
        
        # Configure main grid with better proportions
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        
        # Handle window close
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
    def create_modern_interface(self):
        """Create modern fluent interface"""
        # Main container with padding
        main_container = ctk.CTkFrame(
            self.root,
            fg_color="transparent",
            corner_radius=0
        )
        main_container.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        main_container.grid_columnconfigure(1, weight=1)
        main_container.grid_rowconfigure(0, weight=1)
        
        # Modern sidebar
        self.create_modern_sidebar(main_container)
        
        # Main content area
        self.create_modern_content(main_container)
        
    def create_modern_sidebar(self, parent):
        """Create modern sidebar with glassmorphism effect"""
        sidebar = ctk.CTkFrame(
            parent,
            width=350,
            fg_color=self.theme.colors['bg_secondary'],
            corner_radius=20,
            border_width=1,
            border_color=self.theme.colors['border']
        )
        sidebar.grid(row=0, column=0, sticky="nsew", padx=(0, 20))
        sidebar.grid_propagate(False)
        
        # Modern header with gradient-like effect
        header_frame = ctk.CTkFrame(
            sidebar,
            fg_color=self.theme.colors['bg_card'],
            corner_radius=16,
            height=140
        )
        header_frame.pack(fill="x", padx=20, pady=20)
        header_frame.pack_propagate(False)
        
        # App branding with modern typography
        brand_container = ctk.CTkFrame(header_frame, fg_color="transparent")
        brand_container.pack(expand=True, fill="both", padx=25, pady=20)
        
        # Modern icon
        icon_frame = ctk.CTkFrame(
            brand_container,
            fg_color=self.theme.colors['accent_primary'],
            corner_radius=12,
            width=50,
            height=50
        )
        icon_frame.pack(pady=(0, 10))
        icon_frame.pack_propagate(False)
        
        icon_label = ctk.CTkLabel(
            icon_frame,
            text="♪",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color=self.theme.colors['text_primary']
        )
        icon_label.pack(expand=True)
        
        # Modern title
        title_label = ctk.CTkLabel(
            brand_container,
            text="Music Downloader",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color=self.theme.colors['text_primary']
        )
        title_label.pack()
        
        subtitle_label = ctk.CTkLabel(
            brand_container,
            text="Modern • Fast • Reliable",
            font=ctk.CTkFont(size=12),
            text_color=self.theme.colors['text_tertiary']
        )
        subtitle_label.pack(pady=(2, 0))
        
        # Modern mode selection
        self.create_mode_selector(sidebar)
        
        # System status with modern cards
        self.create_status_section(sidebar)
        
        # Download settings
        self.create_settings_section(sidebar)
        
    def create_mode_selector(self, parent):
        """Create modern mode selector with toggle-like design"""
        mode_frame = ctk.CTkFrame(
            parent,
            fg_color=self.theme.colors['bg_card'],
            corner_radius=16
        )
        mode_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        mode_title = ctk.CTkLabel(
            mode_frame,
            text="Download Mode",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=self.theme.colors['text_primary']
        )
        mode_title.pack(pady=(20, 15))
        
        # Modern toggle-style buttons
        buttons_container = ctk.CTkFrame(mode_frame, fg_color="transparent")
        buttons_container.pack(fill="x", padx=20, pady=(0, 20))
        
        self.multi_mode_btn = ctk.CTkButton(
            buttons_container,
            text="Multiple Songs",
            height=50,
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color=self.theme.colors['accent_primary'],
            hover_color=self.theme.colors['accent_secondary'],
            text_color=self.theme.colors['text_primary'],
            corner_radius=12,
            command=lambda: self.switch_mode("multi")
        )
        self.multi_mode_btn.pack(fill="x", pady=(0, 10))
        
        self.playlist_mode_btn = ctk.CTkButton(
            buttons_container,
            text="Playlist Selector",
            height=50,
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color=self.theme.colors['bg_surface'],
            hover_color=self.theme.colors['hover'],
            text_color=self.theme.colors['text_secondary'],
            corner_radius=12,
            command=lambda: self.switch_mode("playlist")
        )
        self.playlist_mode_btn.pack(fill="x")
        
    def create_status_section(self, parent):
        """Create modern status section with cards"""
        status_frame = ctk.CTkFrame(
            parent,
            fg_color=self.theme.colors['bg_card'],
            corner_radius=16
        )
        status_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        status_title = ctk.CTkLabel(
            status_frame,
            text="System Status",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=self.theme.colors['text_primary']
        )
        status_title.pack(pady=(20, 15))
        
        # Status cards container
        status_container = ctk.CTkFrame(status_frame, fg_color="transparent")
        status_container.pack(fill="x", padx=20, pady=(0, 20))
        
        # yt-dlp status card
        ytdlp_card = ctk.CTkFrame(
            status_container,
            fg_color=self.theme.colors['bg_surface'],
            corner_radius=10,
            height=60
        )
        ytdlp_card.pack(fill="x", pady=(0, 8))
        ytdlp_card.pack_propagate(False)
        
        ytdlp_content = ctk.CTkFrame(ytdlp_card, fg_color="transparent")
        ytdlp_content.pack(expand=True, fill="both", padx=15, pady=10)
        ytdlp_content.grid_columnconfigure(0, weight=1)
        
        self.ytdlp_status = ctk.CTkLabel(
            ytdlp_content,
            text="yt-dlp: Checking...",
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=self.theme.colors['text_secondary'],
            anchor="w"
        )
        self.ytdlp_status.grid(row=0, column=0, sticky="ew")
        
        # FFmpeg status card
        ffmpeg_card = ctk.CTkFrame(
            status_container,
            fg_color=self.theme.colors['bg_surface'],
            corner_radius=10,
            height=60
        )
        ffmpeg_card.pack(fill="x")
        ffmpeg_card.pack_propagate(False)
        
        ffmpeg_content = ctk.CTkFrame(ffmpeg_card, fg_color="transparent")
        ffmpeg_content.pack(expand=True, fill="both", padx=15, pady=10)
        ffmpeg_content.grid_columnconfigure(0, weight=1)
        
        self.ffmpeg_status = ctk.CTkLabel(
            ffmpeg_content,
            text="FFmpeg: Checking...",
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=self.theme.colors['text_secondary'],
            anchor="w"
        )
        self.ffmpeg_status.grid(row=0, column=0, sticky="ew")
        
    def create_settings_section(self, parent):
        """Create modern settings section"""
        settings_frame = ctk.CTkFrame(
            parent,
            fg_color=self.theme.colors['bg_card'],
            corner_radius=16
        )
        settings_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        settings_title = ctk.CTkLabel(
            settings_frame,
            text="Download Settings",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=self.theme.colors['text_primary']
        )
        settings_title.pack(pady=(20, 15))
        
        # Location selector with modern design
        location_container = ctk.CTkFrame(settings_frame, fg_color="transparent")
        location_container.pack(fill="x", padx=20, pady=(0, 20))
        
        location_label = ctk.CTkLabel(
            location_container,
            text="Save Location",
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=self.theme.colors['text_secondary']
        )
        location_label.pack(anchor="w", pady=(0, 8))
        
        location_input_frame = ctk.CTkFrame(location_container, fg_color="transparent")
        location_input_frame.pack(fill="x")
        location_input_frame.grid_columnconfigure(0, weight=1)
        
        self.location_entry = ctk.CTkEntry(
            location_input_frame,
            placeholder_text="Select download folder...",
            font=ctk.CTkFont(size=12),
            fg_color=self.theme.colors['bg_surface'],
            border_color=self.theme.colors['border'],
            text_color=self.theme.colors['text_primary'],
            height=40,
            corner_radius=10
        )
        self.location_entry.grid(row=0, column=0, sticky="ew", padx=(0, 10))
        
        browse_btn = ctk.CTkButton(
            location_input_frame,
            text="Browse",
            width=80,
            height=40,
            font=ctk.CTkFont(size=12, weight="bold"),
            fg_color=self.theme.colors['accent_teal'],
            hover_color=self.theme.colors['accent_secondary'],
            text_color=self.theme.colors['text_primary'],
            corner_radius=10,
            command=self.browse_location
        )
        browse_btn.grid(row=0, column=1)
        
        # Set default location
        self.current_location = os.getcwd()
        self.location_entry.insert(0, self.current_location)
        
    def create_modern_content(self, parent):
        """Create modern main content area"""
        content_container = ctk.CTkFrame(
            parent,
            fg_color="transparent",
            corner_radius=0
        )
        content_container.grid(row=0, column=1, sticky="nsew")
        content_container.grid_columnconfigure(0, weight=1)
        content_container.grid_rowconfigure(0, weight=1)
        content_container.grid_rowconfigure(1, weight=0)
        
        # Main work area with modern design
        self.work_area = ctk.CTkFrame(
            content_container,
            fg_color=self.theme.colors['bg_secondary'],
            corner_radius=20,
            border_width=1,
            border_color=self.theme.colors['border']
        )
        self.work_area.grid(row=0, column=0, sticky="nsew", pady=(0, 20))
        self.work_area.grid_columnconfigure(0, weight=1)
        self.work_area.grid_rowconfigure(0, weight=1)
        
        # Create modern tabbed interface
        self.create_modern_tabs()
        
        # Modern log area
        self.create_modern_log_area(content_container)
        
    def create_modern_tabs(self):
        """Create modern tabbed interface"""
        self.notebook = ctk.CTkTabview(
            self.work_area,
            fg_color=self.theme.colors['bg_secondary'],
            segmented_button_fg_color=self.theme.colors['bg_card'],
            segmented_button_selected_color=self.theme.colors['accent_primary'],
            segmented_button_selected_hover_color=self.theme.colors['accent_secondary'],
            text_color=self.theme.colors['text_primary'],
            corner_radius=16
        )
        self.notebook.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        
        # Add tabs
        self.multi_tab = self.notebook.add("Multiple Songs")
        self.playlist_tab = self.notebook.add("Playlist Selector")
        
        # Create content
        self.create_multi_songs_modern()
        self.create_playlist_modern()    
    
    def create_modern_log_area(self, parent):
        """Create modern log area with glassmorphism effect"""
        log_container = ctk.CTkFrame(
            parent,
            fg_color=self.theme.colors['bg_secondary'],
            corner_radius=20,
            border_width=1,
            border_color=self.theme.colors['border'],
            height=280
        )
        log_container.grid(row=1, column=0, sticky="ew")
        log_container.grid_propagate(False)
        log_container.grid_columnconfigure(0, weight=1)
        log_container.grid_rowconfigure(1, weight=1)
        
        # Modern log header
        log_header = ctk.CTkFrame(
            log_container,
            fg_color=self.theme.colors['bg_card'],
            corner_radius=16,
            height=60
        )
        log_header.grid(row=0, column=0, sticky="ew", padx=20, pady=(20, 10))
        log_header.grid_propagate(False)
        log_header.grid_columnconfigure(1, weight=1)
        
        # Header content
        header_left = ctk.CTkFrame(log_header, fg_color="transparent")
        header_left.grid(row=0, column=0, sticky="w", padx=20, pady=15)
        
        log_icon = ctk.CTkLabel(
            header_left,
            text="📊",
            font=ctk.CTkFont(size=18),
            text_color=self.theme.colors['accent_primary']
        )
        log_icon.pack(side="left", padx=(0, 8))
        
        log_title = ctk.CTkLabel(
            header_left,
            text="Activity Monitor",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=self.theme.colors['text_primary']
        )
        log_title.pack(side="left")
        
        # Progress info
        self.progress_info = ctk.CTkLabel(
            log_header,
            text="Ready",
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=self.theme.colors['accent_success']
        )
        self.progress_info.grid(row=0, column=1, padx=20, pady=15, sticky="e")
        
        # Clear button
        clear_btn = ctk.CTkButton(
            log_header,
            text="Clear",
            width=60,
            height=30,
            font=ctk.CTkFont(size=11, weight="bold"),
            fg_color=self.theme.colors['accent_error'],
            hover_color=self.theme.colors['accent_pink'],
            text_color=self.theme.colors['text_primary'],
            corner_radius=8,
            command=self.clear_log
        )
        clear_btn.grid(row=0, column=2, padx=(10, 20), pady=15)
        
        # Modern log content
        log_content = ctk.CTkFrame(
            log_container,
            fg_color=self.theme.colors['bg_tertiary'],
            corner_radius=16
        )
        log_content.grid(row=1, column=0, sticky="nsew", padx=20, pady=(0, 20))
        log_content.grid_columnconfigure(0, weight=1)
        log_content.grid_rowconfigure(1, weight=1)
        
        # Modern progress bar
        progress_container = ctk.CTkFrame(log_content, fg_color="transparent")
        progress_container.grid(row=0, column=0, sticky="ew", padx=15, pady=15)
        progress_container.grid_columnconfigure(0, weight=1)
        
        self.progress_bar = ctk.CTkProgressBar(
            progress_container,
            height=8,
            progress_color=self.theme.colors['accent_primary'],
            fg_color=self.theme.colors['bg_surface'],
            corner_radius=4
        )
        self.progress_bar.grid(row=0, column=0, sticky="ew")
        self.progress_bar.set(0)
        
        # Modern log text area
        self.log_text = ctk.CTkTextbox(
            log_content,
            font=ctk.CTkFont(family="SF Mono", size=11),
            fg_color=self.theme.colors['bg_primary'],
            text_color=self.theme.colors['text_secondary'],
            corner_radius=12,
            state="disabled",
            wrap="word",
            border_width=1,
            border_color=self.theme.colors['border']
        )
        self.log_text.grid(row=1, column=0, sticky="nsew", padx=15, pady=(0, 15))
        
    def create_multi_songs_modern(self):
        """Create modern multiple songs interface"""
        # Configure grid
        self.multi_tab.grid_columnconfigure(0, weight=1)
        self.multi_tab.grid_rowconfigure(1, weight=1)
        
        # Modern header
        header = ctk.CTkFrame(
            self.multi_tab,
            fg_color=self.theme.colors['bg_card'],
            corner_radius=16,
            height=120
        )
        header.grid(row=0, column=0, sticky="ew", padx=25, pady=(25, 20))
        header.grid_propagate(False)
        
        header_content = ctk.CTkFrame(header, fg_color="transparent")
        header_content.pack(expand=True, fill="both", padx=30, pady=25)
        
        # Header with icon
        header_top = ctk.CTkFrame(header_content, fg_color="transparent")
        header_top.pack(fill="x")
        
        icon_container = ctk.CTkFrame(
            header_top,
            fg_color=self.theme.colors['accent_primary'],
            corner_radius=10,
            width=40,
            height=40
        )
        icon_container.pack(side="left", padx=(0, 15))
        icon_container.pack_propagate(False)
        
        icon = ctk.CTkLabel(
            icon_container,
            text="♫",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color=self.theme.colors['text_primary']
        )
        icon.pack(expand=True)
        
        title_container = ctk.CTkFrame(header_top, fg_color="transparent")
        title_container.pack(side="left", fill="x", expand=True)
        
        title = ctk.CTkLabel(
            title_container,
            text="Multiple Songs Download",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color=self.theme.colors['text_primary'],
            anchor="w"
        )
        title.pack(anchor="w")
        
        subtitle = ctk.CTkLabel(
            title_container,
            text="Add up to 15 YouTube music URLs for batch download",
            font=ctk.CTkFont(size=14),
            text_color=self.theme.colors['text_tertiary'],
            anchor="w"
        )
        subtitle.pack(anchor="w", pady=(5, 0))
        
        # Main content with modern cards
        content = ctk.CTkFrame(
            self.multi_tab,
            fg_color=self.theme.colors['bg_card'],
            corner_radius=16
        )
        content.grid(row=1, column=0, sticky="nsew", padx=25, pady=(0, 25))
        content.grid_columnconfigure(0, weight=1)
        content.grid_rowconfigure(1, weight=1)
        
        # Modern URL input section
        input_section = ctk.CTkFrame(
            content,
            fg_color=self.theme.colors['bg_surface'],
            corner_radius=12
        )
        input_section.grid(row=0, column=0, sticky="ew", padx=25, pady=25)
        
        input_content = ctk.CTkFrame(input_section, fg_color="transparent")
        input_content.pack(fill="x", padx=25, pady=20)
        input_content.grid_columnconfigure(0, weight=1)
        
        # Modern URL input
        self.url_entry = ctk.CTkEntry(
            input_content,
            placeholder_text="🔗 Paste YouTube music URL here...",
            height=55,
            font=ctk.CTkFont(size=15),
            fg_color=self.theme.colors['bg_tertiary'],
            border_color=self.theme.colors['accent_primary'],
            border_width=2,
            text_color=self.theme.colors['text_primary'],
            placeholder_text_color=self.theme.colors['text_quaternary'],
            corner_radius=12
        )
        self.url_entry.grid(row=0, column=0, sticky="ew", padx=(0, 15))
        
        add_btn = ctk.CTkButton(
            input_content,
            text="Add Song",
            width=120,
            height=55,
            font=ctk.CTkFont(size=15, weight="bold"),
            fg_color=self.theme.colors['accent_primary'],
            hover_color=self.theme.colors['accent_secondary'],
            text_color=self.theme.colors['text_primary'],
            corner_radius=12,
            command=self.add_music_url
        )
        add_btn.grid(row=0, column=1)
        
        # Bind Enter key
        self.url_entry.bind("<Return>", lambda e: self.add_music_url())
        
        # Modern controls
        controls_frame = ctk.CTkFrame(input_content, fg_color="transparent")
        controls_frame.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(15, 0))
        controls_frame.grid_columnconfigure(1, weight=1)
        
        self.url_counter = ctk.CTkLabel(
            controls_frame,
            text="Songs: 0/15",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=self.theme.colors['accent_primary']
        )
        self.url_counter.grid(row=0, column=0, sticky="w")
        
        clear_all_btn = ctk.CTkButton(
            controls_frame,
            text="Clear All",
            width=100,
            height=35,
            font=ctk.CTkFont(size=12, weight="bold"),
            fg_color=self.theme.colors['accent_error'],
            hover_color=self.theme.colors['accent_pink'],
            text_color=self.theme.colors['text_primary'],
            corner_radius=8,
            command=self.clear_all_urls
        )
        clear_all_btn.grid(row=0, column=2, sticky="e")
        
        # Modern songs list
        self.songs_list = ctk.CTkScrollableFrame(
            content,
            fg_color=self.theme.colors['bg_tertiary'],
            corner_radius=12,
            border_width=1,
            border_color=self.theme.colors['border']
        )
        self.songs_list.grid(row=1, column=0, sticky="nsew", padx=25, pady=(0, 20))
        self.songs_list.grid_columnconfigure(0, weight=1)
        
        # Modern download section
        download_section = ctk.CTkFrame(content, fg_color="transparent")
        download_section.grid(row=2, column=0, sticky="ew", padx=25, pady=(0, 25))
        
        self.multi_download_btn = ctk.CTkButton(
            download_section,
            text="🚀 Download All Songs",
            height=60,
            font=ctk.CTkFont(size=18, weight="bold"),
            fg_color=self.theme.colors['accent_success'],
            hover_color=self.theme.colors['accent_primary'],
            text_color=self.theme.colors['text_primary'],
            corner_radius=15,
            command=self.download_multiple_songs,
            state="disabled"
        )
        self.multi_download_btn.pack(fill="x")
        
    def create_playlist_modern(self):
        """Create modern playlist interface"""
        # Configure grid
        self.playlist_tab.grid_columnconfigure(0, weight=1)
        self.playlist_tab.grid_rowconfigure(2, weight=1)
        
        # Modern header
        header = ctk.CTkFrame(
            self.playlist_tab,
            fg_color=self.theme.colors['bg_card'],
            corner_radius=16,
            height=140
        )
        header.grid(row=0, column=0, sticky="ew", padx=25, pady=(25, 20))
        header.grid_propagate(False)
        
        header_content = ctk.CTkFrame(header, fg_color="transparent")
        header_content.pack(expand=True, fill="both", padx=30, pady=25)
        
        # Header with icon
        header_top = ctk.CTkFrame(header_content, fg_color="transparent")
        header_top.pack(fill="x")
        
        icon_container = ctk.CTkFrame(
            header_top,
            fg_color=self.theme.colors['accent_secondary'],
            corner_radius=10,
            width=40,
            height=40
        )
        icon_container.pack(side="left", padx=(0, 15))
        icon_container.pack_propagate(False)
        
        icon = ctk.CTkLabel(
            icon_container,
            text="📋",
            font=ctk.CTkFont(size=18),
            text_color=self.theme.colors['text_primary']
        )
        icon.pack(expand=True)
        
        title_container = ctk.CTkFrame(header_top, fg_color="transparent")
        title_container.pack(side="left", fill="x", expand=True)
        
        title = ctk.CTkLabel(
            title_container,
            text="Playlist Song Selector",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color=self.theme.colors['text_primary'],
            anchor="w"
        )
        title.pack(anchor="w")
        
        subtitle = ctk.CTkLabel(
            title_container,
            text="Load a playlist and choose which songs to download",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=self.theme.colors['accent_success'],
            anchor="w"
        )
        subtitle.pack(anchor="w", pady=(3, 0))
        
        explanation = ctk.CTkLabel(
            title_container,
            text="✓ Blue = Will be downloaded  •  ✗ Gray = Will be skipped",
            font=ctk.CTkFont(size=12),
            text_color=self.theme.colors['text_tertiary'],
            anchor="w"
        )
        explanation.pack(anchor="w", pady=(5, 0))
        
        # Modern URL input section
        url_section = ctk.CTkFrame(
            self.playlist_tab,
            fg_color=self.theme.colors['bg_card'],
            corner_radius=16
        )
        url_section.grid(row=1, column=0, sticky="ew", padx=25, pady=(0, 20))
        
        url_content = ctk.CTkFrame(url_section, fg_color="transparent")
        url_content.pack(fill="x", padx=25, pady=20)
        url_content.grid_columnconfigure(0, weight=1)
        
        url_label = ctk.CTkLabel(
            url_content,
            text="Playlist URL",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=self.theme.colors['text_primary']
        )
        url_label.grid(row=0, column=0, sticky="w", pady=(0, 12))
        
        url_input_frame = ctk.CTkFrame(url_content, fg_color="transparent")
        url_input_frame.grid(row=1, column=0, sticky="ew")
        url_input_frame.grid_columnconfigure(0, weight=1)
        
        self.playlist_url_entry = ctk.CTkEntry(
            url_input_frame,
            placeholder_text="🔗 Paste YouTube playlist URL here...",
            height=55,
            font=ctk.CTkFont(size=15),
            fg_color=self.theme.colors['bg_surface'],
            border_color=self.theme.colors['accent_secondary'],
            border_width=2,
            text_color=self.theme.colors['text_primary'],
            placeholder_text_color=self.theme.colors['text_quaternary'],
            corner_radius=12
        )
        self.playlist_url_entry.grid(row=0, column=0, sticky="ew", padx=(0, 15))
        
        load_btn = ctk.CTkButton(
            url_input_frame,
            text="Load Playlist",
            width=140,
            height=55,
            font=ctk.CTkFont(size=15, weight="bold"),
            fg_color=self.theme.colors['accent_secondary'],
            hover_color=self.theme.colors['accent_indigo'],
            text_color=self.theme.colors['text_primary'],
            corner_radius=12,
            command=self.load_playlist
        )
        load_btn.grid(row=0, column=1)
        
        # Modern playlist content
        playlist_content = ctk.CTkFrame(
            self.playlist_tab,
            fg_color=self.theme.colors['bg_card'],
            corner_radius=16
        )
        playlist_content.grid(row=2, column=0, sticky="nsew", padx=25, pady=(0, 25))
        playlist_content.grid_columnconfigure(0, weight=1)
        playlist_content.grid_rowconfigure(1, weight=1)
        
        # Modern controls
        controls = ctk.CTkFrame(
            playlist_content,
            fg_color=self.theme.colors['bg_surface'],
            corner_radius=12
        )
        controls.grid(row=0, column=0, sticky="ew", padx=25, pady=25)
        
        controls_content = ctk.CTkFrame(controls, fg_color="transparent")
        controls_content.pack(fill="x", padx=20, pady=15)
        controls_content.grid_columnconfigure(3, weight=1)
        
        include_all_btn = ctk.CTkButton(
            controls_content,
            text="✓ Include All",
            width=120,
            height=40,
            font=ctk.CTkFont(size=13, weight="bold"),
            fg_color=self.theme.colors['accent_success'],
            hover_color=self.theme.colors['accent_primary'],
            text_color=self.theme.colors['text_primary'],
            corner_radius=10,
            command=self.include_all_songs
        )
        include_all_btn.grid(row=0, column=0, padx=(0, 10))
        
        exclude_all_btn = ctk.CTkButton(
            controls_content,
            text="✗ Exclude All",
            width=120,
            height=40,
            font=ctk.CTkFont(size=13, weight="bold"),
            fg_color=self.theme.colors['accent_error'],
            hover_color=self.theme.colors['accent_pink'],
            text_color=self.theme.colors['text_primary'],
            corner_radius=10,
            command=self.exclude_all_songs
        )
        exclude_all_btn.grid(row=0, column=1, padx=10)
        
        invert_btn = ctk.CTkButton(
            controls_content,
            text="🔄 Invert",
            width=100,
            height=40,
            font=ctk.CTkFont(size=13, weight="bold"),
            fg_color=self.theme.colors['accent_warning'],
            hover_color=self.theme.colors['accent_teal'],
            text_color=self.theme.colors['text_primary'],
            corner_radius=10,
            command=self.invert_selection
        )
        invert_btn.grid(row=0, column=2, padx=(10, 0))
        
        # Status counter
        self.playlist_counter = ctk.CTkLabel(
            controls_content,
            text="No playlist loaded",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=self.theme.colors['accent_primary']
        )
        self.playlist_counter.grid(row=0, column=3, padx=20, sticky="e")
        
        # Modern playlist items list
        self.playlist_list = ctk.CTkScrollableFrame(
            playlist_content,
            fg_color=self.theme.colors['bg_tertiary'],
            corner_radius=12,
            border_width=1,
            border_color=self.theme.colors['border']
        )
        self.playlist_list.grid(row=1, column=0, sticky="nsew", padx=25, pady=(0, 20))
        self.playlist_list.grid_columnconfigure(0, weight=1)
        
        # Modern download section
        download_section = ctk.CTkFrame(playlist_content, fg_color="transparent")
        download_section.grid(row=2, column=0, sticky="ew", padx=25, pady=(0, 25))
        
        self.playlist_download_btn = ctk.CTkButton(
            download_section,
            text="🚀 Download Selected Songs",
            height=60,
            font=ctk.CTkFont(size=18, weight="bold"),
            fg_color=self.theme.colors['accent_success'],
            hover_color=self.theme.colors['accent_primary'],
            text_color=self.theme.colors['text_primary'],
            corner_radius=15,
            command=self.download_selected_songs,
            state="disabled"
        )
        self.playlist_download_btn.pack(fill="x")     
   
    def switch_mode(self, mode):
        """Switch between modes with modern visual feedback"""
        if mode == "multi":
            self.multi_mode_btn.configure(
                fg_color=self.theme.colors['accent_primary'],
                text_color=self.theme.colors['text_primary']
            )
            self.playlist_mode_btn.configure(
                fg_color=self.theme.colors['bg_surface'],
                text_color=self.theme.colors['text_secondary']
            )
            self.notebook.set("Multiple Songs")
        else:
            self.playlist_mode_btn.configure(
                fg_color=self.theme.colors['accent_primary'],
                text_color=self.theme.colors['text_primary']
            )
            self.multi_mode_btn.configure(
                fg_color=self.theme.colors['bg_surface'],
                text_color=self.theme.colors['text_secondary']
            )
            self.notebook.set("Playlist Selector")
            
    def browse_location(self):
        """Browse for download location"""
        folder = filedialog.askdirectory(
            title="Select Download Location",
            initialdir=self.current_location
        )
        if folder:
            self.current_location = folder
            self.location_entry.delete(0, "end")
            self.location_entry.insert(0, folder)
            self.log_message(f"📁 Download location updated: {folder}", "info")
            
    def format_duration(self, duration_str):
        """Format duration from seconds to H:MM:SS or MM:SS format"""
        if not duration_str or duration_str == "Unknown" or duration_str == "NA":
            return "Unknown"
            
        try:
            total_seconds = int(float(duration_str))
            hours = total_seconds // 3600
            minutes = (total_seconds % 3600) // 60
            seconds = total_seconds % 60
            
            if hours > 0:
                return f"{hours}:{minutes:02d}:{seconds:02d}"
            else:
                return f"{minutes}:{seconds:02d}"
                
        except (ValueError, TypeError):
            return "Unknown"
            
    def validate_youtube_url(self, url):
        """Validate YouTube URL"""
        youtube_patterns = [
            r'youtube\.com/watch\?v=',
            r'youtu\.be/',
            r'music\.youtube\.com/watch\?v=',
            r'youtube\.com/embed/',
            r'm\.youtube\.com/watch\?v='
        ]
        return any(re.search(pattern, url) for pattern in youtube_patterns)
        
    def add_music_url(self):
        """Add music URL with modern validation feedback"""
        url = self.url_entry.get().strip()
        if not url:
            self.log_message("⚠️ Please enter a URL", "warning")
            return
            
        if len(self.music_urls) >= 15:
            self.log_message("⚠️ Maximum 15 URLs allowed", "warning")
            return
            
        if not self.validate_youtube_url(url):
            self.log_message("❌ Please enter a valid YouTube/YouTube Music URL", "error")
            return
            
        if any(item['url'] == url for item in self.music_urls):
            self.log_message("⚠️ URL already added", "warning")
            return
            
        # Add to list
        music_item = {
            'url': url,
            'title': f"Song {len(self.music_urls) + 1}",
            'index': len(self.music_urls),
            'status': 'pending'
        }
        self.music_urls.append(music_item)
        
        # Clear entry and update UI
        self.url_entry.delete(0, "end")
        self.update_songs_list()
        self.update_url_counter()
        
        if self.music_urls:
            self.multi_download_btn.configure(state="normal")
            
        self.log_message(f"✅ Added song {len(self.music_urls)}: {url[:50]}...", "success")
        
    def update_songs_list(self):
        """Update songs list with modern cards"""
        # Clear existing widgets
        for widget in self.songs_list.winfo_children():
            widget.destroy()
            
        # Add each song
        for i, song in enumerate(self.music_urls):
            self.create_modern_song_item(song, i)
            
    def create_modern_song_item(self, song, index):
        """Create modern song item card"""
        item_frame = ctk.CTkFrame(
            self.songs_list,
            fg_color=self.theme.colors['bg_surface'],
            corner_radius=12,
            height=80,
            border_width=1,
            border_color=self.theme.colors['border']
        )
        item_frame.grid(row=index, column=0, sticky="ew", pady=8)
        item_frame.grid_propagate(False)
        item_frame.grid_columnconfigure(1, weight=1)
        
        # Modern index indicator
        index_frame = ctk.CTkFrame(
            item_frame,
            fg_color=self.theme.colors['accent_primary'],
            corner_radius=10,
            width=60
        )
        index_frame.grid(row=0, column=0, padx=15, pady=15, sticky="ns")
        index_frame.grid_propagate(False)
        
        index_label = ctk.CTkLabel(
            index_frame,
            text=f"{index + 1}",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color=self.theme.colors['text_primary']
        )
        index_label.pack(expand=True)
        
        # Song info with modern typography
        info_frame = ctk.CTkFrame(item_frame, fg_color="transparent")
        info_frame.grid(row=0, column=1, sticky="ew", padx=15, pady=15)
        info_frame.grid_columnconfigure(0, weight=1)
        
        # Truncated URL with better formatting
        url_text = song['url']
        if len(url_text) > 65:
            url_text = url_text[:65] + "..."
            
        url_label = ctk.CTkLabel(
            info_frame,
            text=url_text,
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=self.theme.colors['text_primary'],
            anchor="w"
        )
        url_label.grid(row=0, column=0, sticky="ew")
        
        # Status with modern styling
        status_colors = {
            'pending': self.theme.colors['text_tertiary'],
            'downloading': self.theme.colors['accent_warning'],
            'completed': self.theme.colors['accent_success'],
            'failed': self.theme.colors['accent_error']
        }
        
        status_label = ctk.CTkLabel(
            info_frame,
            text=f"Status: {song['status'].title()}",
            font=ctk.CTkFont(size=11),
            text_color=status_colors.get(song['status'], self.theme.colors['text_tertiary']),
            anchor="w"
        )
        status_label.grid(row=1, column=0, sticky="ew")
        
        # Modern remove button
        remove_btn = ctk.CTkButton(
            item_frame,
            text="✕",
            width=45,
            height=45,
            font=ctk.CTkFont(size=16, weight="bold"),
            fg_color=self.theme.colors['accent_error'],
            hover_color=self.theme.colors['accent_pink'],
            text_color=self.theme.colors['text_primary'],
            corner_radius=22,
            command=lambda idx=index: self.remove_song_url(idx)
        )
        remove_btn.grid(row=0, column=2, padx=15, pady=15)
        
    def remove_song_url(self, index):
        """Remove song URL with modern feedback"""
        if 0 <= index < len(self.music_urls):
            removed = self.music_urls.pop(index)
            self.update_songs_list()
            self.update_url_counter()
            
            if not self.music_urls:
                self.multi_download_btn.configure(state="disabled")
                
            self.log_message(f"🗑️ Removed song {index + 1}", "info")
            
    def clear_all_urls(self):
        """Clear all URLs with modern confirmation"""
        if self.music_urls:
            count = len(self.music_urls)
            self.music_urls.clear()
            self.update_songs_list()
            self.update_url_counter()
            self.multi_download_btn.configure(state="disabled")
            self.log_message(f"🗑️ Cleared {count} songs", "info")
            
    def update_url_counter(self):
        """Update URL counter with modern color coding"""
        count = len(self.music_urls)
        self.url_counter.configure(text=f"Songs: {count}/15")
        
        if count == 0:
            color = self.theme.colors['text_tertiary']
        elif count < 10:
            color = self.theme.colors['accent_success']
        elif count < 15:
            color = self.theme.colors['accent_warning']
        else:
            color = self.theme.colors['accent_error']
            
        self.url_counter.configure(text_color=color)
        
    def load_playlist(self):
        """Load playlist with modern feedback"""
        url = self.playlist_url_entry.get().strip()
        if not url:
            self.log_message("⚠️ Please enter a playlist URL", "warning")
            return
            
        if not ("playlist" in url and ("youtube.com" in url or "music.youtube.com" in url)):
            self.log_message("❌ Please enter a valid YouTube playlist URL", "error")
            return
            
        self.log_message("🔄 Loading playlist... This may take a moment", "info")
        self.progress_info.configure(text="Loading playlist...")
        self.progress_bar.set(0.1)
        
        # Load in background
        threading.Thread(target=self._load_playlist_thread, args=(url,), daemon=True).start()
        
    def _load_playlist_thread(self, url):
        """Load playlist in background with modern error handling"""
        try:
            self.root.after(0, lambda: self.progress_bar.set(0.3))
            
            cmd = [
                "yt-dlp",
                "--flat-playlist",
                "--print", "%(title)s|%(id)s|%(url)s|%(duration)s",
                "--no-warnings",
                url
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            
            self.root.after(0, lambda: self.progress_bar.set(0.7))
            
            if result.returncode == 0:
                lines = result.stdout.strip().split('\n')
                playlist_items = []
                
                for i, line in enumerate(lines):
                    if '|' in line and line.strip():
                        parts = line.split('|')
                        if len(parts) >= 3:
                            title = parts[0] if parts[0] != 'NA' else f"Song {i+1}"
                            video_id = parts[1]
                            video_url = parts[2]
                            duration = parts[3] if len(parts) > 3 and parts[3] != 'NA' else "Unknown"
                            
                            formatted_duration = self.format_duration(duration)
                            
                            playlist_items.append({
                                'title': title,
                                'id': video_id,
                                'url': video_url,
                                'duration': formatted_duration,
                                'index': i,
                                'included': True
                            })
                
                self.root.after(0, lambda: self.progress_bar.set(1.0))
                self.root.after(0, self._update_playlist_ui, playlist_items)
            else:
                error_msg = result.stderr or "Unknown error occurred"
                self.root.after(0, self.log_message, f"❌ Failed to load playlist: {error_msg}", "error")
                self.root.after(0, self._reset_playlist_ui)
                
        except subprocess.TimeoutExpired:
            self.root.after(0, self.log_message, "⏱️ Playlist loading timed out (60s)", "error")
            self.root.after(0, self._reset_playlist_ui)
        except Exception as e:
            self.root.after(0, self.log_message, f"❌ Error loading playlist: {str(e)}", "error")
            self.root.after(0, self._reset_playlist_ui)
            
    def _update_playlist_ui(self, playlist_items):
        """Update playlist UI with modern design"""
        self.playlist_items = playlist_items
        self.playlist_include_states = {item['index']: True for item in playlist_items}
        
        # Clear existing items
        for widget in self.playlist_list.winfo_children():
            widget.destroy()
            
        # Add each item
        for item in playlist_items:
            self.create_modern_playlist_item(item)
            
        self.update_playlist_counter()
        self.playlist_download_btn.configure(state="normal")
        
        self.log_message(f"✅ Loaded {len(playlist_items)} songs from playlist", "success")
        self.progress_info.configure(text="Ready")
        self.progress_bar.set(0)
        
    def _reset_playlist_ui(self):
        """Reset playlist UI on error"""
        self.progress_info.configure(text="Ready")
        self.progress_bar.set(0)
        
    def create_modern_playlist_item(self, item):
        """Create modern playlist item card"""
        item_frame = ctk.CTkFrame(
            self.playlist_list,
            fg_color=self.theme.colors['bg_surface'],
            corner_radius=12,
            height=100,
            border_width=1,
            border_color=self.theme.colors['border']
        )
        item_frame.grid(row=item['index'], column=0, sticky="ew", pady=6)
        item_frame.grid_propagate(False)
        item_frame.grid_columnconfigure(1, weight=1)
        
        # Modern toggle button
        toggle_frame = ctk.CTkFrame(
            item_frame,
            fg_color=self.theme.colors['accent_primary'] if item['included'] else self.theme.colors['bg_tertiary'],
            corner_radius=12,
            width=70,
            height=70
        )
        toggle_frame.grid(row=0, column=0, padx=15, pady=15)
        toggle_frame.grid_propagate(False)
        
        toggle_btn = ctk.CTkButton(
            toggle_frame,
            text="✓" if item['included'] else "✗",
            width=60,
            height=60,
            font=ctk.CTkFont(size=20, weight="bold"),
            fg_color="transparent",
            hover_color=self.theme.colors['hover'],
            text_color=self.theme.colors['text_primary'] if item['included'] else self.theme.colors['text_tertiary'],
            corner_radius=10,
            command=lambda idx=item['index']: self.toggle_song_inclusion(idx)
        )
        toggle_btn.pack(expand=True, padx=5, pady=5)
        
        # Store references
        item['toggle_frame'] = toggle_frame
        item['toggle_btn'] = toggle_btn
        
        # Song info with modern layout
        info_frame = ctk.CTkFrame(item_frame, fg_color="transparent")
        info_frame.grid(row=0, column=1, sticky="ew", padx=15, pady=15)
        info_frame.grid_columnconfigure(0, weight=1)
        
        # Title with modern typography
        title_text = item['title']
        if len(title_text) > 55:
            title_text = title_text[:55] + "..."
            
        title_label = ctk.CTkLabel(
            info_frame,
            text=title_text,
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=self.theme.colors['text_primary'] if item['included'] else self.theme.colors['text_tertiary'],
            anchor="w"
        )
        title_label.grid(row=0, column=0, sticky="ew")
        
        # Details
        details_text = f"ID: {item['id']}"
        details_label = ctk.CTkLabel(
            info_frame,
            text=details_text,
            font=ctk.CTkFont(size=11),
            text_color=self.theme.colors['text_quaternary'],
            anchor="w"
        )
        details_label.grid(row=1, column=0, sticky="ew")
        
        # Duration with modern styling
        duration_label = ctk.CTkLabel(
            info_frame,
            text=f"⏱️ {item['duration']}",
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color=self.theme.colors['accent_teal'] if item['included'] else self.theme.colors['text_quaternary'],
            anchor="w"
        )
        duration_label.grid(row=2, column=0, sticky="ew")
        
        # Store references
        item['title_label'] = title_label
        item['details_label'] = details_label
        item['duration_label'] = duration_label
        
        # Modern index
        index_label = ctk.CTkLabel(
            item_frame,
            text=f"#{item['index'] + 1}",
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=self.theme.colors['accent_primary'],
            width=60
        )
        index_label.grid(row=0, column=2, padx=15, pady=15)
        
    def toggle_song_inclusion(self, index):
        """Toggle song inclusion with modern visual feedback"""
        if index < len(self.playlist_items):
            item = self.playlist_items[index]
            item['included'] = not item['included']
            self.playlist_include_states[index] = item['included']
            
            # Update visual state with modern colors
            if item['included']:
                item['toggle_frame'].configure(fg_color=self.theme.colors['accent_primary'])
                item['toggle_btn'].configure(
                    text="✓",
                    text_color=self.theme.colors['text_primary']
                )
                item['title_label'].configure(text_color=self.theme.colors['text_primary'])
                item['duration_label'].configure(text_color=self.theme.colors['accent_teal'])
            else:
                item['toggle_frame'].configure(fg_color=self.theme.colors['bg_tertiary'])
                item['toggle_btn'].configure(
                    text="✗",
                    text_color=self.theme.colors['text_tertiary']
                )
                item['title_label'].configure(text_color=self.theme.colors['text_tertiary'])
                item['duration_label'].configure(text_color=self.theme.colors['text_quaternary'])
                
            self.update_playlist_counter()
            
    def include_all_songs(self):
        """Include all songs in playlist"""
        for item in self.playlist_items:
            if not item['included']:
                self.toggle_song_inclusion(item['index'])
                
    def exclude_all_songs(self):
        """Exclude all songs from playlist"""
        for item in self.playlist_items:
            if item['included']:
                self.toggle_song_inclusion(item['index'])
                
    def invert_selection(self):
        """Invert current selection"""
        for item in self.playlist_items:
            self.toggle_song_inclusion(item['index'])
            
    def update_playlist_counter(self):
        """Update playlist counter with modern styling"""
        if not self.playlist_items:
            self.playlist_counter.configure(
                text="No playlist loaded",
                text_color=self.theme.colors['text_tertiary']
            )
            return
            
        total = len(self.playlist_items)
        included = sum(1 for item in self.playlist_items if item['included'])
        
        # Calculate total duration
        total_seconds = 0
        for item in self.playlist_items:
            if item['included'] and item['duration'] != "Unknown":
                try:
                    duration_str = item['duration']
                    parts = duration_str.split(':')
                    if len(parts) == 3:
                        total_seconds += int(parts[0]) * 3600 + int(parts[1]) * 60 + int(parts[2])
                    elif len(parts) == 2:
                        total_seconds += int(parts[0]) * 60 + int(parts[1])
                except (ValueError, IndexError):
                    pass
        
        # Format display text
        if total_seconds > 0:
            total_duration = self.format_duration(str(total_seconds))
            text = f"Will download: {included}/{total} songs • Total: {total_duration}"
        else:
            text = f"Will download: {included}/{total} songs"
        
        # Modern color coding
        if included == 0:
            color = self.theme.colors['accent_error']
        elif included == total:
            color = self.theme.colors['accent_success']
        else:
            color = self.theme.colors['accent_warning']
            
        self.playlist_counter.configure(text=text, text_color=color)    
    
    def download_multiple_songs(self):
        """Download multiple songs with modern progress tracking"""
        if not self.music_urls:
            self.log_message("⚠️ No songs to download", "warning")
            return
            
        self.log_message(f"🚀 Starting download of {len(self.music_urls)} songs...", "info")
        self.progress_info.configure(text="Downloading songs...")
        self.multi_download_btn.configure(state="disabled", text="Downloading...")
        
        threading.Thread(target=self._download_multiple_thread, daemon=True).start()
        
    def _download_multiple_thread(self):
        """Download multiple songs in background with modern feedback"""
        try:
            download_dir = os.path.join(self.current_location, "YouTube_Music_Songs")
            os.makedirs(download_dir, exist_ok=True)
            
            total = len(self.music_urls)
            successful = 0
            
            for i, song in enumerate(self.music_urls):
                progress = i / total
                self.root.after(0, lambda p=progress: self.progress_bar.set(p))
                self.root.after(0, self.log_message, f"⬇️ Downloading {i+1}/{total}: {song['title']}", "info")
                
                # Update song status
                song['status'] = 'downloading'
                self.root.after(0, self.update_songs_list)
                
                cmd = [
                    "yt-dlp",
                    "--extract-audio",
                    "--audio-format", "opus",
                    "--output", os.path.join(download_dir, "%(title)s.%(ext)s"),
                    "--no-playlist",
                    "--no-warnings",
                    song['url']
                ]
                
                result = subprocess.run(cmd, capture_output=True, text=True)
                
                if result.returncode == 0:
                    successful += 1
                    song['status'] = 'completed'
                    self.root.after(0, self.log_message, f"✅ Completed: {song['title']}", "success")
                else:
                    song['status'] = 'failed'
                    self.root.after(0, self.log_message, f"❌ Failed: {song['title']}", "error")
                    
                self.root.after(0, self.update_songs_list)
                    
            self.root.after(0, lambda: self.progress_bar.set(1.0))
            self.root.after(0, self.log_message, f"🎉 Download complete! {successful}/{total} songs downloaded", "success")
            self.root.after(0, self._download_complete)
            
        except Exception as e:
            self.root.after(0, self.log_message, f"❌ Download error: {str(e)}", "error")
            self.root.after(0, self._download_complete)
            
    def download_selected_songs(self):
        """Download selected playlist songs with modern feedback"""
        included_songs = [item for item in self.playlist_items if item['included']]
        
        if not included_songs:
            self.log_message("⚠️ No songs selected for download", "warning")
            return
            
        self.log_message(f"🚀 Starting download of {len(included_songs)} selected songs...", "info")
        self.progress_info.configure(text="Downloading playlist...")
        self.playlist_download_btn.configure(state="disabled", text="Downloading...")
        
        threading.Thread(target=self._download_playlist_thread, args=(included_songs,), daemon=True).start()
        
    def _download_playlist_thread(self, songs):
        """Download selected playlist songs with modern progress"""
        try:
            download_dir = os.path.join(self.current_location, "YouTube_Music_Playlists")
            os.makedirs(download_dir, exist_ok=True)
            
            total = len(songs)
            successful = 0
            
            for i, song in enumerate(songs):
                progress = i / total
                self.root.after(0, lambda p=progress: self.progress_bar.set(p))
                self.root.after(0, self.log_message, f"⬇️ Downloading {i+1}/{total}: {song['title'][:40]}...", "info")
                
                cmd = [
                    "yt-dlp",
                    "--extract-audio",
                    "--audio-format", "opus",
                    "--output", os.path.join(download_dir, f"{i+1:02d} - %(title)s.%(ext)s"),
                    "--no-playlist",
                    "--no-warnings",
                    song['url']
                ]
                
                result = subprocess.run(cmd, capture_output=True, text=True)
                
                if result.returncode == 0:
                    successful += 1
                    self.root.after(0, self.log_message, f"✅ Completed: {song['title'][:30]}...", "success")
                else:
                    self.root.after(0, self.log_message, f"❌ Failed: {song['title'][:30]}...", "error")
                    
            self.root.after(0, lambda: self.progress_bar.set(1.0))
            self.root.after(0, self.log_message, f"🎉 Playlist download complete! {successful}/{total} songs", "success")
            self.root.after(0, self._download_complete)
            
        except Exception as e:
            self.root.after(0, self.log_message, f"❌ Download error: {str(e)}", "error")
            self.root.after(0, self._download_complete)
            
    def _download_complete(self):
        """Handle download completion with modern UI updates"""
        self.progress_info.configure(text="Ready")
        self.progress_bar.set(0)
        self.multi_download_btn.configure(state="normal", text="🚀 Download All Songs")
        self.playlist_download_btn.configure(state="normal", text="🚀 Download Selected Songs")
        
    def clear_log(self):
        """Clear the log with modern feedback"""
        self.log_text.configure(state="normal")
        self.log_text.delete("1.0", "end")
        self.log_text.configure(state="disabled")
        self.log_message("🗑️ Log cleared", "info")
        
    def log_message(self, message, level="info"):
        """Modern logging with enhanced formatting and emojis"""
        self.log_text.configure(state="normal")
        
        colors = {
            "info": self.theme.colors['accent_primary'],
            "success": self.theme.colors['accent_success'],
            "warning": self.theme.colors['accent_warning'],
            "error": self.theme.colors['accent_error']
        }
        
        import datetime
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        
        # Modern message formatting
        formatted_message = f"[{timestamp}] {message}\n"
        
        self.log_text.insert("end", formatted_message)
        self.log_text.see("end")
        self.log_text.configure(state="disabled")
        
    def check_dependencies(self):
        """Check dependencies with modern feedback"""
        threading.Thread(target=self._check_dependencies_thread, daemon=True).start()
        
    def _check_dependencies_thread(self):
        """Check dependencies in background with modern UI updates"""
        # Check yt-dlp
        try:
            result = subprocess.run(['yt-dlp', '--version'], capture_output=True, text=True, timeout=10)
            ytdlp_ok = result.returncode == 0
            ytdlp_version = result.stdout.strip() if ytdlp_ok else None
        except (FileNotFoundError, subprocess.TimeoutExpired):
            ytdlp_ok = False
            ytdlp_version = None
            
        # Check FFmpeg
        try:
            result = subprocess.run(['ffmpeg', '-version'], capture_output=True, text=True, timeout=10)
            ffmpeg_ok = result.returncode == 0
            ffmpeg_version = result.stdout.split('\n')[0] if ffmpeg_ok else None
        except (FileNotFoundError, subprocess.TimeoutExpired):
            ffmpeg_ok = False
            ffmpeg_version = None
            
        self.root.after(0, self._update_dependencies_ui, ytdlp_ok, ytdlp_version, ffmpeg_ok, ffmpeg_version)
        
    def _update_dependencies_ui(self, ytdlp_ok, ytdlp_version, ffmpeg_ok, ffmpeg_version):
        """Update dependencies UI with modern styling"""
        if ytdlp_ok:
            self.ytdlp_status.configure(
                text=f"yt-dlp: ✅ {ytdlp_version[:20]}..." if ytdlp_version else "yt-dlp: ✅ Ready",
                text_color=self.theme.colors['accent_success']
            )
        else:
            self.ytdlp_status.configure(
                text="yt-dlp: ❌ Not found",
                text_color=self.theme.colors['accent_error']
            )
            
        if ffmpeg_ok:
            version_text = ffmpeg_version.split()[2] if ffmpeg_version else "Ready"
            self.ffmpeg_status.configure(
                text=f"FFmpeg: ✅ {version_text}",
                text_color=self.theme.colors['accent_success']
            )
        else:
            self.ffmpeg_status.configure(
                text="FFmpeg: ❌ Not found",
                text_color=self.theme.colors['accent_error']
            )
            
        if ytdlp_ok and ffmpeg_ok:
            self.log_message("🎉 All dependencies ready!", "success")
        else:
            missing = []
            if not ytdlp_ok:
                missing.append("yt-dlp")
            if not ffmpeg_ok:
                missing.append("FFmpeg")
            self.log_message(f"⚠️ Missing dependencies: {', '.join(missing)}", "warning")
            self.log_message("📥 Install missing dependencies to enable downloads", "info")
            
    def on_closing(self):
        """Handle application closing with cleanup"""
        self.optimizer.shutdown(wait=False)
        self.root.destroy()
        
    def run(self):
        """Start the modern application"""
        self.log_message("🚀 Modern YouTube Music Downloader started!", "success")
        self.root.mainloop()

def main():
    """Main function with modern error handling"""
    try:
        import customtkinter
    except ImportError:
        print("❌ CustomTkinter is required!")
        print("📥 Installing CustomTkinter...")
        try:
            subprocess.run([sys.executable, '-m', 'pip', 'install', 'customtkinter'], check=True)
            print("✅ CustomTkinter installed! Please restart the application.")
            return
        except subprocess.CalledProcessError:
            print("❌ Failed to install CustomTkinter")
            print("Please install manually: pip install customtkinter")
            return
    
    try:
        app = ModernDownloader()
        app.run()
    except Exception as e:
        print(f"❌ Application error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()