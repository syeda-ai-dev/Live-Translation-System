#!/usr/bin/env python3
from mhire.com.config.config import Config
from mhire.com.services.transcription import Transcription
from mhire.com.services.translation import Translation
from mhire.com.visuals.gui import GUI

def main():
    # Initialize configuration
    config = Config()
    
    # Initialize services
    transcription_service = Transcription(config)
    translation_service = Translation(config)
    
    # Initialize and run GUI
    gui = GUI(config, transcription_service, translation_service)
    gui.run()

if __name__ == "__main__":
    main()